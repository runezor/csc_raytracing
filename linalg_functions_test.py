import numpy as np
import math
from linalg_functions.linalg_functions import *

try:
    #Length
    assert(length(np.array([0,0,0])) == 0)
    assert(length(np.array([0,1,0])) == 1)
    assert(length(np.array([4,2,4])) == 6)

    #Normalised
    assert(np.linalg.norm( normalised(np.array([5,0,0])) - np.array([1,0,0])) < 0.01)
    assert(np.linalg.norm( normalised(np.array([1,1,0])) - np.array([math.sqrt(2),math.sqrt(2),0])/2 )<0.01)
    assert(np.linalg.norm( normalised(np.array([1,1,1])) - np.array([math.sqrt(3),math.sqrt(3),math.sqrt(3)])/3 )<0.01)

    #Line
    assert(np.linalg.norm(get_intersections_line_plane(Line(np.array([0,2,0]),np.array([0,-1,0])), Plane(np.array([0,1,0]),0))[0]) == 2)
    assert(np.linalg.norm(get_intersections_line_plane(Line(np.array([0,2,0]),np.array([-1,-1,0])), Plane(np.array([0,1,0]),0))[0]) - math.sqrt(8) < 0.01)

    #Sphere
    assert(np.linalg.norm(get_intersections_line_sphere(Line(np.array([1,2,0]),np.array([-1,0,0])), Sphere(np.array([0,0,0]),2))[0]) == 1)
    assert(np.linalg.norm(get_intersections_line_sphere(Line(np.array([1,2,0]),np.array([-1,0,0])), Sphere(np.array([0,0,0]),2))[1]) == 1)
    assert(np.linalg.norm(get_intersections_line_sphere(Line(np.array([3,0,0]),np.array([-1,0,0])), Sphere(np.array([0,0,0]),2))[1]) == 1)
    assert(np.linalg.norm(get_intersections_line_sphere(Line(np.array([3,0,0]),np.array([-1,0,0])), Sphere(np.array([0,0,0]),2))[0]) == 5)
    print("Godt Klaret!")
except AssertionError as e:
    print("Tough luck mester, se nedestående fejl:")
    raise e