import matplotlib.pyplot as plt
from raytracer_1.raytracer_1_functions import *
from .raytracer_2_functions import *
from .raytracer_2_params import *

# Initialises the image
image = np.zeros((HEIGHT, WIDTH, 3))

# Main loop
for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = screen_pixel_coordinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        # Computes the line from the camera to the pixel
        ray = compute_ray(ORIGIN, pixel_coordinate)
        # Sets the corresponding pixel in the image to black by default
        d, obj_closest = get_nearest_collision(ray, SCENE)

        if d == np.inf:
            image[j, i] = BLACK
        else:
            # Computes where the line intersects with the object
            collision_point = ray[0]+ray[1]*d

            # Checks if the object intersecting is inbetween the intersection point and the light
            if not is_light_blocked(collision_point, LIGHT, SCENE):
                image[j, i] = get_colour(obj_closest)

# Draw the image
plt.imshow(image)
plt.show()