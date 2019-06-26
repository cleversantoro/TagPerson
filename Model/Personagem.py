from Helpers.constantes import const
from Model.__Base__ import Base
from Model.Raca import Race
from Model.Items import Item

class Persona(Base):
    def __init__(self, name='', id=-1):
        Base.__init__(self, name, id)

        self.player = ''
        self.avatar_file = None

        self.level = 1
        self.xp = 0
        self.attributes = [0, 0, 0, 0, 0, 0, 0]
        self.karma = 0
        self.active_defense = 0
        self.passive_defense = 0
        self.max_eh = 0
        self.eh = 0
        self.ef = 0
        self.absorption = 0

        self.race =  -1
        self.profession = -1
        self.specialization = -1

        self.skill_points = 0
        self.combat_points = 0
        self.weapon_points = 0
        self.magic_points = 0

        self.height = 0
        self.weight = 0
        self.age = 0

        self.eyes = ''
        self.hair = ''
        self.skin = ''
        self.appearance = ''

        self.god = -1
        self.social_class = 2
        self.homeland = None
        self.history = ''
        self.goals = ''

        self.copper_coins = const.INITIAL_COPPER
        self.silver_coins = const.INITIAL_SILVER
        self.gold_coins = const.INITIAL_GOLD

        self.combat_equip = const.COMBAT_EQUIP * [None]

        self.combats = {}
        self.spells = {}
        self.equipment = {}
        self.skills = {}
        self.skills_specs = {}

    def __cmp__(self, persona2):
        if persona2 == None:
            return False
        return self.name == persona2.name

    def get_social_class_id(self, sclass):
        try:
            return const.SOCIAL_CLASS.index(sclass)
        except ValueError:
            return -1

    def get_social_class(self):
        return const.SOCIAL_CLASS[self.social_class]

    def get_attributes_total(self):
        if self.attributes and self.race:
            return map(int.__add__, self.attributes, self.race.attribute_bonus)
        return None

    def get_attribute_by_short_name(self, short_name):
        try:
            att = const.ATTRIBUTE_VALUE[short_name]
        except:
            return 0

        return self.attributes[att] + self.race.attribute_bonus[att]

    def get_intelecto(self):
        return self.attributes[const.INT] + self.race.attribute_bonus[const.INT]

    def get_aura(self):
        return self.attributes[const.AUR] + self.race.attribute_bonus[const.AUR]

    def get_carisma(self):
        return self.attributes[const.CAR] + self.race.attribute_bonus[const.CAR]

    def get_forca(self):
        return self.attributes[const.FOR] + self.race.attribute_bonus[const.FOR]

    def get_fisico(self):
        return self.attributes[const.FIS] + self.race.attribute_bonus[const.FIS]

    def get_agilidade(self):
        return self.attributes[const.AGI] + self.race.attribute_bonus[const.AGI]

    def get_percepcao(self):
        return self.attributes[const.PER] + self.race.attribute_bonus[const.PER]

    def get_max_ef(self):
        return self.get_forca() + self.get_fisico() + self.race.ef

    def get_physical_resistance(self):
        return self.level + self.get_fisico()

    def get_magical_resistance(self):
        return self.level + self.get_aura()

    def get_speed(self):
        return self.race.base_speed + self.get_fisico()

    def get_karma(self):
        return self.get_aura() * (self.level + 1)

    def calc_defense(self):
        self.passive_defense = 0

        for d in (const.ARMOUR, const.SHIELD):
            if self.combat_equip[d] is not None:
                self.passive_defense += self.combat_equip[d].base_defense

        self.active_defense = self.passive_defense + self.get_agilidade()

        if self.active_defense < self.passive_defense:
            self.active_defense = self.passive_defense

        return (self.active_defense, self.passive_defense)

    def calc_absorption(self):
        if self.get_armour() is None:
            self.absorption = 0
        else:
            self.absorption = self.get_max_ef()

            for d in (const.ARMOUR, const.HELMET):
                if self.combat_equip[d] is not None:
                    self.absorption += self.combat_equip[d].absorption

        return self.absorption

    def calc_magic_points(self):
        if self.profession.attribute_for_magic == -1:
            return 0
        return self.attributes[self.profession.attribute_for_magic] + \
               const.MAGIC_PTS

    def equip_item(self, item):
        item_kind = get_item_kind(item)
        if item_kind > -1:
            self.combat_equip[item_kind] = item

    def unequip_item(self, item):
        item_kind = Item.get_item_kind(item)
        if item_kind > -1 and self.combat_equip[item_kind] is not None and \
           self.combat_equip[item_kind].id == item.id:
            self.combat_equip[item_kind] = None

    def get_melee_weapon(self):
        return self.combat_equip[const.MELEE_WEAPON]

    def get_ranged_weapon(self):
        return self.combat_equip[const.RANGED_WEAPON]

    def get_armour(self):
        return self.combat_equip[const.ARMOUR]

    def get_helmet(self):
        return self.combat_equip[const.HELMET]

    def get_shield(self):
        return self.combat_equip[const.SHIELD]

    def get_coins(self):
        return [self.copper_coins, self.silver_coins, self.gold_coins]

    def set_coins(self, coins):
        self.copper_coins, self.silver_coins, self.gold_coins = coins

    def add_money(self, money):
        copper, silver, gold = core.convert_to_coins(money)
        self.copper_coins += copper
        self.silver_coins += silver
        self.gold_coins += gold

    def get_money(self):
        return self.copper_coins + \
               self.silver_coins * 10 + \
               self.gold_coins * 100
