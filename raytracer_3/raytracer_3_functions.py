import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *

def get_normal_to_object(point, obj):
    if obj[0] == "sphere":
        origin = obj[1][0]
        return normalised(point-np.array(origin))
    if obj[0] == "plane":
        N = obj[1][0]
        return normalised(np.array(N))
