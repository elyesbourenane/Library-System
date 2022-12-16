from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import sqlite3
from string import digits


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 354)
        Dialog.setFixedSize(412, 354)
        self.label_quantity = QtWidgets.QLabel(Dialog)
        self.label_quantity.setGeometry(QtCore.QRect(30, 260, 81, 21))
        self.label_quantity.setObjectName("label_quantity")
        self.button_confirm = QtWidgets.QPushButton(Dialog)
        self.button_confirm.setGeometry(QtCore.QRect(140, 310, 121, 31))
        self.button_confirm.setObjectName("button_confirm")
        self.entry_title = QtWidgets.QLineEdit(Dialog)
        self.entry_title.setGeometry(QtCore.QRect(130, 110, 251, 31))
        self.entry_title.setObjectName("entry_title")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(30, 110, 61, 21))
        self.label_title.setObjectName("label_title")
        self.label_isbn = QtWidgets.QLabel(Dialog)
        self.label_isbn.setGeometry(QtCore.QRect(30, 40, 61, 21))
        self.label_isbn.setObjectName("label_isbn")
        self.entry_author = QtWidgets.QLineEdit(Dialog)
        self.entry_author.setGeometry(QtCore.QRect(130, 160, 251, 31))
        self.entry_author.setObjectName("entry_author")
        self.label_author = QtWidgets.QLabel(Dialog)
        self.label_author.setGeometry(QtCore.QRect(30, 160, 91, 21))
        self.label_author.setObjectName("label_author")
        self.entry_quantity = QtWidgets.QLineEdit(Dialog)
        self.entry_quantity.setGeometry(QtCore.QRect(130, 260, 251, 31))
        self.entry_quantity.setObjectName("entry_quantity")
        self.entry_isbn = QtWidgets.QLineEdit(Dialog)
        self.entry_isbn.setGeometry(QtCore.QRect(130, 40, 251, 31))
        self.entry_isbn.setObjectName("entry_isbn")
        self.label_category = QtWidgets.QLabel(Dialog)
        self.label_category.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.label_category.setObjectName("label_category")
        self.entry_category = QtWidgets.QLineEdit(Dialog)
        self.entry_category.setGeometry(QtCore.QRect(130, 210, 251, 31))
        self.entry_category.setObjectName("entry_category")
        self.label_enter = QtWidgets.QLabel(Dialog)
        self.label_enter.setGeometry(QtCore.QRect(150, 10, 111, 21))
        self.label_enter.setObjectName("label_enter")
        self.label_infos = QtWidgets.QLabel(Dialog)
        self.label_infos.setGeometry(QtCore.QRect(150, 80, 111, 21))
        self.label_infos.setObjectName("label_infos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.button_confirm.clicked.connect(self.update)
    
    def update(self) :
        isbn = self.entry_isbn.text()
        db = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + "\database.db")
        cr = db.cursor()
        cr.execute("select isbn from books")
        res = [elem[0] for elem in cr.fetchall()]

        if isbn == "" :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations!")
            msg.setText("Please enter ISBN")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        elif not self.are_numbers(isbn) :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations!")
            msg.setText("ISBN must be a number")
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
        
        elif int(isbn) not in res :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("ISBN do not exist!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
            
        else :
            title = self.entry_title.text()
            author = self.entry_author.text()
            category = self.entry_category.text()
            quantity = self.entry_quantity.text()
            if title == "" and author == "" and category == "" and quantity == "" :
                msg = QMessageBox()
                msg.setWindowTitle("Incorrect informations")
                msg.setText("Empty fields!")
                msg.setIcon(QMessageBox.Critical)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                x = msg.exec_()
            
            elif not self.are_numbers(quantity) and quantity != "":
                msg = QMessageBox()
                msg.setWindowTitle("Incorrect informations")
                msg.setText("Quantiy must be a number!")
                msg.setIcon(QMessageBox.Critical)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                x = msg.exec_()
            
            else :
                try :
                    if title != "" :
                        cr.execute(f"update books set title='{title}' where isbn='{isbn}'")

                    if author != "" :
                        cr.execute(f"update books set author='{author}' where isbn='{isbn}'")

                    if category != "" :
                        cr.execute(f"update books set category='{category}' where isbn='{isbn}'")
                    
                    if quantity != "" : 
                        cr.execute(f"update books set quantity='{int(quantity)}' where isbn='{isbn}'")
                    
                    db.commit()

                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("Book informations succesfully updated!")
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_quantity.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Quantity :</span></p></body></html>"))
        self.button_confirm.setText(_translate("Dialog", "Confirm"))
        self.label_title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.label_isbn.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ISBN :</span></p></body></html>"))
        self.label_author.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Author :</span></p></body></html>"))
        self.label_category.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Category :</span></p></body></html>"))
        self.label_enter.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter ISBN :</span></p></body></html>"))
        self.label_infos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Update infos</span></p></body></html>"))


