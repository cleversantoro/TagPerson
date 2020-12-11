from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from View.UI.FrmNovoPersonagem_UI import *

from Controller.ProfissaoCTR import ProfissaoCTR as profissao
from Controller.RacaCTR import RacaCTR as raca
from Controller.EquipamentoCTR import EquipamentoCTR as equipamento

from Model.Personagem import Persona

class Ui_NovoPersonagem(QtWidgets.QMainWindow, Ui_FrmNovoPersonagem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = Ui_NovoPersonagem()
    tela.show()
    app.exec_()
