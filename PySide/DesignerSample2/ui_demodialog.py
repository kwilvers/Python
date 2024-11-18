# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demodialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLCDNumber, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_DemoDialog(object):
    def setupUi(self, DemoDialog):
        if not DemoDialog.objectName():
            DemoDialog.setObjectName(u"DemoDialog")
        DemoDialog.resize(340, 187)
        self.helloPushButton = QPushButton(DemoDialog)
        self.helloPushButton.setObjectName(u"helloPushButton")
        self.helloPushButton.setGeometry(QRect(80, 20, 75, 24))
        self.helloLineEdit = QLineEdit(DemoDialog)
        self.helloLineEdit.setObjectName(u"helloLineEdit")
        self.helloLineEdit.setGeometry(QRect(60, 60, 113, 21))
        self.helloSpinBox = QSpinBox(DemoDialog)
        self.helloSpinBox.setObjectName(u"helloSpinBox")
        self.helloSpinBox.setGeometry(QRect(60, 110, 111, 22))
        self.helloLcdNumber = QLCDNumber(DemoDialog)
        self.helloLcdNumber.setObjectName(u"helloLcdNumber")
        self.helloLcdNumber.setGeometry(QRect(220, 50, 101, 81))

        self.retranslateUi(DemoDialog)

        QMetaObject.connectSlotsByName(DemoDialog)
    # setupUi

    def retranslateUi(self, DemoDialog):
        DemoDialog.setWindowTitle(QCoreApplication.translate("DemoDialog", u"Dialog", None))
        self.helloPushButton.setText(QCoreApplication.translate("DemoDialog", u"Hello", None))
    # retranslateUi

