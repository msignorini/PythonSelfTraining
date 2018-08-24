'''
Installazine su Ubuntu/Debian
sudo apt install pyqt5-dev python3-pyqt5 python3-pyqt5.qtwebengine
'''

# importo librerie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

def init():
    # verifico se l'applicazione è già esistente
    app = QApplication.instance()
    # crea applicazione se non esistente
    if not app: app = QApplication([])
    # crea una finestra
    window = QWidget()
    window.resize(500, 300)
    window.setWindowTitle('Fondamenti di Programmazione')
    return app, window

def run(app, window):
    # mostra la finestra
    window.show()
    # lancia iterazione con utente
    app.exec_()

def button_print_callback():
    print("Clicked Print Button")
    #textedit.setText("Ciao")
    textedit.append("Ciao")


# ---- BEGIN ------
print("ciao")
# inizializzo la GUI
app, window = init()

# creo layout verticale
layoutVert = QVBoxLayout()
# creo layout orizzontale
layoutHoriz = QHBoxLayout()

# creo i bottoni
button_print = QPushButton('Print Ciao')
button_close = QPushButton('Close')

# aggiungo bottoni al layout verticale
layoutVert.addWidget(button_print)
layoutVert.addWidget(button_close)

# aggiungo il layout verticale a quello orizzontale
layoutHoriz.addLayout(layoutVert)

# creo la textbox
textedit = QTextEdit('')
# aggiungo la textbox al layout orizzontale
layoutHoriz.addWidget(textedit)

# imposto il layout della finestra
window.setLayout(layoutHoriz)

# definisco le callback
button_print.clicked.connect(button_print_callback)
button_close.clicked.connect(app.quit)

# eseguo la GUI
run(app, window)
