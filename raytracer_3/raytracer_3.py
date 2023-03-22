import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from raytracer_3_functions import *
from raytracer_3_params import *

# Initialises the image
image = np.zeros((HEIGHT, WIDTH, 3))

# Main loop
for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = screen_pixel_corrdinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        direction_from_camera = normalised(pixel_coordinate-ORIGIN)
        # Computes the line from the camera to the pixel
        ray = compute_ray(ORIGIN, pixel_coordinate)
        # Sets the corresponding pixel in the image to black by default
        d, obj_closest = get_nearest_collision(ray, SCENE)
        if d == np.inf:
            image[j, i] = BLACK
        else:
            k_a, k_d, k_s = obj_closest[3]

            # Adds ambient light
            illumination = AMBIENT * k_a
            for light in LIGHTS:
                # Computes where the line intersects with the object
                collision_point = ray[0]+ray[1]*d

                light_intensity = light[1]

                # Computes the ray going from the intersection point to the light
                vector_to_light = light[0]-collision_point
                direction_to_light = normalised(vector_to_light)
                distance_to_light = length(vector_to_light)
                ray_to_light = (collision_point+direction_to_light * 0.01, direction_to_light)

                # Calculates if there's any objects on the line between the light and the intersection point
                d2, obj_inbetween_light = get_nearest_collision(ray_to_light, SCENE)

                # Checks if the object intersecting is inbetween the intersection point and the light
                if distance_to_light<d2:
                    normal = get_normal_to_object(collision_point, obj_closest)
                    # Computes diffuse
                    diffuse = light_intensity * k_d * np.dot(normal, direction_to_light)
                    # Computes spectral
                    R = 2 * normal * (np.dot(direction_to_light, normal)) - direction_to_light
                    spectral = light_intensity * k_s * (np.dot(R, -direction_from_camera)) ** 20
                    # Adds to illumination (Phong)
                    illumination += diffuse + spectral

            image[j, i] = np.array(obj_closest[2]) * min(illumination,1)

# Draw the image
plt.imshow(image)
plt.show()