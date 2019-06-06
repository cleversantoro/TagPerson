from Model.Items import Item

class Defense(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.type = None
        self.base_defense = 0
        self.absorption = 0

    def __str__(self):
        return '%s\ndb:%d\nab:%d' % \
               (Item.__str__(self), self.base_defense, self.absorption)
