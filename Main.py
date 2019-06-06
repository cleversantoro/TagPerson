from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from View.FrmPrincipal_UI import *

from Controller.PersonagemCTR import PersonagemCTR
from Controller.DivindadeCTR import DivindadeCTR
from Controller.EspecialidadeCTR import EspecialidadeCTR
from Controller.EquipamentoCTR import EquipamentoCTR

from Helpers.constantes import const

from resources.tela import *
from resources.icones import *
from resources.categoria import *
from resources.personagem import *


from View.FrmSobre import Ui_Sobre
from View.FrmNovoPersonagem import Ui_NovoPersonagem

import os

personagem = PersonagemCTR
divindade = DivindadeCTR
especialidade = EspecialidadeCTR
equipamento = EquipamentoCTR
class TelaPrincipal(QtWidgets.QMainWindow, Ui_FrmPrincipal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1525, 784)

        self.AppEvents()
        self.PopularTela()
    
    def AppEvents(self):
        self.tblPersonagens.doubleClicked.connect(self.getPersonagem)
        self.actionSobre.triggered.connect(self.ShowFrmSobre)
        self.actionNovo.triggered.connect(self.ShowFrmNovoPersonagem)
        
        self.HabilidadesProfessionalEvents()        

    def HabilidadesProfessionalEvents(self):
        self.txtAgricultura.textChanged.connect(self.txtAgricultura_changed)
        self.txtCarpintaria.textChanged.connect(self.txtCarpintaria_changed)
        
        #self.txtTrabMetais.textChanged.connect()
        #self.txtTrabManuais.textChanged.connect()
        #self.txtEngenharia.textChanged.connect()
        #self.txtCerco.textChanged.connect()
        #self.txtNautica.textChanged.connect()

    def PopularTela(self):
        self.PopularTabela()
        self.ComboDivindade()
        self.ComboClasseSocial()
        self.ComboEspecializacao()
        self.ComboArmadura()

    def PopularTabela(self):
        rows = personagem.get_persona_list()
        self.tblPersonagens.setColumnHidden(0,True)
        #self.tblPersonagens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblPersonagens.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        header = self.tblPersonagens.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        
        #item = QtGui.QTableWidgetItem(icon, "") # Second argument (required !) is text
        #self.tableWidget.setItem(0, 0, item)

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
        divindade = DivindadeCTR
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
        itens = equipamento.get_equipment_from_group_armor(7)
        self.cbxArmadura.clear()
        self.cbxArmadura.insertItem(-1,'Selecione a Armadura')
        for item in itens:
            self.cbxArmadura.insertItem(item[0],item[1])

    def setTableWidthPersonagems(self):
        width = self.tblPersonagens.verticalHeader().width()
        width += self.tblPersonagens.horizontalHeader().length()
        if self.tblPersonagens.verticalScrollBar().isVisible():
            width += self.tblPersonagens.verticalScrollBar().width()
        width += self.tblPersonagens.frameWidth() * 2
        self.tblPersonagens.setFixedWidth(width)

    ####Professional##############
    def txtAgricultura_changed(self):
        nivel = self.txtAgricultura.text()
        if nivel == '':
            return None

        custo = self.txtAgricultura_custo.text()       
        custo = int(custo) + int(nivel)
        self.txtAgricultura_total.setText(str(custo))

        #self.txtCerco_total
        #self.txtCerco_custo

        #self.txtTrabManuais_total
        #self.txtTrabManuais_custo

        #self.txtTrabMetais_custo
        #self.txtTrabMetais_total

        #self.txtEngenharia_total
        #self.txtEngenharia_custo

        #self.txtNautica_custo
        #self.txtNautica_total

    def txtCarpintaria_changed(self):
        nivel = self.txtCarpintaria.text()
        if nivel == '':
            return None

        custo = self.txtCarpintaria_custo.text()       
        custo = int(custo) + int(nivel)
        self.txtCarpintaria_total.setText(str(custo))

    #def txtAgricultura_changed(self):
    #    nivel = self.txtAgricultura.text()
    #    if nivel == '':
    #        return None

    #    custo = self.txtAgricultura_custo.text()       
    #    custo = int(custo) + int(nivel)
    #    self.txtAgricultura_total.setText(str(custo))
    #def txtAgricultura_changed(self):
    #    nivel = self.txtAgricultura.text()
    #    if nivel == '':
    #        return None

    #    custo = self.txtAgricultura_custo.text()       
    #    custo = int(custo) + int(nivel)
    #    self.txtAgricultura_total.setText(str(custo))
    #def txtAgricultura_changed(self):
    #    nivel = self.txtAgricultura.text()
    #    if nivel == '':
    #        return None

    #    custo = self.txtAgricultura_custo.text()       
    #    custo = int(custo) + int(nivel)
    #    self.txtAgricultura_total.setText(str(custo))
    #def txtAgricultura_changed(self):
    #    nivel = self.txtAgricultura.text()
    #    if nivel == '':
    #        return None

    #    custo = self.txtAgricultura_custo.text()       
    #    custo = int(custo) + int(nivel)
    #    self.txtAgricultura_total.setText(str(custo))
    #def txtAgricultura_changed(self):
    #    nivel = self.txtAgricultura.text()
    #    if nivel == '':
    #        return None

    #    custo = self.txtAgricultura_custo.text()       
    #    custo = int(custo) + int(nivel)
    #    self.txtAgricultura_total.setText(str(custo))
    
    ####Influencia##############

    def getPersonagem(self):
        linha = self.tblPersonagens.currentItem().row()
        id_persona = self.tblPersonagens.item(linha, 0).text()
        persona = personagem.get_persona(id_persona)
        
        self.txtNome.setText(persona.name)
        self.txtJogador.setText(persona.player)
        self.lblRaca.setText(persona.race.name)
        self.lblProfissao.setText(persona.profession.name)
        self.txtExperiencia.setText(str(persona.xp))
        self.spnNivel.setValue(persona.level)

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

        #self.txtAgricultura.setText(persona.skills)

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