from Model.Items import Item

class Defense(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        #self.type = None
        self.equipment_id = 0
        self.base_defense = 0
        self.absorption = 0
        self.min_strength = 0
        self.max_strength = 0
        self.P = 0
        self.A = 0
        self.E = 0
        self.M = 0
        self.H = 0



    def __str__(self):
        return '%s\ndb:%d\nab:%d' % \
               (Item.__str__(self), self.base_defense, self.absorption)
