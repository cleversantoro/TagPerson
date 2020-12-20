# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmNovoPersonagem.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.lblhumano = QtWidgets.QLabel(self.frame_2)
        self.lblhumano.setGeometry(QtCore.QRect(32, 152, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblhumano.setFont(font)
        self.lblhumano.setObjectName("lblhumano")
        self.lblpequenino = QtWidgets.QLabel(self.frame_2)
        self.lblpequenino.setGeometry(QtCore.QRect(150, 152, 75, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblpequenino.setFont(font)
        self.lblpequenino.setObjectName("lblpequenino")
        self.lblanao = QtWidgets.QLabel(self.frame_2)
        self.lblanao.setGeometry(QtCore.QRect(279, 152, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblanao.setFont(font)
        self.lblanao.setObjectName("lblanao")
        self.lblelfofloresta = QtWidgets.QLabel(self.frame_2)
        self.lblelfofloresta.setGeometry(QtCore.QRect(390, 152, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblelfofloresta.setFont(font)
        self.lblelfofloresta.setObjectName("lblelfofloresta")
        self.lblelfodourado = QtWidgets.QLabel(self.frame_2)
        self.lblelfodourado.setGeometry(QtCore.QRect(500, 152, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblelfodourado.setFont(font)
        self.lblelfodourado.setObjectName("lblelfodourado")
        self.lblmeioelfo = QtWidgets.QLabel(self.frame_2)
        self.lblmeioelfo.setGeometry(QtCore.QRect(640, 150, 65, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblmeioelfo.setFont(font)
        self.lblmeioelfo.setObjectName("lblmeioelfo")
        self.btnHumano = QtWidgets.QPushButton(self.frame_2)
        self.btnHumano.setGeometry(QtCore.QRect(12, 27, 101, 121))
        font = QtGui.QFont()
        font.setKerning(True)
        self.btnHumano.setFont(font)
        self.btnHumano.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHumano.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnHumano.setAutoFillBackground(False)
        self.btnHumano.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Raca/raca/humano.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHumano.setIcon(icon1)
        self.btnHumano.setIconSize(QtCore.QSize(83, 117))
        self.btnHumano.setCheckable(False)
        self.btnHumano.setAutoDefault(True)
        self.btnHumano.setFlat(True)
        self.btnHumano.setObjectName("btnHumano")
        self.btnPequenino = QtWidgets.QPushButton(self.frame_2)
        self.btnPequenino.setGeometry(QtCore.QRect(130, 21, 101, 121))
        self.btnPequenino.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPequenino.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPequenino.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Raca/raca/pequenino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPequenino.setIcon(icon2)
        self.btnPequenino.setIconSize(QtCore.QSize(112, 139))
        self.btnPequenino.setFlat(True)
        self.btnPequenino.setObjectName("btnPequenino")
        self.btnAnao = QtWidgets.QPushButton(self.frame_2)
        self.btnAnao.setGeometry(QtCore.QRect(250, 21, 101, 121))
        self.btnAnao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAnao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAnao.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Raca/raca/anao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnao.setIcon(icon3)
        self.btnAnao.setIconSize(QtCore.QSize(90, 125))
        self.btnAnao.setFlat(True)
        self.btnAnao.setObjectName("btnAnao")
        self.btnElfoFlorestal = QtWidgets.QPushButton(self.frame_2)
        self.btnElfoFlorestal.setGeometry(QtCore.QRect(370, 21, 101, 121))
        self.btnElfoFlorestal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnElfoFlorestal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnElfoFlorestal.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Raca/raca/elfoflorestal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnElfoFlorestal.setIcon(icon4)
        self.btnElfoFlorestal.setIconSize(QtCore.QSize(100, 132))
        self.btnElfoFlorestal.setFlat(True)
        self.btnElfoFlorestal.setObjectName("btnElfoFlorestal")
        self.btnElfoDourado = QtWidgets.QPushButton(self.frame_2)
        self.btnElfoDourado.setGeometry(QtCore.QRect(490, 21, 101, 121))
        self.btnElfoDourado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnElfoDourado.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnElfoDourado.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Raca/raca/elfodourado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnElfoDourado.setIcon(icon5)
        self.btnElfoDourado.setIconSize(QtCore.QSize(90, 125))
        self.btnElfoDourado.setFlat(True)
        self.btnElfoDourado.setObjectName("btnElfoDourado")
        self.btnMeioElfo = QtWidgets.QPushButton(self.frame_2)
        self.btnMeioElfo.setGeometry(QtCore.QRect(610, 21, 101, 121))
        self.btnMeioElfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMeioElfo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMeioElfo.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Raca/raca/meioelfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMeioElfo.setIcon(icon6)
        self.btnMeioElfo.setIconSize(QtCore.QSize(90, 125))
        self.btnMeioElfo.setFlat(True)
        self.btnMeioElfo.setObjectName("btnMeioElfo")
        self.frame_3 = QtWidgets.QFrame(FrmNovoPersonagem)
        self.frame_3.setGeometry(QtCore.QRect(198, 237, 721, 171))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lblguerreiro = QtWidgets.QLabel(self.frame_3)
        self.lblguerreiro.setGeometry(QtCore.QRect(28, 140, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblguerreiro.setFont(font)
        self.lblguerreiro.setObjectName("lblguerreiro")
        self.lblladino = QtWidgets.QLabel(self.frame_3)
        self.lblladino.setGeometry(QtCore.QRect(151, 141, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblladino.setFont(font)
        self.lblladino.setObjectName("lblladino")
        self.lblsacerdote = QtWidgets.QLabel(self.frame_3)
        self.lblsacerdote.setGeometry(QtCore.QRect(261, 141, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblsacerdote.setFont(font)
        self.lblsacerdote.setObjectName("lblsacerdote")
        self.lblmago = QtWidgets.QLabel(self.frame_3)
        self.lblmago.setGeometry(QtCore.QRect(396, 141, 43, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblmago.setFont(font)
        self.lblmago.setObjectName("lblmago")
        self.lblrastreador = QtWidgets.QLabel(self.frame_3)
        self.lblrastreador.setGeometry(QtCore.QRect(505, 141, 70, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblrastreador.setFont(font)
        self.lblrastreador.setObjectName("lblrastreador")
        self.lblbardo = QtWidgets.QLabel(self.frame_3)
        self.lblbardo.setGeometry(QtCore.QRect(638, 141, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblbardo.setFont(font)
        self.lblbardo.setObjectName("lblbardo")
        self.btnGuerreiro = QtWidgets.QPushButton(self.frame_3)
        self.btnGuerreiro.setGeometry(QtCore.QRect(13, 13, 80, 114))
        self.btnGuerreiro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuerreiro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnGuerreiro.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Profissao/profissao/guerreiro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuerreiro.setIcon(icon7)
        self.btnGuerreiro.setIconSize(QtCore.QSize(90, 106))
        self.btnGuerreiro.setFlat(True)
        self.btnGuerreiro.setObjectName("btnGuerreiro")
        self.btnLadino = QtWidgets.QPushButton(self.frame_3)
        self.btnLadino.setGeometry(QtCore.QRect(130, 13, 80, 114))
        self.btnLadino.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLadino.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnLadino.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Profissao/profissao/ladino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLadino.setIcon(icon8)
        self.btnLadino.setIconSize(QtCore.QSize(114, 108))
        self.btnLadino.setFlat(True)
        self.btnLadino.setObjectName("btnLadino")
        self.lblSacerdote = QtWidgets.QPushButton(self.frame_3)
        self.lblSacerdote.setGeometry(QtCore.QRect(253, 13, 80, 114))
        self.lblSacerdote.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblSacerdote.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lblSacerdote.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Profissao/profissao/sacerdote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lblSacerdote.setIcon(icon9)
        self.lblSacerdote.setIconSize(QtCore.QSize(144, 104))
        self.lblSacerdote.setFlat(True)
        self.lblSacerdote.setObjectName("lblSacerdote")
        self.btnMago = QtWidgets.QPushButton(self.frame_3)
        self.btnMago.setGeometry(QtCore.QRect(374, 13, 80, 114))
        self.btnMago.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMago.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMago.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Profissao/profissao/mago.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMago.setIcon(icon10)
        self.btnMago.setIconSize(QtCore.QSize(152, 109))
        self.btnMago.setFlat(True)
        self.btnMago.setObjectName("btnMago")
        self.btnRastreador = QtWidgets.QPushButton(self.frame_3)
        self.btnRastreador.setGeometry(QtCore.QRect(489, 13, 80, 114))
        self.btnRastreador.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRastreador.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRastreador.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Profissao/profissao/rastreador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRastreador.setIcon(icon11)
        self.btnRastreador.setIconSize(QtCore.QSize(144, 107))
        self.btnRastreador.setFlat(True)
        self.btnRastreador.setObjectName("btnRastreador")
        self.btnBardo = QtWidgets.QPushButton(self.frame_3)
        self.btnBardo.setGeometry(QtCore.QRect(614, 13, 80, 114))
        self.btnBardo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBardo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnBardo.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Profissao/profissao/bardo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBardo.setIcon(icon12)
        self.btnBardo.setIconSize(QtCore.QSize(144, 102))
        self.btnBardo.setFlat(True)
        self.btnBardo.setObjectName("btnBardo")
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
        self.btnCancelar = QtWidgets.QPushButton(FrmNovoPersonagem)
        self.btnCancelar.setGeometry(QtCore.QRect(710, 420, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnCriar = QtWidgets.QPushButton(FrmNovoPersonagem)
        self.btnCriar.setGeometry(QtCore.QRect(820, 420, 93, 28))
        self.btnCriar.setObjectName("btnCriar")
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
        self.lblhumano.setText(_translate("FrmNovoPersonagem", "Humano"))
        self.lblpequenino.setText(_translate("FrmNovoPersonagem", "Pequenino"))
        self.lblanao.setText(_translate("FrmNovoPersonagem", "Anão"))
        self.lblelfofloresta.setText(_translate("FrmNovoPersonagem", "Elfo Florestal"))
        self.lblelfodourado.setText(_translate("FrmNovoPersonagem", "Elfo Dourado"))
        self.lblmeioelfo.setText(_translate("FrmNovoPersonagem", "Meio Elfo"))
        self.lblguerreiro.setText(_translate("FrmNovoPersonagem", "Guerreiro"))
        self.lblladino.setText(_translate("FrmNovoPersonagem", "Ladino"))
        self.lblsacerdote.setText(_translate("FrmNovoPersonagem", "Sacerdote"))
        self.lblmago.setText(_translate("FrmNovoPersonagem", "Mago"))
        self.lblrastreador.setText(_translate("FrmNovoPersonagem", "Rastreador"))
        self.lblbardo.setText(_translate("FrmNovoPersonagem", "Bardo"))
        self.label_2.setText(_translate("FrmNovoPersonagem", "Raça:"))
        self.label_3.setText(_translate("FrmNovoPersonagem", "Profissão:"))
        self.btnCancelar.setText(_translate("FrmNovoPersonagem", "Cancelar"))
        self.btnCriar.setText(_translate("FrmNovoPersonagem", "Criar"))
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
