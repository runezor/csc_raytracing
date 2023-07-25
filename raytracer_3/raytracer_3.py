import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from .raytracer_3_functions import *
from .raytracer_3_params import *

# Initialises the image
image = np.zeros((HEIGHT, WIDTH, 3))

# Main loop
for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = screen_pixel_coordinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        direction_from_camera = normalised(pixel_coordinate-ORIGIN)
        # Computes the line from the camera to the pixel
        ray = compute_ray(ORIGIN, pixel_coordinate)
        # Sets the corresponding pixel in the image to black by default
        d, obj_closest = get_nearest_collision(ray, SCENE)
        if d == np.inf:
            image[j, i] = BLACK
        else:

            collision_point = ray.L0 + ray.L * d
            # Adds ambient light
            color = calculate_phong_color(collision_point, obj_closest, direction_from_camera, AMBIENT, LIGHTS, SCENE)
            image[j, i] = color

# Draw the image
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

plt.imshow(image)
plt.show()