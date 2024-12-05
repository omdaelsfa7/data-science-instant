# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor, QBrush, QColor, QLinearGradient, QRadialGradient, QConicalGradient, QPainter, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTabWidget, QMenuBar, QStatusBar ,QLCDNumber ,QDialog ,QStackedWidget
from PyQt5.uic import loadUi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 961, 761))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 70, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.Balance = QLCDNumber(self.widget)
        self.Balance.setObjectName(u"Balance")
        self.Balance.setGeometry(QRect(270, 190, 141, 61))
        self.Balance.setLayoutDirection(Qt.LeftToRight)
        self.Balance.setStyleSheet(u"color: white ; ")
        self.Balance.setSegmentStyle(QLCDNumber.Flat)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 190, 211, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Transfer_Money_B = QPushButton(self.widget)
        self.Transfer_Money_B.setObjectName(u"Transfer_Money_B")
        self.Transfer_Money_B.setGeometry(QRect(160, 330, 181, 81))
        self.Transfer_Money_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Withdraw_B = QPushButton(self.widget)
        self.Withdraw_B.setObjectName(u"Withdraw_B")
        self.Withdraw_B.setGeometry(QRect(680, 330, 181, 81))
        self.Withdraw_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Edit_Acc_B = QPushButton(self.widget)
        self.Edit_Acc_B.setObjectName(u"Edit_Acc_B")
        self.Edit_Acc_B.setGeometry(QRect(680, 510, 181, 81))
        self.Edit_Acc_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Deposit_Money_B = QPushButton(self.widget)
        self.Deposit_Money_B.setObjectName(u"Deposit_Money_B")
        self.Deposit_Money_B.setGeometry(QRect(160, 510, 181, 81))
        self.Deposit_Money_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"current balance ", None))
        self.Transfer_Money_B.setText(QCoreApplication.translate("MainWindow", u"Transfer money", None))
        self.Withdraw_B.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.Edit_Acc_B.setText(QCoreApplication.translate("MainWindow", u"Edit account", None))
        self.Deposit_Money_B.setText(QCoreApplication.translate("MainWindow", u"Deposit money ", None))
    # retranslateUi

