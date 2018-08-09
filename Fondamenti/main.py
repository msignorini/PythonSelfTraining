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
#print(help(modulo.area_cilindro))

print(modulo.first_n_fibo(8))
print(modulo.quoziente_resto(44, 7))

rubrica = ["Monica", "Anna", "Ugo", "Francesco"]
print(sorted(rubrica))
print(list("Anna"))
print(modulo.primi(7))

# comprehension, modo succinto di fare operazioni sulle liste
# es. calcolo quadrati
quadrati = [i ** 2 for i in range(5)]
print(quadrati)

print(id(quadrati))

# ----------------- DIZIONARI -----------------
# Dizionari
telefono = {'Sergio':'123456', 'Marco':'456123'} # creazione
print("Telefono:", telefono)
telefono['Carlo'] = '789456' # aggiunta
print("Telefono:", telefono)
telefono.pop('Sergio')
print("Telefono:", telefono)

# comprehension sui dizionari
# es. calcolo cubi
cubi = {i: i ** 3 for i in range(5)}
print(cubi)

# ----------------- INSIEMI -----------------
# insieme, lista di elementi unici
insieme = {5, 'five'}
print(insieme)

# ----------------- TABELLE -----------------
# tabella, lista di Dizionari
dati = [
    {'nome':'Sofia', 'anno':1973, 'tel':'123456'},
    {'nome':'Marco', 'anno':1988, 'tel':'145688'},
    {'nome':'Angela', 'anno':1993, 'tel':'456963'},
]
print(dati)
from pprint import pprint
pprint(dati)

def ricerca(dati, nome, chiave):
    for dato in dati:
        if dato['nome'] == nome:
            return dato[chiave]
    return None

print(ricerca(dati, 'Marco', 'tel'))

# ----------------- FILE -----------------
import os
print(os.getcwd()) # print cartella corrente

# aprire un file con 'with' permette di chiuderlo automaticamente
# alla fine del blocco istruzioni
# anche a causa di un errore
with open('text.txt') as myFile:
    print("File aperto")

# ----------------- LETTURA FILE -----------------
with open('pg28885.txt') as alice:
    testo = alice.read() # legge l'intero file
    print(len(testo))
    #print(testo[686:1020])

# ----------------- JSON -----------------
import json
# salva dati su disco in JSON
with open('dati.json', 'w') as f:
    json.dump(dati, f)
    print("Scrittura JSON")
# leggo JSON
with open('dati.json') as f:
    nuovi_dati = json.load(f)
    pprint(nuovi_dati)

# ----------------- CSV -----------------
# leggo il CSV, splitto per ',' e lo scrivo in JSON
stat = []
diz = {}
with open('stat.csv') as f:
    linee = f.readlines() # legge l'intero file
    for linea in linee:
        ts, tm, hm = linea.split(',')
        hm = hm[0:-1]
        diz['timestamp'],diz['temperature'],diz['humidity'] = ts, tm, hm
        stat.append(diz)
    #pprint(stat)
    with open('stat.json', 'w') as js:
        json.dump(stat, js)
