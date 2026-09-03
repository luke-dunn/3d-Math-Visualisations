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


def generate_helicoid(
    line_count=120,
    radius=1.2,
    turns=2.0,
    height=2.5
):
    segments = []

    for i in range(line_count):
        t = i / (line_count - 1)

        angle = turns * 2 * math.pi * t
        z = height * (t - 0.5)

        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)

        p1 = (-dx, -dy, z)
        p2 = ( dx,  dy, z)

        segments.append((p1, p2))

    return segments
