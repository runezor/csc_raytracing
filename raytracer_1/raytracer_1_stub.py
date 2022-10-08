import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *

# Sets up the pixel grid
width = 300
height = 200

# Needed to avoid stretching
ratio = float(height)/width

# Sets the three points of the screen
screen_top_left = np.array([1,ratio,0])
screen_top_right = np.array([-1,ratio,0])
screen_bottom_left = np.array([1,-ratio,0])

# Defines the vectors for moving along the screen
x_vector = (screen_top_right-screen_top_left)/width
y_vector = (screen_bottom_left-screen_top_left)/height

# The camera origin point
origin = np.array([0,0,-1])

# Defines the scene
BLACK = (0,0,0)
RED = (1,0,0)
GREEN = (0,1,0)
BLUE = (0,0,1)
scene = [("sphere", ((1,0,12), 4), RED),("sphere", ((1.5,-1.5,4), 1), BLUE),("plane",((0,1,0),2),GREEN)]

# Initialises the image
image = np.zeros((height, width, 3))

# Main loop
for i in range(0, width):
    for j in range(0, height):
        # Computes the point of the pixel in 3d-space
        pixel_coordinate = ???
        # Computes the line from the camera to the pixel
        ray = ???
        # Sets the corresponding pixel in the image to black by default
        image[j, i] = ???
        # Used for finding the closest object
        d = np.inf
        # Loop through objects
        for obj in scene:
            ???

# Draw the image
im = plt.imshow(image)
plt.show()