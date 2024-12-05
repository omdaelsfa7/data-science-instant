import sys
import sqlite3
from PyQt5.QtCore import (Qt,QRect ,QMetaObject,QCoreApplication,QSize)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QLabel,QLineEdit,QPushButton,QMenuBar,QStatusBar,QStackedWidget,QLCDNumber,QMessageBox,)


def show_success_message(self):

        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("done :)    ")
        msg_box.setWindowTitle("Success")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

def show_error_message(self):

        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("error :)    ")
        msg_box.setWindowTitle("error")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

conn = sqlite3.connect('atm.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        full_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone_number INTEGER NOT NULL,
        balance INTEGER 
    )
''')

conn.commit()
conn.close()
conn = sqlite3.connect('atm.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS balance (
        amount INTEGER NOT NULL
    )
''')

conn.commit()
conn.close()



def insert_user(fullname, phonenumber, password, email):
    conn = sqlite3.connect('atm.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (full_name, phone_number, password, email) 
        VALUES (?, ?, ?, ?)
    ''', (fullname, phonenumber, password, email))
    conn.commit()
    conn.close()


class LoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.SignUpButton.clicked.connect(self.go_to_signUp)
        self.Login_B.clicked.connect(self.checkLogin)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(960, 771)
        self.setMinimumSize(960, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setGeometry(QRect(0, 0, 961, 741))
        self.widget_3.setStyleSheet("background-color:#404066;")

        self.label = QLabel("Welcome to el bank", self.widget_3)
        self.label.setGeometry(QRect(120, 150, 331, 141))
        self.label.setStyleSheet("font:30px; color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setGeometry(QRect(620, 70, 301, 581))
        self.widget_4.setStyleSheet("background-color: white;")

        self.Login_B = QPushButton("LOGIN", self.widget_4)
        self.Login_B.setGeometry(QRect(60, 460, 161, 41))
        self.Login_B.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")

        self.label_11 = QLabel("password", self.widget_4)
        self.label_11.setGeometry(QRect(10, 310, 91, 41))
        self.label_11.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.label_14 = QLabel("email", self.widget_4)
        self.label_14.setGeometry(QRect(10, 210, 81, 41))
        self.label_14.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.label_15 = QLabel("User LOGIN", self.widget_4)
        self.label_15.setGeometry(QRect(60, 60, 191, 51))
        self.label_15.setStyleSheet("font:30px")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.Uemail = QLineEdit(self.widget_4)
        self.Uemail.setGeometry(QRect(110, 210, 171, 41))

        self.Upass = QLineEdit(self.widget_4)
        self.Upass.setGeometry(QRect(110, 310, 171, 41))

        self.SignUpButton = QPushButton("SIGN UP", self.widget_4)
        self.SignUpButton.setGeometry(QRect(210, 390, 81, 31))
        self.SignUpButton.setStyleSheet("background-color: rgb(204, 204, 204); font:10px;")

        self.label_3 = QLabel("Dont have an acc", self.widget_4)
        self.label_3.setGeometry(QRect(60, 389, 151, 31))
        self.label_3.setStyleSheet("font-size:15px;")

        self.label_5 = QLabel("made by\nAhmed \nOmar \nAdham \nAhmed", self.widget_3)
        self.label_5.setGeometry(QRect(0, 550, 211, 191))
        self.label_5.setStyleSheet("font:20px; color:white;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.label_7 = QLabel("made since 2024 ( in 4days)", self.widget_3)
        self.label_7.setGeometry(QRect(180, 250, 281, 51))
        self.label_7.setStyleSheet("font:15px; color:white;")

        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

    def go_to_signUp(self):
        self.stacked_widget.setCurrentIndex(1)

    def checkLogin(self):
        # self.stacked_widget.setCurrentIndex(2)
        pass

class SignUpWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.To_Login_Page_B.clicked.connect(self.go_to_login)
        self.Sign_Up_B.clicked.connect(self.signUp)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)  

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setGeometry(QRect(0, 0, 961, 761))
        self.widget_3.setStyleSheet("background-color:#404066;")

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setGeometry(QRect(30, 50, 901, 631))
        self.widget_4.setStyleSheet("background-color: white;")

        self.Sign_Up_B = QPushButton("Sign up", self.widget_4)
        self.Sign_Up_B.setGeometry(QRect(60, 510, 161, 41))
        self.Sign_Up_B.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")

        self.label_11 = QLabel("password", self.widget_4)
        self.label_11.setGeometry(QRect(30, 370, 111, 41))
        self.label_11.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.label_14 = QLabel("email", self.widget_4)
        self.label_14.setGeometry(QRect(30, 280, 91, 41))
        self.label_14.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.label_15 = QLabel("Sign Up", self.widget_4)
        self.label_15.setGeometry(QRect(20, 140, 191, 51))
        self.label_15.setStyleSheet("font:30px")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.NUemail = QLineEdit(self.widget_4)
        self.NUemail.setGeometry(QRect(170, 280, 171, 41))

        self.NUpass = QLineEdit(self.widget_4)
        self.NUpass.setGeometry(QRect(170, 370, 171, 41))

        self.To_Login_Page_B = QPushButton("Login", self.widget_4)
        self.To_Login_Page_B.setGeometry(QRect(690, 530, 141, 41))
        self.To_Login_Page_B.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")

        self.label_3 = QLabel("Already have acc ?", self.widget_4)
        self.label_3.setGeometry(QRect(540, 530, 151, 41))
        self.label_3.setStyleSheet("font-size:15px;")

        self.label = QLabel("Welcome to el bank", self.widget_4)
        self.label.setGeometry(QRect(210, 40, 451, 141))
        self.label.setStyleSheet("font:20px; color: black; background-color:white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.Phone_number = QLineEdit(self.widget_4)
        self.Phone_number.setGeometry(QRect(590, 370, 171, 41))

        self.label_16 = QLabel("Phone number", self.widget_4)
        self.label_16.setGeometry(QRect(400, 370, 161, 41))
        self.label_16.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.label_17 = QLabel("Full name", self.widget_4)
        self.label_17.setGeometry(QRect(400, 280, 161, 41))
        self.label_17.setStyleSheet("background-color: rgb(204, 204, 204); font:20px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.NName = QLineEdit(self.widget_4)
        self.NName.setGeometry(QRect(580, 280, 171, 41))

        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(0)


    def signUp(self):
        try:
            insert_user(self.NName.text() , self.Phone_number.text() , self.NUpass.text() ,self.NUemail.text())
            show_success_message(self)
            self.stacked_widget.setCurrentIndex(0)

        except:
            show_error_message(self)
            

class actionsWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Transfer_Money_B.clicked.connect(self.go_to_transferMoney)
        self.Withdraw_B.clicked.connect(self.go_to_withdrawMonaey)
        self.Deposit_Money_B.clicked.connect(self.go_to_deposit)
        self.Edit_Acc_B.clicked.connect(self.go_to_edit)
    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 961, 761))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 70, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
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
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Transfer_Money_B = QPushButton(self.widget)
        self.Transfer_Money_B.setObjectName(u"Transfer_Money_B")
        self.Transfer_Money_B.setGeometry(QRect(160, 330, 181, 81))
        self.Transfer_Money_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Withdraw_B = QPushButton(self.widget)
        self.Withdraw_B.setObjectName(u"Withdraw_B")
        self.Withdraw_B.setGeometry(QRect(680, 330, 181, 81))
        self.Withdraw_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Edit_Acc_B = QPushButton(self.widget)
        self.Edit_Acc_B.setObjectName(u"Edit_Acc_B")
        self.Edit_Acc_B.setGeometry(QRect(680, 510, 181, 81))
        self.Edit_Acc_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Deposit_Money_B = QPushButton(self.widget)
        self.Deposit_Money_B.setObjectName(u"Deposit_Money_B")
        self.Deposit_Money_B.setGeometry(QRect(160, 510, 181, 81))
        self.Deposit_Money_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()



    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"current balance ", None))
        self.Transfer_Money_B.setText(QCoreApplication.translate("MainWindow", u"Transfer money", None))
        self.Withdraw_B.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.Edit_Acc_B.setText(QCoreApplication.translate("MainWindow", u"Edit account", None))
        self.Deposit_Money_B.setText(QCoreApplication.translate("MainWindow", u"Deposit money ", None))

    def go_to_transferMoney(self) :
        self.stacked_widget.setCurrentIndex(3)
    def go_to_withdrawMonaey(self) :
        self.stacked_widget.setCurrentIndex(4)
    def go_to_deposit(self):
        self.stacked_widget.setCurrentIndex(5)
    def go_to_edit(self):
        self.stacked_widget.setCurrentIndex(6)
    
class withdrawWindow(QMainWindow):

    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Actions_B.clicked.connect(self.go_to_actions)
        self.Withdraw_B.clicked.connect(self.withdraw)

    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(0, -10, 971, 801))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 100, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 370, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Withdraw_B = QPushButton(self.widget)
        self.Withdraw_B.setObjectName(u"Withdraw_B")
        self.Withdraw_B.setGeometry(QRect(750, 630, 181, 81))
        self.Withdraw_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Back_To_Actions_B = QPushButton(self.widget)
        self.Back_To_Actions_B.setObjectName(u"Back_To_Actions_B")
        self.Back_To_Actions_B.setGeometry(QRect(30, 630, 181, 81))
        self.Back_To_Actions_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Withdraw_Amount = QLineEdit(self.widget)
        self.Withdraw_Amount.setObjectName(u"Withdraw_Amount")
        self.Withdraw_Amount.setGeometry(QRect(310, 380, 211, 51))

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome user1"))
        self.label_2.setText(_translate("MainWindow", "Withdraw amount"))
        self.Withdraw_B.setText(_translate("MainWindow", "Withdraw"))
        self.Back_To_Actions_B.setText(_translate("MainWindow", "Back"))

    def go_to_actions(self):
        self.stacked_widget.setCurrentIndex(2)
    
    def withdraw(self):
        pass
    
class depositWindow(QMainWindow):
    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.backB.clicked.connect(self.go_to_actions)
        self.Deposit_Confirm_B.clicked.connect(self.deposit)

    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -30, 961, 781))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 140, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 390, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Deposit_Confirm_B = QPushButton(self.widget)
        self.Deposit_Confirm_B.setObjectName(u"Deposit_Confirm_B")
        self.Deposit_Confirm_B.setGeometry(QRect(760, 650, 181, 81))
        self.Deposit_Confirm_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.backB = QPushButton(self.widget)
        self.backB.setObjectName(u"Back")
        self.backB.setGeometry(QRect(40, 650, 181, 81))
        self.backB.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Deposit_Amount = QLineEdit(self.widget)
        self.Deposit_Amount.setObjectName(u"Deposit_Amount")
        self.Deposit_Amount.setGeometry(QRect(290, 390, 211, 51))

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Deposit Window"))
        self.label.setText(_translate("MainWindow", "Welcome user1"))
        self.label_2.setText(_translate("MainWindow", "Deposit amount"))
        self.Deposit_Confirm_B.setText(_translate("MainWindow", "Deposit"))
        self.backB.setText(_translate("MainWindow", "Back"))

    def go_to_actions(self):

        self.stacked_widget.setCurrentIndex(2) 

    
    def deposit(self):
        ##############database
        show_success_message(self)
        self.go_to_actions()

class transferWindow(QMainWindow):

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Actions_B.clicked.connect(self.go_to_actions)
        self.Complete_Transfer_B.clicked.connect(self.transfer)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -80 , 970, 1000))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.Back_To_Actions_B = QPushButton(self.widget)
        self.Back_To_Actions_B.setObjectName(u"Back_To_Actions_B")
        self.Back_To_Actions_B.setGeometry(QRect(40, 700, 181, 81))
        self.Back_To_Actions_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Complete_Transfer_B = QPushButton(self.widget)
        self.Complete_Transfer_B.setObjectName(u"Complete_Transfer_B")
        self.Complete_Transfer_B.setGeometry(QRect(770, 700, 181, 81))
        self.Complete_Transfer_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 330, 251, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Transfer_Email = QLineEdit(self.widget)
        self.Transfer_Email.setObjectName(u"Transfer_Email")
        self.Transfer_Email.setGeometry(QRect(350, 350, 191, 41))

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 460, 141, 61))
        self.label_3.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Transfer_Amount = QLineEdit(self.widget)
        self.Transfer_Amount.setObjectName(u"Transfer_Amount")
        self.Transfer_Amount.setGeometry(QRect(349, 470, 191, 41))

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 130, 291, 61))
        self.label_4.setStyleSheet(u"font:40px ; \n""color: white;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MoneyTransferPage", "Money Transfer Page"))
        self.Back_To_Actions_B.setText(_translate("MoneyTransferPage", "Back"))
        self.Complete_Transfer_B.setText(_translate("MoneyTransferPage", "Complete"))
        self.label_2.setText(_translate("MoneyTransferPage", "Account Email"))
        self.label_3.setText(_translate("MoneyTransferPage", "Amount"))
        self.label_4.setText(_translate("MoneyTransferPage", "Money Transfer"))

    def go_to_actions(self):
        self.stacked_widget.setCurrentIndex(2)

    def transfer(self,amount):
        conn = sqlite3.connect('atm.db')
        c = conn.cursor()
        c.execute('''
        INSERT INTO balance (amount) 
        VALUES (?, ?, ?, ?)
        ''', (amount))
        conn.commit()
        conn.close()
        show_success_message(self)
        self.go_to_actions()
        
class editWindow(QMainWindow):
    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Actions_B.clicked.connect(self.go_to_actions)
        self.Change_Email_B.clicked.connect(self.goto_email)
        self.Change_Name_B.clicked.connect(self.goto_name)
        self.Change_Number_B.clicked.connect(self.goto_number)
        self.Change_Pass_B.clicked.connect(self.goto_pass)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -30, 971, 761))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 110, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.Change_Name_B = QPushButton(self.widget)
        self.Change_Name_B.setObjectName(u"Change_Name_B")
        self.Change_Name_B.setGeometry(QRect(140, 310, 181, 81))
        self.Change_Name_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")
        self.Change_Email_B = QPushButton(self.widget)
        self.Change_Email_B.setObjectName(u"Change_Email_B")
        self.Change_Email_B.setGeometry(QRect(610, 310, 181, 81))
        self.Change_Email_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Change_Number_B = QPushButton(self.widget)
        self.Change_Number_B.setObjectName(u"Change_Number_B")
        self.Change_Number_B.setGeometry(QRect(620, 480, 181, 81))
        self.Change_Number_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Change_Pass_B = QPushButton(self.widget)
        self.Change_Pass_B.setObjectName(u"Change_Pass_B")
        self.Change_Pass_B.setGeometry(QRect(140, 480, 181, 81))
        self.Change_Pass_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Back_To_Actions_B = QPushButton(self.widget)
        self.Back_To_Actions_B.setObjectName(u"Back_To_Actions_B")
        self.Back_To_Actions_B.setGeometry(QRect(20, 660, 171, 61))
        self.Back_To_Actions_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("ChangeDetailsPage", "Change Details"))
        self.label.setText(_translate("ChangeDetailsPage", "Welcome user1"))
        self.Change_Name_B.setText(_translate("ChangeDetailsPage", "Change Name"))
        self.Change_Email_B.setText(_translate("ChangeDetailsPage", "Change Email"))
        self.Change_Number_B.setText(_translate("ChangeDetailsPage", "Change Number"))
        self.Change_Pass_B.setText(_translate("ChangeDetailsPage", "Change Pass"))
        self.Back_To_Actions_B.setText(_translate("ChangeDetailsPage", "Back"))

    def go_to_actions(self):
        self.stacked_widget.setCurrentIndex(2)
    def goto_email(self):
        self.stacked_widget.setCurrentIndex(9)
    def goto_name(self):
        self.stacked_widget.setCurrentIndex(7)
    def goto_number(self):
        self.stacked_widget.setCurrentIndex(10)
    def goto_pass(self):
        self.stacked_widget.setCurrentIndex(8)

class changePhoneWindow(QMainWindow):

    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.backB.clicked.connect(self.goto_edit)
        self.confirm.clicked.connect(self.change)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -20, 971, 801))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 130, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 370, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.confirm = QPushButton(self.widget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(750, 650, 181, 81))
        self.confirm.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")
        
        self.backB = QPushButton(self.widget)
        self.backB.setObjectName(u"backB")
        self.backB.setGeometry(QRect(50, 650, 181, 81))
        self.backB.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.NewPhoneNumber = QLineEdit(self.widget)
        self.NewPhoneNumber.setObjectName(u"NewPhoneNumber")
        self.NewPhoneNumber.setGeometry(QRect(320, 380, 211, 51))

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"change phone number", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New phone number", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.backB.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    
    def goto_edit(self):
        self.stacked_widget.setCurrentIndex(6)

    def change(self):
        show_success_message(self)

class changePassWindow(QMainWindow):

    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Edit_B.clicked.connect(self.goto_edit)
        self.Change_B.clicked.connect(self.change)

    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -40, 971, 811))
        self.widget.setStyleSheet(u"background-color:#404066;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 120, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 270, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Change_B = QPushButton(self.widget)
        self.Change_B.setObjectName(u"Change_B")
        self.Change_B.setGeometry(QRect(750, 650, 181, 81))
        self.Change_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Back_To_Edit_B = QPushButton(self.widget)
        self.Back_To_Edit_B.setObjectName(u"Back_To_Edit_B")
        self.Back_To_Edit_B.setGeometry(QRect(30, 650, 181, 81))
        self.Back_To_Edit_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Current_Pass = QLineEdit(self.widget)
        self.Current_Pass.setObjectName(u"Current_Pass")
        self.Current_Pass.setGeometry(QRect(310, 280, 211, 51))

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 370, 261, 61))
        self.label_3.setStyleSheet(u"font:30px ; \n""color: white;")

        self.New_Pass = QLineEdit(self.widget)
        self.New_Pass.setObjectName(u"New_Pass")
        self.New_Pass.setGeometry(QRect(310, 380, 211, 51))

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 460, 261, 61))
        self.label_4.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Confirm_New_Pass = QLineEdit(self.widget)
        self.Confirm_New_Pass.setObjectName(u"Confirm_New_Pass")
        self.Confirm_New_Pass.setGeometry(QRect(310, 470, 211, 51))

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Current Password", None))
        self.Change_B.setText(QCoreApplication.translate("MainWindow", "Change", None))
        self.Back_To_Edit_B.setText(QCoreApplication.translate("MainWindow", "Back", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "New Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Confirm Password", None))
    
    def goto_edit(self):
        self.stacked_widget.setCurrentIndex(6)

    def change(self):
        show_success_message(self)

class changeNameWindow(QMainWindow):

    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Edit_B.clicked.connect(self.goto_edit)
        self.Confirm_Change_B.clicked.connect(self.change)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 961, 771))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 100, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 340, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Confirm_Change_B = QPushButton(self.widget)
        self.Confirm_Change_B.setObjectName(u"Confirm_Change_B")
        self.Confirm_Change_B.setGeometry(QRect(720, 600, 181, 81))
        self.Confirm_Change_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Back_To_Edit_B = QPushButton(self.widget)
        self.Back_To_Edit_B.setObjectName(u"Back_To_Edit_B")
        self.Back_To_Edit_B.setGeometry(QRect(40, 600, 181, 81))
        self.Back_To_Edit_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.New_Name = QLineEdit(self.widget)
        self.New_Name.setObjectName(u"New_Name")
        self.New_Name.setGeometry(QRect(350, 350, 211, 51))

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Change Username", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "New Name", None))
        self.Confirm_Change_B.setText(QCoreApplication.translate("MainWindow", "Confirm", None))
        self.Back_To_Edit_B.setText(QCoreApplication.translate("MainWindow", "Back", None))

    def goto_edit(self):
        self.stacked_widget.setCurrentIndex(6)
    
    def change(self):
        show_success_message(self)

class changeEmailWindow(QMainWindow):

    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.Back_To_Edit_B.clicked.connect(self.goto_edit)
        self.Confirm_B.clicked.connect(self.change)

    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -30, 961, 871))
        self.widget.setStyleSheet(u"background-color:#404066;")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 120, 291, 71))
        self.label.setStyleSheet(u"font:30px ; \n""color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 370, 261, 61))
        self.label_2.setStyleSheet(u"font:30px ; \n""color: white;")

        self.Confirm_B = QPushButton(self.widget)
        self.Confirm_B.setObjectName(u"Confirm_B")
        self.Confirm_B.setGeometry(QRect(760, 650, 181, 81))
        self.Confirm_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.Back_To_Edit_B = QPushButton(self.widget)
        self.Back_To_Edit_B.setObjectName(u"Back_To_Edit_B")
        self.Back_To_Edit_B.setGeometry(QRect(30, 650, 181, 81))
        self.Back_To_Edit_B.setStyleSheet(u"font:20px ; \n""background-color: rgb(115, 115, 115);\n""color: white;")

        self.New_Email = QLineEdit(self.widget)
        self.New_Email.setObjectName(u"New_Email")
        self.New_Email.setGeometry(QRect(310, 380, 211, 51))

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Change Email", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Welcome user1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "New Email", None))
        self.Confirm_B.setText(QCoreApplication.translate("MainWindow", "Confirm", None))
        self.Back_To_Edit_B.setText(QCoreApplication.translate("MainWindow", "Back", None))
    
    def goto_edit(self):
        self.stacked_widget.setCurrentIndex(6)

    def change(self) :
        show_success_message(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    login_window = LoginWindow(stacked_widget)
    sign_up_window = SignUpWindow(stacked_widget)
    actions_Window = actionsWindow(stacked_widget)
    transfer_window = transferWindow(stacked_widget)
    withdraw_window = withdrawWindow(stacked_widget)
    deposit_window =  depositWindow(stacked_widget)
    edit_window = editWindow(stacked_widget)
    Cname_window = changeNameWindow(stacked_widget)
    Cpass_window = changePassWindow(stacked_widget)
    Cemail_window = changeEmailWindow(stacked_widget)
    CphoneNumber = changePhoneWindow(stacked_widget)

    stacked_widget.addWidget(login_window)
    stacked_widget.addWidget(sign_up_window)
    stacked_widget.addWidget(actions_Window)
    stacked_widget.addWidget(transfer_window)
    stacked_widget.addWidget(withdraw_window)
    stacked_widget.addWidget(deposit_window)
    stacked_widget.addWidget(edit_window)
    stacked_widget.addWidget(Cname_window)
    stacked_widget.addWidget(Cpass_window)
    stacked_widget.addWidget(Cemail_window)
    stacked_widget.addWidget(CphoneNumber)


    stacked_widget.setCurrentIndex(0)

    stacked_widget.setWindowTitle("Bank Application")  
    stacked_widget.resize(960, 771)
    stacked_widget.show()

    sys.exit(app.exec_())
