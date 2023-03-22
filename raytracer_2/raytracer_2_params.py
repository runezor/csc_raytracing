import numpy as np

# Sets up the pixel grid
WIDTH = 300
HEIGHT = 200

# Needed to avoid stretching
RATIO = float(HEIGHT)/WIDTH

# The camera origin point
ORIGIN = np.array([0,0,-1])

# Sets the three points of the screen
SCREEN_TOP_LEFT = np.array([1,RATIO,0])
SCREEN_TOP_RIGHT = np.array([-1,RATIO,0])
SCREEN_BOTTOM_LEFT = np.array([1,-RATIO,0])

# Defines the vectors for moving along the screen
SCREEN_X_VECTOR = (SCREEN_TOP_RIGHT-SCREEN_TOP_LEFT)/WIDTH
SCREEN_Y_VECTOR = (SCREEN_BOTTOM_LEFT-SCREEN_TOP_LEFT)/HEIGHT

# Defines the scene
BLACK = (0,0,0)
RED = (1,0,0)
GREEN = (0,1,0)
BLUE = (0,0,1)
SCENE = [("sphere", ((1,0,12), 4), RED),("sphere", ((1.5,-1.5,4), 1), BLUE),("plane",((0,1,0),2),GREEN)]
LIGHT = np.array([10,10,10])