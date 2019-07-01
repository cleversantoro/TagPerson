from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from View.UI.FrmEquipamento_UI import *

class Ui_Equipamento(QtWidgets.QMainWindow, Ui_FrmEquipamento):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def preencherEquipamento(self):
        self.lblAlcance.setText('alcance')
        self.lblBonus.setText('bonus')
        self.lblTipo.setText('tipo')
        self.lblForcaMinima.setText('Forca_minima')
        
        self.lbl_leve.setText('leve')
        self.lbl_media.setText('media')
        self.lbl_pesada.setText('pesada')
        
        self.lbl_25.setText('25')
        self.lbl_50.setText('50')
        self.lbl_75.setText('75')
        self.lbl_100.setText('100')

        self.lbl_an.setText('an')
        self.lbl_el.setText('el')
        self.lbl_hu.setText('hu')
        self.lbl_me.setText('m')
        self.lbl_pq.setText('pq')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = Ui_Equipamento()
    tela.show()
    app.exec()
