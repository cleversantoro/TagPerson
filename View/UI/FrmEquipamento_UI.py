# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmEquipamento.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmEquipamento(object):
    def setupUi(self, FrmEquipamento):
        FrmEquipamento.setObjectName("FrmEquipamento")
        FrmEquipamento.setWindowModality(QtCore.Qt.WindowModal)
        FrmEquipamento.resize(780, 372)
        self.centralwidget = QtWidgets.QWidget(FrmEquipamento)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_imagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagem.setGeometry(QtCore.QRect(9, 10, 266, 331))
        self.lbl_imagem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_imagem.setText("")
        self.lbl_imagem.setScaledContents(False)
        self.lbl_imagem.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imagem.setWordWrap(False)
        self.lbl_imagem.setObjectName("lbl_imagem")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(279, 9, 491, 351))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(8, 31, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(8, 73, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(8, 116, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(8, 158, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(7, 202, 31, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(182, 202, 28, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(357, 202, 28, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lblTipo = QtWidgets.QLabel(self.groupBox)
        self.lblTipo.setGeometry(QtCore.QRect(136, 28, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblTipo.setFont(font)
        self.lblTipo.setObjectName("lblTipo")
        self.lblAlcance = QtWidgets.QLabel(self.groupBox)
        self.lblAlcance.setGeometry(QtCore.QRect(136, 70, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblAlcance.setFont(font)
        self.lblAlcance.setObjectName("lblAlcance")
        self.lblForcaMinima = QtWidgets.QLabel(self.groupBox)
        self.lblForcaMinima.setGeometry(QtCore.QRect(136, 113, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblForcaMinima.setFont(font)
        self.lblForcaMinima.setObjectName("lblForcaMinima")
        self.lblBonus = QtWidgets.QLabel(self.groupBox)
        self.lblBonus.setGeometry(QtCore.QRect(136, 155, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblBonus.setFont(font)
        self.lblBonus.setObjectName("lblBonus")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(123, 254, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(247, 254, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(5, 254, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(100, 311, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(200, 311, 30, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(8, 311, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(290, 311, 40, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(380, 311, 40, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(362, 254, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lbl_leve = QtWidgets.QLabel(self.groupBox)
        self.lbl_leve.setGeometry(QtCore.QRect(35, 203, 90, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_leve.setFont(font)
        self.lbl_leve.setObjectName("lbl_leve")
        self.lbl_media = QtWidgets.QLabel(self.groupBox)
        self.lbl_media.setGeometry(QtCore.QRect(215, 203, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_media.setFont(font)
        self.lbl_media.setObjectName("lbl_media")
        self.lbl_pesada = QtWidgets.QLabel(self.groupBox)
        self.lbl_pesada.setGeometry(QtCore.QRect(390, 203, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_pesada.setFont(font)
        self.lbl_pesada.setObjectName("lbl_pesada")
        self.lbl_25 = QtWidgets.QLabel(self.groupBox)
        self.lbl_25.setGeometry(QtCore.QRect(63, 254, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_25.setFont(font)
        self.lbl_25.setObjectName("lbl_25")
        self.lbl_50 = QtWidgets.QLabel(self.groupBox)
        self.lbl_50.setGeometry(QtCore.QRect(182, 254, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_50.setFont(font)
        self.lbl_50.setObjectName("lbl_50")
        self.lbl_75 = QtWidgets.QLabel(self.groupBox)
        self.lbl_75.setGeometry(QtCore.QRect(306, 254, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_75.setFont(font)
        self.lbl_75.setObjectName("lbl_75")
        self.lbl_100 = QtWidgets.QLabel(self.groupBox)
        self.lbl_100.setGeometry(QtCore.QRect(432, 254, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_100.setFont(font)
        self.lbl_100.setObjectName("lbl_100")
        self.lbl_pq = QtWidgets.QLabel(self.groupBox)
        self.lbl_pq.setGeometry(QtCore.QRect(47, 312, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_pq.setFont(font)
        self.lbl_pq.setObjectName("lbl_pq")
        self.lbl_an = QtWidgets.QLabel(self.groupBox)
        self.lbl_an.setGeometry(QtCore.QRect(141, 312, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_an.setFont(font)
        self.lbl_an.setObjectName("lbl_an")
        self.lbl_el = QtWidgets.QLabel(self.groupBox)
        self.lbl_el.setGeometry(QtCore.QRect(232, 312, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_el.setFont(font)
        self.lbl_el.setObjectName("lbl_el")
        self.lbl_me = QtWidgets.QLabel(self.groupBox)
        self.lbl_me.setGeometry(QtCore.QRect(330, 312, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_me.setFont(font)
        self.lbl_me.setObjectName("lbl_me")
        self.lbl_hu = QtWidgets.QLabel(self.groupBox)
        self.lbl_hu.setGeometry(QtCore.QRect(421, 310, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_hu.setFont(font)
        self.lbl_hu.setObjectName("lbl_hu")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(6, 345, 268, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        FrmEquipamento.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmEquipamento)
        QtCore.QMetaObject.connectSlotsByName(FrmEquipamento)

    def retranslateUi(self, FrmEquipamento):
        _translate = QtCore.QCoreApplication.translate
        FrmEquipamento.setWindowTitle(_translate("FrmEquipamento", "MainWindow"))
        self.groupBox.setTitle(_translate("FrmEquipamento", "Informação"))
        self.label_2.setText(_translate("FrmEquipamento", "Tipo:.................."))
        self.label_3.setText(_translate("FrmEquipamento", "Alcance:................"))
        self.label_4.setText(_translate("FrmEquipamento", "Forca Minima:......"))
        self.label_5.setText(_translate("FrmEquipamento", "Bônus:.................."))
        self.label_6.setText(_translate("FrmEquipamento", "L - "))
        self.label_7.setText(_translate("FrmEquipamento", "M - "))
        self.label_8.setText(_translate("FrmEquipamento", "P - "))
        self.lblTipo.setText(_translate("FrmEquipamento", "N/D"))
        self.lblAlcance.setText(_translate("FrmEquipamento", "N/D"))
        self.lblForcaMinima.setText(_translate("FrmEquipamento", "N/D"))
        self.lblBonus.setText(_translate("FrmEquipamento", "N/D"))
        self.label_13.setText(_translate("FrmEquipamento", "50% -"))
        self.label_14.setText(_translate("FrmEquipamento", "75% - "))
        self.label_15.setText(_translate("FrmEquipamento", "25% - "))
        self.label_16.setText(_translate("FrmEquipamento", "An - "))
        self.label_17.setText(_translate("FrmEquipamento", "El - "))
        self.label_18.setText(_translate("FrmEquipamento", "Pq - "))
        self.label_19.setText(_translate("FrmEquipamento", "Me - "))
        self.label_20.setText(_translate("FrmEquipamento", "Hu - "))
        self.label_21.setText(_translate("FrmEquipamento", "100% -"))
        self.lbl_leve.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_media.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_pesada.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_25.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_50.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_75.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_100.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_pq.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_an.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_el.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_me.setText(_translate("FrmEquipamento", "N/D"))
        self.lbl_hu.setText(_translate("FrmEquipamento", "N/D"))
        self.lblNome.setText(_translate("FrmEquipamento", "N/D"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmEquipamento = QtWidgets.QMainWindow()
    ui = Ui_FrmEquipamento()
    ui.setupUi(FrmEquipamento)
    FrmEquipamento.show()
    sys.exit(app.exec_())
