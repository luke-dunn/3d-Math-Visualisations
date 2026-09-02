# transform3d.py

import math


def rotate(point, angle, tilt):
    x, y, z = point

    # Rotate around the vertical y-axis.
    xr = x * math.cos(angle) + z * math.sin(angle)
    zr = -x * math.sin(angle) + z * math.cos(angle)

    # Apply fixed camera tilt.
    yr = y * math.cos(tilt) - zr * math.sin(tilt)
    zr = y * math.sin(tilt) + zr * math.cos(tilt)

    return xr, yr, zr


def project(point, angle, tilt, distance, focal, width, height):
    xr, yr, zr = rotate(point, angle, tilt)

    scale = focal / (distance - zr)

    return (
        width / 2 + xr * scale,
        height / 2 - yr * scale,
    )
