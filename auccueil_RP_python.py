from accueil_RP import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QWidget

class MySideBar(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Accueil Responsable Pedagogique (RP)")

        self.icon_name_widget.setHidden(True)

        self.Accueil_1.clicked.connect(self.passer_a_accueil)
        self.Accueil_2.clicked.connect(self.passer_a_accueil)

        self.Cahier_1.clicked.connect(self.passer_a_cahierDeTexte)
        self.Cahier_2.clicked.connect(self.passer_a_cahierDeTexte)

        self.Effectivite_1.clicked.connect(self.passer_a_effectiviteEnseignements)
        self.Effectivite_2.clicked.connect(self.passer_a_effectiviteEnseignements)

        self.Conformite_1.clicked.connect(self.passer_a_conformiteCours)
        self.Conformite_2.clicked.connect(self.passer_a_conformiteCours)

        self.Deroulement_1.clicked.connect(self.passer_a_deroulementProgramme)
        self.Deroulement_2.clicked.connect(self.passer_a_deroulementProgramme)

        self.Fiches_1.clicked.connect(self.passer_a_fichesEvaluation)
        self.Fiches_2.clicked.connect(self.passer_a_fichesEvaluation)

        self.Avis_1.clicked.connect(self.passer_a_avisEtudiants)
        self.Avis_2.clicked.connect(self.passer_a_avisEtudiants)
        
        self.Rapport_1.clicked.connect(self.passer_a_rapportMensuel)
        self.Rapport_2.clicked.connect(self.passer_a_rapportMensuel)

        self.Rattrapages_1.clicked.connect(self.passer_a_rattrapagesCours)
        self.Rattrapages_2.clicked.connect(self.passer_a_rattrapagesCours)



    def passer_a_accueil(self):
        self.stackedWidget.setCurrentIndex(0) 
    
    def passer_a_cahierDeTexte(self):
        self.stackedWidget.setCurrentIndex(1) 

    def passer_a_effectiviteEnseignements(self):
        self.stackedWidget.setCurrentIndex(2) 

    def passer_a_conformiteCours(self):
        self.stackedWidget.setCurrentIndex(3) 

    def passer_a_deroulementProgramme(self):
        self.stackedWidget.setCurrentIndex(4) 

    def passer_a_fichesEvaluation(self):
        self.stackedWidget.setCurrentIndex(5) 

    def passer_a_avisEtudiants(self):
        self.stackedWidget.setCurrentIndex(6) 

    def passer_a_rapportMensuel(self):
        self.stackedWidget.setCurrentIndex(7) 

    def passer_a_rattrapagesCours(self):
        self.stackedWidget.setCurrentIndex(8) 

