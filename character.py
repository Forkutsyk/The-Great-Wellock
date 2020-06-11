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
        self.spells = []
        self.inventory = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
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

    def fight(self, enemy, player):
        print(" How do you wanna atack?\n 1. Beat\n 2. By spells")
        choise = input(" > ")
        if choise == "1":
            damage = self.STR
            damage -= enemy.maxDEF
            enemy.HP -= damage
            if enemy.HP < 0:
                enemy.HP = 0
            print(" You are attacking.\n")
            print(damage)

        if choise == "2":
            ##### mage spells
            if self.job == "mage":
                print(""" Spells:
    1. Fire - MP:25  DMG:60
    2. Thunder - MP:25  DMG:60
    3. Meteor - MP:80  DMG:120
    4. Cure - MP:25  DMG:62
    5. Cura - MP:32  DMG:70
    6. Curaga - MP:50  DMG:120
    """)
                print(" Which of them do you wanna use ?\n")
                telling = input(" > ")
                acceptable_actions = ['1', '2', '3', '4', '5', '6']
                if telling not in acceptable_actions:
                    print(""" Here is no such spell, try again
 Spells:
    1. Fire - MP:25  DMG:60
    2. Thunder - MP:25  DMG:60
    3. Meteor - MP:80  DMG:120
    4. Cure - MP:25  DMG:62
    5. Cura - MP:32  DMG:70
    6. Curaga - MP:50  DMG:120
    """)
                elif telling == "1":
                    if self.MP >= 25:
                        self.MP -= 25
                        damage = 60
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "2":
                    if self.MP >= 25:
                        self.MP -= 25
                        damage = 60
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "3":
                    if self.MP >= 80:
                        self.MP -= 80
                        damage = 120
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "4":
                    if self.MP >= 25:
                        self.MP -= 25
                        damage = 62
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "5":
                    if self.MP >= 32:
                        self.MP -= 32
                        damage = 70
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "6":
                    if self.MP >= 50:
                        self.MP -= 50
                        damage = 120
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
            ### warrior spels
            elif self.job == 'warrior':
                print(""" Spells:
    1. Fire Sword - MP:20  DMG:35
    2. Blizard - MP:25  DMG:50
                   """)
                print(" Which of them do you wanna use ?\n")
                telling = input(" > ")
                acceptable_actions = ['1', '2']
                if telling not in acceptable_actions:
                    print(""" Here is no such spell, try again
 Spells:
    1. Fire Sword - MP:20  DMG:35
    2. Blizard - MP:25  DMG:50
                   """)
                elif telling == "1":
                    if self.MP >= 20:
                        self.MP -= 20
                        damage = 35
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "2":
                    if self.MP >= 25:
                        self.MP -= 25
                        damage = 50
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
            #### ranger spels
            elif self.job == 'ranger':
                print(""" Spells:
    1. Blood King - MP:50  DMG:70
    2. Dark Dagger Technique - MP:20  DMG:45
                        """)
                print(" Which of them do you wanna use ?\n")
                telling = input(" > ")
                acceptable_actions = ['1', '2']
                if telling not in acceptable_actions:
                    print(""" Here is no such spell, try again
Spells:
    1. Blood King - MP:50  DMG:70
    2. Dark Dagger Technique - MP:20  DMG:45
                              """)
                elif telling == "1":
                    if self.MP >= 50:
                        self.MP -= 50
                        damage = 70
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")
                elif telling == "2":
                    if self.MP >= 20:
                        self.MP -= 20
                        damage = 45
                        damage -= enemy.maxDEF
                        enemy.HP -= damage
                    else:
                        print(" You have not enough mana points")

    def show(self):
        print(self.name, " I have left:", self.HP, "hp. ", "\n")

    def heal(self):
        self.HP += random.randrange(10, 40)
        if self.HP > self.maxHP and self.MP >= 5:
             self.HP = self.maxHP
             self.MP -= 5
        else:
            print(" You have not enoght mana or you health is full")

    def die(self):
        print(self.name, "~ I'm dead. ")
        # sys.exit()
    def regenaration_mana(self):
        if self.MP < self.maxMP:
            regeneration = self.maxMP
            self.MP = regeneration

    def move(self, dest=None):
        if not dest:
            ask = " Where would you like to move to?\n"
            print(ask)
            dest = input(" ")
        none_move = ["0", "1", "2", "3", "4"]
        district_2 = ['b1', 'b2', 'b3', 'b4', 'b5']
        district_3 = ['c1', 'c2', 'c3', 'c4', 'c5']

        if dest in ['up', 'west']:
            if zonemap[self.location][UP] in none_move:
                print(" !!! Here is a big wall !!! ")
            else:
                if zonemap[self.location][UP] in district_2 and self.level < 3:
                    print(" Level up and then go to district 2 ")
                elif zonemap[self.location][UP] in district_2 and self.level >= 3:
                    destination = zonemap[self.location][UP]
                    self.movement_handler(destination)
                elif zonemap[self.location][UP] in district_3 and self.level < 5:
                    print(" Level up and then go to district 3 ")
                elif zonemap[self.location][UP] in district_3 and self.level >= 5:
                    destination = zonemap[self.location][UP]
                    self.movement_handler(destination)
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
        self.regenaration_mana()
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
        if enemy.HP < 0:
            enemy.HP = 0
        print(self.name, "attack.\n")
        print(dmg)

    def show(self):
        print(self.name," I have left:", self.HP, "hp.\n")

    def die(self):
        print("I'm dead. ~", self.name)

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
            self.xp += 20

    def boss(self):
        self.name = 'Big buddy'
        self.job = 'animal'
        self.HP = 200
        self.MP = 0
        self.maxDEF = 15
        self.STR = 20
        print(" Holly molly it`s a Big buddy !")
        self.parent.fight()