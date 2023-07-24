import matplotlib.pyplot as plt
from raytracer_1_params import *
from raytracer_1_functions import *
from linalg_functions.linalg_functions import *

# Initialises the image
image = np.zeros((HEIGHT, WIDTH, 3))

# Main loop
for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = screen_pixel_coordinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        # Computes the line from the camera to the pixel
        ray = compute_ray(ORIGIN, pixel_coordinate)
        # Used for finding the closest object
        d = np.inf
        closet_obj = None
        # Loop through objects
        for obj in SCENE:
            distance = compute_distance_to_obj(ray, obj)
            if d > distance:
                # If not, then use the color of the object to set the corresponding pixel
                d = distance
                closet_obj = obj
        # Sets the corresponding pixel in the image to black by default
        image[j, i] = get_colour(closet_obj)

# Draw the image
plt.imshow(image)
plt.show()