import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QStackedWidget
from PyQt5.QtCore import Qt, QEasingCurve, QVariantAnimation
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Messenger App')
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(100, 100, 600, 400)

        app = QApplication.instance()
        app.setStyleSheet(Path('login.qss').read_text())

        self.layout = QVBoxLayout(self)

        self.menu_frame = QFrame(self)
        self.menu_frame.setObjectName('menuFrame')

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap('assets/logo.png'))

        self.menu_layout = QVBoxLayout(self)
        self.menu_layout.addWidget(self.logo_label)

        self.menu_frame.setLayout(self.menu_layout)

        self.container = QFrame(self)
        self.container.setObjectName('containerFrame')

        self.layout.addWidget(self.menu_frame)
        self.layout.addWidget(self.container)

        self.pages = QStackedWidget(self)
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)

        self.pages.addWidget(self.login_page)
        self.pages.addWidget(self.register_page)

        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.addWidget(self.pages)
        self.container.setLayout(self.container_layout)

        self.animations = []

        self.start_page = 0
        self.pages.setCurrentIndex(self.start_page)

        self.show()

    def animate_slide(self, start, end):
        animation = QVariantAnimation()
        animation.setStartValue(start)
        animation.setEndValue(end)
        animation.setEasingCurve(QEasingCurve.OutQuart)
        animation.setDuration(400)

        animation.valueChanged.connect(lambda value: self.pages.setGeometry(value, 0, self.pages.width(), self.pages.height()))
        animation.finished.connect(lambda: self.animations.clear())

        self.animations.clear()
        self.animations.append(animation)
        animation.start()

    def show_login(self):
        self.animate_slide(self.pages.x(), 0)
        self.pages.setCurrentIndex(0)

    def show_register(self):
        self.animate_slide(self.pages.x(), -self.pages.width())
        self.pages.setCurrentIndex(1)

class LoginPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName('loginPage')

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        heading = QLabel('Welcome Back', self)
        heading.setObjectName('heading')

        subheading = QLabel('Please enter your email and password to log in.', self)
        subheading.setObjectName('subheading')

        self.email = QLineEdit(self)
        self.email.setPlaceholderText('Enter your email')

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Enter your password')

        self.btn_login = QPushButton('Login', self)
        self.btn_login.setObjectName('loginBtn')

        self.btn_register = QPushButton('Register', self)
        self.btn_register.setObjectName('registerBtn')

        layout.addStretch()
        layout.addWidget(heading)
        layout.addWidget(subheading)
        layout.addWidget(QLabel('Email:', self))
        layout.addWidget(self.email)
        layout.addWidget(QLabel('Password:', self))
        layout.addWidget(self.password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_register)
        layout.addStretch()

class RegisterPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName('registerPage')

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        heading = QLabel('Create an Account', self)
        heading.setObjectName('heading')

        subheading = QLabel('Please enter your information to create an account.', self)
        subheading.setObjectName('subheading')

        self.username = QLineEdit(self)
        self.username.setPlaceholderText('Enter a username')

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Enter a password')

        self.btn_register = QPushButton('Register', self)
        self.btn_register.setObjectName('registerBtn')

        layout.addStretch()
        layout.addWidget(heading)
        layout.addWidget(subheading)
        layout.addWidget(QLabel('Username:', self))
        layout.addWidget(self.username)
        layout.addWidget(QLabel('Password:', self))
        layout.addWidget(self.password)
        layout.addWidget(self.btn_register)
        layout.addStretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(0, 0, 0))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(255, 0, 0))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    app.setPalette(palette)

    window = MainWindow()
    sys.exit(app.exec())



























