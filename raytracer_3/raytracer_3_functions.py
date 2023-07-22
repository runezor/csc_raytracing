import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from linalg_functions.colours import *
from raytracer_2.raytracer_2_functions import *

def get_normal_to_object(point, obj):
    if "Sphere" in type(obj).__name__:
        return normalised(point-np.array(obj.C))
    if "Plane" in type(obj).__name__:
        return normalised(np.array(obj.N))

def calculate_phong_color(collision_point, obj, direction_from_camera, ambient, lights, scene):
    # Computes where the line intersects with the object
    k_a, k_d, k_s = obj.phongVals

    diffuse = 0
    specular = 0
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
            diffuse += light_intensity * np.dot(normal, direction_to_light)
            # Computes spectral
            R = 2 * normal * (np.dot(direction_to_light, normal)) - direction_to_light
            specular += light_intensity * (np.dot(R, -direction_from_camera)) ** 20

    color = np.array(obj.color)*(ambient*k_a+diffuse*k_d)+np.array([1,1,1])*(specular*k_s)

    return color
