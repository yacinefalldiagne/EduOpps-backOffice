import sys
import requests
from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow, QMessageBox
from form import Ui_Form
from accueil_RP import Ui_Form_RP
from accueil_CF import Ui_Form_CF
from accueil_DE import Ui_Form_DE
from MembreEquipePedagogique import Ui_Form_MEP

from dotenv import load_dotenv
import os

role_pages = {
    "RESPONSABLE_DEPARTEMENT": Ui_Form_RP,
    "RESPONSABLE_PEDAGOGIQUE": Ui_Form_RP,
    "CHEF_DEPARTEMENT": Ui_Form_CF,
    "MEMBRE_EQUIPE_PEDAGOGIQUE": Ui_Form_MEP,
    "MEMBRE_COMMISSION_PEDAGOGIQUE": Ui_Form_MEP,
    "DIRECTEUR_ETUDES": Ui_Form_DE
}

load_dotenv()

endpoint = os.getenv('endpoint')

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.Username.text()
        password = self.ui.lineEdit_2.text()
        response = requests.post(f"http://localhost:3000/auth/login", json={"username": username, "password": password, "originType": "BackOfficeRole"})
        print(response)
        if response.status_code == 200:
            token = response.json()
            data=response.json()['data']
            token = data['token']
            role= data['role']
            fullName=data['fullName']
            if token and role in role_pages:
                QMessageBox.information(self, "Success", f"Bienvenue {username}!")
                self.accueil_window = QMainWindow()
                role_page_class = role_pages[role]
                self.ui = role_page_class()
                self.ui.setupUi(self.accueil_window)
                self.accueil_window.show()
                self.close()
            else: 
                QMessageBox.warning(self, "Error", "Token not found in response!")
        else:
            QMessageBox.warning(self, "Error", "Nom d'utilisateur ou mot de passe invalide")

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_form = LoginForm()
        self.login_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()  
    sys.exit(app.exec_())