import numpy as np
from collections import namedtuple
from linalg_functions.colours import *

# New, even more Phong-tastic types
SpherePhong = namedtuple("Sphere",["C","r","color","phongVals"])
PlanePhong = namedtuple("Plane",["N","d","color","phongVals"])

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
AMBIENT = 0.4
LIGHTS = [(np.array([4,4,1]),1.0)]

SCENE = [SpherePhong((1,0,12), 4, RED, (0.8,0.8,0.4)),
         SpherePhong((1.5,-1.5,4), 1, BLUE, (0.9,0.9,0.9)),
         SpherePhong((3.5,-1.5,4), 0.2, YELLOW, (0.9,0.9,0.9)),
         SpherePhong((-3.5,-2.5,8), 0.8, GREEN, (0.9,0.9,0.9))]

