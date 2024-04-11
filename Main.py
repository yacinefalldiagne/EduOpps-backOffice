from auccueil_RP_python import MySideBar
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QTableWidgetItem,QTableWidget, QMessageBox
from PySide6.QtCore import Slot

import sys
import pandas as pd
import mysql.connector 

def search_cahier(self):
    classe = self.edit_classe.text()
    matiere = self.edit_matiere.text()

app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()
