from Model.Items import Item

class Weapon(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        #self.skill_id = None
        self.equipment_id = None
        self.cust = 0
        #self.handling = {}
        self.min_strength = 0
        self.min_damage = 0
        self.attack_defense = {'l' : 0, 'm' : 0, 'p' : 0}
        self.range = 0
        self.bonus = 0
        self.type = None
        self._25 = 0
        self._50 = 0
        self._75 = 0
        self._100 = 0
        self.Pq = None
        self.An = None
        self.El = None
        self.Me = None
        self.Hu = None



    def __str__(self):
        return '%s\n%s\n%s\nfm:%d\nat:%s,dn:%d' % \
               (Item.__str__(self), self.skill_group,
                self.min_strength, self.attack_defense,
                self.damage, self.range)
