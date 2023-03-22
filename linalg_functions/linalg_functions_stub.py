import numpy as np

def length(v):
    return np.sqrt(np.sum(v**2))

def normalised(v):
    return v / np.sqrt(np.sum(v**2))

def get_intersections_line_plane(line, plane):
    origin = line[0]
    direction = line[1]

    if np.dot(plane[0], direction) is 0:
        return []
    s = - (plane[1] + np.dot(plane[0], origin)) / np.dot(plane[0], direction)

    return [s]

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