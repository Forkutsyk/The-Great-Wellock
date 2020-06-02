import random
from global_variables import *


class Player:
    def __init__(self, parent):
        self.parent = parent
        self.name = ''
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxDEF = 0
        self.spels = []
        self.location = 'a0'
        self.cash = 0
        self.xp = 0
        self.game_over = False
        self.STR = 0
        self.HP = self.maxHP
        self.MP = self.maxMP

    @property
    def level(self):
        return (self.xp // 100) + 1

    def fight(self, enemy):
        damage = self.STR
        damage -= enemy.maxDEF
        enemy.maxHP -= damage
        if enemy.maxHP < 0:
            enemy.maxHP = 0
        print(" Atakujesz.\n")
        print(damage)

    def show(self):
        print(self.name, " Zostało mi", self.maxHP, "hp. ", "\n")

    def heal(self):
        self.HP += random.randrange(15, 30)
        if self.maxHP > self.HP:
             self.HP = self.HP

    def die(self):
        print(" Jestem martwy. ~", self.name)

    def move(self, dest=None):
        if not dest:
            ask = " Where would you like to move to?\n"
            print(ask)
            dest = input(" ")
        none_move = ["0", "1", "2", "3", "4"]
        if dest in ['up', 'west']:
            if zonemap[self.location][UP] in none_move:
                print(" !!! Here is a big wall !!! ")
            else:
                destination = zonemap[self.location][UP]
                self.movement_handler(destination)
        elif dest in ['left', 'west']:
            if zonemap[self.location][LEFT] in none_move:
                print(" !!! Here is a big wall !!! ")
            else:
                destination = zonemap[self.location][LEFT]
                self.movement_handler(destination)
        elif dest in ['right', 'east']:
            if zonemap[self.location][RIGHT] in none_move:
                print(" !!! Here is a big wall !!! ")
            else:
                destination = zonemap[self.location][RIGHT]
                self.movement_handler(destination)
        elif dest in ['down', 'south']:
            if zonemap[self.location][DOWN] not in none_move:
                print(" !!! Here is a big wall !!!")
            else:
                destination = zonemap[self.location][DOWN]
                self.movement_handler(destination)

    def movement_handler(self, destination):
        self.parent.myEnemy.randomize_enemy()
        print("\n" + " You have moved to the " + destination + ".")
        self.location = destination
        self.parent.location_print()


class Enemy(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = ''
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxSTR = 0
        self.STR = 0

    def walcz(self, enemy):
        dmg = self.STR
        dmg -= enemy.maxDEF
        enemy.maxHP -= dmg
        print(self.name, "atakuje.\n")
        print(dmg)

    def show(self):
        print("Zostało mi", self.maxHP, "hp. ~", self.name, "\n")

    def die(self):
        print("Jestem martwy. ~", self.name)

    def randomize_enemy(self):
        i = int(random.randrange(1, 5))
        if i == 1:
            print(" You have not encountered anything dangerous on your way ")
        elif i == 2:
            self.name = 'robber'
            self.job = 'robber'
            self.maxHP = 100
            self.maxMP = 20
            self.maxDEF = 5
            self.STR = 60
            print(" On the way you met a robber")
            self.parent.fight()
        elif i == 3:
            self.name = 'goblins'
            self.job = 'robber'
            self.maxHP = 70
            self.maxMP = 0
            self.maxDEF = 2
            self.STR = 45
            print(" On the way you met a goblins")
            self.parent.fight()
        elif i == 4:
            self.name = 'traveling warrior'
            self.job = 'warrior'
            self.maxHP = 150
            self.maxMP = 20
            self.maxDEF = 10
            self.STR = 65
            print(" On the way you met a traveling warrior")
            self.parent.fight()
        elif i == 5:
            self.name = 'aggressive wolf'
            self.job = 'animal'
            self.maxHP = 90
            self.maxMP = 0
            self.maxDEF = 0
            self.STR = 55
            print(" On the way you met an aggressive wolf")
            self.parent.fight()
