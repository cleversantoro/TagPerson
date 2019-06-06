from Model.Armas import Weapon
from Model.Defesa import Defense

class Shield(Defense, Weapon):
    def __init__(self, name):
        Defense.__init__(self, name)
        Weapon.__init__(self, name)

    def __str__(self):
        return '%s\ndb:%d\nab:%d\n%s\nat:%s,dn:%d' % \
               (Item.__str__(self), self.base_defense, self.absorption,
                self.attack_defense, self.damage)
