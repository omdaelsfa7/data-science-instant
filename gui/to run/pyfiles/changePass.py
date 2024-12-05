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
        self.widget.setGeometry(QRect(0, -40, 971, 811))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 120, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 270, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Change_B = QPushButton(self.widget)
        self.Change_B.setObjectName(u"Change_B")
        self.Change_B.setGeometry(QRect(750, 650, 181, 81))
        self.Change_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Back_To_Edit_B = QPushButton(self.widget)
        self.Back_To_Edit_B.setObjectName(u"Back_To_Edit_B")
        self.Back_To_Edit_B.setGeometry(QRect(30, 650, 181, 81))
        self.Back_To_Edit_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Current_Pass = QLineEdit(self.widget)
        self.Current_Pass.setObjectName(u"Current_Pass")
        self.Current_Pass.setGeometry(QRect(310, 280, 211, 51))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 370, 261, 61))
        self.label_3.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.New_Pass = QLineEdit(self.widget)
        self.New_Pass.setObjectName(u"New_Pass")
        self.New_Pass.setGeometry(QRect(310, 380, 211, 51))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 460, 261, 61))
        self.label_4.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Confirm_New_Pass = QLineEdit(self.widget)
        self.Confirm_New_Pass.setObjectName(u"Confirm_New_Pass")
        self.Confirm_New_Pass.setGeometry(QRect(310, 470, 211, 51))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Password", None))
        self.Change_B.setText(QCoreApplication.translate("MainWindow", u"Change ", None))
        self.Back_To_Edit_B.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
    # retranslateUi

