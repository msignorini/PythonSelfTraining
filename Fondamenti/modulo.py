# importo solo il pigreco dal modulo math
from math import pi

def area_cilindro(raggio=1, altezza=1):
    '''Calcola l'area di un cilindro'''
    area = pi * raggio ** 2
    circonferenza = 2 * pi * raggio
    area_cilindro = 2 * area + altezza * circonferenza

    if __name__ == '__main__':
        print("Area Cilindro =", area_cilindro)

    return area_cilindro

def first_n_fibo(val=1):
    first = 0
    second = 1
    i = 0
    list = []
    while i < val:
        list.append(second)
        i += 1
        temp = second
        second += first
        first = temp

    return list

def quoziente_resto(x, y):
    return x // y, x % y

def primi(n_primi = 1):

    if n_primi < 1:
        return []

    i = 1
    primi = [2]
    counter = 3
    while i < n_primi:
        for val in primi:
            if counter % val == 0:
                break
        else:
            primi.append(counter)
            i += 1
        counter += 1

    return primi
