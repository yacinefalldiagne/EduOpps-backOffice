# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 528)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalFrame_2 = QtWidgets.QFrame(Form)
        self.horizontalFrame_2.setGeometry(QtCore.QRect(40, 0, 701, 41))
        self.horizontalFrame_2.setStyleSheet("background-color: rgb(73, 144, 196);")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Username = QtWidgets.QLineEdit(Form)
        self.Username.setGeometry(QtCore.QRect(250, 220, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Username.setFont(font)
        self.Username.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(210, 214, 214);")
        self.Username.setObjectName("Username")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(210, 214, 214);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 410, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(73, 144, 196);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.logESP = QtWidgets.QLabel(Form)
        self.logESP.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.logESP.setPixmap(QtGui.QPixmap("images/logoTypeEsp.jpg"))
        self.logESP.setScaledContents(True)
        self.logESP.setObjectName("logESP")
        self.logESP_2 = QtWidgets.QLabel(Form)
        self.logESP_2.setGeometry(QtCore.QRect(190, 220, 41, 41))
        self.logESP_2.setStyleSheet("image: url(:/img/images/loco pers (1).jpg);")
        self.logESP_2.setObjectName("logESP_2")
        self.logESP_3 = QtWidgets.QLabel(Form)
        self.logESP_3.setGeometry(QtCore.QRect(190, 330, 45, 45))
        self.logESP_3.setPixmap(QtGui.QPixmap("images/lock.png"))
        self.logESP_3.setScaledContents(True)
        self.logESP_3.setObjectName("logESP_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 60, 101, 141))
        self.label_2.setPixmap(QtGui.QPixmap("images/user.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalFrame_2.raise_()
        self.Username.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.logESP.raise_()
        self.logESP_2.raise_()
        self.logESP_3.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "BIENVENUE DANS VOTRE PLATEFORME"))
        self.Username.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Connexion"))
