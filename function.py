
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QTableWidget, QLineEdit, QMessageBox, QWidget, QVBoxLayout

import sys
import pandas as pd
import mysql.connector 

def search_cahier(self):
    classe = self.edit_classe.text()
    matiere = self.edit_matiere.text()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="projet_sgbd",
            passwd="passer",
            database="ecole" 
        )

        cursor = connection.cursor()

        query = "SELECT * FROM cahier WHERE classe = %s AND matiere= %s"
        cursor.execute(query, (classe, matiere))

        rows = cursor.fetchall()

        self.table_cahier.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.table_cahier.setItem(i, j, QTableWidgetItem(str(value)))

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à la base de données:", error)