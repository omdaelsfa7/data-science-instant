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
        self.widget.setGeometry(QRect(0, -30, 971, 761))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 110, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.Change_Name_B = QPushButton(self.widget)
        self.Change_Name_B.setObjectName(u"Change_Name_B")
        self.Change_Name_B.setGeometry(QRect(140, 310, 181, 81))
        self.Change_Name_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Change_Email_B = QPushButton(self.widget)
        self.Change_Email_B.setObjectName(u"Change_Email_B")
        self.Change_Email_B.setGeometry(QRect(610, 310, 181, 81))
        self.Change_Email_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Change_Number_B = QPushButton(self.widget)
        self.Change_Number_B.setObjectName(u"Change_Number_B")
        self.Change_Number_B.setGeometry(QRect(620, 480, 181, 81))
        self.Change_Number_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Change_Pass_B = QPushButton(self.widget)
        self.Change_Pass_B.setObjectName(u"Change_Pass_B")
        self.Change_Pass_B.setGeometry(QRect(140, 480, 181, 81))
        self.Change_Pass_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Back_To_Actions_B = QPushButton(self.widget)
        self.Back_To_Actions_B.setObjectName(u"Back_To_Actions_B")
        self.Back_To_Actions_B.setGeometry(QRect(20, 660, 171, 61))
        self.Back_To_Actions_B.setStyleSheet(u"font:20px ; \n"
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
        self.Change_Name_B.setText(QCoreApplication.translate("MainWindow", u"Change Name", None))
        self.Change_Email_B.setText(QCoreApplication.translate("MainWindow", u"Change Email", None))
        self.Change_Number_B.setText(QCoreApplication.translate("MainWindow", u"Change Number", None))
        self.Change_Pass_B.setText(QCoreApplication.translate("MainWindow", u"Change pass", None))
        self.Back_To_Actions_B.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

