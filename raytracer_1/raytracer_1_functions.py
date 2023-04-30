from linalg_functions.linalg_functions import *

# TO IMPLEMENT
def screen_pixel_corrdinate_to_3d_point(x, y, SCREEN_TOP_LEFT, SCREEN_X_VECTOR, SCREEN_Y_VECTOR):
    return SCREEN_TOP_LEFT+SCREEN_X_VECTOR*x+SCREEN_Y_VECTOR*y

def compute_ray(camera_p, pixel_p):
    return (camera_p, normalised(pixel_p-camera_p))

def get_colour(obj):
    return obj.color
