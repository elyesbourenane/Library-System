from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import sqlite3



class Ui_history(object):
    def setupUi(self, history, username):
        self.username = username
        history.setObjectName("history")
        history.resize(354, 387)
        history.setFixedSize(354, 387)
        self.label_books = QtWidgets.QLabel(history)
        self.label_books.setGeometry(QtCore.QRect(130, 10, 71, 31))
        self.label_books.setObjectName("label_books")
        self.butto_ok = QtWidgets.QPushButton(history)
        self.butto_ok.setGeometry(QtCore.QRect(90, 340, 81, 31))
        self.butto_ok.setObjectName("butto_ok")
        self.butto_return = QtWidgets.QPushButton(history)
        self.butto_return.setGeometry(QtCore.QRect(200, 340, 81, 31))
        self.butto_return.setObjectName("butto_return")
        self.tableWidget = QtWidgets.QTableWidget(history)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 331, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11) 
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


        self.retranslateUi(history)
        QtCore.QMetaObject.connectSlotsByName(history)

        self.butto_return.clicked.connect(self.return_book)

        db = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) +"\database.db")
        cr = db.cursor()

        res = cr.execute(f"select actually, history from users where username = '{self.username}'").fetchall()[0]
        actually = res[0].split("-")
        history = res[1].split("-")

        for row in range(self.tableWidget.rowCount()) :
            self.tableWidget.removeRow(0)
        
        index = 0
        for book in actually :
            if book != "" :
                self.tableWidget.insertRow(index)
                self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(book))
                self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem("No"))
                index += 1
        
        for book in history :
            if book != "" and book not in actually:
                self.tableWidget.insertRow(index)
                self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(book))
                self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem("Yes"))
                index += 1
    
    def return_book(self) :
        db = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) +"\database.db")
        cr = db.cursor()

        row = self.tableWidget.currentRow()
        
        if self.tableWidget.selectionModel().hasSelection() :
            row = self.tableWidget.currentRow()
            sauv = cr.execute(f"select quantity from books where title = '{self.tableWidget.item(row, 0).text()}'").fetchall()[0]
            quantity = int(sauv[0])

            sauv2 = cr.execute(f"select actually, nb_borrow from users where username = '{self.username}'").fetchall()[0]
            actually = sauv2[0].split("-")
            nb = int(sauv2[1])

            ac = ""
            for s in actually :
                if s != self.tableWidget.item(row, 0).text() and s != "":
                    ac = ac + s + "-"
            
            cr.execute(f"update books set quantity = '{quantity + 1}' where title = '{self.tableWidget.item(row, 0).text()}'")
            cr.execute(f"update users set actually = '{ac}', nb_borrow = '{nb - 1}' where username = '{self.username}'")

            db.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Informations")
            msg.setText("Book succesfully returned!")
            msg.setIcon(QMessageBox.Information)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()

        else :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("You did not selected any book!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()

    def retranslateUi(self, history):
        _translate = QtCore.QCoreApplication.translate
        history.setWindowTitle(_translate("history", "Dialog"))
        self.label_books.setText(_translate("history", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">History : </span></p></body></html>"))
        self.butto_ok.setText(_translate("history", "OK"))
        self.butto_return.setText(_translate("history", "Return book"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("history", "Book"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("history", "Returned"))


