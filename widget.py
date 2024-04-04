import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from form import Ui_Form
from Accueil import Ui_MainWindow
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
            
            self.accueil_window = QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.accueil_window)
            self.accueil_window.show()
            self.close() 
        else:
            print("Invalid username or password")
        cursor.close()
        connection.close()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_form = LoginForm()
        self.login_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec())
