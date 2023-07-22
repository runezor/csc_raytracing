import numpy as np

from linalg_functions.colours import *
from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from raytracer_3.raytracer_3_functions import *

def get_incoming_light_at_point(S,M, SCENE, LIGHTS, AMBIENT, rec_i):
    ray = (S, M)
    d, obj_closest = get_nearest_collision(ray, SCENE)

    return BLACK