from linalg_functions.linalg_functions import *
from linalg_functions.colours import *

def screen_pixel_coordinate_to_3d_point(x, y, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR):
    return 0

def compute_ray(camera_p, pixel_p):
        return (0, 0)

def compute_distance_to_obj(ray, obj):
    if "Sphere" in type(obj).__name__:
        intersections = []
    if "Plane" in type(obj).__name__:
        intersections = []

    # Checks if there are any intersections
    if len(intersections) > 0:
        # Checks if we have a closer intersection
        return min(intersections)
    else:
        return np.inf

# obj kan være none her, og det skal der tjekkes efter
def get_colour(obj):
    return BLACK