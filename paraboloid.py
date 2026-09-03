from animate import animate, add_sound
from shapes import generate_hyperbolic_paraboloid

segments = generate_hyperbolic_paraboloid()
video = animate(
    segments,
    video_name="paraboloid.mp4",
    fps=15,
)

final_video = add_sound(video, fps=15)
