from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import sqlite3
import re


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 493)
        Dialog.setFixedSize(476, 493)
        self.label_firstname = QtWidgets.QLabel(Dialog)
        self.label_firstname.setGeometry(QtCore.QRect(30, 120, 121, 31))
        self.label_firstname.setObjectName("label_firstname")
        self.label_lastname = QtWidgets.QLabel(Dialog)
        self.label_lastname.setGeometry(QtCore.QRect(30, 170, 111, 31))
        self.label_lastname.setObjectName("label_lastname")
        self.label_address = QtWidgets.QLabel(Dialog)
        self.label_address.setGeometry(QtCore.QRect(30, 220, 131, 31))
        self.label_address.setObjectName("label_address")
        self.label_gender = QtWidgets.QLabel(Dialog)
        self.label_gender.setGeometry(QtCore.QRect(30, 270, 111, 31))
        self.label_gender.setObjectName("label_gender")
        self.label_job = QtWidgets.QLabel(Dialog)
        self.label_job.setGeometry(QtCore.QRect(30, 320, 111, 31))
        self.label_job.setObjectName("label_job")
        self.label_email = QtWidgets.QLabel(Dialog)
        self.label_email.setGeometry(QtCore.QRect(30, 370, 111, 31))
        self.label_email.setObjectName("label_email")
        self.label_username_new = QtWidgets.QLabel(Dialog)
        self.label_username_new.setGeometry(QtCore.QRect(30, 50, 111, 31))
        self.label_username_new.setObjectName("label_username_new")
        self.entry_firstname = QtWidgets.QLineEdit(Dialog)
        self.entry_firstname.setGeometry(QtCore.QRect(140, 120, 211, 31))
        self.entry_firstname.setText("")
        self.entry_firstname.setObjectName("entry_firstname")
        self.entry_lastname = QtWidgets.QLineEdit(Dialog)
        self.entry_lastname.setGeometry(QtCore.QRect(140, 170, 211, 31))
        self.entry_lastname.setObjectName("entry_lastname")
        self.entry_address = QtWidgets.QLineEdit(Dialog)
        self.entry_address.setGeometry(QtCore.QRect(140, 220, 211, 31))
        self.entry_address.setObjectName("entry_address")
        self.comboBox_gender = QtWidgets.QComboBox(Dialog)
        self.comboBox_gender.setGeometry(QtCore.QRect(140, 270, 211, 31))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_job = QtWidgets.QComboBox(Dialog)
        self.comboBox_job.setGeometry(QtCore.QRect(140, 320, 211, 31))
        self.comboBox_job.setObjectName("comboBox_job")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.entry_email = QtWidgets.QLineEdit(Dialog)
        self.entry_email.setGeometry(QtCore.QRect(140, 370, 211, 31))
        self.entry_email.setObjectName("entry_email")
        self.entry_username_new = QtWidgets.QLineEdit(Dialog)
        self.entry_username_new.setGeometry(QtCore.QRect(140, 50, 211, 31))
        self.entry_username_new.setObjectName("entry_username_new")
        self.label_enter = QtWidgets.QLabel(Dialog)
        self.label_enter.setGeometry(QtCore.QRect(160, 10, 141, 41))
        self.label_enter.setObjectName("label_enter")
        self.label_infos = QtWidgets.QLabel(Dialog)
        self.label_infos.setGeometry(QtCore.QRect(180, 90, 121, 21))
        self.label_infos.setObjectName("label_infos")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 430, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.update_user)

    def update_user(self) :
        fname = self.entry_firstname.text()
        lname = self.entry_lastname.text()
        address = self.entry_address.text()
        gender = self.comboBox_gender.currentText()
        job = self.comboBox_job.currentText()
        email = self.entry_email.text()
        username = self.entry_username_new.text()

        db = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) +"\database.db")
        cr = db.cursor()

        if username == "" :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Enter Username!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        elif not cr.execute(f"select username from users where username = '{username}'").fetchall() :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Username does not exists!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()

        elif fname == "" and lname == "" and address == "" and email == "" and gender == "Choose gender" and job == "Choose job":
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Empty field!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
            x = msg.exec_()
        
        elif email not in re.findall(r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+\.[a-zA-Z]{2,5}$", email)[0] :
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect informations")
            msg.setText("Enter a valid email!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" +"logo.jpg"))
            x = msg.exec_()
        
        else :
            try :
                    if lname != "" :
                        cr.execute(f"update users set lname='{lname}' where username='{username}'")

                    if fname != "" :
                        cr.execute(f"update users set fname='{fname}' where username='{username}'")

                    if address != "" :
                        cr.execute(f"update users set address='{address}' where username='{username}'")
                    
                    if email != "" : 
                        cr.execute(f"update users set email='{email}' where username='{username}'")
                    
                    if gender == "Male" :
                        gen = "M"
                        cr.execute(f"update users set gender='{gen}' where username='{username}'")
                    elif gender == "Female" :
                        gen = "F"
                        cr.execute(f"update users set gender='{gen}' where username='{username}'")
                    
                    if job != "Choose job" :
                        cr.execute(f"update users set job='{job}' where username='{username}'")
                    
                    db.commit()

                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("User informations succesfully updated!")
                    msg.setIcon(QMessageBox.Information)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                    x = msg.exec_()

                    self.entry_username_new.setText("")
                    self.entry_lastname.setText("")
                    self.entry_firstname.setText("")
                    self.entry_address.setText("")
                    self.entry_email.setText("")
                
            except :
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error occured!")
                msg.setIcon(QMessageBox.Critical)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + "/" + "logo.jpg"))
                x = msg.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_firstname.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name :</span></p></body></html>"))
        self.label_lastname.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name :</span></p></body></html>"))
        self.label_address.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.label_gender.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gender :</span></p></body></html>"))
        self.label_job.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Job :</span></p></body></html>"))
        self.label_email.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email :</span></p></body></html>"))
        self.label_username_new.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Username :</span></p></body></html>"))
        self.comboBox_gender.setItemText(0, _translate("Dialog", "Choose gender"))
        self.comboBox_gender.setItemText(1, _translate("Dialog", "Male"))
        self.comboBox_gender.setItemText(2, _translate("Dialog", "Female"))
        self.comboBox_job.setItemText(0, _translate("Dialog", "Choose job"))
        self.comboBox_job.setItemText(1, _translate("Dialog", "Student"))
        self.comboBox_job.setItemText(2, _translate("Dialog", "Employee"))
        self.comboBox_job.setItemText(3, _translate("Dialog", "Unemployed"))
        self.label_enter.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter username</span></p></body></html>"))
        self.label_infos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Update infos</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))

