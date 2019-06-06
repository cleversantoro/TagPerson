# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmSobre.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmSobre(object):
    def setupUi(self, FrmSobre):
        FrmSobre.setObjectName("FrmSobre")
        FrmSobre.resize(390, 225)
        self.label = QtWidgets.QLabel(FrmSobre)
        self.label.setGeometry(QtCore.QRect(10, 62, 381, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FrmSobre)
        self.label_2.setGeometry(QtCore.QRect(10, 3, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FrmSobre)
        self.label_3.setGeometry(QtCore.QRect(4, 35, 391, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(FrmSobre)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 170, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_4 = QtWidgets.QLabel(FrmSobre)
        self.label_4.setGeometry(QtCore.QRect(39, 103, 141, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Principal/python.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FrmSobre)
        self.label_5.setGeometry(QtCore.QRect(219, 99, 121, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Principal/sqlite-database.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(FrmSobre)
        QtCore.QMetaObject.connectSlotsByName(FrmSobre)

    def retranslateUi(self, FrmSobre):
        _translate = QtCore.QCoreApplication.translate
        FrmSobre.setWindowTitle(_translate("FrmSobre", "Sobre"))
        self.label.setText(_translate("FrmSobre", "PyQT - Qt Designer 5.11.1 - Python 3.7"))
        self.label_2.setText(_translate("FrmSobre", "Gerador de Personagens - TagPerson"))
        self.label_3.setText(_translate("FrmSobre", "Copyright (c) - Clever Santoro Lopes"))
        self.commandLinkButton.setText(_translate("FrmSobre", "https://github.com/cleversantoro/TagPerson"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmSobre = QtWidgets.QDialog()
    ui = Ui_FrmSobre()
    ui.setupUi(FrmSobre)
    FrmSobre.show()
    sys.exit(app.exec_())
