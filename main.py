import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PageLogin import Ui_Form  # Importation de la classe Ui_Form depuis le fichier PageLogin.
from Accueil import Ui_MainWindow

 # Importez la classe Accueil si elle existe déjà

import mysql.connector


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
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='passer',
            database='Tests'  
        )
        cursor = connection.cursor()

        # Exemple de requête pour vérifier les informations d'identification
        cursor.execute("SELECT * FROM utilisateurs WHERE login=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            # Si les informations de connexion sont valides, affichez la page d'accueil
            self.accueil_window = QMainWindow()  # Utilisez QMainWindow
            self.ui = Ui_MainWindow()  # Instanciez la classe Ui_MainWindow
            self.ui.setupUi(self.accueil_window)  # Initialisez l'interface utilisateur
            self.accueil_window.show()  # Affichez la fenêtre
            self.close()  # Fermez la fenêtre de connexion
        else:
            print("Invalid username or password")
        cursor.close()
        connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())
