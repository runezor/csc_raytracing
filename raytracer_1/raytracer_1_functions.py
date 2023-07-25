from linalg_functions.linalg_functions import *
from linalg_functions.colours import *

def screen_pixel_coordinate_to_3d_point(x, y, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR):
    return SCREEN_TOP_LEFT+SCREEN_X_VECTOR*x+SCREEN_Y_VECTOR*y

def compute_ray(camera_p, pixel_p):
    return Line(np.array([0,0,0]), np.array([0,0,0]))

def compute_distance_to_obj(ray, obj):
    if "Sphere" in type(obj).__name__:
        intersections = list(filter(lambda i: i > 0, get_intersections_line_sphere(ray, obj)))
    if "Plane" in type(obj).__name__:
        intersections = list(filter(lambda i: i > 0, get_intersections_line_plane(ray, obj)))

    # Checks if there are any intersections
    if len(intersections) > 0:
        # Checks if we have a closer intersection
        return min(intersections)
    else:
        return np.inf

def get_colour(obj):
    if obj is None:
        return BLACK #FIXME WITHOUT IMPORTING PARAMS
    else:
        return obj.color
