# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setGeometry(QRect(64, 20, 187, 481))
        self.icon_name_widget.setMaximumSize(QSize(200, 16777215))
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	color: white;\n"
"	height: 30px;\n"
"	border:none;\n"
"	font-family: \"Comic Sans MS\", cursive, sans-serif; \n"
"	font-size: 12px; \n"
"    padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 20, -1)
        self.label_13 = QLabel(self.icon_name_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"image: url(:/logo pers.jpeg);")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.icon_name_widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 15, -1, -1)
        self.Accueil_3 = QPushButton(self.icon_name_widget)
        self.Accueil_3.setObjectName(u"Accueil_3")
        icon = QIcon()
        icon.addFile(u"Images/page-accueil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Accueil_3.setIcon(icon)
        self.Accueil_3.setCheckable(True)
        self.Accueil_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Accueil_3)

        self.Cahier_3 = QPushButton(self.icon_name_widget)
        self.Cahier_3.setObjectName(u"Cahier_3")
        icon1 = QIcon()
        icon1.addFile(u"Images/cahier-de-texte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cahier_3.setIcon(icon1)
        self.Cahier_3.setCheckable(True)
        self.Cahier_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Cahier_3)

        self.Effectivite_3 = QPushButton(self.icon_name_widget)
        self.Effectivite_3.setObjectName(u"Effectivite_3")
        icon2 = QIcon()
        icon2.addFile(u"Images/enseignement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Effectivite_3.setIcon(icon2)
        self.Effectivite_3.setCheckable(True)
        self.Effectivite_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Effectivite_3)

        self.Conformite_3 = QPushButton(self.icon_name_widget)
        self.Conformite_3.setObjectName(u"Conformite_3")
        icon3 = QIcon()
        icon3.addFile(u"Images/conformite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Conformite_3.setIcon(icon3)
        self.Conformite_3.setCheckable(True)
        self.Conformite_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Conformite_3)

        self.Deroulement_3 = QPushButton(self.icon_name_widget)
        self.Deroulement_3.setObjectName(u"Deroulement_3")
        icon4 = QIcon()
        icon4.addFile(u"Images/verifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Deroulement_3.setIcon(icon4)
        self.Deroulement_3.setCheckable(True)
        self.Deroulement_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Deroulement_3)

        self.Fiches_3 = QPushButton(self.icon_name_widget)
        self.Fiches_3.setObjectName(u"Fiches_3")
        icon5 = QIcon()
        icon5.addFile(u"Images/bonne-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Fiches_3.setIcon(icon5)
        self.Fiches_3.setCheckable(True)
        self.Fiches_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Fiches_3)

        self.Avis_3 = QPushButton(self.icon_name_widget)
        self.Avis_3.setObjectName(u"Avis_3")
        icon6 = QIcon()
        icon6.addFile(u"Images/avis-client.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Avis_3.setIcon(icon6)
        self.Avis_3.setCheckable(True)
        self.Avis_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Avis_3)

        self.Rapport_3 = QPushButton(self.icon_name_widget)
        self.Rapport_3.setObjectName(u"Rapport_3")
        icon7 = QIcon()
        icon7.addFile(u"Images/rapport-dactivite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rapport_3.setIcon(icon7)
        self.Rapport_3.setCheckable(True)
        self.Rapport_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Rapport_3)

        self.Rattrapages_3 = QPushButton(self.icon_name_widget)
        self.Rattrapages_3.setObjectName(u"Rattrapages_3")
        icon8 = QIcon()
        icon8.addFile(u"Images/calendrier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rattrapages_3.setIcon(icon8)
        self.Rattrapages_3.setCheckable(True)
        self.Rattrapages_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Rattrapages_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(18, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButton_26 = QPushButton(self.icon_name_widget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        icon9 = QIcon()
        icon9.addFile(u"Images/sortir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_26.setIcon(icon9)
        self.pushButton_26.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_26)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setGeometry(QRect(20, 20, 38, 481))
        self.icon_only_widget.setMaximumSize(QSize(60, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	height: 30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.label_15 = QLabel(self.icon_only_widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"image: url(:/logo pers.jpeg);")

        self.verticalLayout_8.addWidget(self.label_15)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 15, -1, -1)
        self.Accueil_4 = QPushButton(self.icon_only_widget)
        self.Accueil_4.setObjectName(u"Accueil_4")
        self.Accueil_4.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.Accueil_4.setIcon(icon)
        self.Accueil_4.setCheckable(True)
        self.Accueil_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Accueil_4)

        self.Cahier_4 = QPushButton(self.icon_only_widget)
        self.Cahier_4.setObjectName(u"Cahier_4")
        self.Cahier_4.setStyleSheet(u"text-align:center;")
        self.Cahier_4.setIcon(icon1)
        self.Cahier_4.setCheckable(True)
        self.Cahier_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Cahier_4)

        self.Effectivite_4 = QPushButton(self.icon_only_widget)
        self.Effectivite_4.setObjectName(u"Effectivite_4")
        self.Effectivite_4.setStyleSheet(u"text-align:center;\n"
"")
        self.Effectivite_4.setIcon(icon2)
        self.Effectivite_4.setCheckable(True)
        self.Effectivite_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Effectivite_4)

        self.Conformite_4 = QPushButton(self.icon_only_widget)
        self.Conformite_4.setObjectName(u"Conformite_4")
        self.Conformite_4.setStyleSheet(u"text-align:center;")
        self.Conformite_4.setIcon(icon3)
        self.Conformite_4.setCheckable(True)
        self.Conformite_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Conformite_4)

        self.Deroulement_4 = QPushButton(self.icon_only_widget)
        self.Deroulement_4.setObjectName(u"Deroulement_4")
        self.Deroulement_4.setStyleSheet(u"text-align:center;")
        self.Deroulement_4.setIcon(icon4)
        self.Deroulement_4.setCheckable(True)
        self.Deroulement_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Deroulement_4)

        self.Fiches_4 = QPushButton(self.icon_only_widget)
        self.Fiches_4.setObjectName(u"Fiches_4")
        self.Fiches_4.setStyleSheet(u"text-align:center;")
        self.Fiches_4.setIcon(icon5)
        self.Fiches_4.setCheckable(True)
        self.Fiches_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Fiches_4)

        self.Avis_4 = QPushButton(self.icon_only_widget)
        self.Avis_4.setObjectName(u"Avis_4")
        self.Avis_4.setStyleSheet(u"text-align:center;")
        self.Avis_4.setIcon(icon6)
        self.Avis_4.setCheckable(True)
        self.Avis_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Avis_4)

        self.Rapport_4 = QPushButton(self.icon_only_widget)
        self.Rapport_4.setObjectName(u"Rapport_4")
        self.Rapport_4.setStyleSheet(u"text-align:center;\n"
"")
        self.Rapport_4.setIcon(icon7)
        self.Rapport_4.setCheckable(True)
        self.Rapport_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Rapport_4)

        self.Rattrapages_4 = QPushButton(self.icon_only_widget)
        self.Rattrapages_4.setObjectName(u"Rattrapages_4")
        self.Rattrapages_4.setStyleSheet(u"text-align:center;")
        self.Rattrapages_4.setIcon(icon8)
        self.Rattrapages_4.setCheckable(True)
        self.Rattrapages_4.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.Rattrapages_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.pushButton_10 = QPushButton(self.icon_only_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"text-align:center;\n"
"")
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_8.addWidget(self.pushButton_10)

        self.verticalSpacer_4 = QSpacerItem(38, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(257, 20, 572, 481))
        self.verticalLayout_10 = QVBoxLayout(self.main_menu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_2 = QWidget(self.main_menu)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.header_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.menu_2 = QPushButton(self.header_2)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setStyleSheet(u"border: none;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"Images/barre-de-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_2.setIcon(icon10)
        self.menu_2.setIconSize(QSize(30, 30))
        self.menu_2.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.menu_2)

        self.horizontalSpacer_3 = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_2 = QLineEdit(self.header_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.pushButton_31 = QPushButton(self.header_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"	border:none;\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"Images/loupe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_31.setIcon(icon11)
        self.pushButton_31.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton_31)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_4 = QSpacerItem(137, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.pushButton_32 = QPushButton(self.header_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"border: none;\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"Images/profil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon12)
        self.pushButton_32.setIconSize(QSize(30, 20))

        self.horizontalLayout_7.addWidget(self.pushButton_32)


        self.verticalLayout_10.addWidget(self.header_2)

        self.stackedWidget_2 = QStackedWidget(self.main_menu)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Accueil_5 = QWidget()
        self.Accueil_5.setObjectName(u"Accueil_5")
        self.label_16 = QLabel(self.Accueil_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(140, 120, 161, 41))
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_16.setFont(font)
        self.stackedWidget_2.addWidget(self.Accueil_5)
        self.Conformite_5 = QWidget()
        self.Conformite_5.setObjectName(u"Conformite_5")
        self.label_17 = QLabel(self.Conformite_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(90, 110, 251, 41))
        self.label_17.setFont(font)
        self.stackedWidget_2.addWidget(self.Conformite_5)
        self.Deroulementprogramme_2 = QWidget()
        self.Deroulementprogramme_2.setObjectName(u"Deroulementprogramme_2")
        self.label_18 = QLabel(self.Deroulementprogramme_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 120, 321, 41))
        self.label_18.setFont(font)
        self.stackedWidget_2.addWidget(self.Deroulementprogramme_2)
        self.FichesEvaluation_2 = QWidget()
        self.FichesEvaluation_2.setObjectName(u"FichesEvaluation_2")
        self.label_19 = QLabel(self.FichesEvaluation_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(120, 160, 331, 41))
        self.label_19.setFont(font)
        self.stackedWidget_2.addWidget(self.FichesEvaluation_2)
        self.AvisEtudiants_2 = QWidget()
        self.AvisEtudiants_2.setObjectName(u"AvisEtudiants_2")
        self.label_20 = QLabel(self.AvisEtudiants_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(140, 150, 251, 41))
        self.label_20.setFont(font)
        self.stackedWidget_2.addWidget(self.AvisEtudiants_2)
        self.RapportMensuel_2 = QWidget()
        self.RapportMensuel_2.setObjectName(u"RapportMensuel_2")
        self.label_21 = QLabel(self.RapportMensuel_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(150, 140, 261, 41))
        self.label_21.setFont(font)
        self.stackedWidget_2.addWidget(self.RapportMensuel_2)
        self.Rattrapagecours_2 = QWidget()
        self.Rattrapagecours_2.setObjectName(u"Rattrapagecours_2")
        self.label_22 = QLabel(self.Rattrapagecours_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(140, 150, 321, 41))
        self.label_22.setFont(font)
        self.stackedWidget_2.addWidget(self.Rattrapagecours_2)
        self.Effectivite_5 = QWidget()
        self.Effectivite_5.setObjectName(u"Effectivite_5")
        self.label_23 = QLabel(self.Effectivite_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 160, 511, 41))
        self.label_23.setFont(font)
        self.stackedWidget_2.addWidget(self.Effectivite_5)
        self.Cahierdetexte_2 = QWidget()
        self.Cahierdetexte_2.setObjectName(u"Cahierdetexte_2")
        self.label_24 = QLabel(self.Cahierdetexte_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(160, 100, 251, 41))
        self.label_24.setFont(font)
        self.stackedWidget_2.addWidget(self.Cahierdetexte_2)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" RP", None))
        self.Accueil_3.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.Cahier_3.setText(QCoreApplication.translate("MainWindow", u"Cahier de texte", None))
        self.Effectivite_3.setText(QCoreApplication.translate("MainWindow", u"Effectivit\u00e9 enseignements", None))
        self.Conformite_3.setText(QCoreApplication.translate("MainWindow", u"Conformit\u00e9 cours", None))
        self.Deroulement_3.setText(QCoreApplication.translate("MainWindow", u"D\u00e9roulement programme", None))
        self.Fiches_3.setText(QCoreApplication.translate("MainWindow", u"Fiches d'evaluations", None))
        self.Avis_3.setText(QCoreApplication.translate("MainWindow", u"Avis etudiants", None))
        self.Rapport_3.setText(QCoreApplication.translate("MainWindow", u"Rapport mensuel", None))
        self.Rattrapages_3.setText(QCoreApplication.translate("MainWindow", u"Rattrapages cours", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Deconnexion", None))
        self.label_15.setText("")
        self.Accueil_4.setText("")
        self.Cahier_4.setText("")
        self.Effectivite_4.setText("")
        self.Conformite_4.setText("")
        self.Deroulement_4.setText("")
        self.Fiches_4.setText("")
        self.Avis_4.setText("")
        self.Rapport_4.setText("")
        self.Rattrapages_4.setText("")
        self.pushButton_10.setText("")
        self.menu_2.setText("")
        self.pushButton_31.setText("")
        self.pushButton_32.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ACCUEIL", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CONFORMITE COURS", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"DEROULMENT PROGRAMMES", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"FICHES D' EVALUATION", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"AVIS ETUDIANTS", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"RAPPORT MENSUEL", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"RATTRAPAGE DES COURS", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"EFFECTIVITE DES ENSEIGNEMENTS", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"CAHIER DE TEXTE", None))
    # retranslateUi

