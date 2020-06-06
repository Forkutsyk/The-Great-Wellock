import random
#import sys
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
        self.HP = 0
        self.MP = 0
    @property
    def level(self):
        return (self.xp // 100) + 1

    # i dont know how to realize spells atacking
    def fight(self, enemy, player):
        print(" How do you wanna atack?\n 1. Beat\n 2. By spells")
        choise = input(" > ")
        if choise == "1":
            damage = self.STR
            damage -= enemy.maxDEF
            enemy.HP -= damage
            if enemy.HP < 0:
                enemy.HP = 0
            print(" Atakujesz.\n")
            print(damage)
        if choise == "2":
            #player.list_of_spells()
            print(" Which of them do you wanna use ?")

    def show(self):
        print(self.name, " Zostało mi", self.HP, "hp. ", "\n")

    def heal(self):
        self.HP += random.randrange(15, 30)
        if self.HP > self.maxHP:
             self.HP = self.maxHP

    def die(self):
        print(" Jestem martwy. ~", self.name)
        # sys.exit()

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
            if zonemap[self.location][DOWN] in none_move:
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
        self.HP = 0
        self.HP = 0
        self.STR = 0

    def walcz(self, enemy):
        dmg = self.STR
        dmg -= enemy.maxDEF
        enemy.HP -= dmg
        print(self.name, "atakuje.\n")
        print(dmg)

    def show(self):
        print("Zostało mi", self.HP, "hp. ~", self.name, "\n")

    def die(self):
        print("Jestem martwy. ~", self.name)

    def randomize_enemy(self):
        i = int(random.randrange(1, 5))
        if i == 1:
            print(" You have not encountered anything dangerous on your way ")
        elif i == 2:
            self.name = 'robber'
            self.job = 'robber'
            self.HP = 80
            self.MP = 20
            self.maxDEF = 5
            self.STR = 60
            print(" On the way you met a robber")
            self.parent.fight()
        elif i == 3:
            self.name = 'goblins'
            self.job = 'robber'
            self.HP = 45
            self.MP = 0
            self.maxDEF = 2
            self.STR = 45
            print(" On the way you met a goblins")
            self.parent.fight()
        elif i == 4:
            self.name = 'traveling warrior'
            self.job = 'warrior'
            self.HP = 98
            self.MP = 20
            self.maxDEF = 10
            self.STR = 65
            print(" On the way you met a traveling warrior")
            self.parent.fight()
        elif i == 5:
            self.name = 'aggressive wolf'
            self.job = 'animal'
            self.HP = 76
            self.MP = 0
            self.maxDEF = 0
            self.STR = 55
            print(" On the way you met an aggressive wolf")
            self.parent.fight()
    def mini_boss(self):
        self.name = 'Big buddy'
        self.job = 'animal'
        self.HP = 200
        self.MP = 0
        self.maxDEF = 15
        self.STR = 20
        print(" Holly molly it`s a Big buddy !")
        self.parent.fight()