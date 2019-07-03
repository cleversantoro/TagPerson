from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from View.FrmPrincipal_UI import *

from Controller.PersonagemCTR import PersonagemCTR as personagem
from Controller.DivindadeCTR import DivindadeCTR as divindade
from Controller.EspecialidadeCTR import EspecialidadeCTR as especialidade
from Controller.EquipamentoCTR import EquipamentoCTR as equipamento
from Controller.MagiaCTR import MagiaCTR as magia

from Helpers.constantes import const
from Helpers.helpers import utils

from resources.tela import *
from resources.icones import *
from resources.categoria import *
from resources.personagem import *

from View.FrmSobre import Ui_Sobre
from View.FrmNovoPersonagem import Ui_NovoPersonagem
from View.FrmEquipamento import Ui_Equipamento

import os

class TelaPrincipal(QtWidgets.QMainWindow, Ui_FrmPrincipal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1525, 922)
        self.center()
        
        self.niveisHabilidade = []
        self.niveisCombat = []
        self.personArmas = []
        self.personPertences = []

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
        self.actionSalvar_toolbar.triggered.connect(self.gravarPersonagem)
        self.tblMagiaBasica.cellClicked.connect(self.on_Clicked_CellMagia)
        self.tblMagiaEspecializacao.cellClicked.connect(self.on_Clicked_CellMagiaEsp)
        self.cbxPertencesGrupo.currentIndexChanged.connect(self.on_Change_ComboPertencesGrupo)
        self.tblArma.doubleClicked.connect(self.on_Clicked_CellArma)
        self.btnAdicionarArma.clicked.connect(self.on_Clicked_btnAdicionarArma)
        self.btnAdicionarPertences.clicked.connect(self.on_Clicked_btnAdicionarPertences)

    def PopularTela(self):
        self.popularGridPersonagens()
        self.ComboDivindade()
        self.ComboClasseSocial()
        self.ComboEspecializacao()
        self.ComboArmadura()
        self.ComboEscudo()
        self.ComboCapacete()
        self.ComboArmas()
        self.ComboPertencesGrupo()

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

    def setTableWidthPersonagems(self):
        width = self.tblCombate.verticalHeader().width()
        width += self.tblCombate.horizontalHeader().length()
        if self.tblCombate.verticalScrollBar().isVisible():
            width += self.tblCombate.verticalScrollBar().width()
        width += self.tblCombate.frameWidth() * 2
        self.tblCombate.setFixedWidth(width)


    ###Eventos#####
    def on_Change_NivelCombat(self, index):
        value = index
        #row = self.tblCombate.currentRow()
        #column = self.tblCombate.currentColumn()
        #self.ID = self.tblCombate. item(row, 4)
        #self.tblCombate.item(row,4).setText('2')
        #index  = self.tblCombate.currentIndex()
        #nome = self.niveisCombat[row]['name']
        #valor = self.niveisCombat[row]['spin'].value()
        #idhabilidade = self.niveisCombat[row]['idcombate']
        self.niveisCombat
    
    def on_Change_NivelProfissional(self, index):
        value = index
        #row = self.tblProfissional.currentRow()
        #column = self.tblCombate.currentColumn()
        #self.ID = self.tblCombate. item(row, 4)
        #self.tblProfissional.item(row,4).setText('2')
        #index  = self.tblCombate.currentIndex()
        #nome = self.niveisHabilidade[row]['name']
        #valor = self.niveisHabilidade[row]['spin'].value()
        #idhabilidade = self.niveisHabilidade[row]['idhabilidade']
        self.niveisHabilidade

    def on_Clicked_CellArma(self, index):
        row = self.tblArma.currentRow()
        idequipamento = self.personArmas[row]['idequipamento']
        self.ShowFrmEquipamento(idequipamento)
        
    def on_Clicked_CellMagia(self, row, column):
        if(column == 4):
            idmagia = self.niveisMagia[row]['idmagia']
            mg = magia.get_spell(idmagia)
            self.txtNomeMagia.setText(str(mg.name))
            self.txtEvocacao.setText(str(mg.evocation))
            self.txtAlcance.setText(str(mg.range))
            self.txtDuracao.setText(str(mg.duration))
            self.txtEfeitos.setText(str(mg.level))
            self.txtDescricao.setText(str(mg.description))

    def on_Clicked_CellMagiaEsp(self, row, column):
        if(column == 4):
            idmagia = self.niveisMagiaEsp[row]['idmagia']
            mg = magia.get_spell(idmagia)
            self.txtNomeMagia.setText(str(mg.name))
            self.txtEvocacao.setText(str(mg.evocation))
            self.txtAlcance.setText(str(mg.range))
            self.txtDuracao.setText(str(mg.duration))
            self.txtEfeitos.setText(str(mg.level))
            self.txtDescricao.setText(str(mg.description))

    def on_Change_ComboPertencesGrupo(self,index):
        group_id = self.cbxPertencesGrupo.itemData(index)
        self.ComboPertencesItens(group_id)

    def on_Clicked_btnAdicionarArma(self):
        weapon_id = self.cbxArma.itemData(self.cbxArma.currentIndex())
        index = self.tblArma.rowCount()
        equip = equipamento.get_equipment_item(weapon_id)
        self.person.combat_weapon[index] = equip
        self.popularArmas(self.person)

    def on_Clicked_btnAdicionarPertences(self):
        weapon_group_id = self.cbxPertencesGrupo.itemData(self.cbxPertencesGrupo.currentIndex())
        weapon_id = self.cbxPertencesItem.itemData(self.cbxPertencesItem.currentIndex())
        self.person.equipment[weapon_id] = 1
        #group_id = self.cbxPertencesGrupo.itemData(index)
        #self.ComboPertencesItens(group_id)
        pass

    def on_tableWidget_itemClicked(self):
        pass


    ### CRUD #####
    def getPersonagem(self):
        while (self.tblProfissao.rowCount() > 0):
                self.tblProfissao.removeRow(0)

        while (self.tblEspecializacao.rowCount() > 0):
                self.tblEspecializacao.removeRow(0)

        while (self.tblMagiaBasica.rowCount() > 0):
                self.tblMagiaBasica.removeRow(0)

        while (self.tblMagiaEspecializacao.rowCount() > 0):
                self.tblMagiaEspecializacao.removeRow(0)

        self.txtNomeMagia.setText(None)
        self.txtEvocacao.setText(None)
        self.txtAlcance.setText(None)
        self.txtDuracao.setText(None)
        self.txtEfeitos.setText(None)
        self.txtDescricao.setText(None)

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
        if(persona.profession.id == 1 or persona.profession.id == 2):
            self.popularCombateTecnicasRestritas(persona)
            
        if(persona.profession.is_magic_user()):
            self.popularMagiaBasica(persona)

        if(persona.specialization != None):
            self.popularCombateTecnicasEspecializacao(persona)
            self.popularMagiaEspecializacao(persona)         

        self.popularHabilidadeProfissional(persona)
        self.popularHabilidadeSubterfugio(persona)
        self.popularHabilidadeManobra(persona)
        self.popularHabilidadeInfluencia(persona)
        self.popularHabilidadeConhecimento(persona)
        self.popularHabilidadeGeral(persona)
        self.popularArmas(persona)
        self.popularPertences(persona)
        
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

        armadura = persona.get_armour()
        escudo = persona.get_shield()
        elmo = persona.get_helmet()
            
        if(escudo != None):
            indexEsc = self.cbxEscudos.findText(escudo.name,QtCore.Qt.MatchFixedString)
            self.cbxEscudos.setCurrentIndex(indexEsc)
        else:
            self.cbxEscudos.setCurrentIndex(0)
        
        if(elmo != None):
            indexElm = self.cbxElmos.findText(elmo.name,QtCore.Qt.MatchFixedString)
            self.cbxElmos .setCurrentIndex(indexElm)
        else:
            self.cbxElmos.setCurrentIndex(0)
        
        if(armadura != None):
            indexArm = self.cbxArmadura.findText(armadura.name,QtCore.Qt.MatchFixedString)
            self.cbxArmadura .setCurrentIndex(indexArm)
        else:
            self.cbxArmadura.setCurrentIndex(0)

        resistencia_fisica = persona.get_physical_resistance()
        resistencia_magia = persona.get_magical_resistance()
        velocidade = persona.get_speed()
        karma = persona.get_karma()
        defesa = persona.calc_defense()
        energia_fisica = persona.get_max_ef()
        energia_heroica = utils.calc_eh(persona)
        absorcao = persona.calc_absorption()

        self.lblDefesa.setText('{}/{}'.format(defesa[0],defesa[1]))
        self.lblResistenciaFisica.setText(str(resistencia_magia))
        self.lblEnergiaFisica.setText(str('{}/{}'.format(energia_fisica,absorcao)))
        self.lblEnergiaHeroica.setText(str(energia_heroica)) 
        self.lblResistenciaMagia.setText(str(resistencia_magia))
        self.lblVelocidade.setText(str(velocidade))
        self.lblKarma.setText(str(karma))
        
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
        persona.combat_skills

        #persona.race.
        tot  = persona.get_attributes_total()
        self.lblPontos.setText(str(tot))

        self.txtEquipamentosIniciais.clear()
        for item in persona.profession.posessions:
            self.txtEquipamentosIniciais.insertPlainText('%s\n' % item)

        self.person = persona

    def gravarPersonagem(self):
        self.gravarCombate()
        self.gravarHabilidade()
        self.gravarMagia()
        personagem.save_persona(self.person)

    def gravarCombate(self):
        for item in self.niveisCombat:
            self.person.combat_skills[item['idcombate']] = item['spin'].value()

    def gravarHabilidade(self):
        for item in self.niveisHabilidade:
            self.person.skills[item['idhabilidade']] = item['spin'].value()

    def gravarMagia(self):
        for item in self.niveisMagia:
            self.person.spells[item['idmagia']] = item['spin'].value()


    ### Armas/Pertences #####
    def popularArmas(self,persona):
        person = persona

        self.tblArma.setColumnHidden(0,True)
        self.tblArma.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblArma.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblArma.verticalHeader().hide()

        header = self.tblArma.horizontalHeader()       
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblArma.rowCount() > 0):
                self.tblArma.removeRow(0)

        row = 0
        for item in person.combat_weapon:
            self.tblArma.insertRow(row)

            value, coin = utils.convert_to_coins_single(person.combat_weapon[item].price)
            money_fmt = '{} {}'.format(int(value), const.COIN_LABEL[coin])
            id= QTableWidgetItem(str(person.combat_weapon[item].equipment_id))
            nome = QTableWidgetItem(str(person.combat_weapon[item].name))
            descricao = QTableWidgetItem(str(person.combat_weapon[item].description))
            valor = QTableWidgetItem(str(money_fmt))

            self.personArmas.append({'name':'arma_{}'.format(row),'idequipamento':person.combat_weapon[item].equipment_id}) 

            self.tblArma.setItem(row, 0, id)
            self.tblArma.setItem(row, 1, nome)
            self.tblArma.setItem(row, 2, descricao)
            self.tblArma.setItem(row, 3, valor)
            row = row + 1

    def popularPertences(self,persona):
        person = persona

        self.tblPertences.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblPertences.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblPertences.verticalHeader().hide()

        header = self.tblPertences.horizontalHeader()       
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblPertences.rowCount() > 0):
                self.tblPertences.removeRow(0)

        row = 0
        for item in person.equipment:
            self.tblPertences.insertRow(row)

            value, coin = utils.convert_to_coins_single(person.equipment[item].price)
            money_fmt = '{} {}'.format(int(value), const.COIN_LABEL[coin])
            nome = QTableWidgetItem(str(person.equipment[item].name))
            descricao = QTableWidgetItem(str(person.equipment[item].description))
            valor = QTableWidgetItem(str(money_fmt))
            id= person.equipment[item].id

            self.personPertences.append({'name':'objeto_{}'.format(row),'idequipamento':id}) 

            self.tblPertences.setItem(row, 0, nome)
            self.tblPertences.setItem(row, 1, descricao)
            self.tblPertences.setItem(row, 2, valor)
            row = row + 1


    ### Combate #####
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
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivelcombatbas = QtWidgets.QSpinBox()
            self.nivelcombatbas.setObjectName('nivelcombatbas_{}'.format(row))
            self.nivelcombatbas.setValue(item[2])
            self.nivelcombatbas.valueChanged.connect(self.on_Change_NivelCombat)

            self.niveisCombat.append({'spin':self.nivelcombatbas,'name':'nivelcombatbas_{}'.format(row),'idcombate':item[0]}) 

            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            self.tblCombate.setItem(row, 0, descricao)
            self.tblCombate.setCellWidget(row, 1, self.nivelcombatbas)
            self.tblCombate.setItem(row, 2, custo)
            self.tblCombate.setItem(row, 3, ajuste)
            self.tblCombate.setItem(row, 4, total)
            self.tblCombate.setItem(row, 5, categoria)
            self.tblCombate.setItem(row, 6, icone)
            row = row + 1

    def popularCombateTecnicasEspecializacao(self,persona):
        person = persona
        rows = personagem.get_combat_persona(person.id, person.specialization.combat_group)        

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

        while (self.tblEspecializacao.rowCount() > 0):
                self.tblEspecializacao.removeRow(0)

        row = 0
        for item in rows:
            self.tblEspecializacao.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivelcombatesp = QtWidgets.QSpinBox()
            self.nivelcombatesp.setObjectName('nivelcombatesp_{}'.format(row))
            self.nivelcombatesp.setValue(item[2])
            self.nivelcombatesp.valueChanged.connect(self.on_Change_NivelCombat)

            self.niveisCombat.append({'spin':self.nivelcombatesp,'name':'nivelcombatesp_{}'.format(row),'idcombate':item[0]}) 

            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            self.tblEspecializacao.setItem(row, 0, descricao)
            self.tblEspecializacao.setCellWidget(row, 1, self.nivelcombatesp)
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

        while (self.tblProfissao.rowCount() > 0):
                self.tblProfissao.removeRow(0)

        row = 0
        for item in rows:
            self.tblProfissao.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivelcombatpro = QtWidgets.QSpinBox()
            self.nivelcombatpro.setObjectName('nivelcombatpro_{}'.format(row))
            self.nivelcombatpro.setValue(item[2])
            self.nivelcombatpro.valueChanged.connect(self.on_Change_NivelCombat)

            self.niveisCombat.append({'spin':self.nivelcombatpro,'name':'nivelcombatpro_{}'.format(row),'idcombate':item[0]}) 

            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            self.tblProfissao.setItem(row, 0, descricao)
            self.tblProfissao.setCellWidget(row, 1, self.nivelcombatpro)
            self.tblProfissao.setItem(row, 2, custo)
            self.tblProfissao.setItem(row, 3, ajuste)
            self.tblProfissao.setItem(row, 4, total)
            self.tblProfissao.setItem(row, 5, categoria)
            self.tblProfissao.setItem(row, 6, icone)
            row = row + 1


    ### Magia #####
    def popularMagiaBasica(self,persona):
        self.niveisMagia = []
        person = persona
        rows = personagem.get_spell_persona(person.id, person.profession.spell_group)        

        self.tblMagiaBasica.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMagiaBasica.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMagiaBasica.verticalHeader().hide()

        header = self.tblMagiaBasica.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblMagiaBasica.rowCount() > 0):
                self.tblMagiaBasica.removeRow(0)

        row = 0
        for item in rows:
            self.tblMagiaBasica.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivelmagiabas = QtWidgets.QSpinBox()
            self.nivelmagiabas.setValue(item[2])
            self.nivelmagiabas.setObjectName('nivelmagiabas_{}'.format(row))
            self.nivelmagiabas.valueChanged.connect(self.on_Change_NivelCombat)

            self.niveisMagia.append({'spin':self.nivelmagiabas,'name':'nivelmagiabas_{}'.format(row),'idmagia':item[0]}) 

            custo = QTableWidgetItem(str(item[3]))
            total = QTableWidgetItem(str(item[4]))
            
            icon = QtGui.QIcon(QtGui.QPixmap(":/menu/iconfinder_question_12319.png"))

            self.icone = QTableWidgetItem(icon,None) 

            self.tblMagiaBasica.setItem(row, 0, descricao)
            self.tblMagiaBasica.setCellWidget(row, 1, self.nivelmagiabas)
            self.tblMagiaBasica.setItem(row, 2, custo)
            self.tblMagiaBasica.setItem(row, 3, total)
            self.tblMagiaBasica.setItem(row, 4, self.icone)
            row = row + 1

    def popularMagiaEspecializacao(self,persona):
        self.niveisMagiaEsp = []
        person = persona
        rows = personagem.get_spell_persona(person.id, person.specialization.spell_group)        

        self.tblMagiaEspecializacao.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMagiaEspecializacao.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMagiaEspecializacao.verticalHeader().hide()

        header = self.tblMagiaEspecializacao.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblMagiaEspecializacao.rowCount() > 0):
                self.tblMagiaEspecializacao.removeRow(0)

        row = 0
        for item in rows:
            self.tblMagiaEspecializacao.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivelmagiaesp = QtWidgets.QSpinBox()
            self.nivelmagiaesp.setValue(item[2])
            self.nivelmagiaesp.setObjectName('nivelmagiaesp_{}'.format(row))
            self.nivelmagiaesp.valueChanged.connect(self.on_Change_NivelCombat)

            self.niveisMagiaEsp.append({'spin':self.nivelmagiaesp,'name':'nivelmagiaesp_{}'.format(row),'idmagia':item[0]}) 

            custo = QTableWidgetItem(str(item[3]))
            total = QTableWidgetItem(str(item[4]))
            
            icon = QtGui.QIcon(QtGui.QPixmap(":/menu/iconfinder_question_12319.png"))

            self.icone = QTableWidgetItem(icon,None) 

            self.tblMagiaEspecializacao.setItem(row, 0, descricao)
            self.tblMagiaEspecializacao.setCellWidget(row, 1, self.nivelmagiaesp)
            self.tblMagiaEspecializacao.setItem(row, 2, custo)
            self.tblMagiaEspecializacao.setItem(row, 3, total)
            self.tblMagiaEspecializacao.setItem(row, 4, self.icone)
            row = row + 1


    ### Habilidades#####
    def popularHabilidadeProfissional(self,persona):
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
            
            self.nivelProfissional = QtWidgets.QSpinBox()
            self.nivelProfissional.setValue(item[3])
            self.nivelProfissional.setObjectName('nivelprofissional_{}'.format(row))
            self.nivelProfissional.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelProfissional,'name':'nivelprofissional_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblProfissional.setItem(row, 0, descricao)
            self.tblProfissional.setItem(row, 1, restrito)
            self.tblProfissional.setCellWidget(row, 2, self.nivelProfissional)
            self.tblProfissional.setItem(row, 3, custo)
            self.tblProfissional.setItem(row, 4, ajuste)
            self.tblProfissional.setItem(row, 5, total)
            row = row + 1

    def popularHabilidadeSubterfugio(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,2)        

        self.tblSubterfugio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSubterfugio.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblSubterfugio.verticalHeader().hide()

        header = self.tblSubterfugio.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblSubterfugio.rowCount() > 0):
                self.tblSubterfugio.removeRow(0)

        row = 0
        for item in rows:
            self.tblSubterfugio.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivelSubterfugio = QtWidgets.QSpinBox()
            self.nivelSubterfugio.setValue(item[3])
            self.nivelSubterfugio.setObjectName('nivelsubterfugio_{}'.format(row))
            self.nivelSubterfugio.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelSubterfugio,'name':'nivelsubterfugio_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblSubterfugio.setItem(row, 0, descricao)
            self.tblSubterfugio.setItem(row, 1, restrito)
            self.tblSubterfugio.setCellWidget(row, 2, self.nivelSubterfugio)
            self.tblSubterfugio.setItem(row, 3, custo)
            self.tblSubterfugio.setItem(row, 4, ajuste)
            self.tblSubterfugio.setItem(row, 5, total)
            row = row + 1

    def popularHabilidadeManobra(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,3)        

        self.tblManobras.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblManobras.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblManobras.verticalHeader().hide()

        header = self.tblManobras.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblManobras.rowCount() > 0):
                self.tblManobras.removeRow(0)

        row = 0
        for item in rows:
            self.tblManobras.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivelManobras = QtWidgets.QSpinBox()
            self.nivelManobras.setValue(item[3])
            self.nivelManobras.setObjectName('nivelmanobras_{}'.format(row))
            self.nivelManobras.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelManobras,'name':'nivelmanobras_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblManobras.setItem(row, 0, descricao)
            self.tblManobras.setItem(row, 1, restrito)
            self.tblManobras.setCellWidget(row, 2, self.nivelManobras)
            self.tblManobras.setItem(row, 3, custo)
            self.tblManobras.setItem(row, 4, ajuste)
            self.tblManobras.setItem(row, 5, total)
            row = row + 1

    def popularHabilidadeInfluencia(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,4)        

        self.tblInfluencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInfluencia.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInfluencia.verticalHeader().hide()

        header = self.tblInfluencia.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblInfluencia.rowCount() > 0):
                self.tblInfluencia.removeRow(0)

        row = 0
        for item in rows:
            self.tblInfluencia.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivelInfluencia = QtWidgets.QSpinBox()
            self.nivelInfluencia.setValue(item[3])
            self.nivelInfluencia.setObjectName('nivelinfluencia_{}'.format(row))
            self.nivelInfluencia.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelInfluencia,'name':'nivelinfluencia_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblInfluencia.setItem(row, 0, descricao)
            self.tblInfluencia.setItem(row, 1, restrito)
            self.tblInfluencia.setCellWidget(row, 2, self.nivelInfluencia)
            self.tblInfluencia.setItem(row, 3, custo)
            self.tblInfluencia.setItem(row, 4, ajuste)
            self.tblInfluencia.setItem(row, 5, total)
            row = row + 1

    def popularHabilidadeConhecimento(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,5)        

        self.tblConhecimento.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblConhecimento.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblConhecimento.verticalHeader().hide()

        header = self.tblConhecimento.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblConhecimento.rowCount() > 0):
                self.tblConhecimento.removeRow(0)

        row = 0
        for item in rows:
            self.tblConhecimento.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivelConhecimento = QtWidgets.QSpinBox()
            self.nivelConhecimento.setValue(item[3])
            self.nivelConhecimento.setObjectName('nivelconhecimento_{}'.format(row))
            self.nivelConhecimento.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelConhecimento,'name':'nivelconhecimento_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblConhecimento.setItem(row, 0, descricao)
            self.tblConhecimento.setItem(row, 1, restrito)
            self.tblConhecimento.setCellWidget(row, 2, self.nivelConhecimento)
            self.tblConhecimento.setItem(row, 3, custo)
            self.tblConhecimento.setItem(row, 4, ajuste)
            self.tblConhecimento.setItem(row, 5, total)
            row = row + 1

    def popularHabilidadeGeral(self,persona):
        person = persona
        rows = personagem.get_skills_persona(person.id,6)        

        self.tblGeral.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblGeral.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblGeral.verticalHeader().hide()

        header = self.tblGeral.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        while (self.tblGeral.rowCount() > 0):
                self.tblGeral.removeRow(0)

        row = 0
        for item in rows:
            self.tblGeral.insertRow(row)
            descricao = QTableWidgetItem(str(item[1]))
            restrito = QTableWidgetItem(str(item[2]))
            
            self.nivelGeral = QtWidgets.QSpinBox()
            self.nivelGeral.setValue(item[3])
            self.nivelGeral.setObjectName('nivelgeral_{}'.format(row))
            self.nivelGeral.valueChanged.connect(self.on_Change_NivelProfissional)

            self.niveisHabilidade.append({'spin':self.nivelGeral,'name':'nivelgeral_{}'.format(row),'idhabilidade':item[0]}) 

            custo = QTableWidgetItem(str(item[4]))
            ajuste = QTableWidgetItem(str(item[5]))
            total = QTableWidgetItem(str(item[6]))

            self.tblGeral.setItem(row, 0, descricao)
            self.tblGeral.setItem(row, 1, restrito)
            self.tblGeral.setCellWidget(row, 2, self.nivelGeral)
            self.tblGeral.setItem(row, 3, custo)
            self.tblGeral.setItem(row, 4, ajuste)
            self.tblGeral.setItem(row, 5, total)
            row = row + 1


    ### Combos #####
    def ComboPertencesGrupo(self):
        itens = equipamento.get_equipment_groups_misc()
        self.cbxPertencesGrupo.clear()
        self.cbxPertencesGrupo.addItem('Selecione o Grupo',0)
        for item in itens:
            self.cbxPertencesGrupo.addItem(item[1],item[0])

    def ComboPertencesItens(self,group_id):
        if(group_id > 0):
            itens = equipamento. get_equipment_from_group(group_id)
            self.cbxPertencesItem.clear()
            self.cbxPertencesItem.addItem('Selecione o Item',0)
            for item in itens:
                self.cbxPertencesItem.addItem(item[1],item[0])

    def ComboDivindade(self):
        #divindade = DivindadeCTR
        itens = divindade.get_gods_list()
        self.cbxDivindade.clear()
        self.cbxDivindade.addItem('Selecione uma Divindade',0)
        for item in itens:
            #'{}-({})'.format(item[1],item[2]))
            self.cbxDivindade.addItem(item[1],str(item[0]))

    def ComboClasseSocial(self):
        const.SOCIAL_CLASS.sort()
        socialclass = const.SOCIAL_CLASS
        self.cbxClasseSocial.clear()
        self.cbxClasseSocial.addItem('Selecione uma Classe Social')
        self.cbxClasseSocial.addItems(socialclass)

    def ComboEspecializacao(self):
        itens = especialidade.get_specializations_list()
        self.cbxEspecializao.clear()
        self.cbxEspecializao.addItem('Selecione uma Especialização',0)
        for item in itens:
            self.cbxEspecializao.addItem(item[1],item[0])

    def ComboArmadura(self):
        itens = equipamento.get_equipment_from_group_armour(7)
        self.cbxArmadura.clear()
        self.cbxArmadura.addItem('Selecione a Armadura',0)
        for item in itens:
            self.cbxArmadura.addItem(item[1],item[0])

    def ComboEscudo(self):
        itens = equipamento.get_equipment_from_group_shield(7)
        self.cbxEscudos.clear()
        self.cbxEscudos.addItem('Selecione o Escudo',0)
        for item in itens:
            self.cbxEscudos.addItem(item[1],item[0])

    def ComboCapacete(self):
        itens = equipamento.get_equipment_from_group_helmet(7)
        self.cbxElmos.clear()
        self.cbxElmos.addItem('Selecione o Elmo',0)
        for item in itens:
            self.cbxElmos.addItem(item[1],item[0])

    def ComboArmas(self):
        itens = equipamento.get_equipment_from_group(6)
        self.cbxArma.clear()
        self.cbxArma.addItem('Selecione uma Arma',0)
        for item in itens:
            self.cbxArma.addItem(item[1],item[0])


    ### Modals #####
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

    def ShowFrmEquipamento(self,id):
        self.FrmEquipamento = QtWidgets.QMainWindow()
        self.ui = Ui_Equipamento()
        self.ui.setupUi(self.FrmEquipamento)        
        self.ui.preencherEquipamento(id)
        self.FrmEquipamento.show()

                                                     
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela = TelaPrincipal()
    tela.show()
    app.exec()