import numpy as np

# Should return the normalised vector of v
def normalised(v):
    return v / np.sqrt(np.sum(v**2))

# Should return a list of intersections between a line and a plane
# The line is a list of the format (origin, direction), and the plane (N, d)
# If no intersections it should return the empty list
def get_intersections_line_plane(line, plane):
    origin = line[0]
    direction = line[1]

    if np.dot(plane[0], direction) is 0:
        return []
    s = - (plane[1] + np.dot(plane[0], origin)) / np.dot(plane[0], direction)

    return [s]

# Should return a list of intersections between a line and a sphere
# The line is a list of the format (origin, direction), and the sphere (O, r)
# If no intersections it should return the empty list
def get_intersections_line_sphere(line, sphere):
    origin = line[0]
    direction = line[1]

    a = np.dot(direction, direction)
    b = np.dot(2 * direction, origin - sphere[0])
    c = np.dot(origin - sphere[0], origin - sphere[0]) - sphere[1] ** 2
    if b ** 2 - 4 * a * c < 0:
        return []
    else:
        d = np.sqrt(b ** 2 - 4 * a * c)
        s1 = (-b + d) / (2 * a)
        s2 = (-b - d) / (2 * a)
        return [s1, s2]