# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Change_phone_numbereUsgyS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -20, 971, 801))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 130, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 370, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.confirm = QPushButton(self.widget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(750, 650, 181, 81))
        self.confirm.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.backB = QPushButton(self.widget)
        self.backB.setObjectName(u"backB")
        self.backB.setGeometry(QRect(50, 650, 181, 81))
        self.backB.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.NewPhoneNumber = QLineEdit(self.widget)
        self.NewPhoneNumber.setObjectName(u"NewPhoneNumber")
        self.NewPhoneNumber.setGeometry(QRect(320, 380, 211, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New phone number", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.backB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

