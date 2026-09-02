from animate import animate, add_sound
from shapes import generate_hyperboloid


segments = generate_hyperboloid(
    line_count=120,
    height=1.5,
    radius=1.0,
    twist=0.75,
)

video = animate(
    segments,
    video_name="hyperboloid_3d.mp4",
    fps=15,
)

final_video = add_sound(video, fps=15)
