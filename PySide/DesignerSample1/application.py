import sys
from PySide6 import QtWidgets, QtCore
from ui_mainwindow import Ui_MainWindow

# Notre classe hérite de la fenêtre générée : Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # La fonction setupUi doit être invoquée pour créer 
        # les contrôles, fonction du fichier .py généré
        self.setupUi(self)

        # il est maintenant possible de connecter un bouton
        # à une fonction de notre classe
        self.alarmButton.pressed.connect(self.onAlarmButton)

        # Affichage de la fenêtre
        self.show()

    def onAlarmButton(self):
        # Utilisation de la zone d'édition de la fenêtre générée
        self.alarmLineEdit.setText("Hello World")

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()