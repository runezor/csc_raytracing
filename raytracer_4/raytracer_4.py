import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from raytracer_1.raytracer_1_functions import *
from raytracer_2.raytracer_2_functions import *
from raytracer_3.raytracer_3_functions import *
from raytracer_4_params import *
from raytracer_4_functions import *

# Initialises the image
image = np.zeros((HEIGHT, WIDTH, 3))

# Main loop
normaliser = 1

for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = screen_pixel_corrdinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        direction_from_camera = normalised(pixel_coordinate-ORIGIN)

        color = get_incoming_light_at_point(pixel_coordinate, direction_from_camera, SCENE, LIGHTS, AMBIENT, 3)

        image[j, i] = color
        normaliser = max([normaliser, color[0], color[1], color[2]])*0.999

for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        image[j, i] = np.clip(image[j, i] / normaliser, 0, 1)

# Draw the image
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

plt.imshow(image)
plt.show()