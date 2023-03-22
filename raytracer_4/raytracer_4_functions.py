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

        # Adds ambient light
        illumination = AMBIENT * k_a

        # Computes where the line intersects with the object
        collision_point = ray[0] + ray[1] * d
        normal = get_normal_to_object(collision_point, obj_closest)
        for light in LIGHTS:
            light_intensity = light[1]

            # Computes the ray going from the intersection point to the light
            vector_to_light = light[0] - collision_point
            direction_to_light = normalised(vector_to_light)
            distance_to_light = length(vector_to_light)
            ray_to_light = (collision_point + direction_to_light * 0.01, direction_to_light)

            # Calculates if there's any objects on the line between the light and the intersection point
            d2, obj_inbetween_light = get_nearest_collision(ray_to_light, SCENE)

            # Checks if the object intersecting is inbetween the intersection point and the light
            if distance_to_light < d2:
                # Computes diffuse
                diffuse = light_intensity * k_d * np.dot(normal, direction_to_light)
                # Computes spectral
                R = 2 * normal * (np.dot(direction_to_light, normal)) - direction_to_light
                spectral = light_intensity * k_s * (np.dot(R, -N)) ** 20
                # Adds to illumination (Phong)
                illumination += diffuse + spectral

        color = np.array(obj_closest[2]) * illumination
        if rec_i>0:
            reflection_direction = N - (2.0 * N.dot(normal) * normal)
            color += get_incoming_light_at_point(collision_point + normal * 0.01, reflection_direction, rec_i-1, SCENE, LIGHTS, AMBIENT) * k_t

        return color