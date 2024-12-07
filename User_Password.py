import sys
from PyQt6.QtWidgets import (QApplication, QPushButton, QLabel, QLineEdit, QVBoxLayout,
                             QMainWindow, QWidget)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class Login_Account(QWidget):
    def __init__(self, show_register):
        super().__init__()
        self.setWindowTitle("Login")

        #self.setWindowTitle("Username__n__Password")
        self.setWindowIcon(QIcon("C:/users/thall/Downloads/Ayodhya_Ram_Mandir_Inauguration_Day_Picture.jpg"))
        

        layout = QVBoxLayout(self)

        self.label1 = QLabel("Username: ")
        self.label2 = QLabel("Password: ")
        self.label3 = QLabel("Don't have an account ? ")
        self.label3.setStyleSheet("color : blue;")

        self.input1 = QLineEdit(self)
        #self.input1.setFixedSize(170, 25)
        self.input1.setPlaceholderText("username")
        self.input2 = QLineEdit(self)
        #self.input2.setFixedSize(170, 25)
        self.input2.setPlaceholderText("password")
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_but = QPushButton("Login", self)
        self.login_but.setFixedSize(70, 30)
        self.login_but.clicked.connect(self.login)

        # This line connects the "Create Account" button to the show_register method in the Window class
        self.register_but = QPushButton("Create Account", self)
        #self.login_but.setFixedSize(70, 30)
        self.register_but.setFixedWidth(100)
        self.register_but.clicked.connect(show_register)


        self.output_label = QLabel("")

        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        #layout.addWidget(self.login_but)
        
        layout.addWidget(self.login_but, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label3)
        layout.addWidget(self.label3, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.register_but, alignment=Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.register_but)
        
        layout.addWidget(self.output_label)


        



        self.setLayout(layout)
        self.new_dict = {}


    def login(self):
        username = self.input1.text().strip()
        password = self.input2.text().strip()
        if username in self.new_dict and self.new_dict[username] == password:
            self.output_label.setText('Login Successful, Welcome Back')
            self.output_label.setStyleSheet(""" color : green; """)
            self.input1.clear()
            self.input2.clear()
        else:
            self.output_label.setText('Wrong username or password, try again')
            self.output_label.setStyleSheet(""" color : red; """)

    def set_data_dict(self, data_dict):
            self.new_dict = data_dict



class Register_Account(QWidget):
    def __init__(self, show_login_call):
        super().__init__()
        self.setWindowTitle("New Registration")
        self.setWindowIcon(QIcon("C:/users/thall/Downloads/Ayodhya_Ram_Mandir_Inauguration_Day_Picture.jpg"))

        layout = QVBoxLayout(self)

        self.label1 = QLabel("Username: ")
        self.label2 = QLabel("Password: ")

        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Enter Username")
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Enter Password")
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_but = QPushButton("Register", self)
        self.register_but.clicked.connect(self.register)


        self.login_but = QPushButton("Back to Login", self)
        # This line connects the "Back to Login" button to the show_login_call method in the Window class
        self.login_but.clicked.connect(show_login_call)

        self.output_label = QLabel("")

        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        #layout.addWidget(self.login_but)
        #layout.addWidget(self.register_but)
        layout.addWidget(self.register_but, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.login_but, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output_label)

        
        
        


        self.setLayout(layout)
        self.new_dict = {}
    
    def register(self):
        username = self.input1.text().strip()
        password = self.input2.text().strip()

        if not username or not password:
            self.output_label.setText('Please fill both fields properly')
            self.output_label.setStyleSheet(""" color : red; """)
            return

        if username in self.new_dict:
            self.output_label.setText("Username is already taken, Please choose another username")
            self.output_label.setStyleSheet(""" color : red; """)
            return

        if not self.password_check(password):
            return

        self.new_dict[username] = password
        self.output_label.setText("New User created Successfully")
        self.output_label.setStyleSheet(""" color : green; """)
        self.input1.clear()
        self.input2.clear()

    def set_data_dict(self, data_dict):
        self.new_dict = data_dict

    def password_check(self, password):
        #password = self.input2.text().strip()

        if len(password) < 12:
            self.output_label.setText("Password must have 12 characters.")
            self.input2.clear()
            return False

        if not any(char.isdigit() for char in password):
            self.output_label.setText("Password must include at least one number.")
            self.output_label.setStyleSheet(""" color : red; """)
            self.input2.clear()
            return False

        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            self.output_label.setText("Password must include at least one special character.")
            self.output_label.setStyleSheet(""" color : red; """)
            self.input2.clear()
            return False
        
        return True
        


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Username_n_Password")
        #self.setFixedSize(300, 300)
        self.setWindowIcon(QIcon("C:/users/thall/Downloads/Ayodhya_Ram_Mandir_Inauguration_Day_Picture.jpg"))

        # Create a dictionary to store registered users
        self.new_dict = {}

        # Initialize the login page, passing the show_register_page method as the callback
        self.login_page = Login_Account(self.show_register_page)

        self.login_page.set_data_dict(self.new_dict)

        self.setCentralWidget(self.login_page)


    def show_register_page(self):

        self.register_page = Register_Account(self.show_login_page)

        self.register_page.set_data_dict(self.new_dict)
        self.setCentralWidget(self.register_page)

    def show_login_page(self):

        self.login_page = Login_Account(self.show_register_page)

        self.login_page.set_data_dict(self.new_dict)
        self.setCentralWidget(self.login_page)


### This is the first line to run

app = QApplication(sys.argv)
window = Window()  ## Calls Class MainWindow That then Calls Other Classes through Methods as Follows
## Other colors LavenderBlush, LightCyan

window.setStyleSheet("""
QMainWindow{
            background-color : LavenderBlush;}

QLabel{
    font-weight : bold;
}""")
window.show()
app.exec()

