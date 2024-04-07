#uebung04
import sys
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
        vornameLine1 = QLineEdit()
        nameLabel2 = QLabel("Name:")
        nameLine2 = QLineEdit()
        gebLabel3 = QLabel("Geburtstag:")
        gebLine3 = QDateEdit()
        adrLabel4 = QLabel("Adresse:")
        adrLine4 = QLineEdit()
        plzLabel5 = QLabel("Postleitzahl:")
        plzLine5 = QLineEdit()
        ortLabel6 = QLabel("Ort:")
        ortLine6 = QLineEdit()
        landLabel7 = QLabel("Land:")
        landLine7 = QComboBox()
        button = QPushButton("Save")

        # Widgets mit Grid-Koordinaten dem Layout hinzufügen
        layout.addWidget(vornameLabel1, 0, 0)
        layout.addWidget(vornameLine1, 0, 1)
        layout.addWidget(nameLabel2, 1, 0)
        layout.addWidget(nameLine2, 1, 1)
        layout.addWidget(gebLabel3, 2, 0)
        layout.addWidget(gebLine3, 2, 1)
        layout.addWidget(adrLabel4, 3, 0)
        layout.addWidget(adrLine4, 3, 1)
        layout.addWidget(plzLabel5, 4, 0)
        layout.addWidget(plzLine5, 4, 1)
        layout.addWidget(ortLabel6, 5, 0)
        layout.addWidget(ortLine6, 5, 1)
        layout.addWidget(landLabel7, 6, 0)
        layout.addWidget(landLine7, 6, 1)
        layout.addWidget(button, 7, 1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Länderauswahl hinzufügen
        landLine7.addItems(["Schweiz", "Deutschland", "Österreich"])

        #Menu erstellen
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        quit = QAction("Quit", self)
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

    #Datei wird gespeicheicht mit Button
    def button_clicked(self):
        self.lineEdits = {}
        data = []
        for key, lineEdit in self.lineEdits.items():
            data.append(lineEdit.text())
            data.append(self.gebLine3.currentText())
            data.append(self.comboBox.currentText())
        with open('output.txt', 'w') as file:
            file.write(','.join(data))
        print("Die Datei wurde gesichert")


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()