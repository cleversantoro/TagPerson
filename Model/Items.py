from Model.__Base__ import Base
from Helpers.constantes import const 

class Item(Base):
    def __init__(self, name):
        Base.__init__(self, name)
        self.price = 0
        self.description = None

    def get_item_kind(item):
        item_type = type(item)

        if item_type == Shield:
            item_kind = const.SHIELD

        elif item_type == Defense:
            if item.is_helmet():
                item_kind = const.HELMET
            else:
                item_kind = const.ARMOUR

        elif item_type == Weapon:
            if item.is_ranged():
                item_kind = const.RANGED_WEAPON
            else:
                item_kind = const.MELEE_WEAPON

        else:
            item_kind = -1

        return item_kind

    def __str__(self):
        return '%s\t%s\t%s' % \
                    (self.name, str(self.price), self.description)


