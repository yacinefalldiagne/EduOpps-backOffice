from accueil_DE import Ui_Form_DE
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_Form_DE):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Accueil Directeur Etude (DE)")
        self.Accueil_1.clicked.connect(self.passer_a_accueil)
        self.Accueil_2.clicked.connect(self.passer_a_accueil)
        self.ExploiterEnseigne_1.clicked.connect(self.passer_a_exploiterEnseignement)
        self.ExploiterEnseigne_2.clicked.connect(self.passer_a_exploiterEnseignement)
        self.ExploiterPV_1.clicked.connect(self.passer_a_exploiterPV)
        self.ExploiterPV_2.clicked.connect(self.passer_a_exploiterPV)
        self.ExploiterRapport_1.clicked.connect(self.passer_a_ExploiterRapport)
        self.ExploiterRapport_2.clicked.connect(self.passer_a_ExploiterRapport)
    def passer_a_accueil(self):
        self.stackedWidget.setCurrentIndex(0) 
    def passer_a_exploiterEnseignement(self):
        self.stackedWidget.setCurrentIndex(1) 
    def passer_a_exploiterPV(self):
        self.stackedWidget.setCurrentIndex(2) 
    def passer_a_ExploiterRapport(self):
        self.stackedWidget.setCurrentIndex(3) 

