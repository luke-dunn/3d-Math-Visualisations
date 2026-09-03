from animate import animate, add_sound
from shapes import generate_torus_knot

segments = generate_torus_knot()
video = animate(
    segments,
    video_name="torus_knot.mp4",
    fps=15,
)

final_video = add_sound(video, fps=15)
