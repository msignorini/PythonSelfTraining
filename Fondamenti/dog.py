'''
APPUNTI
il primo parametro di costruttore e metodi deve essere "self"
'''
class Dog:

    # costruttore
    def __init__(self, name):
        self.name = name
    # definiamo un metodo che accede al nome e lo stampa
    def print_name(self):
        print(self.name)
