from animate import animate, add_sound
from shapes import generate_lissajous_curve

segments = generate_lissajous_curve()
video = animate(
    segments,
    video_name="lissajous.mp4",
    fps=15,
)

final_video = add_sound(video, fps=15)
