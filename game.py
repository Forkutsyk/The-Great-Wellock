# Python Text RPG
# Poplavskyi Oleksandr
# Group: sr-13

import sys
import os
from mage import Spell
from character import Player, Enemy
from diologs import dialogs
import pickle
import random
from global_variables import *
from quests import Quests

#### COLORED TEXT IN PROMPT
YOU = '\x1b[1;34;40m'
SYSTEM = "\x1b[1;32;40m"
DANGER = "\x1b[1;31;40m"
NPC = "\x1b[1;36;40m"
END = '\x1b[0m'


class Text:
    dialogs = dialogs()
    YOU = '\x1b[1;34;40m'
    SYSTEM = "\x1b[1;32;40m"
    DANGER = "\x1b[1;31;40m"
    NPC = "\x1b[1;36;40m"
    END = '\x1b[0m'

    @classmethod
    def you(cls, text, begin_txt='YOU', txt_only=False, print_text=True, print_function='dialog_print0025'):
        if txt_only:
            val = cls.YOU + text + cls.END
        else:
            val = cls.YOU + f" {begin_txt}: " + cls.END + text
        if print_text:
            cls.dialogs.dialog = val
            func = getattr(cls.dialogs, print_function)
            func()

    @classmethod
    def system(cls, text, begin_txt='SYSTEM', txt_only=False, print_text=True, print_function='dialog_print0025'):
        if txt_only:
            val = cls.SYSTEM + text + cls.END
        else:
            val = cls.SYSTEM + f" {begin_txt}: " + cls.END + text
        if print_text:
            cls.dialogs.dialog = val
            func = getattr(cls.dialogs, print_function)
            func()

    @classmethod
    def npc(cls, text, begin_txt='Stranger', txt_only=False, print_text=True, print_function='dialog_print0025'):
        if txt_only:
            val = cls.NPC + text + cls.END
        else:
            val = cls.NPC + f" {begin_txt}: " + cls.END + text
        if print_text:
            cls.dialogs.dialog = val
            func = getattr(cls.dialogs, print_function)
            func()

    @classmethod
    def danger(cls, text, begin_txt='Strange noise', txt_only=False, print_text=True,
               print_function='dialog_print0025'):
        if txt_only:
            val = cls.DANGER + text + cls.END
        else:
            val = cls.DANGER + f" {begin_txt}: " + cls.END + text
        if print_text:
            cls.dialogs.dialog = val
            func = getattr(cls.dialogs, print_function)
            func()


