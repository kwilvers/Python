from PySide6 import QtWidgets
from PySide6.QtCore import *
from Ui_MainWindow import *
import time
import sys

#Pyside, QThread, Signal

class MoteurDc(QThread):
    ReportValue = Signal(tuple)

    def __init__(self, parent = None):
        QThread.__init__(self, parent)

    # Signale qu’une donnée est arrivée
    def NotifyNewValues(self, data):        
        self.ReportValue.emit((data, "Hello"))
    
    # Simule le fonctionnement d’un thread
    def run(self):
        for i in range(3):
            print(i)
            self.NotifyNewValues(i)
            time.sleep(1)


class MainWindowMotor(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindowMotor, self).__init__()
        self.setupUi(self)
        self.bStop.pressed.connect(self.onButonStop)
        # Instanciation d'un MoteurDc et connection au signal
        self.myMotor = MoteurDc()
        self.myMotor.ReportValue.connect(self.ReportSpeed)

    def onButonStop(self):
        self.myMotor.start() #démarrage du thread

    def ReportSpeed(self, data):
        self.leText.setText(f"{data[0]} - {data[1]}")


app = QtWidgets.QApplication(sys.argv)
main = MainWindowMotor()
main.show()
app.exec()
