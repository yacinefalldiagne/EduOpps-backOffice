# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(739, 528)
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(40, 0, 701, 41))
        self.horizontalFrame.setStyleSheet(u"background-color: rgb(73, 144, 196);")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalFrame1 = QFrame(Form)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setGeometry(QRect(0, 490, 751, 41))
        self.horizontalFrame1.setStyleSheet(u"background-color: rgb(73, 144, 196);")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 100, 481, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.Username = QLineEdit(Form)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(250, 200, 271, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.Username.setFont(font1)
        self.Username.setStyleSheet(u"border-radius:15px;")
        self.Username.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(250, 290, 271, 41))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"border-radius:15px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 370, 131, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(73, 144, 196);\n"
"color: rgb(28, 39, 255);\n"
"border-radius:15px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" ")
        self.logESP = QLabel(Form)
        self.logESP.setObjectName(u"logESP")
        self.logESP.setGeometry(QRect(0, 0, 41, 41))
        self.logESP.setStyleSheet(u"image: url(:/img/images/logoTypeEsp.jpg);\n"
"background-image: url(:/img/images/logoTypeEsp.jpg);")
        self.logESP_2 = QLabel(Form)
        self.logESP_2.setObjectName(u"logESP_2")
        self.logESP_2.setGeometry(QRect(180, 200, 41, 41))
        self.logESP_2.setStyleSheet(u"background-image: url(:/img/images/loco pers (1).jpg);\n"
"image: url(:/img/images/loco pers (1).jpg);")
        self.horizontalFrame.raise_()
        self.horizontalFrame.raise_()
        self.label.raise_()
        self.Username.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.logESP_2.raise_()
        self.logESP.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">username</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"           BIENVENU DANS VOTRE PLATEFORME", None))
#if QT_CONFIG(tooltip)
        self.Username.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">username</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Username.setText("")
        self.Username.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Connexion", None))
        self.logESP.setText("")
        self.logESP_2.setText("")
    # retranslateUi

