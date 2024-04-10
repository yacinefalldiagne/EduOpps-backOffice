from auccueil_RP_python import MySideBar
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()
