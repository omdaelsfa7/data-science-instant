import sys

from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor, QBrush, QColor, QLinearGradient, QRadialGradient, QConicalGradient, QPainter, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTabWidget, QMenuBar, QStatusBar ,QLCDNumber ,QDialog ,QStackedWidget
from PyQt5.uic import loadUi


class moneyTransferPage(object):
    def setupUi(self, MoneyTransferPage):
        if MoneyTransferPage.objectName():
            MoneyTransferPage.setObjectName(u"MoneyTransferPage")
        MoneyTransferPage.resize(961, 771)
        self.centralwidget = QWidget(MoneyTransferPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -70, 1021, 901))
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.Back_To_Actions_B = QPushButton(self.widget)
        self.Back_To_Actions_B.setObjectName(u"Back_To_Actions_B")
        self.Back_To_Actions_B.setGeometry(QRect(40, 700, 181, 81))
        self.Back_To_Actions_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.Complete_Transfer_B = QPushButton(self.widget)
        self.Complete_Transfer_B.setObjectName(u"Complete_Transfer_B")
        self.Complete_Transfer_B.setGeometry(QRect(770, 700, 181, 81))
        self.Complete_Transfer_B.setStyleSheet(u"font:20px ; \n"
"background-color: rgb(115, 115, 115);\n"
"color: white;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 330, 251, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Transfer_Email = QLineEdit(self.widget)
        self.Transfer_Email.setObjectName(u"Transfer_Email")
        self.Transfer_Email.setGeometry(QRect(350, 350, 191, 41))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 460, 141, 61))
        self.label_3.setStyleSheet(u"font:30px ; \n"
"color: white;")
        self.Transfer_Amount = QLineEdit(self.widget)
        self.Transfer_Amount.setObjectName(u"Transfer_Amount")
        self.Transfer_Amount.setGeometry(QRect(349, 470, 191, 41))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 130, 291, 61))
        self.label_4.setStyleSheet(u"font:40px ; \n"
"color: white;")
        self.label_4.setAlignment(Qt.AlignCenter)
        MoneyTransferPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MoneyTransferPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        MoneyTransferPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MoneyTransferPage)
        self.statusbar.setObjectName(u"statusbar")
        MoneyTransferPage.setStatusBar(self.statusbar)

        self.retranslateUi(MoneyTransferPage)

        QMetaObject.connectSlotsByName(MoneyTransferPage)
    # setupUi

    def retranslateUi(self, MoneyTransferPage):
        MoneyTransferPage.setWindowTitle(QCoreApplication.translate("MoneyTransferPage", u"MainWindow", None))
        self.Back_To_Actions_B.setText(QCoreApplication.translate("MoneyTransferPage", u"Back", None))
        self.Complete_Transfer_B.setText(QCoreApplication.translate("MoneyTransferPage", u"complete", None))
        self.label_2.setText(QCoreApplication.translate("MoneyTransferPage", u"Account email", None))
        self.label_3.setText(QCoreApplication.translate("MoneyTransferPage", u"Amount ", None))
        self.label_4.setText(QCoreApplication.translate("MoneyTransferPage", u"Money Transfer", None))
    # retranslateUi

