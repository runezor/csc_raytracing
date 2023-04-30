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
        pixel_coordinate = screen_pixel_corrdinate_to_3d_point(i, j, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR)
        # Computes the line from the camera to the pixel
        ray = compute_ray(ORIGIN, pixel_coordinate)
        # Sets the corresponding pixel in the image to black by default
        image[j, i] = BLACK
        # Used for finding the closest object
        d = np.inf
        # Loop through objects
        for obj in SCENE:
            if "Sphere" in type(obj).__name__:
                intersections = list(filter(lambda i: i > 0, get_intersections_line_sphere(ray, obj)))
            if "Plane" in type(obj).__name__:
                intersections = list(filter(lambda i: i > 0, get_intersections_line_plane(ray, obj)))

            # Checks if there are any intersections
            if len(intersections) > 0:
                # Checks if we have a closer intersection
                if d > min(intersections):
                    # If not, then use the color of the object to set the corresponding pixel
                    d = min(intersections)
                    image[j, i] = get_colour(obj)

# Draw the image
plt.imshow(image)
plt.show()