# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accueil_RP.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(847, 663)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.icon_only_widget = QWidget(Form)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setGeometry(QRect(9, 9, 38, 661))
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
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.Accueil_1 = QPushButton(self.icon_only_widget)
        self.Accueil_1.setObjectName(u"Accueil_1")
        self.Accueil_1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight:bold;\n"
"}")
        icon = QIcon()
        icon.addFile(u"Images/page-accueil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Accueil_1.setIcon(icon)
        self.Accueil_1.setCheckable(True)
        self.Accueil_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Accueil_1)

        self.Cahier_1 = QPushButton(self.icon_only_widget)
        self.Cahier_1.setObjectName(u"Cahier_1")
        self.Cahier_1.setStyleSheet(u"text-align:center;")
        icon1 = QIcon()
        icon1.addFile(u"Images/cahier-de-texte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cahier_1.setIcon(icon1)
        self.Cahier_1.setCheckable(True)
        self.Cahier_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Cahier_1)

        self.Effectivite_1 = QPushButton(self.icon_only_widget)
        self.Effectivite_1.setObjectName(u"Effectivite_1")
        self.Effectivite_1.setStyleSheet(u"text-align:center;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Images/enseignement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Effectivite_1.setIcon(icon2)
        self.Effectivite_1.setCheckable(True)
        self.Effectivite_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Effectivite_1)

        self.Conformite_1 = QPushButton(self.icon_only_widget)
        self.Conformite_1.setObjectName(u"Conformite_1")
        self.Conformite_1.setStyleSheet(u"text-align:center;")
        icon3 = QIcon()
        icon3.addFile(u"Images/conformite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Conformite_1.setIcon(icon3)
        self.Conformite_1.setCheckable(True)
        self.Conformite_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Conformite_1)

        self.Deroulement_1 = QPushButton(self.icon_only_widget)
        self.Deroulement_1.setObjectName(u"Deroulement_1")
        self.Deroulement_1.setStyleSheet(u"text-align:center;")
        icon4 = QIcon()
        icon4.addFile(u"Images/verifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Deroulement_1.setIcon(icon4)
        self.Deroulement_1.setCheckable(True)
        self.Deroulement_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Deroulement_1)

        self.Fiches_1 = QPushButton(self.icon_only_widget)
        self.Fiches_1.setObjectName(u"Fiches_1")
        self.Fiches_1.setStyleSheet(u"text-align:center;")
        icon5 = QIcon()
        icon5.addFile(u"Images/bonne-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Fiches_1.setIcon(icon5)
        self.Fiches_1.setCheckable(True)
        self.Fiches_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Fiches_1)

        self.Avis_1 = QPushButton(self.icon_only_widget)
        self.Avis_1.setObjectName(u"Avis_1")
        self.Avis_1.setStyleSheet(u"text-align:center;")
        icon6 = QIcon()
        icon6.addFile(u"Images/avis-client.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Avis_1.setIcon(icon6)
        self.Avis_1.setCheckable(True)
        self.Avis_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Avis_1)

        self.Rapport_1 = QPushButton(self.icon_only_widget)
        self.Rapport_1.setObjectName(u"Rapport_1")
        self.Rapport_1.setStyleSheet(u"text-align:center;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"Images/rapport-dactivite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rapport_1.setIcon(icon7)
        self.Rapport_1.setCheckable(True)
        self.Rapport_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Rapport_1)

        self.Rattrapages_1 = QPushButton(self.icon_only_widget)
        self.Rattrapages_1.setObjectName(u"Rattrapages_1")
        self.Rattrapages_1.setStyleSheet(u"text-align:center;")
        icon8 = QIcon()
        icon8.addFile(u"Images/calendrier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rattrapages_1.setIcon(icon8)
        self.Rattrapages_1.setCheckable(True)
        self.Rattrapages_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Rattrapages_1)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(38, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.icon_only_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"text-align:center;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"Images/sortir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.icon_name_widget = QWidget(Form)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setGeometry(QRect(53, 9, 187, 661))
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
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"image: url(:/logo pers.jpeg);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Accueil_2 = QPushButton(self.icon_name_widget)
        self.Accueil_2.setObjectName(u"Accueil_2")
        self.Accueil_2.setIcon(icon)
        self.Accueil_2.setCheckable(True)
        self.Accueil_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Accueil_2)

        self.Cahier_2 = QPushButton(self.icon_name_widget)
        self.Cahier_2.setObjectName(u"Cahier_2")
        self.Cahier_2.setIcon(icon1)
        self.Cahier_2.setCheckable(True)
        self.Cahier_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Cahier_2)

        self.Effectivite_2 = QPushButton(self.icon_name_widget)
        self.Effectivite_2.setObjectName(u"Effectivite_2")
        self.Effectivite_2.setIcon(icon2)
        self.Effectivite_2.setCheckable(True)
        self.Effectivite_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Effectivite_2)

        self.Conformite_2 = QPushButton(self.icon_name_widget)
        self.Conformite_2.setObjectName(u"Conformite_2")
        self.Conformite_2.setIcon(icon3)
        self.Conformite_2.setCheckable(True)
        self.Conformite_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Conformite_2)

        self.Deroulement_2 = QPushButton(self.icon_name_widget)
        self.Deroulement_2.setObjectName(u"Deroulement_2")
        self.Deroulement_2.setIcon(icon4)
        self.Deroulement_2.setCheckable(True)
        self.Deroulement_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Deroulement_2)

        self.Fiches_2 = QPushButton(self.icon_name_widget)
        self.Fiches_2.setObjectName(u"Fiches_2")
        self.Fiches_2.setIcon(icon5)
        self.Fiches_2.setCheckable(True)
        self.Fiches_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Fiches_2)

        self.Avis_2 = QPushButton(self.icon_name_widget)
        self.Avis_2.setObjectName(u"Avis_2")
        self.Avis_2.setIcon(icon6)
        self.Avis_2.setCheckable(True)
        self.Avis_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Avis_2)

        self.Rapport_2 = QPushButton(self.icon_name_widget)
        self.Rapport_2.setObjectName(u"Rapport_2")
        self.Rapport_2.setIcon(icon7)
        self.Rapport_2.setCheckable(True)
        self.Rapport_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Rapport_2)

        self.Rattrapages_2 = QPushButton(self.icon_name_widget)
        self.Rattrapages_2.setObjectName(u"Rattrapages_2")
        self.Rattrapages_2.setIcon(icon8)
        self.Rattrapages_2.setCheckable(True)
        self.Rattrapages_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Rattrapages_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(18, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_25 = QPushButton(self.icon_name_widget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon9)
        self.pushButton_25.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_25)

        self.main_menu = QWidget(Form)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(246, 9, 621, 651))
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header = QWidget(self.main_menu)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.menu = QPushButton(self.header)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border: none;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"Images/barre-de-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon10)
        self.menu.setIconSize(QSize(30, 30))
        self.menu.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton_29 = QPushButton(self.header)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setStyleSheet(u"	border:none;\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"Images/loupe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_29.setIcon(icon11)
        self.pushButton_29.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_29)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton_30 = QPushButton(self.header)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"border: none;\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"Images/profil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_30.setIcon(icon12)
        self.pushButton_30.setIconSize(QSize(30, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_30)


        self.verticalLayout_5.addWidget(self.header)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Accueil = QWidget()
        self.Accueil.setObjectName(u"Accueil")
        self.label_4 = QLabel(self.Accueil)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 160, 111, 41))
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.Accueil)
        self.Cahierdetexte = QWidget()
        self.Cahierdetexte.setObjectName(u"Cahierdetexte")
        self.groupBox_2 = QGroupBox(self.Cahierdetexte)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 100, 581, 321))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.widget = QWidget(self.Cahierdetexte)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 551, 80))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, 0, 20, 81))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 201, 20))
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 0, 221, 16))
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 30, 216, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setBaseSize(QSize(0, 0))
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(280, 30, 216, 26))
        self.horizontalLayout_7 = QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)

        self.pushButton_2 = QPushButton(self.widget2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.stackedWidget.addWidget(self.Cahierdetexte)
        self.Effectivite = QWidget()
        self.Effectivite.setObjectName(u"Effectivite")
        self.label_9 = QLabel(self.Effectivite)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 160, 511, 41))
        self.label_9.setFont(font)
        self.stackedWidget.addWidget(self.Effectivite)
        self.Conformite = QWidget()
        self.Conformite.setObjectName(u"Conformite")
        self.label_7 = QLabel(self.Conformite)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 110, 251, 41))
        self.label_7.setFont(font)
        self.stackedWidget.addWidget(self.Conformite)
        self.Deroulementprogramme = QWidget()
        self.Deroulementprogramme.setObjectName(u"Deroulementprogramme")
        self.label_8 = QLabel(self.Deroulementprogramme)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 120, 321, 41))
        self.label_8.setFont(font)
        self.stackedWidget.addWidget(self.Deroulementprogramme)
        self.FichesEvaluation = QWidget()
        self.FichesEvaluation.setObjectName(u"FichesEvaluation")
        self.label_10 = QLabel(self.FichesEvaluation)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 160, 331, 41))
        self.label_10.setFont(font)
        self.stackedWidget.addWidget(self.FichesEvaluation)
        self.AvisEtudiants = QWidget()
        self.AvisEtudiants.setObjectName(u"AvisEtudiants")
        self.label_5 = QLabel(self.AvisEtudiants)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 150, 251, 41))
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.AvisEtudiants)
        self.RapportMensuel = QWidget()
        self.RapportMensuel.setObjectName(u"RapportMensuel")
        self.label_11 = QLabel(self.RapportMensuel)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 140, 261, 41))
        self.label_11.setFont(font)
        self.stackedWidget.addWidget(self.RapportMensuel)
        self.Rattrapagecours = QWidget()
        self.Rattrapagecours.setObjectName(u"Rattrapagecours")
        self.label_12 = QLabel(self.Rattrapagecours)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(140, 150, 321, 41))
        self.label_12.setFont(font)
        self.stackedWidget.addWidget(self.Rattrapagecours)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 36, 16))
        self.label.setStyleSheet(u"image: url(:/logo pers.jpeg);")

        self.retranslateUi(Form)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.pushButton_9.toggled.connect(Form.close)
        self.pushButton_25.toggled.connect(Form.close)
        self.Accueil_1.toggled.connect(self.Accueil_2.setChecked)
        self.Accueil_2.toggled.connect(self.Accueil_1.setChecked)
        self.Cahier_1.toggled.connect(self.Cahier_2.setChecked)
        self.Cahier_2.toggled.connect(self.Cahier_1.setChecked)
        self.Effectivite_1.toggled.connect(self.Effectivite_2.setChecked)
        self.Effectivite_2.toggled.connect(self.Effectivite_1.setChecked)
        self.Conformite_1.toggled.connect(self.Conformite_2.setChecked)
        self.Conformite_2.toggled.connect(self.Conformite_1.setChecked)
        self.Deroulement_2.toggled.connect(self.Deroulement_1.setChecked)
        self.Deroulement_1.toggled.connect(self.Deroulement_2.setChecked)
        self.Fiches_2.toggled.connect(self.Fiches_1.setChecked)
        self.Fiches_1.toggled.connect(self.Fiches_2.setChecked)
        self.Avis_2.toggled.connect(self.Avis_1.setChecked)
        self.Avis_1.toggled.connect(self.Avis_2.setChecked)
        self.Rapport_2.toggled.connect(self.Rapport_1.setChecked)
        self.Rapport_1.toggled.connect(self.Rapport_2.setChecked)
        self.Rattrapages_2.toggled.connect(self.Rattrapages_1.setChecked)
        self.Rattrapages_1.toggled.connect(self.Rattrapages_2.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Accueil_1.setText("")
        self.Cahier_1.setText("")
        self.Effectivite_1.setText("")
        self.Conformite_1.setText("")
        self.Deroulement_1.setText("")
        self.Fiches_1.setText("")
        self.Avis_1.setText("")
        self.Rapport_1.setText("")
        self.Rattrapages_1.setText("")
        self.pushButton_9.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u" RP", None))
        self.Accueil_2.setText(QCoreApplication.translate("Form", u"Accueil", None))
        self.Cahier_2.setText(QCoreApplication.translate("Form", u"Cahier de texte", None))
        self.Effectivite_2.setText(QCoreApplication.translate("Form", u"Effectivit\u00e9 enseignements", None))
        self.Conformite_2.setText(QCoreApplication.translate("Form", u"Conformit\u00e9 cours", None))
        self.Deroulement_2.setText(QCoreApplication.translate("Form", u"D\u00e9roulement programme", None))
        self.Fiches_2.setText(QCoreApplication.translate("Form", u"Fiches d'evaluations", None))
        self.Avis_2.setText(QCoreApplication.translate("Form", u"Avis etudiants", None))
        self.Rapport_2.setText(QCoreApplication.translate("Form", u"Rapport mensuel", None))
        self.Rattrapages_2.setText(QCoreApplication.translate("Form", u"Rattrapages cours", None))
        self.pushButton_25.setText(QCoreApplication.translate("Form", u"Deconnexion", None))
        self.menu.setText("")
        self.pushButton_29.setText("")
        self.pushButton_30.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"ACCUEIL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Cahier de texte", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nom enseignant ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Plan cours", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Duree du cours ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Date du cours", None));
        self.label_6.setText(QCoreApplication.translate("Form", u"Rensigner la date", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Renseigner la classe", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"EFFECTIVITE DES ENSEIGNEMENTS", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"CONFORMITE COURS", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"DEROULMENT PROGRAMMES", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"FICHES D' EVALUATION", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"AVIS ETUDIANTS", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"RAPPORT MENSUEL", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"RATTRAPAGE DES COURS", None))
        self.label.setText("")
    # retranslateUi

