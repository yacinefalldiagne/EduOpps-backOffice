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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1593, 763)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.icon_only_widget = QWidget(Form)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setGeometry(QRect(17, 17, 38, 661))
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
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/logo pers.jpeg);")

        self.verticalLayout_2.addWidget(self.label)

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

        self.Fiches_1 = QPushButton(self.icon_only_widget)
        self.Fiches_1.setObjectName(u"Fiches_1")
        self.Fiches_1.setStyleSheet(u"text-align:center;")
        icon4 = QIcon()
        icon4.addFile(u"Images/bonne-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Fiches_1.setIcon(icon4)
        self.Fiches_1.setCheckable(True)
        self.Fiches_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Fiches_1)

        self.Avis_1 = QPushButton(self.icon_only_widget)
        self.Avis_1.setObjectName(u"Avis_1")
        self.Avis_1.setStyleSheet(u"text-align:center;")
        icon5 = QIcon()
        icon5.addFile(u"Images/avis-client.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Avis_1.setIcon(icon5)
        self.Avis_1.setCheckable(True)
        self.Avis_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Avis_1)

        self.Rapport_1 = QPushButton(self.icon_only_widget)
        self.Rapport_1.setObjectName(u"Rapport_1")
        self.Rapport_1.setStyleSheet(u"text-align:center;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"Images/rapport-dactivite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rapport_1.setIcon(icon6)
        self.Rapport_1.setCheckable(True)
        self.Rapport_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Rapport_1)

        self.Rattrapages_1 = QPushButton(self.icon_only_widget)
        self.Rattrapages_1.setObjectName(u"Rattrapages_1")
        self.Rattrapages_1.setStyleSheet(u"text-align:center;")
        icon7 = QIcon()
        icon7.addFile(u"Images/calendrier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Rattrapages_1.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u"Images/sortir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.icon_name_widget = QWidget(Form)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setGeometry(QRect(61, 17, 187, 658))
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

        self.Fiches_2 = QPushButton(self.icon_name_widget)
        self.Fiches_2.setObjectName(u"Fiches_2")
        self.Fiches_2.setIcon(icon4)
        self.Fiches_2.setCheckable(True)
        self.Fiches_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Fiches_2)

        self.Avis_2 = QPushButton(self.icon_name_widget)
        self.Avis_2.setObjectName(u"Avis_2")
        self.Avis_2.setIcon(icon5)
        self.Avis_2.setCheckable(True)
        self.Avis_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Avis_2)

        self.Rapport_2 = QPushButton(self.icon_name_widget)
        self.Rapport_2.setObjectName(u"Rapport_2")
        self.Rapport_2.setIcon(icon6)
        self.Rapport_2.setCheckable(True)
        self.Rapport_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Rapport_2)

        self.Rattrapages_2 = QPushButton(self.icon_name_widget)
        self.Rattrapages_2.setObjectName(u"Rattrapages_2")
        self.Rattrapages_2.setIcon(icon7)
        self.Rattrapages_2.setCheckable(True)
        self.Rattrapages_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Rattrapages_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(18, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_25 = QPushButton(self.icon_name_widget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon8)
        self.pushButton_25.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_25)

        self.main_menu = QWidget(Form)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(234, 17, 1361, 721))
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
        icon9 = QIcon()
        icon9.addFile(u"Images/barre-de-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"Images/profil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_30.setIcon(icon10)
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
        self.groupBox_2.setGeometry(QRect(10, 110, 721, 471))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_cahier = QTableWidget(self.groupBox_2)
        if (self.table_cahier.columnCount() < 5):
            self.table_cahier.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_cahier.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_cahier.setObjectName(u"table_cahier")
        self.table_cahier.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_cahier.horizontalHeader().setCascadingSectionResizes(False)
        self.table_cahier.horizontalHeader().setDefaultSectionSize(132)
        self.table_cahier.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.table_cahier, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_16.addWidget(self.label_5)

        self.commentaire_cahier = QTextEdit(self.groupBox_2)
        self.commentaire_cahier.setObjectName(u"commentaire_cahier")

        self.verticalLayout_16.addWidget(self.commentaire_cahier)

        self.btn_commentaire_cahier = QPushButton(self.groupBox_2)
        self.btn_commentaire_cahier.clicked.connect(self.insert_commentaire_cahier)
        self.btn_commentaire_cahier.setObjectName(u"btn_commentaire_cahier")
        self.btn_commentaire_cahier.clicked.connect(self.search_cahier)
        self.btn_commentaire_cahier.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_16.addWidget(self.btn_commentaire_cahier)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 0, 1, 1)

        self.widget = QWidget(self.Cahierdetexte)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 721, 91))
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.edit_classe_cahier = QLineEdit(self.widget)
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


        self.verticalLayout_18.addLayout(self.verticalLayout_9)

        self.btn_cahier = QPushButton(self.widget)
        self.btn_cahier.clicked.connect(self.search_cahier)
        self.btn_cahier.setObjectName(u"btn_cahier")
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

        self.verticalLayout_18.addWidget(self.btn_cahier)

        self.stackedWidget.addWidget(self.Cahierdetexte)
        self.Effectivite = QWidget()
        self.Effectivite.setObjectName(u"Effectivite")
        self.groupBox_5 = QGroupBox(self.Effectivite)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 110, 721, 471))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_cahier_2 = QTableWidget(self.groupBox_5)
        if (self.table_cahier_2.columnCount() < 4):
            self.table_cahier_2.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_cahier_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_cahier_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_cahier_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_cahier_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.table_cahier_2.setObjectName(u"table_cahier_2")
        self.table_cahier_2.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_cahier_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_cahier_2.horizontalHeader().setDefaultSectionSize(132)
        self.table_cahier_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.table_cahier_2, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.Effectivite)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 721, 91))
        self.verticalLayout_22 = QVBoxLayout(self.widget_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.edit_classe_effectivite = QLineEdit(self.widget_4)
        self.edit_classe_effectivite.setObjectName(u"edit_classe_effectivite")
        self.edit_classe_effectivite.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
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

        self.horizontalLayout_8.addWidget(self.edit_classe_effectivite)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)


        self.verticalLayout_22.addLayout(self.verticalLayout_14)

        self.btn_cahier_2 = QPushButton(self.widget_4)
        self.btn_cahier_2.clicked.connect(self.search_effectivite)
        self.btn_cahier_2.setObjectName(u"btn_cahier_2")
        self.btn_cahier_2.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_22.addWidget(self.btn_cahier_2)

        self.stackedWidget.addWidget(self.Effectivite)
        self.Conformite = QWidget()
        self.Conformite.setObjectName(u"Conformite")
        self.groupBox_6 = QGroupBox(self.Conformite)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 150, 881, 441))
        self.groupBox_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table_conformite = QTableWidget(self.groupBox_6)
        if (self.table_conformite.columnCount() < 6):
            self.table_conformite.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_conformite.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.table_conformite.setObjectName(u"table_conformite")
        self.table_conformite.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_conformite.horizontalHeader().setCascadingSectionResizes(False)
        self.table_conformite.horizontalHeader().setDefaultSectionSize(132)
        self.table_conformite.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.table_conformite, 0, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.commentaire_conformite = QTextEdit(self.groupBox_6)
        self.commentaire_conformite.setObjectName(u"commentaire_conformite")

        self.verticalLayout_17.addWidget(self.commentaire_conformite)

        self.btn_commentaire_conformite = QPushButton(self.groupBox_6)
        self.btn_commentaire_cahier.clicked.connect(self.insert_commentaire_conformite)
        self.btn_commentaire_conformite.setObjectName(u"btn_commentaire_conformite")
        self.btn_commentaire_conformite.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_17.addWidget(self.btn_commentaire_conformite)


        self.gridLayout_6.addLayout(self.verticalLayout_17, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.Conformite)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 10, 701, 131))
        self.verticalLayout_19 = QVBoxLayout(self.widget_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.widget_5)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_16.addWidget(self.label_27)

        self.edit_matiere_conformite = QLineEdit(self.widget_5)
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
        self.label_28 = QLabel(self.widget_5)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.edit_nomEnseignant_conformite = QLineEdit(self.widget_5)
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


        self.verticalLayout_19.addLayout(self.verticalLayout_10)

        self.btn_conformite = QPushButton(self.widget_5)
        self.btn_conformite.clicked.connect(self.search_conformite)
        self.btn_conformite.setObjectName(u"btn_conformite")
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

        self.verticalLayout_19.addWidget(self.btn_conformite)

        self.stackedWidget.addWidget(self.Conformite)
        self.FichesEvaluation = QWidget()
        self.FichesEvaluation.setObjectName(u"FichesEvaluation")
        self.groupBox_4 = QGroupBox(self.FichesEvaluation)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 150, 701, 281))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.table_evaluation = QTableWidget(self.groupBox_4)
        if (self.table_evaluation.columnCount() < 3):
            self.table_evaluation.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_evaluation.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_evaluation.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_evaluation.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        self.table_evaluation.setObjectName(u"table_evaluation")
        self.table_evaluation.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_evaluation.horizontalHeader().setCascadingSectionResizes(False)
        self.table_evaluation.horizontalHeader().setDefaultSectionSize(132)
        self.table_evaluation.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.table_evaluation, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.FichesEvaluation)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 701, 121))
        self.verticalLayout_20 = QVBoxLayout(self.widget_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_20 = QLabel(self.widget_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout.addWidget(self.label_20)

        self.edit_classe_evaluation = QLineEdit(self.widget_3)
        self.edit_classe_evaluation.setObjectName(u"edit_classe_evaluation")
        self.edit_classe_evaluation.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
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

        self.horizontalLayout.addWidget(self.edit_classe_evaluation)


        self.verticalLayout_20.addLayout(self.horizontalLayout)

        self.btn_evaluation = QPushButton(self.widget_3)
        self.btn_evaluation.clicked.connect(self.search_evaluation)
        self.btn_evaluation.setObjectName(u"btn_evaluation")
        self.btn_evaluation.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_20.addWidget(self.btn_evaluation)

        self.stackedWidget.addWidget(self.FichesEvaluation)
        self.AvisEtudiants = QWidget()
        self.AvisEtudiants.setObjectName(u"AvisEtudiants")
        self.groupBox_3 = QGroupBox(self.AvisEtudiants)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 190, 1341, 281))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_avis = QTableWidget(self.groupBox_3)
        if (self.table_avis.columnCount() < 10):
            self.table_avis.setColumnCount(10)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_avis.setHorizontalHeaderItem(9, __qtablewidgetitem27)
        self.table_avis.setObjectName(u"table_avis")
        self.table_avis.setStyleSheet(u"border: 1px solid #c6c6c6;\n"
"border-radius: 5px;")
        self.table_avis.horizontalHeader().setCascadingSectionResizes(False)
        self.table_avis.horizontalHeader().setDefaultSectionSize(132)
        self.table_avis.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.table_avis, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.AvisEtudiants)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 701, 151))
        self.verticalLayout_12 = QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.edit_matiere_avis = QLineEdit(self.widget_2)
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


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.btn_avis = QPushButton(self.widget_2)
        self.btn_avis.clicked.connect(self.search_avis)
        self.btn_avis.setObjectName(u"btn_avis")
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

        self.verticalLayout_12.addWidget(self.btn_avis)

        self.stackedWidget.addWidget(self.AvisEtudiants)
        self.RapportMensuel = QWidget()
        self.RapportMensuel.setObjectName(u"RapportMensuel")
        self.widget_8 = QWidget(self.RapportMensuel)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 10, 701, 78))
        self.verticalLayout_13 = QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_22.addWidget(self.label_11)

        self.edit_date_Rapport_3 = QDateEdit(self.widget_8)
        self.edit_date_Rapport_3.setObjectName(u"edit_date_Rapport_3")
        self.edit_date_Rapport_3.setStyleSheet(u"QDateEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #f8f8f8;\n"
"    color: #333;\n"
"    font-family: Arial, sans-serif;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    width: 20px;\n"
"    border-left: 2px solid #ccc;\n"
"    border-radius: 0;\n"
"    background-color: #f8f8f8;\n"
"    image: url(drop_down_icon.png);\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.edit_date_Rapport_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_27.addWidget(self.label_13)

        self.edit_nom_Rapport = QLineEdit(self.widget_8)
        self.edit_nom_Rapport.setObjectName(u"edit_nom_Rapport")
        self.edit_nom_Rapport.setMaximumSize(QSize(16777215, 16777215))
        self.edit_nom_Rapport.setBaseSize(QSize(0, 0))
        self.edit_nom_Rapport.setStyleSheet(u"/* Style de base pour le QLineEdit */\n"
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
        self.edit_nom_Rapport.setReadOnly(False)

        self.horizontalLayout_27.addWidget(self.edit_nom_Rapport)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.layoutWidget = QWidget(self.RapportMensuel)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 110, 701, 391))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.contenu_Rapport = QTextEdit(self.layoutWidget)
        self.contenu_Rapport.setObjectName(u"contenu_Rapport")

        self.verticalLayout_6.addWidget(self.contenu_Rapport)

        self.btn_rapport = QPushButton(self.layoutWidget)
        self.btn_rapport.clicked.connect(self.insert_rapport)
        self.btn_rapport.setObjectName(u"btn_rapport")
        self.btn_rapport.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_6.addWidget(self.btn_rapport)

        self.stackedWidget.addWidget(self.RapportMensuel)
        self.Rattrapagecours = QWidget()
        self.Rattrapagecours.setObjectName(u"Rattrapagecours")
        self.widget_6 = QWidget(self.Rattrapagecours)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(20, 30, 711, 261))
        self.layoutWidget1 = QWidget(self.widget_6)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 681, 221))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_32 = QLabel(self.layoutWidget1)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_25.addWidget(self.label_32)

        self.edit_date_rattrapages = QLineEdit(self.layoutWidget1)
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
        self.label_31 = QLabel(self.layoutWidget1)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_20.addWidget(self.label_31)

        self.edit_heure_rattrapages = QLineEdit(self.layoutWidget1)
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
        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.edit_NomEnseignant_rattrapages = QLineEdit(self.layoutWidget1)
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
        self.label_30 = QLabel(self.layoutWidget1)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_19.addWidget(self.label_30)

        self.edit_matiere_rattrapages = QLineEdit(self.layoutWidget1)
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
        self.label_33 = QLabel(self.layoutWidget1)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_26.addWidget(self.label_33)

        self.edit_classe_rattrapages = QLineEdit(self.layoutWidget1)
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

        self.btn_rattrapage = QPushButton(self.layoutWidget1)
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


        self.retranslateUi(Form)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.pushButton_25.toggled.connect(Form.close)
        self.Accueil_1.toggled.connect(self.Accueil_2.setChecked)
        self.Accueil_2.toggled.connect(self.Accueil_1.setChecked)
        self.Cahier_1.toggled.connect(self.Cahier_2.setChecked)
        self.Cahier_2.toggled.connect(self.Cahier_1.setChecked)
        self.Effectivite_1.toggled.connect(self.Effectivite_2.setChecked)
        self.Effectivite_2.toggled.connect(self.Effectivite_1.setChecked)
        self.Conformite_1.toggled.connect(self.Conformite_2.setChecked)
        self.Conformite_2.toggled.connect(self.Conformite_1.setChecked)
        self.Fiches_2.toggled.connect(self.Fiches_1.setChecked)
        self.Fiches_1.toggled.connect(self.Fiches_2.setChecked)
        self.Avis_2.toggled.connect(self.Avis_1.setChecked)
        self.Avis_1.toggled.connect(self.Avis_2.setChecked)
        self.Rapport_2.toggled.connect(self.Rapport_1.setChecked)
        self.Rapport_1.toggled.connect(self.Rapport_2.setChecked)
        self.Rattrapages_2.toggled.connect(self.Rattrapages_1.setChecked)
        self.Rattrapages_1.toggled.connect(self.Rattrapages_2.setChecked)
        self.pushButton_9.toggled.connect(Form.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.Accueil_1.setText("")
        self.Cahier_1.setText("")
        self.Effectivite_1.setText("")
        self.Conformite_1.setText("")
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
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Date du cours", None));
        ___qtablewidgetitem3 = self.table_cahier.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Heure debut cours", None));
        ___qtablewidgetitem4 = self.table_cahier.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Heure fin cours", None));
        self.label_5.setText(QCoreApplication.translate("Form", u"Laisser un commataire", None))
        self.btn_commentaire_cahier.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Renseigner l'id de la classe ", None))
        self.btn_cahier.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Cahier de texte", None))
        ___qtablewidgetitem5 = self.table_cahier_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Nom enseignant ", None));
        ___qtablewidgetitem6 = self.table_cahier_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Date du cours", None));
        ___qtablewidgetitem7 = self.table_cahier_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Heure debut cours", None));
        ___qtablewidgetitem8 = self.table_cahier_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Heure fin cours", None));
        self.label_14.setText(QCoreApplication.translate("Form", u"Renseigner l'id de la classe ", None))
        self.btn_cahier_2.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Conformite", None))
        ___qtablewidgetitem9 = self.table_conformite.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Nom enseignant ", None));
        ___qtablewidgetitem10 = self.table_conformite.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Nom cours", None));
        ___qtablewidgetitem11 = self.table_conformite.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Nombre heures", None));
        ___qtablewidgetitem12 = self.table_conformite.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Objectif contenu", None));
        ___qtablewidgetitem13 = self.table_conformite.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Evaluation", None));
        ___qtablewidgetitem14 = self.table_conformite.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Contenu dans cahier", None));
        self.label_7.setText(QCoreApplication.translate("Form", u"Laisser un commataire", None))
        self.btn_commentaire_conformite.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Rensigner la matiere", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Renseigner le nom de l'enseignant", None))
        self.btn_conformite.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"FIches d'evaluation", None))
        ___qtablewidgetitem15 = self.table_evaluation.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Nom Etudiant", None));
        ___qtablewidgetitem16 = self.table_evaluation.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Matiere", None));
        ___qtablewidgetitem17 = self.table_evaluation.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Note", None));
        self.label_20.setText(QCoreApplication.translate("Form", u"Renseigner la classe", None))
        self.btn_evaluation.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Avis", None))
        ___qtablewidgetitem18 = self.table_avis.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Matiere", None));
        ___qtablewidgetitem19 = self.table_avis.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"cours", None));
        ___qtablewidgetitem20 = self.table_avis.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Syllabus", None));
        ___qtablewidgetitem21 = self.table_avis.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"objectifs clairs", None));
        ___qtablewidgetitem22 = self.table_avis.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"contenu", None));
        ___qtablewidgetitem23 = self.table_avis.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"contenu respecte", None));
        ___qtablewidgetitem24 = self.table_avis.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"schedule respecter", None));
        ___qtablewidgetitem25 = self.table_avis.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"satisfactions", None));
        ___qtablewidgetitem26 = self.table_avis.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"suggestions", None));
        ___qtablewidgetitem27 = self.table_avis.horizontalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"descriptions", None));
        self.label_16.setText(QCoreApplication.translate("Form", u"Rensigner la matiere", None))
        self.btn_avis.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Rensigner la date de redaction du rapport", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Rensigner le nom du  rapport", None))
        self.btn_rapport.setText(QCoreApplication.translate("Form", u"Envoyer le rapport mensuel", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Rensigner la nouvelle date du cours", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Rensigner La nouvelle heure du cours", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Renseigner le nom du prof", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Reinsgeigner la matiere", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Reinsgeigner la classe", None))
        self.btn_rattrapage.setText(QCoreApplication.translate("Form", u"Valider", None))
    # retranslateUi

