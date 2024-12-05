import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMenuBar, QStatusBar, \
    QStackedWidget


class LoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.SignUpButton.clicked.connect(self.go_to_signUp)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(960, 771)
        self.setMinimumSize(960, 771)  # Set minimum size

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


class SignUpWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi()
        self.To_Login_Page_B.clicked.connect(self.go_to_login)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(961, 771)
        self.setMinimumSize(961, 771)  # Set minimum size

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    login_window = LoginWindow(stacked_widget)
    sign_up_window = SignUpWindow(stacked_widget)

    stacked_widget.addWidget(login_window)
    stacked_widget.addWidget(sign_up_window)
    stacked_widget.setCurrentIndex(0)

    stacked_widget.setWindowTitle("Bank Application")  # Set a title for the main window
    stacked_widget.resize(960, 771)  # Ensure the window starts at the desired size
    stacked_widget.show()

    sys.exit(app.exec_())
