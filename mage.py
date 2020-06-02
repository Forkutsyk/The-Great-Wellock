import random


class Spell(object):
    def __init__(self, name, cost, dmg, defence, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.defence = defence
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def show_details(self):
        ### name
        if self.name:
            print("  ~Name: ", self.name)
        else:
            print("  ~NAme: ", "_")
        ### cost
        if self.cost:
            print("  ~Cost: ", self.cost)
        else:
            print("  ~Cost: ", "_")
        ### dmg
        if self.dmg:
            print("  ~Damage: ", self.dmg)
        else:
            print("  ~Damage: ", "_")
        ### defence
        if self.defence:
            print("  ~Defence: ", "+", self.defence)
        else:
            print("  ~Defence: ", "_")

        if self.type:
            print("  ~Type: ", self.type, "\n")
        else:
            print("  ~Type: ", "_")