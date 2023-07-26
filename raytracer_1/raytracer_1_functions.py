from linalg_functions.linalg_functions import *
from linalg_functions.colours import *

def screen_pixel_coordinate_to_3d_point(x, y, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR):
    #INDSÆT KODE HER
    return np.array([0,0,0])

def compute_ray(camera_p, pixel_p):
    #INDSÆT KODE HER
    return Line(np.array([0,0,0]), np.array([0,0,0]))

def compute_distance_to_obj(ray, obj):
    #INDSÆT KODE HER
    #Brug evt. nedestående
    #if "Sphere" in type(obj).__name__:
    #    ...
    #if "Plane" in type(obj).__name__:
    #    ...

    # Returnerer afstanden til objektet
    return np.inf

def get_colour(obj):
    #INDSÆT KODE HER
    if obj is None:
        return BLACK #FIXME WITHOUT IMPORTING PARAMS
    else:
        return obj.color