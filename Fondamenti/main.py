'''
Commento multilinea
'''

import modulo

s = "hello"
print(type(s)) # tipo di un oggetto

# round
print(round(5.49))

# function
def hms(nsec):
    hh = nsec // 3600 # // divisione intera
    nsec = nsec % 3600
    mm = nsec // 60
    ss = nsec % 60
    return hh, mm, ss

h, m, s = hms(4000)
print("hour:", h, "minute:", m, "seconds:", s)

# richiamo funzione in modulo esterno
print(modulo.area_cilindro(altezza=4))

# vedo le funzioni di un modulo
print(dir(modulo))
print(help(modulo.area_cilindro))
