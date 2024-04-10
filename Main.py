from auccueil_RP_python import MySideBar
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QTableWidget, QMessageBox
from PySide6.QtCore import Slot

import sys
import pandas as pd
import mysql.connector 

class ConnectToMySQL():
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'projet_sgbd'
        self.password = 'passer'
        self.port = '3306'
        self.database = 'ecole'
        self.con = None

def connect(self):
    self.con = mysql.connector.connect(
        host=self.host,
        user=self.user,
        passwd=self.password,
        port=self.port,
        database=self.database
    )

def read_cahier_de_texte(self):
    try:
        self.connect()
        cursor = self.con.cursor(dictionnary=True)
        sql = ""
        cursor.execute(sql)
        resultat = cursor.fetchall()

        return resultat
    
    except Exception as e:
        print("get data fail")
        print(e)

    finally:
        if self.con:
            self.con.close() 

@Slot(bool)
def btn_recherche_matiere(self):
    result = ConnectToMySQL().read_cahier_de_texte()

    if result:
        self.result_table.setRowCount(len(result))

        for row, item in enumerate(result):
            Nom_enseignant =QTableWidget(str(item['column1']))
            Plan_cours = QTableWidget(str(item['column2']))
            Duree_cours =QTableWidget(str(item['column3']))
            Date_cours = QTableWidget(str(item['column4']))

            self.result_table.setItem(row,0, Nom_enseignant)
            self.result_table.setItem(row,1, Plan_cours)
            self.result_table.setItem(row,2, Duree_cours)
            self.result_table.setItem(row,3, Date_cours)

        else:
            QMessageBox.information(self,'Attention', 'pas de donnees saisies pour le cahier de texte')
            

    

app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()
