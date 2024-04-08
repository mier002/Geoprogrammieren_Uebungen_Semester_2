#uebung04
import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QGridLayout()

        # Widget-Instanzen erstellen:
        vornameLabel1 = QLabel("Vorname:")
        self.vornameLine1 = QLineEdit()
        nameLabel2 = QLabel("Name:")
        self.nameLine2 = QLineEdit()
        gebLabel3 = QLabel("Geburtstag:")
        self.gebLine3 = QDateEdit()
        adrLabel4 = QLabel("Adresse:")
        self.adrLine4 = QLineEdit()
        plzLabel5 = QLabel("Postleitzahl:")
        self.plzLine5 = QLineEdit()
        ortLabel6 = QLabel("Ort:")
        self.ortLine6 = QLineEdit()
        landLabel7 = QLabel("Land:")
        self.landLine7 = QComboBox()
        button = QPushButton("Save")

        # Widgets mit Grid-Koordinaten dem Layout hinzufügen
        layout.addWidget(vornameLabel1, 0, 0)
        layout.addWidget(self.vornameLine1, 0, 1)
        layout.addWidget(nameLabel2, 1, 0)
        layout.addWidget(self.nameLine2, 1, 1)
        layout.addWidget(gebLabel3, 2, 0)
        layout.addWidget(self.gebLine3, 2, 1)
        layout.addWidget(adrLabel4, 3, 0)
        layout.addWidget(self.adrLine4, 3, 1)
        layout.addWidget(plzLabel5, 4, 0)
        layout.addWidget(self.plzLine5, 4, 1)
        layout.addWidget(ortLabel6, 5, 0)
        layout.addWidget(self.ortLine6, 5, 1)
        layout.addWidget(landLabel7, 6, 0)
        layout.addWidget(self.landLine7, 6, 1)
        layout.addWidget(button, 7, 1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Länderauswahl hinzufügen
        self.landLine7.addItems(["Schweiz", "Deutschland", "Österreich"])

        #Menu erstellen
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        save.triggered.connect(self.menu_quit)
        filemenu.addAction(save)
        filemenu.addAction(quit)

        # Klick auf save
        button.clicked.connect(self.button_clicked)
        

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    #Quit betaetigen
        quit.triggered.connect(self.menu_quit)
    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()

    def menu_save(self):
            self.button_clicked()

    #Datei wird gespeicheicht mit Buttondruck
    def button_clicked(self):
        data = []
        data.append(self.vornameLine1.text())
        data.append(self.nameLine2.text())
        data.append(self.gebLine3.text())
        data.append(self.adrLine4.text())
        data.append(self.plzLine5.text())
        data.append(self.ortLine6.text())
        data.append(self.landLine7.currentText())

        file = open("output.txt", "w", encoding="utf-8")
        writer = csv.writer(file, delimiter=",", lineterminator="\n")
        writer.writerow(data)
        file.close()

        print("Die Datei wurde gesichert")


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()