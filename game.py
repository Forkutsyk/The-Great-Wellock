# Python Text RPG
# Poplavskyi Oleksandr

import sys
import os
from mage import Spell
from character import Player, Enemy
from diologs import dialogs
import pickle
import random
from global_variables import *
from quests import Quests


#### Player Setup ####
class Game:
    def __init__(self):
        self.myPlayer = Player(self)
        self.myEnemy = Enemy(self)
        self.quests = Quests(self)

    ### Create Black Magic
    fire = Spell("Fire", 25, 60, 0, "black")
    thunder = Spell("Thunder", 25, 60, 0, "black")
    meteor = Spell("Meteor", 80, 120, 0, "black")
    blizzard = Spell("Blizzard", 25, 50, 0, "black")
    quake = Spell("Quake", 14, 35, 0, "black")

    ### Create White Magic
    cure = Spell("Cure", 25, 62, 0, "white")
    cura = Spell("Cura", 32, 70, 0, "white")
    curaga = Spell("Curaga", 50, 120, 0, "white")

    ### Create spels for wariore
    FireSword = Spell("Fire Sword", 20, 35, 0, "fire")

    ### Create spells for ranger
    DarkDaggerTechnique = Spell("Dark Dagger Technique", 20, 45, 0, "black")
    bloodKing = Spell("Blood King", 50, 70, 0, "bloody")

    cut_scene = dialogs()

    def fight(self):
        show_enemy_stats()
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
                self.myPlayer.fight(self.myEnemy)
                if self.myEnemy.HP < 1:
                    self.myEnemy.die()
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
                    self.myPlayer.die()
                    break
                self.myPlayer.show()
            elif choice == "0":
                flee()
                break
            else:
                print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

    def location_print(self):
        print('\n' + (" " + '#' * (4 + len(zonemap[self.myPlayer.location][ZONENAME]))))
        print(" " + '# ' + zonemap[self.myPlayer.location][ZONENAME].upper() + ' #')
        print('\n' + (" " + '#' * (4 + len(zonemap[self.myPlayer.location][ZONENAME]))))
        print('\n' + (zonemap[self.myPlayer.location][DESCRIPTION]) + "\n")


    def show_map(self):
        map_coordinates = [['1', '1', '1', '1', '1', '1',  '1'],
                           ['1', 'c1', 'c2', 'c3', 'c4', 'c5', '1', 'd3'],
                           ['1', 'b1', 'b2', 'b3', 'b4', 'b5', '1', 'd2'],
                           ['1', 'a1', 'a2', 'a3', 'a4', 'a5', '1', 'd1'],
                           ['1', '1', '1', 'a0', '1', '1',   '1'],
                           ['1', '1', '1',  '1', '1', '1', '1']]
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


game = Game()


def flee():
    print(" Uciekasz z pola walki.")
    main_game_loop()


