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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(863, 663)
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

        self.horizontalSpacer = QSpacerItem(247, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(246, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton_30 = QPushButton(self.header)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"border: none;\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"Images/profil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_30.setIcon(icon11)
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
        self.label_4.setGeometry(QRect(50, 100, 541, 41))
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
        self.groupBox_2.setGeometry(QRect(10, 150, 581, 321))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_cahier = QTableWidget(self.groupBox_2)
        if (self.table_cahier.columnCount() < 4):
            self.table_cahier.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_cahier.setObjectName(u"table_cahier")
        self.table_cahier.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_cahier.horizontalHeader().setCascadingSectionResizes(False)
        self.table_cahier.horizontalHeader().setDefaultSectionSize(132)
        self.table_cahier.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.table_cahier, 0, 0, 1, 1)

        self.widget = QWidget(self.Cahierdetexte)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 581, 131))
        self.btn_cahier = QPushButton(self.widget)
        self.btn_cahier.clicked.connect(self.search_cahier)
        self.btn_cahier.setObjectName(u"btn_cahier")
        self.btn_cahier.setGeometry(QRect(0, 100, 581, 31))
        self.btn_cahier.setStyleSheet(u"QPushButton {\n"
"    background-color: #333333; \n"
"    color: #FFFFFF; \n"
"    border: 2px solid #333333; /* Bordure */\n"
"    border-radius: 10px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    border-color: #555555; \n"
"}\n"
"\n"
"/* Changement de style lorsqu'on clique */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Couleur de fond lors du clic */\n"
"    border-color: #222222; /* Bordure lors du clic */\n"
"    color: #CCCCCC; /* Couleur du texte lors du clic */\n"
"}\n"
"")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 10, 571, 81))
        self.verticalLayout_9 = QVBoxLayout(self.widget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.edit_classe_cahier = QLineEdit(self.widget1)
        self.edit_classe_cahier.setObjectName(u"edit_classe_cahier")
        self.edit_classe_cahier.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.edit_classe_cahier)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.edit_matiere_cahier = QLineEdit(self.widget1)
        self.edit_matiere_cahier.setObjectName(u"edit_matiere_cahier")
        self.edit_matiere_cahier.setMaximumSize(QSize(16777215, 16777215))
        self.edit_matiere_cahier.setBaseSize(QSize(0, 0))
        self.edit_matiere_cahier.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"")
        self.edit_matiere_cahier.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.edit_matiere_cahier)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

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
        self.groupBox_6 = QGroupBox(self.Conformite)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 150, 581, 321))
        self.groupBox_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table_conformite = QTableWidget(self.groupBox_6)
        if (self.table_conformite.columnCount() < 4):
            self.table_conformite.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.table_conformite.setObjectName(u"table_conformite")
        self.table_conformite.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_conformite.horizontalHeader().setCascadingSectionResizes(False)
        self.table_conformite.horizontalHeader().setDefaultSectionSize(132)
        self.table_conformite.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.table_conformite, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.Conformite)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 10, 581, 121))
        self.btn_conformite = QPushButton(self.widget_5)
        self.btn_conformite.clicked.connect(self.search_conformite)
        self.btn_conformite.setObjectName(u"btn_conformite")
        self.btn_conformite.setGeometry(QRect(10, 80, 561, 39))
        self.btn_conformite.setStyleSheet(u"QPushButton {\n"
"    background-color: #333333; \n"
"    color: #FFFFFF; \n"
"    border: 2px solid #333333; /* Bordure */\n"
"    border-radius: 10px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    border-color: #555555; \n"
"}\n"
"\n"
"/* Changement de style lorsqu'on clique */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Couleur de fond lors du clic */\n"
"    border-color: #222222; /* Bordure lors du clic */\n"
"    color: #CCCCCC; /* Couleur du texte lors du clic */\n"
"}\n"
"")
        self.widget2 = QWidget(self.widget_5)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 571, 68))
        self.verticalLayout_10 = QVBoxLayout(self.widget2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.widget2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_16.addWidget(self.label_27)

        self.edit_matiere_conformite = QLineEdit(self.widget2)
        self.edit_matiere_conformite.setObjectName(u"edit_matiere_conformite")
        self.edit_matiere_conformite.setMaximumSize(QSize(16777215, 16777215))
        self.edit_matiere_conformite.setBaseSize(QSize(0, 0))
        self.edit_matiere_conformite.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"\n"
"")
        self.edit_matiere_conformite.setReadOnly(False)

        self.horizontalLayout_16.addWidget(self.edit_matiere_conformite)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_28 = QLabel(self.widget2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.edit_nomEnseignant_conformite = QLineEdit(self.widget2)
        self.edit_nomEnseignant_conformite.setObjectName(u"edit_nomEnseignant_conformite")
        self.edit_nomEnseignant_conformite.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.edit_nomEnseignant_conformite)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

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
        self.groupBox_3 = QGroupBox(self.AvisEtudiants)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 220, 581, 281))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_avis = QTableWidget(self.groupBox_3)
        if (self.table_avis.columnCount() < 2):
            self.table_avis.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.table_avis.setObjectName(u"table_avis")
        self.table_avis.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_avis.horizontalHeader().setCascadingSectionResizes(False)
        self.table_avis.horizontalHeader().setDefaultSectionSize(132)
        self.table_avis.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.table_avis, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.AvisEtudiants)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 581, 171))
        self.btn_avis = QPushButton(self.widget_2)
        self.btn_avis.clicked.connect(self.search_avis)
        self.btn_avis.setObjectName(u"btn_avis")
        self.btn_avis.setGeometry(QRect(0, 110, 581, 39))
        self.btn_avis.setStyleSheet(u"QPushButton {\n"
"    background-color: #333333; \n"
"    color: #FFFFFF; \n"
"    border: 2px solid #333333; /* Bordure */\n"
"    border-radius: 10px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    border-color: #555555; \n"
"}\n"
"\n"
"/* Changement de style lorsqu'on clique */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Couleur de fond lors du clic */\n"
"    border-color: #222222; /* Bordure lors du clic */\n"
"    color: #CCCCCC; /* Couleur du texte lors du clic */\n"
"}\n"
"")
        self.widget3 = QWidget(self.widget_2)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(0, 10, 581, 79))
        self.verticalLayout_8 = QVBoxLayout(self.widget3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.widget3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.edit_classe_avis = QLineEdit(self.widget3)
        self.edit_classe_avis.setObjectName(u"edit_classe_avis")
        self.edit_classe_avis.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.edit_classe_avis)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.widget3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.edit_matiere_avis = QLineEdit(self.widget3)
        self.edit_matiere_avis.setObjectName(u"edit_matiere_avis")
        self.edit_matiere_avis.setMaximumSize(QSize(16777215, 16777215))
        self.edit_matiere_avis.setBaseSize(QSize(0, 0))
        self.edit_matiere_avis.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"")
        self.edit_matiere_avis.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.edit_matiere_avis)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.AvisEtudiants)
        self.RapportMensuel = QWidget()
        self.RapportMensuel.setObjectName(u"RapportMensuel")
        self.widget_8 = QWidget(self.RapportMensuel)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 10, 571, 41))
        self.widget4 = QWidget(self.widget_8)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(0, 0, 561, 30))
        self.horizontalLayout_22 = QHBoxLayout(self.widget4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_22.addWidget(self.label_11)

        self.edit_date_Rapport = QLineEdit(self.widget4)
        self.edit_date_Rapport.setObjectName(u"edit_date_Rapport")
        self.edit_date_Rapport.setMaximumSize(QSize(16777215, 16777215))
        self.edit_date_Rapport.setBaseSize(QSize(0, 0))
        self.edit_date_Rapport.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	")
        self.edit_date_Rapport.setReadOnly(False)

        self.horizontalLayout_22.addWidget(self.edit_date_Rapport)

        self.widget5 = QWidget(self.RapportMensuel)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(10, 60, 571, 391))
        self.verticalLayout_6 = QVBoxLayout(self.widget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textEdit_Rapport = QTextEdit(self.widget5)
        self.textEdit_Rapport.setObjectName(u"textEdit_Rapport")

        self.verticalLayout_6.addWidget(self.textEdit_Rapport)

        self.recherche_matiere_7 = QPushButton(self.widget5)
        self.recherche_matiere_7.clicked.connect(self.insert_rapport)
        self.recherche_matiere_7.setObjectName(u"recherche_matiere_7")
        self.recherche_matiere_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #333333; \n"
"    color: #FFFFFF; \n"
"    border: 2px solid #333333; /* Bordure */\n"
"    border-radius: 10px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    border-color: #555555; \n"
"}\n"
"\n"
"/* Changement de style lorsqu'on clique */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Couleur de fond lors du clic */\n"
"    border-color: #222222; /* Bordure lors du clic */\n"
"    color: #CCCCCC; /* Couleur du texte lors du clic */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.recherche_matiere_7)

        self.stackedWidget.addWidget(self.RapportMensuel)
        self.Rattrapagecours = QWidget()
        self.Rattrapagecours.setObjectName(u"Rattrapagecours")
        self.widget_6 = QWidget(self.Rattrapagecours)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(20, 30, 581, 361))
        self.widget6 = QWidget(self.widget_6)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(0, 10, 581, 221))
        self.verticalLayout_7 = QVBoxLayout(self.widget6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_32 = QLabel(self.widget6)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_25.addWidget(self.label_32)

        self.edit_date_rattrapages = QLineEdit(self.widget6)
        self.edit_date_rattrapages.setObjectName(u"edit_date_rattrapages")
        self.edit_date_rattrapages.setMaximumSize(QSize(16777215, 16777215))
        self.edit_date_rattrapages.setBaseSize(QSize(0, 0))
        self.edit_date_rattrapages.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	\n"
"")
        self.edit_date_rattrapages.setReadOnly(False)

        self.horizontalLayout_25.addWidget(self.edit_date_rattrapages)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_31 = QLabel(self.widget6)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_20.addWidget(self.label_31)

        self.edit_heure_rattrapages = QLineEdit(self.widget6)
        self.edit_heure_rattrapages.setObjectName(u"edit_heure_rattrapages")
        self.edit_heure_rattrapages.setMaximumSize(QSize(16777215, 16777215))
        self.edit_heure_rattrapages.setBaseSize(QSize(0, 0))
        self.edit_heure_rattrapages.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	")
        self.edit_heure_rattrapages.setReadOnly(False)

        self.horizontalLayout_20.addWidget(self.edit_heure_rattrapages)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_29 = QLabel(self.widget6)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.edit_NomEnseignant_rattrapages = QLineEdit(self.widget6)
        self.edit_NomEnseignant_rattrapages.setObjectName(u"edit_NomEnseignant_rattrapages")
        self.edit_NomEnseignant_rattrapages.setMaximumSize(QSize(16777215, 16777215))
        self.edit_NomEnseignant_rattrapages.setBaseSize(QSize(0, 0))
        self.edit_NomEnseignant_rattrapages.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	")
        self.edit_NomEnseignant_rattrapages.setReadOnly(False)

        self.horizontalLayout_18.addWidget(self.edit_NomEnseignant_rattrapages)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_30 = QLabel(self.widget6)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_19.addWidget(self.label_30)

        self.edit_matiere_rattrapages = QLineEdit(self.widget6)
        self.edit_matiere_rattrapages.setObjectName(u"edit_matiere_rattrapages")
        self.edit_matiere_rattrapages.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	")

        self.horizontalLayout_19.addWidget(self.edit_matiere_rattrapages)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_33 = QLabel(self.widget6)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_26.addWidget(self.label_33)

        self.edit_classe_rattrapages = QLineEdit(self.widget6)
        self.edit_classe_rattrapages.setObjectName(u"edit_classe_rattrapages")
        self.edit_classe_rattrapages.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
