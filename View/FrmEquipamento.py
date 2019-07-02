from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from View.UI.FrmEquipamento_UI import *
from Controller.EquipamentoCTR import EquipamentoCTR as equipamento

class Ui_Equipamento(QtWidgets.QMainWindow, Ui_FrmEquipamento):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def preencherEquipamento(self,id):
        equip = equipamento.get_equipment_item(id)
        
        if(equip.itemtype == 'weapon'):
            #self.lbl_imagem.setPixmap(QtGui.QPixmap('C:\csharp\TagPerson\Imagens\Item\item_arco_composto.png')
            self.lbl_imagem.setPixmap(QtGui.QPixmap(str(equip.image)))
            self.lblNome.setText(str(equip.name))
            self.lblAlcance.setText(str(equip.range))
            self.lblBonus.setText(str(equip.bonus))
            self.lblTipo.setText(str(equip.type))
            self.lblForcaMinima.setText(str(equip.min_strength))
        
            self.lbl_leve.setText(str(equip.attack_defense['l']))
            self.lbl_media.setText(str(equip.attack_defense['m']))
            self.lbl_pesada.setText(str(equip.attack_defense['p']))
        
            self.lbl_25.setText(str(equip._25))
            self.lbl_50.setText(str(equip._50))
            self.lbl_75.setText(str(equip._75))
            self.lbl_100.setText(str(equip._100))

            self.lbl_an.setText(str(equip.An))
            self.lbl_el.setText(str(equip.El))
            self.lbl_hu.setText(str(equip.Hu))
            self.lbl_me.setText(str(equip.Me))
            self.lbl_pq.setText(str(equip.Pq))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = Ui_Equipamento()
    tela.show()
    app.exec()
