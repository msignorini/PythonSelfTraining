'''
sudo apt install pyqt5-dev python3-pyqt5 python3-pyqt5.qtwebengine
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

print("ciao")

# crea applicazione
app = QApplication([])

# crea una finestra
window = QWidget()
window.resize(500,300)
window.setWindowTitle('Fondamenti di Programmazione')

# mostra la finestra
window.show()

# lancia iterazione con utente
app.exec_()
