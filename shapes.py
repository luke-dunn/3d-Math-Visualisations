import math

def generate_hyperboloid(
    line_count=80,
    height=1.5,
    radius=1.0,
    twist=0.75,
):
    segments = []

    for i in range(line_count):
        angle = 2 * math.pi * i / line_count

        bottom = (
            radius * math.cos(angle),
            -height,
            radius * math.sin(angle),
        )

        top = (
            radius * math.cos(angle + twist),
            height,
            radius * math.sin(angle + twist),
        )

        segments.append((bottom, top))

    return segments
