import sys
from PySide6 import QtCore
from PySide6.QtWidgets import *
from functools import partial

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Ma première application")
        layout = QGridLayout(self)
        btn = QPushButton("My button")
        layout.addWidget(btn, 0, 0)  
        btn.clicked.connect(partial(self.say_hello, 1))

    def say_hello(self, entier): 
        dialog = QFileDialog(self)
        # Plusieur fichier possible
        dialog.setFileMode(QFileDialog.AnyFile)
        # Filtre certain types de fichier
        dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            # Récupère la liste des fichiers
            fileNames = dialog.selectedFiles()
            for f in fileNames:
                print(f)

# Déclaration de l'application
app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()