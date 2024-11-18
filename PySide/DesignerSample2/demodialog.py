import sys
from typing import Optional
from PySide6 import QtWidgets, QtCore
from ui_demodialog import *

class DemoDialog(QDialog, Ui_DemoDialog):
    
    def __init__(self, *args, **kwargs):
        super(DemoDialog, self).__init__()
        self.setupUi(self)
        self.helloPushButton.pressed.connect(self.SayHello)
        self.helloSpinBox.valueChanged.connect(self.helloChange)

    def SayHello(self):
        self.helloLineEdit.setText("Bonjour pyside6")

    def helloChange(self):
        v = self.helloSpinBox.value()
        self.helloLcdNumber.display(v)

app = QtWidgets.QApplication(sys.argv)
demo = DemoDialog()
demo.show()

app.exec()