##### Title Screen ####
def title_screen_selections():
    option = input("      > ")
    if option.lower() == ("play"):
        setup_game()  # placeholder until written
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
    ~  write "move" or "go" to move around the map
    ~  write "map" to see a map
    ~  write "purse" to se how much coins you have
    ~  write "inspect" or "look" to view the location for the presence of the quest
    ~  write "stats" to look at your current stats 
    ~  write "quit" to exit the game
    Good luck , and have fun!   
    """)


#### PRINTING HERO STATS ####
def show_stats(action):
    print(" Heroes name: ", game.myPlayer.name)
    print(" Heroes class: ", game.myPlayer.job)
    print(" Heroes level: ", game.myPlayer.level)
    print(" HP: ", game.myPlayer.HP)
    print(" MP: ", game.myPlayer.MP)
    print(" Strength: ", game.myPlayer.STR)
    print(" Defense: ", game.myPlayer.maxDEF)
    print(" Spels: ")
    if game.myPlayer.job == "warrior":
        game.FireSword.show_details()
        game.blizzard.show_details()

    if game.myPlayer.job == "mage":
        game.fire.show_details()
        game.thunder.show_details()
        game.meteor.show_details()
        game.cure.show_details()
        game.cura.show_details()
        game.curaga.show_details()
    if game.myPlayer.job == "ranger":
        game.bloodKing.show_details()
        game.DarkDaggerTechnique.show_details()


def show_enemy_stats():
    print("\n Enemy name: ", game.myEnemy.name)
    print(" Enemy class: ", game.myEnemy.job)
    print(" HP: ", game.myEnemy.HP)
    print(" MP: ", game.myEnemy.MP)
    print(" Strength: ", game.myEnemy.STR)
    print(" Defense: ", game.myEnemy.maxDEF, "\n")


def purse_print():
    print(" You`ve had", game.myPlayer.cash, "coins. \n")


def prompt():
    print("\n" + " =======================")
    print(" What would you like to do?")
    print(" ! print 'help' to see abilities\n")
    action = input(" > ")
    acceptable_actions = ['move', 'travel', 'quit', 'inspect', 'interact', 'look', "stats", "help", "map", "purse", "heal"]
    while action.lower() not in acceptable_actions:
        print(" Unknown action, try again.\n")
        action = input(" > ")
    if action.lower() == 'quit':
        print(" Would you like to save the game Y/N?", "\n")
        ask = input(" > ")
        if ask.lower() == "y":
            saveGame = open('savegame.txt', 'wb')
            saveValues = (
            game.myPlayer.name, game.myPlayer.job, game.myPlayer.maxHP, game.myPlayer.maxMP, game.myPlayer.maxDEF,
            game.myPlayer.location, game.myPlayer.game_over, game.myPlayer.STR, game.myPlayer.xp, game.myPlayer.cash,
            game.myPlayer.HP, game.myPlayer.MP)
            pickle.dump(saveValues, saveGame)
            saveGame.close()
            sys.exit()
        elif ask.lower() == "n":
            print(" Okay, maybe next time!")
            sys.exit()
        else:
            print(" I dont know such command please try again")
            ask = input(" Would you like to save the game Y/N?" + "\n").lower()
            if ask == "y":
                Save = game.myPlayer
                pickle.dump(Save, open("save_game.dat", "wb"))
                sys.exit()
            elif ask == "n":
                print(" Okay, maybe next time!")
                sys.exit()
            else:
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


def player_examine(action):  # Доделать
    if zonemap[game.myPlayer.location][SOLVED]:
        print(" You have already exhausted this zone.")
    elif zonemap[game.myPlayer.location][ZONENAME] == 'Dwarven Valley':
        shop()
    else:
        try:
            quest = getattr(game.quests, f'quest_{game.myPlayer.location}')
            quest()
        except:
            print(" You can trigger a quest here.")


###### GAME FUNCTIONALITY ######

def main_game_loop():
    while game.myPlayer.game_over is False:
        prompt()


#### COLORED TEXT IN PROMPT
YOU = '\x1b[1;34;40m'
SYSTEM = "\x1b[1;32;40m"
DANGER = "\x1b[1;31;40m"
NPC = "\x1b[1;36;40m"
END = '\x1b[0m'

def shop():
    print(" - Jou`re in the shop -\n")
    input(" ")


def load_game():
    os.system('cls')
    with open('savegame.txt', 'rb') as game_save:
        load_values = pickle.load(game_save)
    game.myPlayer.name = load_values[0]
    game.myPlayer.job = load_values[1]
    game.myPlayer.maxHP = load_values[2]
    game.myPlayer.maxMP = load_values[3]
    game.myPlayer.maxDEF = load_values[4]
    game.myPlayer.location = load_values[5]
    game.myPlayer.game_over = load_values[6]
    game.myPlayer.STR = load_values[7]
    game.myPlayer.xp = load_values[8]
    game.myPlayer.cash = load_values[9]
    game.myPlayer.HP = load_values[10]
    game.myPlayer.MP = load_values[11]
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
    game.cut_scene.dialog = "         (You can play as a warrior, mage or ranger)\n"
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
        game.myPlayer.maxMP = 20
        game.myPlayer.MP = 20
        game.myPlayer.STR = 45
        game.myPlayer.maxDEF = 15
        game.myPlayer.cash = 0
        game.myPlayer.spels = [game.FireSword, game.blizzard]
    if game.myPlayer.job == 'mage':
        game.myPlayer.STR = 15
        game.myPlayer.maxHP = 70
        game.myPlayer.HP = 70
        game.myPlayer.maxMP = 120
        game.myPlayer.MP = 120
        game.myPlayer.maxDEF = 10
        game.myPlayer.maxDEF = 4
        game.myPlayer.cash = 0
        game.myPlayer.spels = [game.fire, game.thunder, game.meteor, game.cure, game.cura, game.curaga]
    if game.myPlayer.job == 'ranger':
        game.myPlayer.STR = 70
        game.myPlayer.maxHP = 90
        game.myPlayer.HP = 90
        game.myPlayer.maxMP = 60
        game.myPlayer.MP = 60
        game.myPlayer.maxDEF = 6
        game.myPlayer.cash = 0
        game.myPlayer.spels = [game.bloodKing, game.DarkDaggerTechnique]

    #### INTRODUCTION

    game.cut_scene.dialog = SYSTEM + "\n SYSTEM: " + END + "Welcome, " + player_name + " the " + player_class + "! " + "\n"
    game.cut_scene.dialog_print005()

    input("\n\n\n To start playing press enter")
    os.system('cls')
    game.cut_scene.dialog = SYSTEM + """ 
\n Not far from you noticed an old man. 
 You think you can get some info from him. 
 Maybe you will know where you are and what is happening here\n\n""" + END
    print(game.cut_scene.dialog)

    game.cut_scene.dialog = NPC + " Old man: " + END + """Oh young man, you are in the kingdom of Wellock. 
          It consists of a total of 16 quarters, we are now in the Blacklake quarter i. 
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
    game.myPlayer.cash += 10
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
    print(" ####      Ley`s start now!     ####")
    print(" ###################################" + END)
    main_game_loop()


if __name__ == '__main__':
    title_screen()
