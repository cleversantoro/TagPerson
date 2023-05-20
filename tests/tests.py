#from DAO.DivindadeDAO import DivindadeDAO
from Controller.DivindadeCTR import DivindadeCTR as ctrDivind
from Controller.EquipamentoCTR import EquipamentoCTR as ctrEquip 
from Controller.EspecialidadeCTR import EspecialidadeCTR as ctrEsp 
from Controller.HabilidadeCTR import HabilidadeCTR as ctrHabil
from Controller.LocalidadeCTR import LocalidadeCTR  as ctrLoca
from Controller.MagiaCTR import    MagiaCTR  as ctrMag
from Controller.PersonagemCTR import PersonagemCTR as ctrPerso
from Controller.ProfissaoCTR import ProfissaoCTR  as ctrProf
from Controller.RacaCTR import RacaCTR as ctrRaca
from Controller.TempoCTR import  TempoCTR as ctrTemp
from Controller.CombateCTR import  CombateCTR as ctrCombat
from Model.Combate import Combat as combate

class test:

    def divindade():
        ctrDivind.get_gods_list()
        ctrDivind.get_god_name(1)
        print('')

    def equipamento(self):
        teste1 = ctrEquip.get_equipment_groups_misc()        
        teste1 = ctrEquip.get_equipment_from_group(1)
        teste2 = ctrEquip.get_equipment_groups()
        teste3 = ctrEquip.get_equipment_item(230)
        teste4 = ctrEquip.get_equipment_list()
        print('')
    
    def especialidade():
        teste1 = ctrEsp.get_specialization(1)
        teste2 = ctrEsp.get_specialization_name(1)
        teste3 = ctrEsp.get_specializations_list()
        teste4 = ctrEsp.get_specialization_from_profession(1)
        print('')

    def habilidade():
        teste1 = ctrHabil.get_skill(1)
        teste2 = ctrHabil.get_skill_group_children(1)
        teste3 = ctrHabil.get_skill_group_name(1)
        teste4 = ctrHabil.get_skill_group_parents()
        teste5 = ctrHabil.get_skill_name(1)
        teste6 = ctrHabil.get_skill_specialization_suggestions(22)
        teste7 = ctrHabil.get_skills_from_group(4)
        teste8 = ctrHabil.get_skills_list()
        print('')

    def combate():
        teste1 = ctrCombat.get_combat(1)
        teste3 = ctrCombat.get_combat_group_name(1)
        teste4 = ctrCombat.get_combat_group_parents()
        teste9 = ctrCombat.get_combat_group_children(1)
        teste10 = ctrCombat.get_combat_group_children(2)
        teste2 = ctrCombat.get_combat_group_children(3)
        teste5 = ctrCombat.get_combat_name(4)
        teste7 = ctrCombat.get_combat_from_group(1)
        teste8 = ctrCombat.get_combat_list()
        print('')

    def localidade():
        teste1 = ctrLoca.get_place(1)
        teste2 = ctrLoca.get_place_name(1)
        teste3 = ctrLoca.get_places_list()
        teste4 = ctrLoca.get_places_parents()
        print('')

    def magia():
        teste1 = ctrMag.get_spell(1)
        teste2 = ctrMag.get_spell_group_children(1)
        teste3 = ctrMag.get_spell_group_parents()
        teste4 = ctrMag.get_spell_name(1)
        teste5 = ctrMag.get_spells_from_group(4)
        teste6 = ctrMag.get_spells_list()
        print('')

    def personagem():
        teste1 = ctrPerso.get_persona(8)
        
        #for item in teste1.combat_equip:
        #    if(item.itemtype == 'shield'):
        #        escudo = item.name
        #    elif(item.itemtype == 'helmet'):
        #        elmo = item.name
        #    elif(item.itemtype == 'armour'):
        #        armadura = item.name

        idade_media  = teste1.race.calc_medium_age()
        altura = teste1.race.calc_minmax_height()
        peso = teste1.race.calc_minmax_weight()

        #teste2 = ctrPerso.get_persona_equipment(8)
        #teste3 = ctrPerso.get_persona_list()
        #teste4 = ctrPerso.get_persona_skills(8)
        #teste5 = ctrPerso.get_persona_spells(9)
        #teste11 = ctrPerso.get_persona_combat(9)
        #teste6 = ctrPerso.get_players_names()
        #persona = teste1
        #teste7 = ctrPerso.save_persona(persona)
        #teste8 = ctrPerso.save_persona_equipment(persona)
        #teste9 = ctrPerso.save_persona_skills(persona)
        #teste10 = ctrPerso.save_persona_spells(persona)
        print('')

    def profissao():
        teste1 = ctrProf.get_profession(1)
        teste2 = ctrProf.get_profession_name(1)
        teste3 = ctrProf.get_professions_list()
        print('')

    def raca():
        race1 = ctrRaca.get_race(1)
        race2 = ctrRaca.get_race_name(1)
        race3 = ctrRaca.get_races_list()
        print('')
    
    def tempo():
        teste1 = ctrTemp.get_timeline()
        cmb = combate
        cmb.atributed = 1
        print(cmb)
        print('')

if __name__ == '__main__':
    #test.divindade()
    #test.equipamento()
    #test.especialidade()
    #test.habilidade()
    #test.localidade()
    #test.magia()
    #test.personagem()
    #test.profissao()
    #test.raca()
    test.tempo()
    #test.combate()
    print('fim')
    #print(combate)
