from animate import animate, add_sound
from shapes import generate_helicoid

# segments = generate_helicoid(parameters_here)


video = animate(
    segments,
    video_name="helicoid_3d.mp4",
    fps=15,
)

final_video = add_sound(video, fps=15)
