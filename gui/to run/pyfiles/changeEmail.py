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
        self.widget.setGeometry(QRect(0, -30, 961, 871))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 120, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 370, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Confirm_B = QPushButton(self.widget)
        self.Confirm_B.setObjectName(u"Confirm_B")
        self.Confirm_B.setGeometry(QRect(760, 650, 181, 81))
        self.Confirm_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Back_To_Edit_B = QPushButton(self.widget)
        self.Back_To_Edit_B.setObjectName(u"Back_To_Edit_B")
        self.Back_To_Edit_B.setGeometry(QRect(30, 650, 181, 81))
        self.Back_To_Edit_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.New_Email = QLineEdit(self.widget)
        self.New_Email.setObjectName(u"New_Email")
        self.New_Email.setGeometry(QRect(310, 380, 211, 51))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New Email", None))
        self.Confirm_B.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.Back_To_Edit_B.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

