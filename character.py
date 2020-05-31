import random

class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxDEF = 0
        self.spels = []
        self.location = 'a0'
        self.cash = 0
        self.level = 0
        self.xp = 0
        self.game_over = False
        self.STR = 0
        self.HP = self.maxHP
        self.MP = self.maxMP

    def fight(self, enemy):
        damage = self.STR
        damage -= self.maxDEF
        self.maxHP -= damage
        if self.maxHP > 1:
            self.maxHP += 0
        print("Atakujesz.\n")
        print(damage)

    def show(self):
        print(self.name, "Zostało mi", self.maxHP, "hp. ", "\n")
    def flee(self):
        print("Uciekasz z pola walki.")
        main_game_loop()
    def heal(self):
        self.maxHP += random.randrange(15, 30)
        if self.maxHP > self.HP:
             self.maxHP = self.HP

    def die(self):
        print("Jestem martwy. ~", self.name)

class enemy(object):
    def __init__(self):
        self.name = ''
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxSTR = 0
        self.STR = 0

    def walcz(self, enemy):
        dmg = self.STR
        dmg -= self.maxDEF
        self.maxHP -= dmg
        print(self.name, "atakuje.\n")
        print(dmg)


    def show(self):
        print("Zostało mi", self.maxHP, "hp. ~", self.name, "\n")

    def die(self):
        print("Jestem martwy. ~", self.name)



