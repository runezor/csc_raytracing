import numpy as np

from linalg_functions.colours import *
from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from raytracer_3.raytracer_3_functions import *

def get_incoming_light_at_point(S,M, SCENE, LIGHTS, AMBIENT, rec_i):
    ray = Line(S, M)
    # Sets the cforresponding pixel in the image to black by default
    d, obj_closest = get_nearest_collision(ray, SCENE)
    if d == np.inf:
        return np.array([0.001,0.001,0.001])
    else:
        k_t = obj_closest.rF

        # Computes where the line intersects with the object
        collision_point = ray.L0 + ray.L * d

        # Uses previous Phong illumination
        color = calculate_phong_color(collision_point, obj_closest, M, AMBIENT, LIGHTS, SCENE)

        normal = get_normal_to_object(collision_point, obj_closest)

        if rec_i>0:
            reflection_direction = M - (2.0 * M.dot(normal) * normal)
            mirror_light = get_incoming_light_at_point(collision_point + normal * 0.01, reflection_direction, SCENE, LIGHTS, AMBIENT, rec_i-1)

            color +=  k_t * np.array(mirror_light) * np.dot(mirror_light, np.array(obj_closest.color))

        return color