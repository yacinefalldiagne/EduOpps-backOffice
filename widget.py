import sys

import requests
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from form import Ui_Form
from Accueil import Ui_MainWindow
# import mysql.connector


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Connexion à la base de données MySQL
        # connection = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password='bisko',
        #     database='eduOps'
        # )
        # cursor = connection.cursor()
        response = requests.post("http://localhost:3000/auth/adminLogin", json={"email": username, "password": password})
        # Exemple de requête pour vérifier les informations d'identification
        # cursor.execute("SELECT * FROM User WHERE email=%s AND password=%s", (username, password))
        # user = cursor.fetchone()
        print(response.status_code)
        if response.status_code == 201:
            token = response.json().get("access_token")
            if token:
                # Stocker le token localement pour une utilisation ultérieure
                self.token = token
                self.accueil_window = QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.accueil_window)
                self.accueil_window.show()
                self.close() 
                # Faire quelque chose après la connexion réussie
            else:
                print( "Token not found in response!")
            
        else:
            print("Invalid username or password")



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_form = LoginForm()
        self.login_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec())
