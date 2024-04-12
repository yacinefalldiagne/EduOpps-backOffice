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

    def passer_a_fichesEvaluation(self):
        self.stackedWidget.setCurrentIndex(4) 

    def passer_a_avisEtudiants(self):
        self.stackedWidget.setCurrentIndex(5) 

    def passer_a_rapportMensuel(self):
        self.stackedWidget.setCurrentIndex(6) 

    def passer_a_rattrapagesCours(self):
        self.stackedWidget.setCurrentIndex(7) 

    """
        fini 1
    """
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

            query = "SELECT  enseignant,contenu,dateCours,heureDebut,heureFin FROM coursdanscahierdetexte WHERE idCahierDeTexte IN (SELECT id FROM cahierdetexte WHERE idClasse = %s)"
            cursor.execute(query, (classe,))  

            rows = cursor.fetchall()

            print(rows)

            self.table_cahier.setColumnCount(len(rows[0]))  

            self.table_cahier.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table_cahier.setItem(i, j, item)

            self.table_cahier.repaint()

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    """
        fini 2
    """
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

            query = "SELECT selectedCourse, syllabusProvided, objectivesClear, contentAligned, courseMaterialProvided, contentRespected, scheduleRespected, overallSatisfaction, additionalSuggestions, description FROM avis WHERE selectedCourse = %s"
            cursor.execute(query, (matiere,))  

            rows = cursor.fetchall()

            # Vérifiez que la requête SQL renvoie des résultats
            print("Résultats de la requête SQL :", rows)

            self.table_avis.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_avis.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

            # Vérifiez que les données sont correctement ajoutées à la table
            print("Données ajoutées à la table avec succès.")

        except mysql.connector.Error as error:
            print("Erreur lors de la recherche dans la base de données:", error)

    def insert_commentaire_cahier(self):
        commentaire = self.commentaire_cahier.text() 
        id_classe = self.edit_classe_cahier.text()  # Assurez-vous que ce champ correspond à l'ID du cahier de texte
        
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = "INSERT INTO commentaire_cahier (contenu_commentaire, id_classe) VALUES (%s, %s)"
            cursor.execute(query, (commentaire, id_classe))  
            connection.commit()  

            print("Données insérées avec succès dans la table commentaire_cahier.")

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de l'insertion de données dans la table commentaire_cahier:", error)
     
    def search_conformite(self):
        nomEnseignant = self.edit_nomEnseignant_conformite.text()
        matiere = self.edit_matiere_conformite.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = """SELECT coursdanscahierdetexte.enseignant, syllabus.nomCours, syllabus.nombreHeures,
                            syllabus.objectifGeneral, syllabus.evaluation, coursdanscahierdetexte.contenu
                    FROM coursdanscahierdetexte
                    INNER JOIN syllabus ON coursdanscahierdetexte.selectedCourse = syllabus.nomCours
                    WHERE coursdanscahierdetexte.enseignant = %s AND syllabus.nomCours = %s"""
            cursor.execute(query, (nomEnseignant, matiere))

            rows = cursor.fetchall()

            self.table_conformite.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_conformite.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    def insert_commentaire_conformite(self):
        commentaire = self.commentaire_conformite.text()
        
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops"
            )

            cursor = connection.cursor()

            query = "INSERT INTO commentaire_conformite (contenu) VALUES (%s)"
            cursor.execute(query, (commentaire,))  # Assurez-vous de mettre une virgule après commentaire pour en faire un tuple
            connection.commit()

            print("Données insérées avec succès dans la table commentaire_conformite.")

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de l'insertion de données dans la table commentaire_conformite:", error)

    def search_effectivite(self):
        classe_id = int(self.edit_classe_effectivite.text())
        
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = """SELECT coursdanscahierdetexte.enseignant, coursdanscahierdetexte.dateCours,
                            coursdanscahierdetexte.heureDebut, coursdanscahierdetexte.heureFin,
                            syllabus.objectifGeneral, syllabus.evaluation, coursdanscahierdetexte.contenu
                    FROM coursdanscahierdetexte
                    INNER JOIN cahierdetexte ON coursdanscahierdetexte.idCahierDeTexte = cahierdetexte.id
                    INNER JOIN syllabus ON coursdanscahierdetexte.selectedCourse = syllabus.nomCours
                    WHERE cahierdetexte.idClasse = %s"""
            cursor.execute(query, (classe_id,))

            rows = cursor.fetchall()

            self.table_cahier_2.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_cahier_2.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    """
        fini 3
    """
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
                database="eduops" 
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
        fini 4
    """
    def insert_rapport(self):
        date = self.edit_date_Rapport_3.text() 
        nom = self.edit_nom_Rapport.text()  # Ajoutez .text() ici
        contenu = self.contenu_Rapport.toPlainText()
            
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            query = "INSERT INTO rapport (date_rapport, contenu_rapport, nom_rapport) VALUES (%s, %s, %s)"
            cursor.execute(query, (date, contenu, nom))  # Utilisez nom au lieu de nom.text()
            connection.commit()  # N'oubliez pas de valider la transaction après l'insertion

            print("Données insérées avec succès dans la table rapport.")

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de l'insertion de données dans la table rapport:", error)

    """
        fini 5
    """
    def search_evaluation(self):
        classe = self.edit_classe_evaluation.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="projet_sgbd",
                passwd="passer",
                database="eduops" 
            )

            cursor = connection.cursor()

            # Sélectionnez toutes les colonnes de la table evaluation sauf ID
            query = "SELECT nom_etudiant, matiere, note FROM evaluation WHERE classe = %s"
            cursor.execute(query, (classe,))  

            rows = cursor.fetchall()

            self.table_evaluation.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table_evaluation.setItem(i, j, QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)
