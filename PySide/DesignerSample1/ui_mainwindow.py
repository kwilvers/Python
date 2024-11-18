# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(325, 249)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 321, 181))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.gridLayoutWidget)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 1, 0, 1, 2)

        self.alarmButton = QPushButton(self.gridLayoutWidget)
        self.alarmButton.setObjectName(u"alarmButton")
        icon = QIcon()
        icon.addFile(u":/ico/D:/Icons/o_collection/o_collection_png/office/32x32/alarm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alarmButton.setIcon(icon)
        self.alarmButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.alarmButton, 0, 0, 1, 1)

        self.alarmLineEdit = QLineEdit(self.gridLayoutWidget)
        self.alarmLineEdit.setObjectName(u"alarmLineEdit")

        self.gridLayout.addWidget(self.alarmLineEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 325, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"My Label", None))
        self.alarmButton.setText(QCoreApplication.translate("MainWindow", u"Alarme", None))
    # retranslateUi

