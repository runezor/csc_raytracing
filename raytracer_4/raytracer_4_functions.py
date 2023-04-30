from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from raytracer_3.raytracer_3_functions import *

def get_incoming_light_at_point(P,N,rec_i, SCENE, LIGHTS, AMBIENT):
    ray = (P, N)
    # Sets the corresponding pixel in the image to black by default
    d, obj_closest = get_nearest_collision(ray, SCENE)
    if d == np.inf:
        return np.array([0.0,0.0,0.0])
    else:
        k_a, k_d, k_s, k_t = obj_closest[3]

        # Computes where the line intersects with the object
        collision_point = ray[0] + ray[1] * d

        # Uses previous Phong illumination
        illumination = calculate_phong_illumination(SCENE, N, AMBIENT, LIGHTS, collision_point,
                                                    obj_closest, k_a, k_d, k_s)

        color = np.array(obj_closest[2]) * illumination

        normal = get_normal_to_object(collision_point, obj_closest)
        if rec_i>0:
            reflection_direction = N - (2.0 * N.dot(normal) * normal)
            color += get_incoming_light_at_point(collision_point + normal * 0.01, reflection_direction, rec_i-1, SCENE, LIGHTS, AMBIENT) * k_t

        return color