# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmNovoPersonagem.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmNovoPersonagem(object):
    def setupUi(self, FrmNovoPersonagem):
        FrmNovoPersonagem.setObjectName("FrmNovoPersonagem")
        FrmNovoPersonagem.resize(931, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmNovoPersonagem.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(FrmNovoPersonagem)
        self.frame.setGeometry(QtCore.QRect(4, 5, 191, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(7, 1, 181, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Principal/tagmar_capa_berbert.png"))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(FrmNovoPersonagem)
        self.frame_2.setGeometry(QtCore.QRect(198, 24, 721, 181))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(32, 152, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(142, 152, 75, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(279, 152, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(377, 152, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(493, 152, 95, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(634, 150, 65, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lblHumano = QtWidgets.QLabel(self.frame_2)
        self.lblHumano.setGeometry(QtCore.QRect(20, 19, 80, 114))
        self.lblHumano.setText("")
        self.lblHumano.setPixmap(QtGui.QPixmap(":/Raca/raca/humano.png"))
        self.lblHumano.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHumano.setProperty("id", 1)
        self.lblHumano.setObjectName("lblHumano")
        self.lblPequenino = QtWidgets.QLabel(self.frame_2)
        self.lblPequenino.setGeometry(QtCore.QRect(139, 19, 80, 114))
        self.lblPequenino.setText("")
        self.lblPequenino.setPixmap(QtGui.QPixmap(":/Raca/raca/pequenino.png"))
        self.lblPequenino.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPequenino.setObjectName("lblPequenino")
        self.lblAnao = QtWidgets.QLabel(self.frame_2)
        self.lblAnao.setGeometry(QtCore.QRect(258, 19, 80, 114))
        self.lblAnao.setText("")
        self.lblAnao.setPixmap(QtGui.QPixmap(":/Raca/raca/anao.png"))
        self.lblAnao.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAnao.setObjectName("lblAnao")
        self.lblElfoDourado = QtWidgets.QLabel(self.frame_2)
        self.lblElfoDourado.setGeometry(QtCore.QRect(497, 19, 80, 114))
        self.lblElfoDourado.setText("")
        self.lblElfoDourado.setPixmap(QtGui.QPixmap(":/Raca/raca/elfodourado.png"))
        self.lblElfoDourado.setAlignment(QtCore.Qt.AlignCenter)
        self.lblElfoDourado.setObjectName("lblElfoDourado")
        self.lblElfoFlorestal = QtWidgets.QLabel(self.frame_2)
        self.lblElfoFlorestal.setGeometry(QtCore.QRect(377, 19, 80, 114))
        self.lblElfoFlorestal.setText("")
        self.lblElfoFlorestal.setPixmap(QtGui.QPixmap(":/Raca/raca/elfoflorestal.png"))
        self.lblElfoFlorestal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblElfoFlorestal.setObjectName("lblElfoFlorestal")
        self.lblMeioElfo = QtWidgets.QLabel(self.frame_2)
        self.lblMeioElfo.setGeometry(QtCore.QRect(616, 19, 80, 114))
        self.lblMeioElfo.setText("")
        self.lblMeioElfo.setPixmap(QtGui.QPixmap(":/Raca/raca/meioelfo.png"))
        self.lblMeioElfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMeioElfo.setObjectName("lblMeioElfo")
        self.frame_3 = QtWidgets.QFrame(FrmNovoPersonagem)
        self.frame_3.setGeometry(QtCore.QRect(198, 237, 721, 171))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(19, 141, 69, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(151, 141, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(252, 141, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(389, 141, 43, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(489, 141, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(622, 141, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lblGuerreiro = QtWidgets.QLabel(self.frame_3)
        self.lblGuerreiro.setGeometry(QtCore.QRect(13, 13, 80, 114))
        self.lblGuerreiro.setText("")
        self.lblGuerreiro.setPixmap(QtGui.QPixmap(":/Profissao/profissao/guerreiro.png"))
        self.lblGuerreiro.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGuerreiro.setObjectName("lblGuerreiro")
        self.lblLadino = QtWidgets.QLabel(self.frame_3)
        self.lblLadino.setGeometry(QtCore.QRect(131, 13, 80, 114))
        self.lblLadino.setText("")
        self.lblLadino.setPixmap(QtGui.QPixmap(":/Profissao/profissao/ladino.png"))
        self.lblLadino.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLadino.setObjectName("lblLadino")
        self.lblSacerdote = QtWidgets.QLabel(self.frame_3)
        self.lblSacerdote.setGeometry(QtCore.QRect(248, 13, 80, 114))
        self.lblSacerdote.setText("")
        self.lblSacerdote.setPixmap(QtGui.QPixmap(":/Profissao/profissao/sacerdote.png"))
        self.lblSacerdote.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSacerdote.setObjectName("lblSacerdote")
        self.lblRastreador = QtWidgets.QLabel(self.frame_3)
        self.lblRastreador.setGeometry(QtCore.QRect(483, 13, 80, 114))
        self.lblRastreador.setText("")
        self.lblRastreador.setPixmap(QtGui.QPixmap(":/Profissao/profissao/rastreador.png"))
        self.lblRastreador.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRastreador.setObjectName("lblRastreador")
        self.lblMago = QtWidgets.QLabel(self.frame_3)
        self.lblMago.setGeometry(QtCore.QRect(366, 13, 80, 114))
        self.lblMago.setText("")
        self.lblMago.setPixmap(QtGui.QPixmap(":/Profissao/profissao/mago.png"))
        self.lblMago.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMago.setObjectName("lblMago")
        self.lblBardo = QtWidgets.QLabel(self.frame_3)
        self.lblBardo.setGeometry(QtCore.QRect(601, 13, 80, 114))
        self.lblBardo.setText("")
        self.lblBardo.setPixmap(QtGui.QPixmap(":/Profissao/profissao/bardo.png"))
        self.lblBardo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBardo.setObjectName("lblBardo")
        self.label_2 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_2.setGeometry(QtCore.QRect(202, 414, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_3.setGeometry(QtCore.QRect(202, 437, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnCancel = QtWidgets.QPushButton(FrmNovoPersonagem)
        self.btnCancel.setGeometry(QtCore.QRect(710, 420, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.btnOk = QtWidgets.QPushButton(FrmNovoPersonagem)
        self.btnOk.setGeometry(QtCore.QRect(820, 420, 93, 28))
        self.btnOk.setObjectName("btnOk")
        self.lblRaca = QtWidgets.QLabel(FrmNovoPersonagem)
        self.lblRaca.setGeometry(QtCore.QRect(259, 414, 121, 20))
        self.lblRaca.setObjectName("lblRaca")
        self.lblProfissao = QtWidgets.QLabel(FrmNovoPersonagem)
        self.lblProfissao.setGeometry(QtCore.QRect(285, 439, 101, 16))
        self.lblProfissao.setObjectName("lblProfissao")
        self.label_6 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_6.setGeometry(QtCore.QRect(200, 219, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_7.setGeometry(QtCore.QRect(200, 6, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_4.setGeometry(QtCore.QRect(407, 413, 40, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FrmNovoPersonagem)
        self.label_5.setGeometry(QtCore.QRect(391, 437, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtNome = QtWidgets.QLineEdit(FrmNovoPersonagem)
        self.txtNome.setGeometry(QtCore.QRect(456, 411, 221, 22))
        self.txtNome.setObjectName("txtNome")
        self.txtJogador = QtWidgets.QLineEdit(FrmNovoPersonagem)
        self.txtJogador.setGeometry(QtCore.QRect(456, 435, 221, 22))
        self.txtJogador.setObjectName("txtJogador")

        self.retranslateUi(FrmNovoPersonagem)
        QtCore.QMetaObject.connectSlotsByName(FrmNovoPersonagem)

    def retranslateUi(self, FrmNovoPersonagem):
        _translate = QtCore.QCoreApplication.translate
        FrmNovoPersonagem.setWindowTitle(_translate("FrmNovoPersonagem", "Criar Personagem"))
        self.label_14.setText(_translate("FrmNovoPersonagem", "Humano"))
        self.label_15.setText(_translate("FrmNovoPersonagem", "Pequenino"))
        self.label_16.setText(_translate("FrmNovoPersonagem", "Anão"))
        self.label_17.setText(_translate("FrmNovoPersonagem", "Elfo Florestal"))
        self.label_18.setText(_translate("FrmNovoPersonagem", "Elfo Dourado"))
        self.label_19.setText(_translate("FrmNovoPersonagem", "Meio Elfo"))
        self.label_20.setText(_translate("FrmNovoPersonagem", "Guerreiro"))
        self.label_21.setText(_translate("FrmNovoPersonagem", "Ladino"))
        self.label_22.setText(_translate("FrmNovoPersonagem", "Sacerdote"))
        self.label_23.setText(_translate("FrmNovoPersonagem", "Mago"))
        self.label_24.setText(_translate("FrmNovoPersonagem", "Rastreador"))
        self.label_25.setText(_translate("FrmNovoPersonagem", "Bardo"))
        self.label_2.setText(_translate("FrmNovoPersonagem", "Raça:"))
        self.label_3.setText(_translate("FrmNovoPersonagem", "Profissão:"))
        self.btnCancel.setText(_translate("FrmNovoPersonagem", "Cancelar"))
        self.btnOk.setText(_translate("FrmNovoPersonagem", "Criar"))
        self.lblRaca.setText(_translate("FrmNovoPersonagem", "..."))
        self.lblProfissao.setText(_translate("FrmNovoPersonagem", "..."))
        self.label_6.setText(_translate("FrmNovoPersonagem", "Profissão:"))
        self.label_7.setText(_translate("FrmNovoPersonagem", "Raça:"))
        self.label_4.setText(_translate("FrmNovoPersonagem", "Nome:"))
        self.label_5.setText(_translate("FrmNovoPersonagem", "Jogador:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmNovoPersonagem = QtWidgets.QDialog()
    ui = Ui_FrmNovoPersonagem()
    ui.setupUi(FrmNovoPersonagem)
    FrmNovoPersonagem.show()
    sys.exit(app.exec_())
