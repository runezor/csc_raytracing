from linalg_functions.linalg_functions import *
from linalg_functions.colours import *
import numpy as np

# Given the current collision point, the light point, and the scene...
# ... this function should return true if the object in the origin position of the ray
# Is blocked by the light
def is_light_blocked(collision_point, light_point, scene):
    vector_to_light = light_point - collision_point
    direction_to_light = normalised(vector_to_light)
    distance_to_light = length(vector_to_light)
    ray_to_light = Line(collision_point + direction_to_light * 0.01, direction_to_light)

    d2, obj_inbetween_light = get_nearest_collision(ray_to_light, scene)
    return d2 < distance_to_light

# Line is a (normalised!) tuple with an origin and a direction, the scene is the list of objects
# Returns a tuple with the distance, and the object
def get_nearest_collision(ray, scene):
    # The closest distance observed so far
    d = np.inf

    # The object we will return
    obj_closest = None

    # Loop through objects
    for obj in scene:
        if "Sphere" in type(obj).__name__:
            intersections = list(filter(lambda i: i > 0, get_intersections_line_sphere(ray, obj)))
        if "Plane" in type(obj).__name__:
            intersections = list(filter(lambda i: i > 0, get_intersections_line_plane(ray, obj)))

        # Checks if there are any intersections
        if len(intersections) > 0:
            # Checks if we have a closer intersection
            if d > min(intersections):
                # If not, then use the color of the object to set the corresponding pixel
                d = min(intersections)
                obj_closest = obj

    return d, obj_closest