from linalg_functions.linalg_functions import *
from linalg_functions.colours import *
import numpy as np

# Given the current collision point, the light point, and the scene...
# ... this function should return true if the object in the origin position of the ray
# Is blocked by the light
def is_light_blocked(collision_point, light_point, scene):
    return False

# Line is a (normalised!) tuple with an origin and a direction, the scene is the list of objects
# Returns a tuple with the distance, and the object
def get_nearest_collision(ray, scene):
    return np.Inf, None