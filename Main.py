from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from View.FrmPrincipal_UI import *

from Controller.PersonagemCTR import PersonagemCTR as personagem
from Controller.DivindadeCTR import DivindadeCTR as divindade
from Controller.EspecialidadeCTR import EspecialidadeCTR as especialidade
from Controller.EquipamentoCTR import EquipamentoCTR as equipamento

from Helpers.constantes import const

from resources.tela import *
from resources.icones import *
from resources.categoria import *
from resources.personagem import *


from View.FrmSobre import Ui_Sobre
from View.FrmNovoPersonagem import Ui_NovoPersonagem

import os

class TelaPrincipal(QtWidgets.QMainWindow, Ui_FrmPrincipal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1525, 922)
        self.center()

        self.AppEvents()
        self.PopularTela()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def AppEvents(self):
        self.tblPersonagens.doubleClicked.connect(self.getPersonagem)
        self.actionSobre.triggered.connect(self.ShowFrmSobre)
        self.actionNovo.triggered.connect(self.ShowFrmNovoPersonagem)
        self.HabilidadesProfessionalEvents()
        
    def HabilidadesProfessionalEvents(self):
        #self.spnAgricultura.valueChanged.connect(self.spnAgricultura_changed)
        #self.txtCarpintaria.textChanged.connect(self.txtCarpintaria_changed)
        pass

    def PopularTela(self):
        self.popularGridPersonagens()
        self.ComboDivindade()
        self.ComboClasseSocial()
        self.ComboEspecializacao()
        self.ComboArmadura()
        self.ComboEscudo()
        self.ComboCapacete()
        self.ComboArmas01()

    def popularCombateTecnicasBasicas(self,persona):
        person = persona
        rows = personagem.get_combat_persona(person.id,1)        

        self.tblCombate.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCombate.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblCombate.verticalHeader().hide()

        header = self.tblCombate.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblCombate.rowCount() > 0):
                self.tblCombate.removeRow(0)

        row = 0
        for item in rows:
            self.tblCombate.insertRow(row)
            #id = QTableWidgetItem(str(item[0]))
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[2])
            #self.nivel.valueChanged.connect()

            #nivel = QTableWidgetItem(niv,None)
            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            #self.tblCombate.setItem(row, 0, id)
            self.tblCombate.setItem(row, 0, descricao)
            self.tblCombate.setCellWidget(row, 1, self.nivel)
            self.tblCombate.setItem(row, 2, custo)
            self.tblCombate.setItem(row, 3, ajuste)
            self.tblCombate.setItem(row, 4, total)
            self.tblCombate.setItem(row, 5, categoria)
            self.tblCombate.setItem(row, 6, icone)
            row = row + 1

    def popularCombateTecnicasEspecializacao(self,persona):
        person = persona
        rows = personagem.get_combat_persona(person.id,1)        

        self.tblEspecializacao.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblEspecializacao.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblEspecializacao.verticalHeader().hide()

        header = self.tblEspecializacao.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

        #while (self.tblEspecializacao.rowCount() > 0):
        #        self.tblEspecializacao.removeRow(0)

        row = 0
        for item in rows:
            self.tblEspecializacao.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[2])
            #self.nivel.valueChanged.connect()

            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            self.tblEspecializacao.setItem(row, 0, descricao)
            self.tblEspecializacao.setCellWidget(row, 1, self.nivel)
            self.tblEspecializacao.setItem(row, 2, custo)
            self.tblEspecializacao.setItem(row, 3, ajuste)
            self.tblEspecializacao.setItem(row, 4, total)
            self.tblEspecializacao.setItem(row, 5, categoria)
            self.tblEspecializacao.setItem(row, 6, icone)
            row = row + 1

    def popularCombateTecnicasRestritas(self,persona):
        person = persona

        if persona.profession.id == 1:
            rows = personagem.get_combat_persona(person.id,4)        
        elif persona.profession.id == 2:
            rows = personagem.get_combat_persona(person.id,5)        

        self.tblProfissao.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblProfissao.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblProfissao.verticalHeader().hide()

        header = self.tblProfissao.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

        #while (self.tblProfissao.rowCount() > 0):
        #        self.tblProfissao.removeRow(0)

        row = 0
        for item in rows:
            self.tblProfissao.insertRow(row)
            #id = QTableWidgetItem(str(item[0]))
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[2])
            #self.nivel.valueChanged.connect()

            #nivel = QTableWidgetItem(niv,None)
            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            #self.tblCombate.setItem(row, 0, id)
            self.tblProfissao.setItem(row, 0, descricao)
            self.tblProfissao.setCellWidget(row, 1, self.nivel)
            self.tblProfissao.setItem(row, 2, custo)
            self.tblProfissao.setItem(row, 3, ajuste)
            self.tblProfissao.setItem(row, 4, total)
            self.tblProfissao.setItem(row, 5, categoria)
            self.tblProfissao.setItem(row, 6, icone)
            row = row + 1

    def popularMagiaBasica(self,persona):
        person = persona
        rows = personagem.get_spell_persona(person.id,4)        

        self.tblMagiaBasica.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMagiaBasica.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMagiaBasica.verticalHeader().hide()

        header = self.tblMagiaBasica.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        #while (self.tblMagiaBasica.rowCount() > 0):
        #        self.tblMagiaBasica.removeRow(0)

        row = 0
        for item in rows:
            self.tblMagiaBasica.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[2])
            #self.nivel.valueChanged.connect()

            custo = QTableWidgetItem(str(item[3]))
            total = QTableWidgetItem(str(item[4]))
            
            icon = QtGui.QIcon(QtGui.QPixmap(":/menu/iconfinder_question_12319.png"))
            
            self.icone = QTableWidgetItem(icon,None) #setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            #self.icone.itemClicked.connect(self.on_tableWidget_itemClicked)


            self.tblMagiaBasica.setItem(row, 0, descricao)
            self.tblMagiaBasica.setCellWidget(row, 1, self.nivel)
            self.tblMagiaBasica.setItem(row, 2, custo)
            self.tblMagiaBasica.setItem(row, 3, total)
            self.tblMagiaBasica.setItem(row, 4, self.icone)
            row = row + 1

    def popularHabiidadeProfissional(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,1)        

        self.tblProfissional.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblProfissional.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblProfissional.verticalHeader().hide()

        header = self.tblProfissional.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblProfissional.rowCount() > 0):
                self.tblProfissional.removeRow(0)

        row = 0
        for item in rows:
            self.tblProfissional.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[3])
            #self.nivel.valueChanged.connect()

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblProfissional.setItem(row, 0, descricao)
            self.tblProfissional.setItem(row, 1, restrito)
            self.tblProfissional.setCellWidget(row, 2, self.nivel)
            self.tblProfissional.setItem(row, 3, custo)
            self.tblProfissional.setItem(row, 4, ajuste)
            self.tblProfissional.setItem(row, 5, total)
            row = row + 1
        
            width = self.tblCombate.verticalHeader().width()

        #width += self.tblProfissional.horizontalHeader().length()
        #if self.tblProfissional.verticalScrollBar().isVisible():
        #    width += self.tblProfissional.verticalScrollBar().width()
        #width += self.tblProfissional.frameWidth() * 2
        #self.tblProfissional.setFixedWidth(width)

    def on_tableWidget_itemClicked(self):
        pass

    def popularGridPersonagens(self):
        rows = personagem.get_persona_list()
        self.tblPersonagens.setColumnHidden(0,True)
        #self.tblPersonagens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblPersonagens.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblPersonagens.verticalHeader().hide()

        header = self.tblPersonagens.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        
        while (self.tblPersonagens.rowCount() > 0):
                self.tblPersonagens.removeRow(0)
        
        row = 0
        for item in rows:
            self.tblPersonagens.insertRow(row)
            id = QTableWidgetItem(str(item[0]))
            
            if item[3]== 1:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/warrior.png"))
            elif item[3]== 2:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/thief.png"))
            elif item[3]== 3:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/priest.png"))
            elif item[3]== 4:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/mage.png"))
            elif item[3]== 5:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/ranger.png"))
            elif item[3]== 6:
                icon = QtGui.QIcon(QtGui.QPixmap(":/grid/bard.png"))
            else:
                icon = None
            
            prof = QTableWidgetItem(icon,None)
            
            nome = QTableWidgetItem(str(item[1]))
            nivel = QTableWidgetItem(str(item[4]))

            self.tblPersonagens.setItem(row, 0, id)
            self.tblPersonagens.setItem(row, 1, prof)
            self.tblPersonagens.setItem(row, 2, nome)
            self.tblPersonagens.setItem(row, 3, nivel)
            row = row + 1
        
        self.setTableWidthPersonagems

    def ComboDivindade(self):
        #divindade = DivindadeCTR
        itens = divindade.get_gods_list()
        self.cbxDivindade.clear()
        self.cbxDivindade.insertItem(-1,'Selecione uma Divindade')
        for item in itens:
            self.cbxDivindade.insertItem(item[0],str(item[1]))
            #'{}-({})'.format(item[1],item[2]))

    def ComboClasseSocial(self):
        const.SOCIAL_CLASS.sort()
        socialclass = const.SOCIAL_CLASS
        self.cbxClasseSocial.clear()
        self.cbxClasseSocial.addItem('Selecione uma Classe Social')
        self.cbxClasseSocial.addItems(socialclass)

    def ComboEspecializacao(self):
        itens = especialidade.get_specializations_list()
        self.cbxEspecializao.clear()
        self.cbxEspecializao.insertItem(-1,'Selecione uma Especialização')
        for item in itens:
            self.cbxEspecializao.insertItem(item[0],item[1])

    def ComboArmadura(self):
        itens = equipamento.get_equipment_from_group_armour(7)
        self.cbxArmadura.clear()
        self.cbxArmadura.insertItem(-1,'Selecione a Armadura')
        for item in itens:
            self.cbxArmadura.insertItem(item[0],item[1])

    def ComboEscudo(self):
        itens = equipamento.get_equipment_from_group_shield(7)
        self.cbxEscudos.clear()
        self.cbxEscudos.insertItem(-1,'Selecione o Escudo')
        for item in itens:
            self.cbxEscudos.insertItem(item[0],item[1])

    def ComboCapacete(self):
        itens = equipamento.get_equipment_from_group_helmet(7)
        self.cbxElmos.clear()
        self.cbxElmos.insertItem(-1,'Selecione o Elmo')
        for item in itens:
            self.cbxElmos.insertItem(item[0],item[1])

    def ComboArmas01(self):
        itens = equipamento.get_equipment_from_group(6)
        self.cbxArma01.clear()
        self.cbxArma01.insertItem(-1,'Selecione uma Arma')
        for item in itens:
            self.cbxArma01.insertItem(item[0],item[1])

    def setTableWidthPersonagems(self):
        width = self.tblCombate.verticalHeader().width()
        width += self.tblCombate.horizontalHeader().length()
        if self.tblCombate.verticalScrollBar().isVisible():
            width += self.tblCombate.verticalScrollBar().width()
        width += self.tblCombate.frameWidth() * 2
        self.tblCombate.setFixedWidth(width)

    def getPersonagem(self):
        while (self.tblProfissao.rowCount() > 0):
                self.tblProfissao.removeRow(0)

        while (self.tblEspecializacao.rowCount() > 0):
                self.tblEspecializacao.removeRow(0)

        while (self.tblMagiaBasica.rowCount() > 0):
                self.tblMagiaBasica.removeRow(0)

        linha = self.tblPersonagens.currentItem().row()
        id_persona = self.tblPersonagens.item(linha, 0).text()
        persona = personagem.get_persona(id_persona)
        
        self.txtNome.setText(persona.name)
        self.txtJogador.setText(persona.player)
        self.lblRaca.setText(persona.race.name)
        self.lblProfissao.setText(persona.profession.name)
        self.txtExperiencia.setText(str(persona.xp))
        self.spnNivel.setValue(persona.level)
        
        self.popularCombateTecnicasBasicas(persona)
        if persona.profession.id == 1 or persona.profession.id == 2:
            self.popularCombateTecnicasRestritas(persona)

        #self.popularCombateTecnicasBasicas(persona)
        if persona.profession.id != 1 and persona.profession.id != 2 :
            self.popularMagiaBasica(persona)

        self.popularHabiidadeProfissional(persona)
        
        index = self.cbxClasseSocial.findText(persona.social_class, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.cbxClasseSocial.setCurrentIndex(index)
        else:
            self.cbxClasseSocial.setCurrentIndex(0)

        
        god =divindade.get_god_name(persona.god)
        index = self.cbxDivindade.findText(god,QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.cbxDivindade.setCurrentIndex(index)
        else:
            self.cbxDivindade.setCurrentIndex(0)
        
        if persona.level <=5 :
            self.cbxEspecializao.setCurrentIndex(0)
            self.cbxEspecializao.setEnabled(False)
        else:
            self.cbxEspecializao.setEnabled(True)
            if persona.specialization != None:
                espec = persona.specialization.name
                index = self.cbxEspecializao.findText(persona.specialization.name,QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.cbxEspecializao.setCurrentIndex(index)
            else:
                self.cbxEspecializao.setCurrentIndex(0)

        self.lblDefesa.setText('{}/{}'.format(persona.active_defense,persona.passive_defense))
        self.lblResistenciaFisica.setText(str(persona.get_physical_resistance()))
        self.lblEnergiaFisica.setText(str(persona.ef))
        self.lblEnergiaHeroica.setText(str(persona.eh))
        self.lblResistenciaMagia.setText(str(persona.get_magical_resistance()))
        self.lblVelocidade.setText(str(persona.get_speed()))
        self.lblKarma.setText(str(persona.karma))
        
        self.vsdIntelecto.setValue(persona.attributes[0])
        self.vsdAura.setValue(persona.attributes[1])
        self.vsdCarisma.setValue(persona.attributes[2])
        self.vsdForca.setValue(persona.attributes[3])
        self.vsdFisico.setValue(persona.attributes[4])
        self.vsdAgilidade.setValue(persona.attributes[5])
        self.vsdPercepcao.setValue(persona.attributes[6])

        self.txtOlhos.setText(str(persona.eyes))
        self.txtCabelo.setText(str(persona.hair))
        self.txtPele.setText(str(persona.skin))
        self.lblIdade.setText(str(persona.age))
        self.lblPeso.setText(str(persona.weight))
        self.lblAltura.setText(str(persona.height))
        self.txtAparencia.setText(str(persona.appearance))
        self.txtDescricaoPersonagem.setText(str(persona.history))

        self.txtMC.setText(str(persona.copper_coins))
        self.txtMP.setText(str(persona.silver_coins))
        self.txtMO.setText(str(persona.gold_coins))

        self.lblIntelecto_inicial.setText(str(persona.race.attribute_bonus[0]))
        self.lblAura_inicial.setText(str(persona.race.attribute_bonus[1]))
        self.lblCarisma_inicial.setText(str(persona.race.attribute_bonus[2]))
        self.lblforca_inicial.setText(str(persona.race.attribute_bonus[3]))
        self.lblFisico_inicial.setText(str(persona.race.attribute_bonus[4]))
        self.lblAgilidade_inicial.setText(str(persona.race.attribute_bonus[5]))
        self.lblPercepcao_inicial.setText(str(persona.race.attribute_bonus[6]))

        self.lblPontosAquisicao.setText(str(persona.skill_points))
        persona.spells
        persona.equipment
        persona.skills 
        persona.skills_specs
        persona.combats


        #txtAcoesFurtivas.setText(persona.skills.level_test)
        #tot  = persona.get_attributes_total()
        #self.lblPontos.setText(str(tot))

        self.txtEquipamentosIniciais.clear()
        for item in persona.profession.posessions:
            self.txtEquipamentosIniciais.insertPlainText('%s\n' % item)

    def ShowFrmSobre(self):
        self.FrmSobre = QtWidgets.QMainWindow()
        self.ui = Ui_Sobre()
        self.ui.setupUi(self.FrmSobre)
        self.FrmSobre.show()

    def ShowFrmNovoPersonagem(self):
        self.FrmNovoPersonagem = QtWidgets.QMainWindow()
        self.ui = Ui_NovoPersonagem()
        self.ui.setupUi(self.FrmNovoPersonagem)
        self.FrmNovoPersonagem.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = TelaPrincipal()
    tela.show()
    app.exec()