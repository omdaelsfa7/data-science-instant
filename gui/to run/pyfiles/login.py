import sys

from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor, QBrush, QColor, QLinearGradient, QRadialGradient, QConicalGradient, QPainter, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTabWidget, QMenuBar, QStatusBar ,QLCDNumber ,QDialog ,QStackedWidget
from PyQt5.uic import loadUi


class loginWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 961, 741))
        self.widget_3.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 150, 331, 141))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(620, 70, 301, 581))
        self.widget_4.setStyleSheet(u"background-color : white ;")
        self.Login_B = QPushButton(self.widget_4)
        self.Login_B.setObjectName(u"Login_B")
        self.Login_B.setGeometry(QRect(60, 460, 161, 41))
        self.Login_B.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font:20px;")
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 310, 91, 41))
        self.label_11.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 210, 81, 41))
        self.label_14.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 60, 191, 51))
        self.label_15.setStyleSheet(u"font:30px")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.Uemail = QLineEdit(self.widget_4)
        self.Uemail.setObjectName(u"Uemail")
        self.Uemail.setGeometry(QRect(110, 210, 171, 41))
        self.Upass = QLineEdit(self.widget_4)
        self.Upass.setObjectName(u"Upass")
        self.Upass.setGeometry(QRect(110, 310, 171, 41))
        self.SignUpButton = QPushButton(self.widget_4)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setGeometry(QRect(210, 390, 81, 31))
        self.SignUpButton.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font:10px;")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 389, 151, 31))
        self.label_3.setStyleSheet(u"font-size:15px ; ")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 550, 211, 191))
        self.label_5.setStyleSheet(u"font:20px ; \n"
"color:white ;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 250, 281, 51))
        self.label_7.setStyleSheet(u"font:15px ; \n"
"color:white ;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to el bank", None))
        self.Login_B.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"User LOGIN", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dont have an acc ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"made by\n"
"Ahmed \n"
"Omar \n"
"Adham \n"
"Ahmed \n"
"", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"made since 2024 ( in 4days)", None))

    
