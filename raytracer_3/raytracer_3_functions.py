import matplotlib.pyplot as plt
from linalg_functions.linalg_functions import *
from linalg_functions.colours import *
from raytracer_2.raytracer_2_functions import *

def get_normal_to_object(point, obj):
    # INDSÆT KODE HER
    if "Sphere" in type(obj).__name__:
        return np.array(0,1,0)
    if "Plane" in type(obj).__name__:
        return np.array(0,1,0)

def calculate_phong_color(collision_point, obj, direction_from_camera, ambient, lights, scene):
    # Henter Phong værdierne
    k_a, k_d, k_s = obj.phongVals

    # Brug gerne disse til at beregne summen
    diffuse = 0
    specular = 0
    # Hvis i ønsker at loope gennem lyset kan i bruge for light in lights:

    # INDSÆT KODE HER
    return BLACK