#### Player Setup ####
class Game:
    def __init__(self):
        self.text = Text()
        self.myPlayer = Player(self)
        self.myEnemy = Enemy(self)
        self.quests = Quests(self)
        self.zonemap = zonemap
        self.equipment_set = equipment_set

    ### Create Black Magic
    fire = Spell("Fire", 25, 60, 0, "black")
    thunder = Spell("Thunder", 25, 60, 0, "black")
    meteor = Spell("Meteor", 80, 120, 0, "black")
    blizzard = Spell("Blizzard", 25, 50, 0, "black")
    quake = Spell("Quake", 14, 35, 0, "black")

    ### Create White Magic
    cure = Spell("Cure", 25, 62, 0, "white")
    cura = Spell("Cura", 32, 70, 0, "white")
    curaga = Spell("Curaga", 50, 90, 0, "white")

    ### Create spels for wariore
    FireSword = Spell("Fire Sword", 20, 35, 0, "fire")

    ### Create spells for ranger
    DarkDaggerTechnique = Spell("Dark Dagger Technique", 20, 45, 0, "black")
    bloodKing = Spell("Blood King", 50, 70, 0, "bloody")

    # special - can be learned with a quest
    FireBall = Spell("Fire Ball", 70, 160, 0, "fire")

    cut_scene = dialogs()

    #### FIGHTINGS
    def fight(self):
        self.show_enemy_stats()
        choice = None
        while choice != "0" and self.myEnemy.HP > 0 and self.myPlayer.HP > 0:
            print("""    Fight

            0 - uciekaj
            1 - walcz
            2 - ulecz
            się
            """)
            choice = input(" Choose: ")
            print()
            if choice == "1":
                self.myPlayer.fight(self.myEnemy, self.myPlayer)
                if self.myEnemy.HP < 1:
                    self.myEnemy.die(self.myPlayer)
                    break
                self.myEnemy.show()
                self.myEnemy.walcz(self.myPlayer)
                if self.myPlayer.HP < 1:
                    self.myPlayer.die()
                    break
                self.myPlayer.show()
            elif choice == "2":
                self.myPlayer.heal()
                self.myPlayer.show()
                self.myEnemy.walcz(self.myPlayer)
                if self.myPlayer.HP < 1:
                    self.myPlayer.die(self.myPlayer)
                    break
                self.myPlayer.show()
            elif choice == "0":
                flee()
                break
            else:
                print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

    def fight_dragon(self):
        # setup dragon stats
        self.myEnemy.name = 'Dragon'
        self.myEnemy.job = 'legendary animal'
        self.myEnemy.HP = 250
        self.myEnemy.MP = 0
        self.myEnemy.maxDEF = 0
        self.myEnemy.STR = 55
        self.text.danger(
            "On your way to dark valley you see it.\n Huge wings, lots of fire and the appaling smell.\n Chances of survival are pretty much zero but you try to kill the dragon anyway...\n")
        self.fight()

    def fight_soldiers(self):
        three = 3
        while three != 0:
            self.myEnemy.name = 'Warevolfe'
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 70
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 30
            self.text.danger("*growls aggressively*", begin_txt="Soldier")
            self.fight()
            three -= 1

    def storage_fight(self):
        six = 6
        monsters = ['Striga', 'Ghoul', 'Frightener', 'Vampire']
        while six != 0:
            self.myEnemy.name = random.choice(monsters)
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 45
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 20
            saying = ["I'll dance on your bones", "What makes this delicious steak here", "This pig, my prey"]
            self.text.danger(f"{random.choice(saying)}", begin_txt="soldier")
            self.fight()
            six -= 1

    def training_fight(self):
        four = 4
        monsters = ['Striga', 'Ghoul', 'Frightener', 'Vampire']
        while four != 0:
            self.myEnemy.name = random.choice(monsters)
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 70
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 30
            saying = ["I'll dance on your bones", "What makes this delicious steak here", "This pig, my prey"]
            self.text.danger(f"{random.choice(saying)}", begin_txt="soldier")
            self.fight()
            four -= 1

    def port_fight(self):
        five = 5
        monsters = ['Scarletia', 'Barbegazi', 'Frightener', 'Megalodon']
        while five != 0:
            self.myEnemy.name = random.choice(monsters)
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 55
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 15
            saying = ["I'll dance on your bones", "What makes this delicious steak here", "This pig, my prey"]
            self.text.danger(f"{random.choice(saying)}", begin_txt="soldier")
            self.fight()
            five -= 1

    def fight_boss_soldiers(self):
        five = 5
        monsters = ['Striga', 'Ghoul', 'Frightener', 'Vampire','Scarletia', 'Barbegazi', 'Megalodon']
        while five != 0:
            self.myEnemy.name = random.choice(monsters)
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 45
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 15
            saying = ["I'll dance on your bones", "What makes this delicious steak here", "This pig, my prey"]
            self.text.danger(f"{random.choice(saying)}", begin_txt="soldier")
            self.fight()
            five -= 1

    def boss_soldiers_harder(self):
        five = random.randint(9, 15)
        monsters = ['Striga', 'Ghoul', 'Frightener', 'Vampire','Scarletia', 'Barbegazi', 'Megalodon']
        while five != 0:
            self.myEnemy.name = random.choice(monsters)
            self.myEnemy.job = 'soldier'
            self.myEnemy.HP = 45
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 0
            self.myEnemy.STR = 15
            saying = ["I'll dance on your bones", "What makes this delicious steak here", "This pig, my prey"]
            self.text.danger(f"{random.choice(saying)}", begin_txt="soldier")
            self.fight()
            five -= 1

    def master_fight(self):
        self.myEnemy.name = 'Tetrex'
        self.myEnemy.job = 'Old master'
        self.myEnemy.HP = 5000
        self.myEnemy.MP = 0
        self.myEnemy.maxDEF = 500
        self.myEnemy.STR = 500
        self.text.danger("You're too selfconfident young man. I will teach you a lesson for free",begin_txt="Tetrex")
        self.fight()

    def snakes_fight(self):
        self.text.system("""\n  - Swamp of walking snakes  - \n""", txt_only=True)
        self.text.system(text=""" Try to look out, maybe you find something interesting...(write look)\n""")
        input(" > ")
        self.text.danger("Shhhh\n")
        self.text.you("Strange, what is it the sound ?\n")
        self.text.you("Ahh, reaaaally they??\n")
        randomizer = random.randint(3, 12)
        number_enemies = randomizer
        while number_enemies != 0:
            self.myEnemy.name = 'Walking snake'
            self.myEnemy.job = 'animal'
            self.myEnemy.HP = 45
            self.myEnemy.MP = 0
            self.myEnemy.maxDEF = 20
            self.myEnemy.STR = 45
            self.text.danger("Shhhhh\n")
            self.fight()
            number_enemies -= 1

    #### PRINTING
    def location_print(self):
        print('\n' + (" " + '#' * (4 + len(game.zonemap[self.myPlayer.location][ZONENAME]))))
        print(" " + '# ' + game.zonemap[self.myPlayer.location][ZONENAME].upper() + ' #')
        print('\n' + (" " + '#' * (4 + len(game.zonemap[self.myPlayer.location][ZONENAME]))))
        print('\n' + (game.zonemap[self.myPlayer.location][DESCRIPTION]) + "\n")

    def inventory_print(self):
        print("Your inventory:")
        number = 1
        print(" ")
        if equipment_set['Armor'][Name] != "name":
            print(f""" Armor: {equipment_set['Armor'][Name]}
        +{equipment_set['Armor'][playerHp]} hp
        +{equipment_set['Armor'][playerDEF]} def
        """)
        elif equipment_set['Armor'][Name] == "name":
            print(f""" Armor: none
        0 hp
        0 def
                    """)
        if equipment_set['Weapon'][Name] != "name":
            print(f""" Weapon: {equipment_set['Weapon'][Name]}
        +{equipment_set['Weapon'][playerSTR]} str
        +{equipment_set['Weapon'][playerDEF]} def
        """)
        elif equipment_set['Weapon'][Name] == "name":
            print(f""" Weapon: none
         0 str
         0 def
                    """)
        if equipment_set['Magic stuff'][Name] != "name":
            print(f""" Magic stuff: {equipment_set['Magic stuff'][Name]}
        +{equipment_set['Magic stuff'][playerMP]} mp
        """)
        elif equipment_set['Magic stuff'][Name] == "name":
            print(f""" Magic stuff: none
              0 mp
                    """)
        if equipment_set['Artifact'][Name] != "name":
            print(f""" Artifact: {equipment_set['Artifact'][Name]}
        +{equipment_set['Artifact'][playerSTR]} str
        +{equipment_set['Artifact'][playerDEF]} def
        +{equipment_set['Artifact'][playerHp]} hp
        +{equipment_set['Artifact'][playerMP]} mp
        """)
        elif equipment_set['Artifact'][Name] == "name":
            print(f""" Artifact: none
           0 str
           0 def
           0 hp
           0 mp
                    """)
        for i in range(len(self.myPlayer.inventory)):
            print(f"{number}.{self.myPlayer.inventory[i]}")
            number += 1

    def list_of_spells(self):
        for spell in self.myPlayer.spells:
            spell.show_details()

    def show_map(self):
        map_coordinates = [['1', '1', '1', '1', '1', '1', '1'],
                           ['1', 'c1', 'c2', 'c3', 'c4', 'c5', '1', 'd3'],
                           ['1', 'b1', 'b2', 'b3', 'b4', 'b5', '1', 'd2'],
                           ['1', 'a1', 'a2', 'a3', 'a4', 'a5', '1', 'd1'],
                           ['1', '1', '1', 'a0', '1', '1', '1'],
                           ['1', '1', '1', '1', '1', '1', '1']]
        for r_idx, row in enumerate(map_coordinates):
            for l_idx, loc in enumerate(row):
                if loc == self.myPlayer.location:
                    map_coordinates[r_idx][l_idx] = 'X'
                elif loc == '1':
                    map_coordinates[r_idx][l_idx] = '#'
                elif loc == 'd1':
                    map_coordinates[r_idx][l_idx] = '< District 1'
                elif loc == 'd2':
                    map_coordinates[r_idx][l_idx] = '< District 2'
                elif loc == 'd3':
                    map_coordinates[r_idx][l_idx] = '< District 3'
                else:
                    map_coordinates[r_idx][l_idx] = ' '
        for i in map_coordinates:
            print(i)

    @staticmethod
    def final_titles():
        print(""" 
        
        
        88888888888 888    888 8888888888      8888888888 888b    888 8888888b.  
            888     888    888 888             888        8888b   888 888  "Y88b 
            888     888    888 888             888        88888b  888 888    888 
            888     8888888888 8888888         8888888    888Y88b 888 888    888 
            888     888    888 888             888        888 Y88b888 888    888 
            888     888    888 888             888        888  Y88888 888    888 
            888     888    888 888             888        888   Y8888 888  .d88P 
            888     888    888 8888888888      8888888888 888    Y888 8888888P"  
                      
                      
            You defeated the evil wizard Elminstra, saved the princess. 
            You did it! You saved the kingdom!                                                   
                                               
            Made by: Poplavskyi Oleksandr 
                     sr-13                                                                                         

        """)
        sys.exit()

    def show_enemy_stats(self):
        print("\n Enemy name: ", self.myEnemy.name)
        print(" Enemy class: ", self.myEnemy.job)
        print(" HP: ", self.myEnemy.HP)
        print(" MP: ", self.myEnemy.MP)
        print(" Strength: ", self.myEnemy.STR)
        print(" Defense: ", self.myEnemy.maxDEF, "\n")

