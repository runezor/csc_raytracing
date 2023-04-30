import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from raytracer_2.raytracer_2_functions import *

def get_normal_to_object(point, obj):
    if "Sphere" in type(obj).__name__:
        return normalised(point-np.array(obj.C))
    if "Plane" in type(obj).__name__:
        return normalised(np.array(obj.N))

def calculate_phong_illumination(scene, direction_from_camera, ambient, lights, collision_point, obj, k_a, k_d, k_s):
    # Computes where the line intersects with the object

    illumination = ambient * k_a
    for light in lights:
        light_intensity = light[1]

        # Computes the ray going from the intersection point to the light
        vector_to_light = light[0] - collision_point
        direction_to_light = normalised(vector_to_light)
        distance_to_light = length(vector_to_light)
        ray_to_light = (collision_point + direction_to_light * 0.01, direction_to_light)

        # Calculates if there's any objects on the line between the light and the intersection point
        d2, obj_inbetween_light = get_nearest_collision(ray_to_light, scene)

        # Checks if the object intersecting is inbetween the intersection point and the light
        if distance_to_light < d2:
            normal = get_normal_to_object(collision_point, obj)
            # Computes diffuse
            diffuse = light_intensity * k_d * np.dot(normal, direction_to_light)
            # Computes spectral
            R = 2 * normal * (np.dot(direction_to_light, normal)) - direction_to_light
            spectral = light_intensity * k_s * (np.dot(R, -direction_from_camera)) ** 20
            # Adds to illumination (Phong)
            illumination += diffuse + spectral

    return illumination
