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


def generate_hyperbolic_paraboloid(
    size=250,
    height=180,
    lines=40
):
    """
    Generate a hyperbolic paraboloid as two families of straight 3D lines.

    Returns:
        list of ((x1, y1, z1), (x2, y2, z2))
    """

    segments = []

    for i in range(lines + 1):
        t = -1 + 2 * i / lines

        # Family 1
        p1 = (-size, t * size, -t * height)
        p2 = ( size, t * size,  t * height)
        segments.append((p1, p2))

        # Family 2
        p1 = (t * size, -size,  t * height)
        p2 = (t * size,  size, -t * height)
        segments.append((p1, p2))

    return segments


import math


def generate_lissajous_curve(
    size=250,
    points=1200,
    a=3,
    b=4,
    c=5,
    phase_y=0.0,
    phase_z=0.0
):
    """
    Generate a 3D Lissajous curve as connected line segments.

    Returns:
        list of ((x1, y1, z1), (x2, y2, z2))
    """

    coords = []

    for i in range(points + 1):
        t = 2 * math.pi * i / points

        x = size * math.sin(a * t)
        y = size * math.sin(b * t + phase_y)
        z = size * math.sin(c * t + phase_z)

        coords.append((x, y, z))

    segments = []

    for i in range(len(coords) - 1):
        segments.append((coords[i], coords[i + 1]))

    return segments


import math


def generate_torus_knot(
    major_radius=220,
    minor_radius=90,
    points=1200,
    p=15,
    q=14
):
    """
    Generate a torus knot as connected 3D line segments.

    p = number of turns around the torus axis
    q = number of turns through the torus hole

    Returns:
        list of ((x1, y1, z1), (x2, y2, z2))
    """

    coords = []

    for i in range(points + 1):
        t = 2 * math.pi * i / points

        x = (major_radius + minor_radius * math.cos(q * t)) * math.cos(p * t)
        y = (major_radius + minor_radius * math.cos(q * t)) * math.sin(p * t)
        z = minor_radius * math.sin(q * t)

        coords.append((x, y, z))

    segments = []

    for i in range(len(coords) - 1):
        segments.append((coords[i], coords[i + 1]))

    return segments