game = Game()


def flee():
    flee_chanse = random.randint(1, 4)
    if flee_chanse in range(1, 3):
        print(" Uciekasz z pola walki.")
    else:
        print("You managed to escape, but you stayed in the same location")
        main_game_loop()


##### Title Screen ####
def title_screen_selections():
    option = input("      > ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("load"):
        load_game()
    while option.lower() not in ['play', 'help', 'quit', 'load']:
        print("\n      Please enter a valid command\n")
        title_screen_selections()


def title_screen():
    os.system('cls')
    print(SYSTEM + """


  MMP""MM""YMM   MM                                                            mm        
  P'   MM   `7   MM                                                            MM          
       MM        MMpMMMb.   .gP"Ya       .P"Ybmmm `7Mb,od8  .gP"Ya   ,6"Yb.  mmMMmm         
       MM        MM    MM  ,M'   Yb     :MI  I8     MM' "' ,M'   Yb 8)   MM    MM           
       MM        MM    MM  8M''''''      WmmmP"     MM     8M''''''  ,pm9MM    MM           
       MM        MM    MM  YM.    ,     8M          MM     YM.    , 8M   MM    MM           
     .JMML.    .JMML  JMML. `Mbmmd'      YMMMMMb  .JMML.    `Mbmmd' `Moo9^Yo.  `Mbmo      


     `7MMF'     A     `7MF'         `7MM  `7MM                     `7MM      
       `MA     ,MA     ,V             MM    MM                       MM      
        VM:   ,VVM:   ,V    .gP"Ya    MM    MM   ,pW"Wq.   ,p6"bo    MM  ,MP'
         MM.  M' MM.  M'   ,M'   Yb   MM    MM  6W'   `Wb 6M'  OO    MM ;Y   
         `MM A'  `MM A'    8M''''''   MM    MM  8M     M8 8M         MM;Mm   
          :MM;    :MM;     YM.    ,   MM    MM  YA.   ,A9 YM.    ,   MM `Mb. 
           VF      VF       `Mbmmd' .JMML..JMML. `Ybmd9'   YMbmd'  .JMML. YA.


     """ + END)
    print("""
                          ###############################
                          ~~~ Welcome to the Text RPG ~~~
                          ###############################
                                      - Play - 
                                      - Load -         
                                      - Help -          
                                      - Quit -          
                          ###############################
                          ###############################
    """)
    title_screen_selections()


def help_menu():  # доделать
    print("")
    print("                         ", '#' * 45)
    print("                          Written by Poplavskyi Oleksandr")
    print("                          Version proto (1.0.1 oP)")
    print("                         ", "~" * 45)
    print("                          > Write 'move' or 'go' to move around the map")
    print("                          > Write 'inspect' or 'look' to view the location for the presence of the quest")
    print("\n")
    print("                          ? Find different quests on diferent locations")
    print("                          ? When you finnish the final quest, the game will finishes\n")
    print("                          ! Please ensure to type in lowercase for ease.\n")
    print("                         ", '#' * 45)
    print("\n")
    print("                          Please select an option to continue.")
    print("                         ", "#" * 45)
    print("                                            - Play -            ")
    print("                                            - Load -            ")
    print("                                            - Help -            ")
    print("                                            - Quit -            ")
    print("                         ", "#" * 45)
    print("                         ", "#" * 45)
    title_screen_selections()


def game_help(action):  # доделать
    print(""" 
    Your abilities:
    ~  write "look" or "inspect" to view the location for the presence of the quest
    ~  write "move" to move around the map
    ~  write "map" to see a map
    ~  write "purse" to se how much coins you have
    ~  write "inventory" to se what do you have
    ~  write "stats" to look at your current stats 
    ~  write "quit" to exit the game
    
    ! You can heal yourself writing 'heal', but it costs 9 mana points 
    Good luck , and have fun!   
    """)


#### PRINTING HERO STATS
def show_stats(action):
    print(" Heroes name: ", game.myPlayer.name)
    print(" Heroes class: ", game.myPlayer.job)
    print(" Heroes level: ", game.myPlayer.level)
    print(" HP: ", game.myPlayer.HP)
    print(" MP: ", game.myPlayer.MP)
    print(" Strength: ", game.myPlayer.STR)
    print(" Defense: ", game.myPlayer.maxDEF)
    print(" Spels: ")
    game.list_of_spells()


def purse_print():
    print(" You`ve had", game.myPlayer.cash, "coins. \n")


def player_examine(action):
    if game.zonemap[game.myPlayer.location][SOLVED]:
        print(" You have already exhausted this zone.")
    elif game.zonemap[game.myPlayer.location][ZONENAME] == 'Stronghold':
        shop()
    elif game.zonemap[game.myPlayer.location][ZONENAME] == 'Docks':
        print(" I have nothing to do here , i have to go up ")
    else:
        try:
            quest = getattr(game.quests, f'quest_{game.myPlayer.location}')
            quest()
        except:
            print(" You can trigger a quest here.")


def shop():
    print("\n - Jou`re in the shop -\n")
    print(" Hello stranger !\n I greet you in the guild shop\n ")
    print(" Here you can buy things which will upgrade your stats ! ")
    print(" This is the only such place in whole Wellock")
    print("""

            #######################################################
            ~~~~~~               Guild shop                  ~~~~~~
            #######################################################
            |                                                     |
            |  So, what would you like ?                          |
            |  1. Weapon - 50 coins                               |
            |  2. Armor - 50 coins                                |
            |  3. Magic stuff -50 coins                           |
            |  4. Artifact enhancing the spirit - 150 coins       |
            |                                                     |
            |  5. YOU: What is  that things ?                     |
            |  6. YOU: Ok, thanks maybe next time...              |
            |                                                     |
            #######################################################
            #######################################################\n""")
    answer = input(" > ")
    if game.myPlayer.cash >= 50:
        if answer == "1":
            weapons = ['Wooden sword', 'Iron sword of a knight', 'Stylish lightweight sword',
                       'The sword of the former general']
            game.myPlayer.cash -= 50
            buff = random.randrange(5, 20)
            equipment_set['Weapon'][Name] = random.choice(weapons)
            equipment_set['Weapon'][playerSTR] = buff
            game.myPlayer.maxDEF += equipment_set['Weapon'][playerDEF]
            game.myPlayer.STR += equipment_set['Weapon'][playerSTR]
            print(f" You've got: {equipment_set['Weapon'][Name]} And it will add you, {equipment_set['Weapon'][playerSTR]} strenght.")
        elif answer == "2":
            armor = ['Lether armor', 'Iron chain mail', 'Full iron armor', 'Armor of a fallen general']
            game.myPlayer.cash -= 50
            buff1 = random.randrange(5, 40)
            buff2 = random.randrange(5, 20)
            equipment_set['Armor'][Name] = random.choice(armor)
            equipment_set['Armor'][playerHp] = buff1
            equipment_set['Armor'][playerDEF] = buff2
            game.myPlayer.maxDEF += equipment_set['Armor'][playerDEF]
            game.myPlayer.maxHP += equipment_set['Armor'][playerHp]
            print(f" You've got: {equipment_set['Armor'][Name]} ; And it will add you, {equipment_set['Armor'][playerDEF]} defense and {equipment_set['Armor'][playerHp]} hp.")
        elif answer == "3":
            magic = ['The mana ring of the beast', "Midnight Demon's Bone Necklaces", ' ????????? ',
                     'The ring of the fallen general']
            game.myPlayer.cash -= 50
            buff = random.randrange(5, 40)
            equipment_set['Magic stuff'][Name] = random.choice(magic)
            equipment_set['Magic stuff'][playerMP] = buff
            print(f" You've got: {equipment_set['Magic stuff'][Name]} ; And it will add you, {equipment_set['Magic stuff'][playerMP]} mana points.")
        elif answer == "4":
            if game.myPlayer.cash >= 150:
                artifact = ['The bone of a colossal beast', "Midnight Demon's eye", ' The king grail', '']
                game.myPlayer.cash -= 150
                choise = random.randrange(1, 5)
                if choise == 1:
                    buff1 = random.randrange(15, 50)
                    buff2 = random.randrange(15, 50)
                    equipment_set['Artifact'][Name] = random.choice(artifact)
                    equipment_set['Artifact'][playerDEF] = buff1
                    equipment_set['Artifact'][playerHp] = buff2
                    game.myPlayer.maxDEF += equipment_set['Artifact'][playerDEF]
                    game.myPlayer.maxHP += equipment_set['Artifact'][playerHp]
                    print(f" You've got: {equipment_set['Artifact'][Name]} ; And it will add you, {equipment_set['Artifact'][playerDEF]} defense and {equipment_set['Artifact'][playerHp]} hp.")
                elif choise == 2:
                    buff1 = random.randrange(15, 50)
                    buff2 = random.randrange(15, 50)
                    equipment_set['Artifact'][Name] = random.choice(artifact)
                    equipment_set['Artifact'][playerDEF] = buff1
                    equipment_set['Artifact'][playerSTR] = buff2
                    game.myPlayer.maxDEF += equipment_set['Artifact'][playerDEF]
                    game.myPlayer.STR += equipment_set['Artifact'][playerSTR]
                    print(f" You've got: {equipment_set['Artifact'][Name]} ; And it will add you, {equipment_set['Artifact'][playerDEF]} defense and {equipment_set['Artifact'][playerSTR]} hp.")
                elif choise == 3:
                    buff1 = random.randrange(15, 50)
                    buff2 = random.randrange(15, 50)
                    equipment_set['Artifact'][Name] = random.choice(artifact)
                    equipment_set['Artifact'][playerDEF] = buff1
                    equipment_set['Artifact'][playerMP] = buff2
                    game.myPlayer.maxDEF += equipment_set['Artifact'][playerDEF]
                    game.myPlayer.maxMP += equipment_set['Artifact'][playerMP]
                    print(f" You've got: {equipment_set['Artifact'][Name]} ; And it will add you, {equipment_set['Artifact'][playerDEF]} defense and {equipment_set['Artifact'][playerMP]} hp.")
                elif choise == 4:
                    buff1 = random.randrange(15, 50)
                    buff2 = random.randrange(15, 50)
                    equipment_set['Artifact'][Name] = random.choice(artifact)
                    equipment_set['Artifact'][playerSTR] = buff1
                    equipment_set['Artifact'][playerHp] = buff2
                    game.myPlayer.STR += equipment_set['Artifact'][playerSTR]
                    game.myPlayer.maxHP += equipment_set['Artifact'][playerHp]
                    print(f" You've got: {equipment_set['Artifact'][Name]} ; And it will add you, {equipment_set['Artifact'][playerSTR]} defense and {equipment_set['Artifact'][playerHp]} hp.")
                elif choise == 5:
                    buff1 = random.randrange(15, 50)
                    buff2 = random.randrange(15, 50)
                    buff3 = random.randrange(15, 50)
                    equipment_set['Artifact'][Name] = random.choice(artifact)
                    equipment_set['Artifact'][playerSTR] = buff1
                    equipment_set['Artifact'][playerHp] = buff2
                    equipment_set['Artifact'][playerDEF] = buff3
                    game.myPlayer.STR += equipment_set['Artifact'][playerSTR]
                    game.myPlayer.maxHP += equipment_set['Artifact'][playerHp]
                    game.myPlayer.maxDEF += equipment_set['Artifact'][playerDEF]
                    print(f" You've got: {equipment_set['Artifact'][Name]} ; And it will add you, {equipment_set['Artifact'][playerSTR]} defense and {equipment_set['Artifact'][playerHp]} hp and {equipment_set['Artifact'][playerDEF]}.")
            else:
                print(" I'm sorry you don't have enough money")
        elif answer == "5":
            print("""  Guild Shop:
        ~  If you choose weapon you will get random weapon which will add you strength (5-20) and 4 defense
        ~  If you choose Armor you will get random armor which will add you defense (5-20) and (5-40) health
        ~  If you choose Magic stuff you will get random magic stuff which will add you mana points(5-40)
        ~  If you choose Artifact you will get random Artifact which will add points to your one random characteristic(It could be health also)
            """)
            shop()
        elif answer == "6":
            print(" Come when you want, stranger! ")
            main_game_loop()
    else:
        print(" I'm sorry you don't have enough money")
        main_game_loop()

###### GAME FUNCTIONALITY ######


def main_game_loop():
    while game.myPlayer.game_over is False:
        # game.myPlayer.__pass_time()
        prompt()

def prompt():
    print("\n" + " =======================")
    print(" What would you like to do?")
    print(" ! print 'help' to see abilities\n")
    action = input(" > ")
    acceptable_actions = ['move', 'travel', 'quit', 'inspect', 'interact', 'look', "stats", "help", "map", "purse",
                          "heal", 'inventory']
    while action.lower() not in acceptable_actions:
        print(" Unknown action, try again.\n")
        action = input(" > ")
    if action.lower() == 'quit':
        print(" Would you like to save the game Y/N?", "\n")
        ask = input(" > ")
        if ask.lower() == "y":
            with open('save_game.txt', 'wb') as save_file:
                pickle.dump((game.myPlayer, game.zonemap, game.equipment_set), save_file)
            sys.exit()
        elif ask.lower() == "n":
            print(" Okay, maybe next time!")
            sys.exit()
        else:
            print(" I don`t know such command please try again")
            print(" Would you like to save the game Y/N?", "\n")
            ask = input(" > ")
            if ask.lower() == "y":
                with open('save_game.txt', 'wb') as save_file:
                    pickle.dump((game.myPlayer, game.zonemap), save_file)
                sys.exit()
            elif ask.lower() == "n":
                print(" Okay, maybe next time!")
                sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        game.myPlayer.move()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() == "map":
        game.show_map()
    elif action.lower() == "purse":
        purse_print()
    elif action.lower() == "heal":
        game.myPlayer.heal()
    elif action.lower() == "stats":
        show_stats(action.lower())
    elif action.lower() == "help":
        game_help(action.lower())
    elif action.lower() == "inventory":
        game.inventory_print()


def load_game():
    os.system('cls')
    with open('save_game.txt', 'rb') as game_save:
        game_load = pickle.load(game_save)
    game.myPlayer = game_load[0]
    game.zonemap = game_load[1]
    game.equipment_set = game_load[2]
    main_game_loop()


def setup_game():
    os.system('cls')

    #### NAME COLLECTING
    game.cut_scene.dialog = YOU + "\n YOU: " + END + "Uhhhh...\n      What`s going on ?\n      Where am i... ?\n" + "\n"
    game.cut_scene.dialog_print01()
    game.cut_scene.dialog = SYSTEM + " SYSTEM: " + END + "Hello stranger, what`s your name?\n"
    game.cut_scene.dialog_print005()
    game.cut_scene.dialog = YOU + "\n YOU: " + END + "What`s my name ??\n      Hmm......\n"
    game.cut_scene.dialog_print01()

    player_name = input(" > ")
    game.myPlayer.name = player_name

    #### CLASS HANDLING
    game.cut_scene.dialog = "\n" + SYSTEM + " SYSTEM: " + END + "Hello, " + player_name + "! What`s class do you wanna to play?\n"
    game.cut_scene.dialog_print005()
    game.cut_scene.dialog = "         (You can play as a warrior, mage or ranger if you wanna show stats write help)\n"
    game.cut_scene.dialog_print005()

    player_class = input(" > ")
    valid_jobs = ['warrior', 'mage', 'ranger']
    if player_class.lower() in valid_jobs:
        game.myPlayer.job = player_class
        print(SYSTEM + " Initialization")
        game.cut_scene.dialog = (" .............\n" + END)
        game.cut_scene.dialog_print03()
        print("\n You now a " + player_class + "!\n")
    while player_class.lower() not in valid_jobs:
        if player_class.lower() == 'help':
            game.cut_scene.print_classes()
            player_class = input(" > ")
            if player_class.lower() in valid_jobs:
                game.myPlayer.job = player_class
                print(SYSTEM + " Initialization")
                game.cut_scene.dialog = (" .............\n" + END)
                game.cut_scene.dialog_print03()
                print("\n You now a " + player_class + "\n")
        else:
            print(" I don`t know such class....")
            player_class = input(" > ")
            if player_class.lower() in valid_jobs:
                game.myPlayer.job = player_class
                print(SYSTEM + " Initialization")
                game.cut_scene.dialog = (" .............\n" + END)
                game.cut_scene.dialog_print03()
                print("\n You now a " + player_class + "\n")

    ##### PLAYER STATS
    if game.myPlayer.job == 'warrior':
        game.myPlayer.maxHP = 160
        game.myPlayer.HP = 160
        game.myPlayer.maxMP = 25
        game.myPlayer.MP = 25
        game.myPlayer.STR = 45
        game.myPlayer.maxDEF = 15
        game.myPlayer.cash = 0
        game.myPlayer.xp = 500
        game.myPlayer.spells = [game.FireSword, game.blizzard]
    if game.myPlayer.job == 'mage':
        game.myPlayer.STR = 15
        game.myPlayer.maxHP = 70
        game.myPlayer.HP = 70
        game.myPlayer.maxMP = 120
        game.myPlayer.MP = 120
        game.myPlayer.maxDEF = 10
        game.myPlayer.maxDEF = 4
        game.myPlayer.cash = 0
        game.myPlayer.xp = 0
        game.myPlayer.spells = [game.fire, game.thunder, game.meteor, game.cure, game.cura, game.curaga]
    if game.myPlayer.job == 'ranger':
        game.myPlayer.STR = 70
        game.myPlayer.maxHP = 90
        game.myPlayer.HP = 90
        game.myPlayer.maxMP = 60
        game.myPlayer.MP = 60
        game.myPlayer.maxDEF = 6
        game.myPlayer.cash = 0
        game.myPlayer.xp = 0
        game.myPlayer.spells = [game.bloodKing, game.DarkDaggerTechnique]

    #### INTRODUCTION

    game.cut_scene.dialog = SYSTEM + "\n SYSTEM: " + END + "Welcome, " + player_name + " the " + player_class + "! " + "\n"
    game.cut_scene.dialog_print005()
    skip = input("\n\n\n To start playing press enter")
    if skip == 's':
        os.system('cls')
        game.myPlayer.cash += 10
        main_game_loop()
    os.system('cls')
    game.cut_scene.dialog = SYSTEM + """ 
\n Not far from you noticed an old man. 
 You think you can get some info from him. 
 Maybe you will know where you are and what is happening here\n\n""" + END
    print(game.cut_scene.dialog)

    game.cut_scene.dialog = NPC + " Old man: " + END + """Oh young man, you are in the kingdom of Wellock. 
          It consists of a total of 16 quarters, we are now in the Docks . 
          After the young princess is kidnapped by the great magician Elminster,
          the King is still looking for a brave hero who will save her from captivity
          Recently things are going very badly in this kingdom 
          A lot has happened this year, who knows what awaits us in the future ...     
"""
    game.cut_scene.dialog_print0025()
    input(" You > ")
    game.cut_scene.dialog = (
            "\n" + NPC + " Old man: " + END + "And remember, on the way between the quarters you can meet a lot of monsters or robbers.\n" + "\n")
    game.cut_scene.dialog_print0025()
    print(" ### The old man just disappeared ###\n")
    game.myPlayer.cash += 100
    print(SYSTEM + " ! You have found 10 coins" + END)
    game.cut_scene.dialog = (
        DANGER + " Strange voice: " + END, "Who knows, maybe the hero I've been waiting for so long is you... ",
        game.myPlayer.name, ", the ", game.myPlayer.job, "!\n")
    game.cut_scene.dialog_print0025()
    game.cut_scene.dialog = (SYSTEM + " System: " + END,
                             "Good luck, I hope you enjoy the gameplay\n         If you don't die soon...\n         Hehehe.....\n")
    game.cut_scene.dialog_print0025()
    input(" You > ")

    os.system('cls')
    print("")
    print(SYSTEM + " ###################################")
    print(" ####      Let`s start now!     ####")
    print(" ###################################" + END)
    main_game_loop()


if __name__ == '__main__':
    title_screen()
