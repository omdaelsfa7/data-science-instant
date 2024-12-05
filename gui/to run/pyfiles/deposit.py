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
        self.widget.setGeometry(QRect(0, -30, 961, 781))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 140, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 390, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Deposit_Confirm_B = QPushButton(self.widget)
        self.Deposit_Confirm_B.setObjectName(u"Deposit_Confirm_B")
        self.Deposit_Confirm_B.setGeometry(QRect(760, 650, 181, 81))
        self.Deposit_Confirm_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 650, 181, 81))
        self.pushButton_3.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Deposit_Amount = QLineEdit(self.widget)
        self.Deposit_Amount.setObjectName(u"Deposit_Amount")
        self.Deposit_Amount.setGeometry(QRect(290, 390, 211, 51))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Deposit amount ", None))
        self.Deposit_Confirm_B.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

