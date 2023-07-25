import numpy as np
from collections import namedtuple

# We will override these later
Sphere = namedtuple("Sphere",["C","r"])
Plane = namedtuple("Plane",["N","d"])
Line = namedtuple("Line",["L0","L"])

# Should return the length of v
def length(v):
    return 0

# Should return the normalised vector of v
def normalised(v):
    return 0

# Should return a list of intersections between a line and a plane
# The line is a list of the format (origin, direction), and the plane as given above
# If no intersections it should return the empty list
def get_intersections_line_plane(line, plane):
    origin = line.L0
    direction = line.L

    N = plane.N
    d = plane.d

    return []

# Should return a list of intersections between a line and a sphere
# The line is a list of the format (origin, direction), and the sphere as given above
# If no intersections it should return the empty list
def get_intersections_line_sphere(line, sphere):
    origin = line.L0
    direction = line.L

    C = sphere.C
    r = sphere.r

    return []