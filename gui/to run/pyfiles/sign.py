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
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 961, 761))
        self.widget_3.setStyleSheet(u"background-color:#404066;")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(30, 50, 901, 631))
        self.widget_4.setStyleSheet(u"background-color : white ;")
        self.Sign_Up_B = QPushButton(self.widget_4)
        self.Sign_Up_B.setObjectName(u"Sign_Up_B")
        self.Sign_Up_B.setGeometry(QRect(60, 510, 161, 41))
        self.Sign_Up_B.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font:20px;")
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 370, 111, 41))
        self.label_11.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 280, 91, 41))
        self.label_14.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 140, 191, 51))
        self.label_15.setStyleSheet(u"font:30px")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.NUemail = QLineEdit(self.widget_4)
        self.NUemail.setObjectName(u"NUemail")
        self.NUemail.setGeometry(QRect(170, 280, 171, 41))
        self.NUpass = QLineEdit(self.widget_4)
        self.NUpass.setObjectName(u"NUpass")
        self.NUpass.setGeometry(QRect(170, 370, 171, 41))
        self.To_Login_Page_B = QPushButton(self.widget_4)
        self.To_Login_Page_B.setObjectName(u"To_Login_Page_B")
        self.To_Login_Page_B.setGeometry(QRect(690, 530, 141, 41))
        self.To_Login_Page_B.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font:20px;")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 530, 151, 41))
        self.label_3.setStyleSheet(u"font-size:15px ; ")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 451, 141))
        self.label.setStyleSheet(u"font:20px ; \n"
"color: black;\n"
"background-color:white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.Phone_number = QLineEdit(self.widget_4)
        self.Phone_number.setObjectName(u"Phone_number")
        self.Phone_number.setGeometry(QRect(590, 370, 171, 41))
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(400, 370, 161, 41))
        self.label_16.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(400, 280, 161, 41))
        self.label_17.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font :20px ;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.NName = QLineEdit(self.widget_4)
        self.NName.setObjectName(u"NName")
        self.NName.setGeometry(QRect(580, 280, 171, 41))
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
        self.Sign_Up_B.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.To_Login_Page_B.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Already have acc ?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to el bank", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Full name ", None))
    # retranslateUi