"QLineEdit {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure par d\u00e9faut */\n"
"    border-bottom: 1px solid #CCCCCC; /* Bordure en bas seulement */\n"
"    padding: 2px; /* Espacement du texte \u00e0 l'int\u00e9rieur */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    color: #333333; /* Couleur du texte */\n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QLineEdit:hover {\n"
"    border-bottom-color: #AAAAAA; /* Couleur de la bordure en bas au survol */\n"
"}\n"
"\n"
"/* Changement de style lorsqu'il est actif/focus */\n"
"QLineEdit:focus {\n"
"    border-bottom-color: #007ACC; /* Couleur de la bordure en bas lorsqu'il est actif */\n"
"}\n"
"	")

        self.horizontalLayout_26.addWidget(self.edit_classe_rattrapages)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.btn_rattrapage = QPushButton(self.widget6)
        self.btn_rattrapage.clicked.connect(self.insert_rattrapages)
        self.btn_rattrapage.setObjectName(u"btn_rattrapage")
        self.btn_rattrapage.setStyleSheet(u"QPushButton {\n"
"    background-color: #333333; \n"
"    color: #FFFFFF; \n"
"    border: 2px solid #333333; /* Bordure */\n"
"    border-radius: 10px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Changement de style au survol */\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"    border-color: #555555; \n"
"}\n"
"\n"
"/* Changement de style lorsqu'on clique */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; /* Couleur de fond lors du clic */\n"
"    border-color: #222222; /* Bordure lors du clic */\n"
"    color: #CCCCCC; /* Couleur du texte lors du clic */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.btn_rattrapage)

        self.stackedWidget.addWidget(self.Rattrapagecours)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 36, 16))
        self.label.setStyleSheet(u"image: url(:/logo pers.jpeg);")
        self.widget7 = QWidget(Form)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_17 = QHBoxLayout(self.widget7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget8 = QWidget(Form)
        self.widget8.setObjectName(u"widget8")
        self.widget8.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_21 = QHBoxLayout(self.widget8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget9 = QWidget(Form)
        self.widget9.setObjectName(u"widget9")
        self.widget9.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_23 = QHBoxLayout(self.widget9)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)

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

        self.stackedWidget.setCurrentIndex(7)


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
        self.pushButton_30.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"BIENVENU DANS VOTRE PAGE D' ACCUEIL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Cahier de texte", None))
        ___qtablewidgetitem = self.table_cahier.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nom enseignant ", None));
        ___qtablewidgetitem1 = self.table_cahier.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Plan cours", None));
        ___qtablewidgetitem2 = self.table_cahier.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Duree du cours ", None));
        ___qtablewidgetitem3 = self.table_cahier.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Date du cours", None));
        self.btn_cahier.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Renseigner la classe", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Rensigner la matiere", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"EFFECTIVITE DES ENSEIGNEMENTS", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Conformite", None))
        ___qtablewidgetitem4 = self.table_conformite.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Nom enseignant ", None));
        ___qtablewidgetitem5 = self.table_conformite.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Duree du cours ", None));
        ___qtablewidgetitem6 = self.table_conformite.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Plan cours", None));
        ___qtablewidgetitem7 = self.table_conformite.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Syllabus", None));
        self.btn_conformite.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Rensigner la matiere", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Renseigner le nom de l'enseignant", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"DEROULMENT PROGRAMMES", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"FICHES D' EVALUATION", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Avis", None))
        ___qtablewidgetitem8 = self.table_avis.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Matiere", None));
        ___qtablewidgetitem9 = self.table_avis.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Avis", None));
        self.btn_avis.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Renseigner la classe", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Rensigner la matiere", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Rensigner la date de redaction du rapport", None))
        self.recherche_matiere_7.setText(QCoreApplication.translate("Form", u"Envoyer le rapport mensuel", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Rensigner la nouvelle date du cours", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Rensigner La nouvelle heure du cours", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Renseigner le nom du prof", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Reinsgeigner la matiere", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Reinsgeigner la classe", None))
        self.btn_rattrapage.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label.setText("")
    # retranslateUi

