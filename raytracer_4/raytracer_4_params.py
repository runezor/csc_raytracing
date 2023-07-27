import numpy as np
from collections import namedtuple
from linalg_functions.colours import *

# New, fancier Phong-tastic types with a reflection variable in the phongvals as well
SpherePhongEx = namedtuple("Sphere",["C","r","color","phongVals","rF"])
PlanePhongEx = namedtuple("Plane",["N","d","color","phongVals","rF"])

# This generally doesn't look great, so we default to false
NORMALISE = False

# Sets up the pixel grid
WIDTH = 450
HEIGHT = 300

# Needed to avoid stretching
RATIO = float(HEIGHT)/WIDTH

# The camera origin point
ORIGIN = np.array([0,0,-1])-np.array([0,0.2,0])

# Sets the three points of the screen
SCREEN_TOP_LEFT = np.array([1,RATIO,0])-np.array([0,0.2,0])
SCREEN_TOP_RIGHT = np.array([-1,RATIO,0])-np.array([0,0.2,0])
SCREEN_BOTTOM_LEFT = np.array([1,-RATIO,0])-np.array([0,0.2,0])

# Defines the vectors for moving along the screen
SCREEN_X_VECTOR = (SCREEN_TOP_RIGHT-SCREEN_TOP_LEFT)/WIDTH
SCREEN_Y_VECTOR = (SCREEN_BOTTOM_LEFT-SCREEN_TOP_LEFT)/HEIGHT

# Defines the scene
AMBIENT = 0.1
LIGHTS = [(np.array([10,20,10]),1.0)]

SCENE = [SpherePhongEx((1,1,12), 4, DARK, (0.8,0.8,0.8),0.8),
         SpherePhongEx((1.5,-2,4), 1, BLUE, (0.9,0.9,0.4),0),
         SpherePhongEx((3.5,-2.8,4), 0.2, YELLOW, (0.9,0.9,0.4),0.05),
         SpherePhongEx((-5.5,-2.2,8), 0.8, GREEN, (0.9,0.9,0.4),0.5),
         PlanePhongEx((0,1,0),3,BROWN,(0.9,0.9,0.0),0.5)]
