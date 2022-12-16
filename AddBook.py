from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from string import digits
import sqlite3
import os



class Ui_Addbook(object):
    def setupUi(self, Addbook):
        Addbook.setObjectName("Addbook")
        Addbook.resize(409, 306)
        Addbook.setFixedSize(409, 306)
        Addbook.setWindowTitle("Free Book")
        self.label_title = QtWidgets.QLabel(Addbook)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_title.setObjectName("label_title")
        self.label_author = QtWidgets.QLabel(Addbook)
        self.label_author.setGeometry(QtCore.QRect(20, 70, 91, 21))
        self.label_author.setObjectName("label_author")
        self.label_quantity = QtWidgets.QLabel(Addbook)
        self.label_quantity.setGeometry(QtCore.QRect(20, 170, 81, 21))
        self.label_quantity.setObjectName("label_quantity")
        self.label_category = QtWidgets.QLabel(Addbook)
        self.label_category.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_category.setObjectName("label_category")
        self.label_isbn = QtWidgets.QLabel(Addbook)
        self.label_isbn.setGeometry(QtCore.QRect(30, 220, 61, 21))
        self.label_isbn.setObjectName("label_isbn")
        self.entry_title = QtWidgets.QLineEdit(Addbook)
        self.entry_title.setGeometry(QtCore.QRect(120, 20, 251, 31))
        self.entry_title.setObjectName("entry_title")
        self.entry_author = QtWidgets.QLineEdit(Addbook)
        self.entry_author.setGeometry(QtCore.QRect(120, 70, 251, 31))
        self.entry_author.setObjectName("entry_author")
        self.entry_category = QtWidgets.QLineEdit(Addbook)
        self.entry_category.setGeometry(QtCore.QRect(120, 120, 251, 31))
        self.entry_category.setObjectName("entry_category")
        self.entry_quantity = QtWidgets.QLineEdit(Addbook)
        self.entry_quantity.setGeometry(QtCore.QRect(120, 170, 251, 31))
        self.entry_quantity.setObjectName("entry_quantity")
        self.entry_isbn = QtWidgets.QLineEdit(Addbook)
        self.entry_isbn.setGeometry(QtCore.QRect(120, 220, 251, 31))
        self.entry_isbn.setObjectName("entry_isbn")
        self.button_add = QtWidgets.QPushButton(Addbook)
        self.button_add.setGeometry(QtCore.QRect(140, 260, 121, 31))
        self.button_add.setObjectName("button_add")

        self.retranslateUi(Addbook)
        QtCore.QMetaObject.connectSlotsByName(Addbook)

        self.button_add.clicked.connect(self.add)


    
    def add(self) :
        title = self.entry_title.text()
        author = self.entry_author.text()
        category = self.entry_category.text()
        quantity = self.entry_quantity.text()
        isbn = self.entry_isbn.text()

        if title == "" or author =="" or category == "" or quantity == "" or isbn == "" :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Empty fields!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()

        elif not self.are_numbers(isbn) :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("ISBN must be a number!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        elif len(isbn) != 13 :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("ISBN must be a number of 13 digits!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        elif not self.are_numbers(quantity) :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Quantiy must be a number!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        else :
            try :   
                db = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + "\database.db")
                cr = db.cursor()
                cr.execute(f"insert into books (title, author, category, quantity, nb_borrow, isbn) values ('{title}', '{author}', '{category}', '{int(quantity)}', '0', '{int(isbn)}')")
                db.commit()

                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Book succesfully added!")
                msg.setIcon(QMessageBox.Information)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                x = msg.exec_()
                
                self.entry_title.setText("")
                self.entry_author.setText("")
                self.entry_category.setText("")
                self.entry_quantity.setText("")
                self.entry_isbn.setText("")

            except :
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error occured!")
                msg.setIcon(QMessageBox.Critical)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                x = msg.exec_()

    def are_numbers(self, s) :
        for c in s :
            if c not in digits :
                return False
        return True


    def retranslateUi(self, Addbook):
        _translate = QtCore.QCoreApplication.translate
        Addbook.setWindowTitle(_translate("Addbook", "Dialog"))
        self.label_title.setText(_translate("Addbook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.label_author.setText(_translate("Addbook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Author :</span></p></body></html>"))
        self.label_quantity.setText(_translate("Addbook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Quantity :</span></p></body></html>"))
        self.label_category.setText(_translate("Addbook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Category :</span></p></body></html>"))
        self.label_isbn.setText(_translate("Addbook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ISBN :</span></p></body></html>"))
        self.button_add.setText(_translate("Addbook", "Add"))

