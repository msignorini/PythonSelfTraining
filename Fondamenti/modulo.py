# importo solo il pigreco dal modulo math
from math import pi

def area_cilindro(raggio=1, altezza=1):
    '''Calcola l'area di un cilindro'''
    area = pi * raggio ** 2
    circonferenza = 2 * pi * raggio
    return 2 * area + altezza * circonferenza
