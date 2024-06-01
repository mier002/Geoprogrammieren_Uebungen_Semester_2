#Uebung05
import sys
from PyQt5.QtWidgets import *
import urllib.parse

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnect()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI Programmierung")
        layout = QFormLayout()
        self.setMinimumSize(800,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        self.vorname = QLineEdit()
        self.nachname = QLineEdit()
        self.bday = QDateEdit()
        self.bday.setDisplayFormat("dd/MM/yyyy")
        self.adr = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich", "andere"])

        self.karte = QPushButton("Auf Karte anzeigen")
        self.savek = QPushButton("Save")
        self.laden = QPushButton("Laden")
        

        ## Layout füllen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Nachname:", self.nachname)
        layout.addRow("Geburtstag:", self.bday)
        layout.addRow("Adresse:", self.adr)
        layout.addRow("PLZ:", self.plz)
        layout.addRow("Ortschaft:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.karte)
        layout.addRow(self.laden)
        layout.addRow(self.savek)



        ## Menueleiste
        menubar = self.menuBar()
        filemenu1 = menubar.addMenu("File")
        filemenu2 = menubar.addMenu("View")
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        filemenu1.addAction(self.save)
        filemenu1.addAction(self.quit)

        ## Fenster anzeigen
        self.show()


    def createConnect(self):
        self.quit.triggered.connect(self.close)
        self.save.triggered.connect(self.speicher)
        self.savek.clicked.connect(self.speicher)
        self.karte.clicked.connect(self.karte)
        self.laden.clicked.connect(self.laden)



    def close(self):
        super().close()

    def speicher(self):
        filename, typ = QFileDialog.getSaveFileName(self, "Datei speichern","","Alle (*.*)")
        export = f"{self.vorname.text()},{self.nachname.text()},{self.bday.text()},{self.adr.text()},{self.plz.text()},{self.ort.text()},{self.land.currentText()}"

        f = open("output.txt", "w")
        f.write(export)
        f.close()

    def karte(self):
        query = f"{self.adr.text}+{self.plz}+{self.ort.text}"
        encoding = urllib.parse.quote(query)
        link = f"https://www.google.ch/maps/place/{encoding}"
        QDesktopServices.openUrl(QUrl(link))

        address = self.findChild(QLineEdit, "Adresse").text()
        plz = self.findChild(QLineEdit, "PLZ").text()
        ort = self.findChild(QLineEdit, "Ort").text()
        land = self.findChild(QComboBox, "Land").currentText()

        # URL für Google Maps zusammensetzen
        encoded_address = urllib.parse.quote(address)
        encoded_plz = urllib.parse.quote(plz)
        encoded_ort = urllib.parse.quote(ort)
        encoded_land = urllib.parse.quote(land)

        url = f"https://www.google.com/maps/place/{encoded_address}+{encoded_plz}+{encoded_ort}+{encoded_land}"

        # Google Maps im Standard-Webbrowser öffnen
        QDesktopServices.openUrl(QUrl(url))

def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()