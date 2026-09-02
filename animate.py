# animate.py
import wave
import numpy as np
import math
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw
from transform3d import project


def animate(
    segments,
    video_name="shape_3d.mp4",
    width=1080,
    height=1920,
    fps=15,
    rotation_seconds=30,
    tilt=math.radians(20),
    hold_seconds=15,
    background=(16, 20, 30),
    tip_colour=(255, 190, 80),
    line_width=3,
):
    reveal_frames = len(segments)
    hold_frames = hold_seconds * fps
    total_frames = reveal_frames + hold_frames

    all_points = [
        point
        for segment in segments
        for point in segment
    ]

    radius = max(
        math.sqrt(x*x + y*y + z*z)
        for x, y, z in all_points
    )

    distance = 3 * radius
    focal = 0.7 * min(width, height) * (distance - radius) / radius

    output = Path(tempfile.mkdtemp(
        prefix="shape_",
        dir=Path(__file__).parent,
    ))

    for frame in range(total_frames):
        angle = 2 * math.pi * frame / (fps * rotation_seconds)
        visible_count = min(frame + 1, len(segments))

        image = Image.new("RGB", (width, height), background)
        draw = ImageDraw.Draw(image)

        for i, (start, end) in enumerate(segments[:visible_count]):
            p1 = project(
                start, angle, tilt,
                distance, focal,
                width, height,
            )

            p2 = project(
                end, angle, tilt,
                distance, focal,
                width, height,
            )

            t = i / max(1, len(segments) - 1)

            colour = (
                int(70 + 150 * t),
                int(120 + 90 * t),
                int(255 - 90 * t),
            )

            draw.line(
                [p1, p2],
                fill=colour,
                width=line_width,
            )

        if frame < reveal_frames:
            newest_end = segments[visible_count - 1][1]

            x, y = project(
                newest_end, angle, tilt,
                distance, focal,
                width, height,
            )

            draw.ellipse(
                (x - 6, y - 6, x + 6, y + 6),
                fill=tip_colour,
            )

        image.save(output / f"frame_{frame:05d}.png")

        if (frame + 1) % 20 == 0 or frame == total_frames - 1:
            print(f"Frames: {frame + 1}/{total_frames}")

    video = output / video_name

    subprocess.run([
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-n",
        "-framerate", str(fps),
        "-start_number", "0",
        "-i", str(output / "frame_%05d.png"),
        "-frames:v", str(total_frames),
        "-c:v", "libx264",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(video),
    ], check=True)

    print(f"Saved: {video}")
    return video


def add_sound(video, fps=15, sample_rate=44100):
    video = Path(video)
    frame_dir = video.parent
    files = sorted(frame_dir.glob("frame_*.png"))

    if not files:
        raise ValueError(f"No frames found in {frame_dir}")

    duration = len(files) / fps
    samples = int(duration * sample_rate)

    brightness = []
    change = []
    previous = None

    for filename in files:
        with Image.open(filename) as image:
            image = image.convert("L").resize((64, 64))
            array = np.asarray(image, dtype=np.float32) / 255.0

        brightness.append(array.mean())

        if previous is None:
            change.append(0.0)
        else:
            change.append(np.abs(array - previous).mean())

        previous = array

    brightness = np.asarray(brightness)
    change = np.asarray(change)

    brightness = (
        (brightness - brightness.min())
        / (np.ptp(brightness) + 1e-9)
    )

    change = (
        (change - change.min())
        / (np.ptp(change) + 1e-9)
    )

    frame_times = np.arange(len(files)) / fps
    audio_times = np.arange(samples) / sample_rate

    b = np.interp(audio_times, frame_times, brightness)
    c = np.interp(audio_times, frame_times, change)

    t = audio_times

    # Deep evolving drone
    drone = np.sin(2 * np.pi * (10 + 10*b) * t)

    # Low harmonic controlled by visual change
    shimmer = np.sin(2 * np.pi * (40 + 40*c) * t)

    # Slow positive pulse
    pulse = np.sin(2 * np.pi * (0.5 + 2*c) * t)
    pulse = np.maximum(pulse, 0)

    audio = (
        1.2 * drone +
        0.25 * shimmer
    ) * (0.4 + 0.6 * pulse)

    audio /= np.max(np.abs(audio)) + 1e-9
    audio = (audio * 32767).astype(np.int16)

    wav_file = frame_dir / "soundtrack.wav"
    output_video = video.with_name(
        f"{video.stem}_sound{video.suffix}"
    )

    with wave.open(str(wav_file), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(audio.tobytes())

    subprocess.run([
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-n",
        "-i", str(video),
        "-i", str(wav_file),
        "-shortest",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        str(output_video),
    ], check=True)

    print(f"Saved with sound: {output_video}")
    return output_video
