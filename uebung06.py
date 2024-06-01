import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import urllib.parse

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("showmap.ui", self)

        self.pushButton.clicked.connect(self.karte_anzeigen)
    
    def karte_anzeigen(self):
        # URL für Google Maps zusammensetzen
        encoded_breite = self.lineEdit_1.text()
        encoded_laenge = self.lineEdit_2.text()

        url = f"https://www.google.com/maps/place/{encoded_breite},{encoded_laenge}"

        # Google Maps im Standard-Webbrowser öffnen
        QDesktopServices.openUrl(QUrl(url))

app = QApplication([])
window = Fenster()
window.show()


app.exec()