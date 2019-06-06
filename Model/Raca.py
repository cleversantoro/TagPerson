from Model.__Base__ import Base
from Helpers.constantes import const as race

class Race(Base):
    def __init__(self, name, id=-1):
        Base.__init__(self, name, id)
        self.available_professions = []
        self.attribute_bonus = [0, 0, 0, 0, 0, 0, 0]
        self.base_speed = 0
        self.ef = 0
        self.base_height = 0
        self.base_weight = 0
        self.age = (0, 0)

    def set_attribute_bonus(self, attribute, value):
        self.attribute_bonus[race.ATTRIBUTES[attribute]] = value

    def get_attribute_bonus(self):
        return self.attribute_bonus

    def calc_medium_age(self):
        return int((self.age[0] + self.age[1]) / 2)

    def calc_minmax_height(self):
        min_height = max_height = self.base_height
        min_height -= (min_height * 0.1)
        max_height += (max_height * 0.1)
        return min_height, max_height

    def calc_minmax_weight(self):
        min_weight = max_weight = self.base_weight
        min_weight -= (min_weight * 0.1)
        max_weight += (max_weight * 0.1)
        return min_weight, max_weight

    def __str__(self):
        return '%s\n%s\n%s\n%s\nvb:%d\nef:%d\nidade:%s\naltura:%d,peso:%d' % \
                    (self.name, self.description, str(self.available_professions),
                    str(self.attribute_bonus), self.base_speed, self.ef,
                    str(self.age), self.base_height, self.base_weight)

