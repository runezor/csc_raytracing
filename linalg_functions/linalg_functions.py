import numpy as np
from collections import namedtuple

# We will override these later
Sphere = namedtuple("Sphere",["C","r"])
Plane = namedtuple("Plane",["N","d"])
Line = namedtuple("Line",["L0","L"])

# Should return the length of v
def length(v):
    return np.sqrt(np.sum(v**2))

# Should return the normalised vector of v
def normalised(v):
    return v / np.sqrt(np.sum(v**2))

# Should return a list of intersections between a line and a plane
# The line is a list of the format (origin, direction), and the plane as given above
# If no intersections it should return the empty list
def get_intersections_line_plane(line, plane):
    origin = line.L0
    direction = line.L

    if np.dot(plane.N, direction) is 0:
        return []
    s = - (plane.d + np.dot(plane.N, origin)) / np.dot(plane.N, direction)

    return [s]

# Should return a list of intersections between a line and a sphere
# The line is a list of the format (origin, direction), and the sphere as given above
# If no intersections it should return the empty list
def get_intersections_line_sphere(line, sphere):
    origin = line.L0
    direction = line.L

    a = np.dot(direction, direction)
    b = np.dot(2 * direction, origin - sphere.C)
    c = np.dot(origin - sphere.C, origin - sphere.C) - sphere.r ** 2
    if b ** 2 - 4 * a * c < 0:
        return []
    else:
        d = np.sqrt(b ** 2 - 4 * a * c)
        s1 = (-b + d) / (2 * a)
        s2 = (-b - d) / (2 * a)
        return [s1, s2]