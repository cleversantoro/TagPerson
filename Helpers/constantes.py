class const:
    INT = 0 
    AUR = 1
    CAR = 2
    FOR = 3
    FIS = 4
    AGI = 5
    PER = 6

    ATTRIBUTE_PTS = 15
    MAGIC_PTS = 5
    INITIAL_COPPER = 5
    INITIAL_SILVER = 6
    INITIAL_GOLD = 1
    SKILL_POINTS = 1
    WEAPON_POINTS = 2    
    
    ATTRIBUTES = {'intelecto':0, 'aura':1, 'carisma':2, 'forca':3, 'fisico':4, 'agilidade':5, 'percepcao':6}
    ATTRIBUTE_NAMES = ('Intelecto', 'Aura', 'Carisma', 'Força', 'Físico', 'Agilidade', 'Percepção')
    ATTRIBUTE_SHORT_NAMES = ('Int', 'Aur', 'Car', 'For', 'Fís', 'Agi', 'Per', '')
    ATTRIBUTE_VALUE = {'Int' : 0, 'Aur' : 1, 'Car' : 2, 'For' : 3, 'Fís' : 4, 'Agi' : 5, 'Per' : 6}

    COIN_LABEL = ['m.c.', 'm.p.', 'm.o.']
    SOCIAL_CLASS = ['Ex-escravo', 'Ex-servo', 'Livre', 'Artífice', 'Pequeno comerciante', 'Grande comerciante', 'Baixa nobreza', 'Alta nobreza']
    EVOLUTION_TABLE = [10, 20, 30, 45, 60, 75, 95, 115, 135, 165, 195, 225, 265,
                       305, 345, 385, 435, 485, 535, 585, 645, 705, 765, 825, 895,
                       965, 1035, 1105, 1185, 1265, 1345, 1425, 1515, 1605, 1695,
                       1785, 1885, 1985, 2085, 2185]

    COMBAT_EQUIP = 5
    (MELEE_WEAPON, RANGED_WEAPON, ARMOUR, HELMET, SHIELD) = range(COMBAT_EQUIP)

    COINS = 3
    (COPPER, SILVER, GOLD) = range(COINS)





