# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluate import Ui_Dialog
from newteamName import Ui_Dialog1
import math
import sqlite3
import time
class Ui_MainWindow(object):
    def __init__(self):
        self.nBat=0
        self.nBow=0
        self.nAr=0
        self.nWk=0
        self.pavailable=1000
        self.pused=0
        self.teamvalue=0

    def showMessage(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def displayBAT(self,MainWindow):
        self.playersavailableList.clear ()
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT Player FROM Stats WHERE Ctg='BAT';")
        result=curs.fetchall()
        c=self.playersusedList.count()
        if self.BATButton.isChecked()==True:
            for record in result:
                check=0
                for i in range(0,c):
                    if self.playersusedList.item(i).text() == record[0]:
                        check=1
                if check==0:
                    self.playersavailableList.addItem(record[0])
    def displayBOW(self,MainWindow):
        self.playersavailableList.clear ()
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT Player FROM Stats WHERE Ctg='BOW';")
        result=curs.fetchall()
        c=self.playersusedList.count()
        if self.BOWButton.isChecked()==True:
            for record in result:
                check=0
                for i in range(0,c):
                    if self.playersusedList.item(i).text() == record[0]:
                        check=1
                if check==0:
                    self.playersavailableList.addItem(record[0])
    def displayAR(self,MainWindow):
        self.playersavailableList.clear ()
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT Player FROM Stats WHERE Ctg='AR';")
        result=curs.fetchall()
        c=self.playersusedList.count()
        if self.ARButton.isChecked()==True:
            for record in result:
                check=0
                for i in range(0,c):
                    if self.playersusedList.item(i).text() == record[0]:
                        check=1
                if check==0:
                    self.playersavailableList.addItem(record[0])
    def displayWK(self,MainWindow):
        self.playersavailableList.clear ()
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT Player FROM Stats WHERE Ctg='WK';")
        result=curs.fetchall()
        c=self.playersusedList.count()
        if self.WKButton.isChecked()==True:
            for record in result:
                check=0
                for i in range(0,c):
                    if self.playersusedList.item(i).text() == record[0]:
                        check=1
                if check==0:
                    self.playersavailableList.addItem(record[0])
                    
        

    def selectplayer(self, item):
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("SELECT * FROM Teams;")
        result=curs.fetchall()
        for record in result:
            if record[2]=="X":
                self.teamnameLabel.setText(record[0])
                break
        if self.playersusedList.count()>=11:
            self.showMessage('Warning',"You can't select more than 11 players !!")
            return
        #connection=sqlite3.connect('Cricket.db')
        #curs=connection.cursor()
        l=0
        c=self.playersusedList.count()
        curs.execute("SELECT * FROM Stats WHERE Ctg='WK' AND Player='"+self.playersavailableList.item(self.playersavailableList.row(item)).text()+"';")
        record=curs.fetchall()
        if len(record)>0:
            for i in range(0,c):
                curs.execute("SELECT * FROM Stats WHERE Ctg='WK' AND Player='"+self.playersusedList.item(i).text()+"';")
                record=curs.fetchall()
                l=l+len(record)
            if l>0:
                self.showMessage('Warning',"You can't select more than one Wicket-Keeper")
                return
        curs.execute("SELECT Value FROM Stats WHERE Player='"+self.playersavailableList.item(self.playersavailableList.row(item)).text()+"';")
        record=curs.fetchone()
        if self.pavailable<int(record[0]):
            self.showMessage("Warning","You don't have enough points remaining")
            return
        self.pavailable-=int(record[0])
        self.pused+=int(record[0])
        self.pointsavailableButton.setText(str(self.pavailable))
        self.pointsusedButton.setText(str(self.pused))
        self.playersusedList.addItem(item.text())
        if self.BATButton.isChecked()==True:
            self.nBat+=1
            self.BATLabel.setText(str(self.nBat))
        if self.BOWButton.isChecked()==True:
            self.nBow+=1
            self.BOWLabel.setText(str(self.nBow))
        if self.ARButton.isChecked()==True:
            self.nAr+=1
            self.ARLabel.setText(str(self.nAr))
        if self.WKButton.isChecked()==True:
            self.nWk+=1
            self.WKLabel.setText(str(self.nWk))
        self.playersavailableList.takeItem(self.playersavailableList.row(item))
    def deselectplayer(self,item):
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        check=0
        if self.BATButton.isChecked()==True:
            curs.execute("SELECT * FROM Stats WHERE Ctg='BAT' AND Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
            record=curs.fetchall()
            if len(record)>0:
                check=1
        elif self.BOWButton.isChecked()==True:
            curs.execute("SELECT * FROM Stats WHERE Ctg='BOW' AND Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
            record=curs.fetchall()
            if len(record)>0:
                check=1
        elif self.ARButton.isChecked()==True:
            curs.execute("SELECT * FROM Stats WHERE Ctg='AR' AND Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
            record=curs.fetchall()
            if len(record)>0:
                check=1
        elif self.WKButton.isChecked()==True:
            curs.execute("SELECT * FROM Stats WHERE Ctg='WK' AND Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
            record=curs.fetchall()
            if len(record)>0:
                check=1
        if check==1:
            self.playersavailableList.addItem(item.text())
        curs.execute("SELECT Ctg FROM Stats WHERE Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
        record=curs.fetchone()
        if record[0]=="BAT":
            self.nBat-=1
            self.BATLabel.setText(str(self.nBat))
        if record[0]=="BOW":
            self.nBow-=1
            self.BOWLabel.setText(str(self.nBow))
        if record[0]=="AR":
            self.nAr-=1
            self.ARLabel.setText(str(self.nAr))
        if record[0]=="WK":
            self.nWk-=1
            self.WKLabel.setText(str(self.nWk))
        curs.execute("SELECT Value FROM Stats WHERE Player='"+self.playersusedList.item(self.playersusedList.row(item)).text()+"';")
        record=curs.fetchone()
        self.pavailable+=int(record[0])
        self.pused-=int(record[0])
        self.pointsavailableButton.setText(str(self.pavailable))
        self.pointsusedButton.setText(str(self.pused))
        self.playersusedList.takeItem(self.playersusedList.row(item))

    def clickmenu(self,action):
        txt=(action.text())
        if txt=="EVALUATE Team":
            self.onclickingEVALUATE()
        elif txt=="NEW Team":
            self.onclickingNEW()
        elif txt=="SAVE Team":
            self.onclickingSAVE()

    def onclickingSAVE(self):
        if self.playersusedList.count()<11:
            self.showMessage('Warning',"You have to select only 11 players!!")
            return
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("DELETE FROM Teams WHERE Value='X';")
        connection.commit()
        self.teamvalue=0
        #print(self.teamnameLabel.text())
        for i in range(0,11):
            s1=self.teamnameLabel.text()
            s2=self.playersusedList.item(i).text()
            curs.execute("SELECT * FROM Match WHERE Player='"+s2+"';")
            record=curs.fetchone()
            pscored=record[1]//2
            if record[1]>=50 and record[1]<100:
                pscored+=5
            elif record[1]>=100:
                pscored+=10
            if record[2]!=0 and (record[1]/record[2])>=0.8 and (record[1]/record[2])<=1:
                pscored+=2
            elif record[2]!=0 and (record[1]/record[2])>1:
                pscored+=4
            pscored+=record[3]
            pscored+=(record[4]*2)
            pscored+=(10*record[8])
            if record[5]!=0 and (record[7]/record[5])>=3.5 and (record[7]/record[5])<4.5:
                pscored+=4
            elif record[5]!=0 and (record[7]/record[5])>=2 and (record[7]/record[5])<3.5:
                pscored+=7
            elif record[5]!=0 and (record[7]/record[5])<2:
                pscored+=10
            if record[8]>=3 and record[8]<5:
                pscored+=5
            elif record[8]>=5:
                pscored+=10
            pscored+=record[9]
            pscored+=record[10]
            pscored+=record[11]
            self.teamvalue+=pscored
            s3=str(pscored)
            curs.execute("INSERT INTO Teams(Name,Players,Value) VALUES(?,?,?);",(s1,s2,s3))
        connection.commit()
        curs.execute("UPDATE TeamsList SET Value='"+str(self.teamvalue)+"' WHERE Name='"+s1+"';")
        connection.commit()

    def onclickingNEW(self):
        self.playersusedList.clear()
        self.nBat=0
        self.nBow=0
        self.nAr=0
        self.nWk=0
        self.pavailable=1000
        self.pused=0
        connection=sqlite3.connect('Cricket.db')
        curs=connection.cursor()
        curs.execute("DELETE FROM Teams WHERE Value='X';")
        connection.commit()
        self.pointsavailableButton.setText(str(self.pavailable))
        self.pointsusedButton.setText(str(self.pused))
        self.WKLabel.setText(str(self.nWk))
        self.BATLabel.setText(str(self.nBat))
        self.ARLabel.setText(str(self.nAr))
        self.BOWLabel.setText(str(self.nBow))
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window)
        self.window.show()
        self.BATButton.setChecked(True)
        
        
        

    def onclickingEVALUATE(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        #print(self.playersavailableList.item(1).text())
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 433)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 578, 16))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.BATLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.BATLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.BATLabel.setObjectName("BATLabel")
        self.horizontalLayout.addWidget(self.BATLabel)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.BOWLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.BOWLabel.setObjectName("BOWLabel")
        self.horizontalLayout.addWidget(self.BOWLabel)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.ARLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ARLabel.setObjectName("ARLabel")
        self.horizontalLayout.addWidget(self.ARLabel)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.WKLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.WKLabel.setObjectName("WKLabel")
        self.horizontalLayout.addWidget(self.WKLabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 100, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BATButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.BATButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.BATButton.setObjectName("BATButton")
        self.horizontalLayout_3.addWidget(self.BATButton)
        self.BOWButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.BOWButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.BOWButton.setObjectName("BOWButton")
        self.horizontalLayout_3.addWidget(self.BOWButton)
        self.ARButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.ARButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.ARButton.setObjectName("ARButton")
        self.horizontalLayout_3.addWidget(self.ARButton)
        self.WKButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.WKButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.WKButton.setObjectName("WKButton")

        self.BATButton.toggled.connect(self.displayBAT)
        self.BOWButton.toggled.connect(self.displayBOW)
        self.ARButton.toggled.connect(self.displayAR)
        self.WKButton.toggled.connect(self.displayWK)

        self.horizontalLayout_3.addWidget(self.WKButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(330, 100, 201, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.teamnameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.teamnameLabel.setStyleSheet("")
        self.teamnameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.teamnameLabel.setObjectName("teamnameLabel")
        self.horizontalLayout_4.addWidget(self.teamnameLabel)
        self.playersavailableList = QtWidgets.QListWidget(self.centralwidget)
        self.playersavailableList.setGeometry(QtCore.QRect(40, 131, 201, 221))
        self.playersavailableList.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.playersavailableList.setObjectName("playersavailableList")
        self.playersavailableList.itemDoubleClicked.connect(self.selectplayer)
        
        self.playersusedList = QtWidgets.QListWidget(self.centralwidget)
        self.playersusedList.setGeometry(QtCore.QRect(330, 130, 201, 221))
        self.playersusedList.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.playersusedList.setObjectName("playersusedList")
        self.playersusedList.itemDoubleClicked.connect(self.deselectplayer)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 80, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pointsavailableButton = QtWidgets.QLabel(self.centralwidget)
        self.pointsavailableButton.setGeometry(QtCore.QRect(140, 80, 51, 16))
        self.pointsavailableButton.setObjectName("pointsavailableButton")
        self.pointsusedButton = QtWidgets.QLabel(self.centralwidget)
        self.pointsusedButton.setGeometry(QtCore.QRect(410, 80, 51, 16))
        self.pointsusedButton.setObjectName("pointsusedButton")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(260, 220, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.playersavailableList.raise_()
        self.playersusedList.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.pointsavailableButton.raise_()
        self.pointsusedButton.raise_()
        self.label_16.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(True)
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setStyleSheet("background-color: rgb(188, 200, 200);")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionOPEN_Team.setFont(font)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionSAVE_Team.setFont(font)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionEVALUATE_Team.setFont(font)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menubar.triggered[QtWidgets.QAction].connect(self.clickmenu)             


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.BATLabel.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.BOWLabel.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.ARLabel.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.WKLabel.setText(_translate("MainWindow", "##"))
        self.BATButton.setText(_translate("MainWindow", "BAT"))
        self.BOWButton.setText(_translate("MainWindow", "BOW"))
        self.ARButton.setText(_translate("MainWindow", "AR"))
        self.WKButton.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name :-"))
        self.teamnameLabel.setText(_translate("MainWindow", "Displayed Here"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Points Available"))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.pointsavailableButton.setText(_translate("MainWindow", "####"))
        self.pointsusedButton.setText(_translate("MainWindow", "###"))
        self.label_16.setText(_translate("MainWindow", ">"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        

#import ab_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

