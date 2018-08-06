# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from score import Ui_Dialog2
class Ui_Dialog(object):

    def givescore(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show()
        #print(self.playersavailableList.item(1).text())

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 374)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.teamcomboBox = QtWidgets.QComboBox(Dialog)
        self.teamcomboBox.setGeometry(QtCore.QRect(70, 40, 69, 22))
        self.teamcomboBox.setObjectName("teamcomboBox")
        self.matchcomboBox = QtWidgets.QComboBox(Dialog)
        self.matchcomboBox.setGeometry(QtCore.QRect(340, 40, 69, 22))
        self.matchcomboBox.setObjectName("matchcomboBox")
        self.matchcomboBox.addItem("")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 60, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.playersList = QtWidgets.QListWidget(Dialog)
        self.playersList.setGeometry(QtCore.QRect(50, 101, 171, 221))
        self.playersList.setObjectName("playersList")
        self.pointslist = QtWidgets.QListWidget(Dialog)
        self.pointslist.setGeometry(QtCore.QRect(260, 100, 171, 221))
        self.pointslist.setObjectName("pointslist")
        self.calculatescoreButton = QtWidgets.QPushButton(Dialog)
        self.calculatescoreButton.setGeometry(QtCore.QRect(190, 330, 101, 23))
        self.calculatescoreButton.clicked.connect(self.givescore)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.calculatescoreButton.setFont(font)
        self.calculatescoreButton.setObjectName("calculatescoreButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 83, 47, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 82, 47, 21))
        self.label_3.setObjectName("label_3")
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT Name FROM TeamsList;")
        result=curs.fetchall()
        for record in result:
            self.teamcomboBox.addItem(record[0])
        item=self.teamcomboBox.currentText()
        curs.execute("SELECT * FROM Teams WHERE Name='"+item+"';")
        result=curs.fetchall()
        for record in result:
            self.playersList.addItem(record[1])
            self.pointslist.addItem(record[2])
        self.teamcomboBox.currentTextChanged.connect(self.change)
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("INSERT INTO Teams(Name,Value) VALUES('"+self.teamcomboBox.currentText()+"','X');")
        connection.commit()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def change(self):
        self.playersList.clear()
        self.pointslist.clear()
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        item=self.teamcomboBox.currentText()
        curs.execute("SELECT * FROM Teams WHERE Name='"+item+"' AND Value!='X';")
        result=curs.fetchall()
        for record in result:
            self.playersList.addItem(record[1])
            self.pointslist.addItem(record[2])
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("UPDATE Teams SET Name='"+item+"' WHERE Value='X';")
        connection.commit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.matchcomboBox.setItemText(0, _translate("Dialog", "Match1"))
        self.calculatescoreButton.setText(_translate("Dialog", "Calculate Score"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.label_3.setText(_translate("Dialog", "Points"))

