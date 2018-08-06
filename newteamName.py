# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewTeamName.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_Dialog1(object):
    def __init__(self):
        self.c=0
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(335, 172)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font1 = QtGui.QFont()
        font1.setPointSize(6.5)
        font1.setBold(True)
        font1.setWeight(70)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2.setFont(font1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.ok)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def ok(self):
        self.label_2.setText("Close this Dialog Box !")
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        try:
            curs.execute("INSERT INTO Teams(Name,Value) VALUES('"+self.lineEdit.text()+"','X');")
            curs.execute("INSERT INTO TeamsList(Name,Value) VALUES('"+self.lineEdit.text()+"','X');")
            connection.commit()
            self.c=0
        except:
            self.showMessage("Warning","This team name already exists")
            connection.rollback()
            self.c=1
        if self.c==0:
            self.lineEdit.setReadOnly(True)

    def showMessage(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
                

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Team Name"))
        self.pushButton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

