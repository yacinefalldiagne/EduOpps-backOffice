from accueil_RP import Ui_Form
#from function import search_cahier 
import mysql.connector

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QWidget,QTableWidget,QTableWidgetItem

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

    def search_cahier(self):
        classe = self.edit_classe_cahier.text()
    
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = "SELECT * FROM coursdanscahierdetexte WHERE idCahierDeTexte IN (SELECT id FROM cahierdetexte WHERE idClasse = %s)"
            cursor.execute(query, (classe,))  # Encapsuler la variable dans un tuple

            rows = cursor.fetchall()

            self.table_cahier.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_cahier.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    def search_avis(self):
        matiere = self.edit_matiere_avis.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = "SELECT * FROM avis WHERE selectedCourse = %s "
            cursor.execute(query, (matiere,))  

            rows = cursor.fetchall()

            self.table_cahier.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_avis.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    """
        Ici apres la BDD qu'on a fera je dois modifier la requete sql
    """
    def search_conformite(self):
        nomEnseignant = self.edit_nomEnseignant_conformite.text()
        matiere = self.edit_matiere_conformite.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="ecole" 
            )

            cursor = connection.cursor()

            query = "SELECT * FROM cahier WHERE nomEnseignant = %s AND matiere= %s"
            cursor.execute(query, (nomEnseignant, matiere))

            rows = cursor.fetchall()

            self.table_cahier.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_cahier.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

        def search_avis(self):
            matiere = self.edit_matiere_avis.text()

            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="projet_sgbd",
                    passwd="passer",
                    database="ecole" 
                )

                cursor = connection.cursor()

                query = "SELECT * FROM avis WHERE selectedCourse = %s "
                cursor.execute(query, (matiere,))  # Encapsuler la variable dans un tuple

                rows = cursor.fetchall()

                self.table_cahier.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        self.table_avis.setItem(i, j, QTableWidgetItem(str(value)))

                cursor.close()
                connection.close()

            except mysql.connector.Error as error:
                print("Erreur lors de la connexion à la base de données:", error)

        
    def insert_rattrapages(self):
        date = self.edit_date_rattrapages.text()
        heure = self.edit_heure_rattrapages.text() 
        prof = self.edit_NomEnseignant_rattrapages.text()
        matiere = self.edit_classe_rattrapages.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="ecole" 
            )

            cursor = connection.cursor()

            query = "INSERT INTO rattrapages (nomProf, date_cours, heure_cours, matiere) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (prof, date, heure, matiere))
            connection.commit()  # N'oubliez pas de valider la transaction après l'insertion

            print("Données insérées avec succès dans la table rattrapages.")

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de l'insertion de données dans la table rattrapages:", error)


    """
        Ici apres la BDD qu'on a fera je dois modifier la requete sql
    """
    def insert_rapport(self):
        date = self.edit_date_Rapport.text() 
        contenu = self.textEdit_Rapport.toPlainText()
            
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="ecole" 
            )

            cursor = connection.cursor()

            query = "INSERT INTO rapport (date_rapport, contenu_rapport) VALUES (%s, %s)"
            cursor.execute(query, (date, contenu))
            connection.commit()  # N'oubliez pas de valider la transaction après l'insertion

            print("Données insérées avec succès dans la table rapport.")

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de l'insertion de données dans la table rapport:", error)


def search_fiche(self):
        classe = self.edit_classe_cahier.text()
        
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = "SELECT * FROM coursdanscahierdetexte WHERE idCahierDeTexte IN (SELECT id FROM cahierdetexte WHERE idClasse = %s)"
            cursor.execute(query, (classe))

            rows = cursor.fetchall()

            self.table_cahier.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_cahier.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)
