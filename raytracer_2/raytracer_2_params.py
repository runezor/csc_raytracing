import numpy as np
from collections import namedtuple
from linalg_functions.colours import *

# Same types as earlier
SphereColored = namedtuple("Sphere",["C","r","color"])
PlaneColored = namedtuple("Plane",["N","d","color"])

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
LIGHT = np.array([10,10,10])

SCENE = [SphereColored((1,0,12), 4, RED),
         SphereColored((1.5,-1.5,4), 1, BLUE),
         PlaneColored((0,1,0),2,GREEN)]