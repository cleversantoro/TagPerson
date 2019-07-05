from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from View.UI.FrmNovoPersonagem_UI import *

#from Main import TelaPrincipal as main

from Controller.ProfissaoCTR import ProfissaoCTR as profissao
from Controller.RacaCTR import RacaCTR as raca
from Controller.EquipamentoCTR import EquipamentoCTR as equipamento

from Model.Personagem import Persona

#from resources.icones import *
#from resources.personagem import *
#from resources.tela import *


class Ui_NovoPersonagem(QtWidgets.QMainWindow, Ui_FrmNovoPersonagem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.appEvents()

    def appEvents(self):
        self.btnCancel.clicked.connect(self.on_clicked_Cancelar)
        self.btnOk.clicked.connect(self.on_clicked_Criar)

        self.lblHumano.mouseDoubleClickEvent = self.on_clicked_Raca(1)
        self.lblPequenino.mouseDoubleClickEvent = self.on_clicked_Raca(1)
        self.lblAnao.mouseDoubleClickEvent = self.on_clicked_Raca(1)
        self.lblElfoFlorestal.mouseDoubleClickEvent = self.on_clicked_Raca(1)
        self.lblElfoDourado.mouseDoubleClickEvent = self.on_clicked_Raca(1)
        self.lblMeioElfo.mouseDoubleClickEvent = self.on_clicked_Raca(1)


    def on_clicked_Raca(self,id):
        self.lblRaca.setText('Humano')
        
    def on_clicked_Criar(self):
        persona = Persona('persona-teste',-1)
        persona.race = raca.get_race(1)
        persona.profession = profissao.get_profession(1)

        #resistencia_fisica = persona.get_physical_resistance()
        #resistencia_magia = persona.get_magical_resistance()
        #velocidade = persona.get_speed()
        #karma = persona.get_karma()
        #defesa = persona.calc_defense()
        #energia_fisica = persona.get_max_ef()
        #energia_heroica = utils.calc_eh(persona)
        #absorcao = persona.calc_absorption()

        i = 0
        y = 0
        for x in persona.profession.posessions:
            equip = equipamento.get_equipment_item(x) 

            if( equip.itemtype == 'armour'):
                persona.combat_equip[0] = equip
            elif(equip.itemtype == 'helmet'):
                persona.combat_equip[1] = equip
            elif(equip.itemtype == 'shield'):
                persona.combat_equip[2] = equip
            elif(equip.itemtype == 'weapon'):
                persona.combat_weapon[y] = equip
                y += 1
            elif(equip.itemtype == 'item'):
                persona.equipment[i] = equip
                i += 1
        #personagem.save_persona(person)
        #main.popularGridPersonagens()
        pass

    def on_clicked_Cancelar(self):
        self.close()    
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = Ui_NovoPersonagem()
    tela.show()
    app.exec()
