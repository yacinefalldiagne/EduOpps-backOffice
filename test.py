import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import mysql.connector

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PAGE DE CONNEXION")
        self.setGeometry(500, 500, 400, 500)

        layout = QVBoxLayout()

        label = QLabel("LOGIN", alignment=Qt.AlignCenter)
        layout.addWidget(label)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("login:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='passer',
            database='Tests'
        )
        self.cursor = self.connection.cursor()

    def login(self):
        username = self.username_input.text()  # Utilisez self.username_input pour accéder au champ de saisie du nom d'utilisateur
        password = self.password_input.text()  # Utilisez self.password_input pour accéder au champ de saisie du mot de passe

        # Exemple de requête pour vérifier les informations d'identification
        self.cursor.execute("SELECT * FROM utilisateurs WHERE login=%s AND password=%s", (username, password))
        user = self.cursor.fetchone()
        if user:
            QMessageBox.information(self, "Login", "Login successful!")
            window = Accueil()
        else:
            QMessageBox.warning(self, "Login", "Login failed!")
class Accueil(QWidget):
    def __init__(self):
        super().__init__()
