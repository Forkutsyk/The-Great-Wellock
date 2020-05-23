# Pythin Text RPG
# Poplavskyi Oleksandr

import sys
import os
import time
from mage import Spell
from character import player, enemy
from diologs import dialogs
import pickle

#### Player Setup ####

myPlayer = player()
myEnemy = enemy()
### Create Black Magic
fire = Spell("Fire", 25, 60, 0, "black")
thunder = Spell("Thunder", 25, 60, 0, "black")
meteor = Spell("Meteor", 80, 120, 0, "black")
blizzard = Spell("Blizzard", 25, 50, 0, "black")
quake = Spell("Quake", 14, 35, 0,  "black")
### Create White Magic
cure = Spell("Cure", 25, 62, 0, "white")
cura = Spell("Cura", 32, 70, 0, "white")
curaga = Spell("Curaga", 50, 120, 0, "white")
### Create spels for wariore
FireSword = Spell("Fire Sword", 20, 35, 0, "fire")
HollyShield = Spell("Holly shield", 20, 0, 50, "holy")
### Create spells for ranger
DarkDaggerTechnique = Spell("Dark Dagger Technique", 20, 45, 0, "black")
bloodKing = Spell("Blood King", 50, 70, 0, "bloody")

cut_scene = dialogs()


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
     
     
     """+ END)
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



def help_menu(): # доделать
    print("")
    print('#' * 45)
    print(" Written by Poplavskyi Oleksandr")
    print(" Version proto (1.0.1 oP)")
    print("~" * 45)
    print(" > Write 'move' or 'go' to move around the map")
    print(" > Write 'inspect' or 'look' to view the location for the presence of the quest")
    print("\n")
    print(" ? Find different quests on diferent locations")
    print(" ? When you finnish the final quest, the game will finishes\n")
    print(" ! Please ensure to type in lowercase for ease.\n")
    print('#' * 45)
    print("\n")
    print(" Please select an option to continue.")
    print("#" * 45)
    print("                  - Play -            ")
    print("                  - Load -            ")
    print("                  - Help -            ")
    print("                  - Quit -            ")
    print("#" * 45)
    print("#" * 45)
    title_screen_selections()

def game_help(action):  # доделать
    print(""" 
    Your abilities:
    ~  write "move" or "go" to move around the map
    ~  write "inspect" or "look" to view the location for the presence of the quest
    ~  write "stats" to look at your current stats 
    ~  write "quit" to exit the game
    Good luck , and have fun!   
    """)
#### MAP ####
"""

_________________
|  |  |  |  |  |  3
_________________
|  |  |  |  |  |  2
_________________ 
|  |  |  |  |  |  1
_________________
----| Start |----
"""
ZONENAME = ''
DESCRIPTION = 'description'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }
zonemap = {
    'a0': {
        ZONENAME: 'Docks',
        DESCRIPTION: " The initial location is the main port of the kingdom of Wellock. You mysteriously appeared at this location. The port is most of the infrastructure of the kingdom.",
        SOLVED: False,
        UP: "a3",
        DOWN: "",
        LEFT: "",
        RIGHT: ""
    },
    'a3': {
        ZONENAME: 'House of a Thousand Faces',
        DESCRIPTION: "Area with taverns where you can eat and stay overnight. It is better not to walk here in the evening.",
        SOLVED: False,
        UP: "b3",
        DOWN: "a0",
        LEFT: "a2",
        RIGHT: "a4"
    },
    'a2': {
        ZONENAME: 'Sharandar',
        DESCRIPTION: "The ancient Feywild homeland of the Iliyanbruen elves.",
        SOLVED: False,
        UP: "b2",
        DOWN: "",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'a1': {
        ZONENAME: 'Stronghold',
        DESCRIPTION: "Area with castles of large guilds.",
        SOLVED: False,
        UP: "b1",
        DOWN: "",
        LEFT: "",
        RIGHT: "a2"
    },
    'a4': {
        ZONENAME: 'Dwarven Valley',
        DESCRIPTION: """Dwarven Valley, has been corrupted by dwarves from the Hammerstone dig up black ice, 
        and the long dead barbarians who once served Akar Kessell rise once more to wage war in the name of their undying master.""",
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: ""
    },
    'a5': {
        ZONENAME: 'Icespire Peak',
        DESCRIPTION: "The place of origin of black ice extracted by dwarves. Dangerous place, it seems that here can survive or very skilled heroes, or very stupid",
        SOLVED: False,
        UP: "b5",
        DOWN: "",
        LEFT: "a4",
        RIGHT: ""
    },
    'b1': {
        ZONENAME: 'Blacklake',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "с1",
        DOWN: "a1",
        LEFT: "",
        RIGHT: "b2"
    },
    'b2': {
        ZONENAME: 'Nezeris',
        DESCRIPTION: " ",
        SOLVED: False,
        UP: "c2",
        DOWN: "a2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'b3': {
        ZONENAME: 'Absol',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "c3",
        DOWN: "a3",
        LEFT: "b2",
        RIGHT: "b4"
    },
    'b4': {
        ZONENAME: 'Cardcaster',
        DESCRIPTION: "Cardcaster is built into the side of a mountain, and is known for having tough warriors. The ruler is fair and just, respected by the populace. ",
        SOLVED: False,
        UP: "c4",
        DOWN: "a4",
        LEFT: "b3",
        RIGHT: "b5"
    },
    'b5': {
        ZONENAME: 'Arahead',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "c5",
        DOWN: "a5",
        LEFT: "a4",
        RIGHT: ""
    },
    'c1': {
        ZONENAME: 'Wyllowwood',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2"
    },
    'c2': {
        ZONENAME: 'Brickell Whyte',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3"
    },
    'c3': {
        ZONENAME: 'The Well of Dragons ',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "c2",
        RIGHT: "c4"
    },
    'c4': {
        ZONENAME: 'The Yarlford',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "c3",
        RIGHT: "c5"
    },
    'c5': {
        ZONENAME: 'The final town',
        DESCRIPTION: "",
        SOLVED: False,
        UP: "",
        DOWN: "b5",
        LEFT: "c4",
        RIGHT: ""
    }
}


##### GAME INTERACTIVITY #####
def location_print():
    print('\n' + (" " + '#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))))
    print(" " + '# ' + zonemap[myPlayer.location][ZONENAME].upper() + ' #')
    print('\n' + (" " + '#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))))
    print('\n' + (zonemap[myPlayer.location][DESCRIPTION]))


#### PRINTING HERO STATS ####
def show_stats(action):
    print(" Heroes name: ", myPlayer.name)
    print(" Heroes class: ", myPlayer.job)
    print(" HP: ", myPlayer.maxHP)
    print(" MP: ", myPlayer.maxMP)
    print(" Strength: ", myPlayer.STR)
    print(" Spels: ")
    if myPlayer.job == "warrior":
        FireSword.show_details()
        blizzard.show_details()
        HollyShield.show_details()
    if myPlayer.job == "mage":
        fire.show_details()
        thunder.show_details()
        meteor.show_details()
        cure.show_details()
        cura.show_details()
        curaga.show_details()
    if myPlayer.job == "ranger":
        bloodKing.show_details()
        DarkDaggerTechnique.show_details()


def prompt():
    print("\n" + " =======================")
    print(" What would you like to do?")
    print(" ! print 'help' to see abilities\n")
    action = input(" > ")
    acceptable_actions = ['move', 'travel', 'quit', 'inspect', 'interact', 'look', "stats", "help","map"]
    while action.lower() not in acceptable_actions:
        print(" Unknown action, try again.\n")
        action = input(" > ")
    if action.lower() == 'quit':
        print(" Would you like to save the game Y/N?", "\n")
        ask = input(" > ")
        if ask.lower() == "y":
            saveGame = open('savegame.txt', 'wb')
            saveValues = (myPlayer.name, myPlayer.job, myPlayer.maxHP, myPlayer.maxMP, myPlayer.maxDEF, myPlayer.location, myPlayer.game_over, myPlayer.STR)
            pickle.dump(saveValues, saveGame)
            saveGame.close()
            sys.exit()
        elif ask.lower() == "n":
            print(" Okay, maybe next time!")
            sys.exit()
        else:
            print(" I dont know such komand please try again")
            ask = input(" Would you like to save the game Y/N?"+"\n").lower()
            if ask == "y":
                Save = player()
                pickle.dump(Save, open("save_game.dat", "wb"))
                sys.exit()
            elif ask == "n":
                print(" Okay, maybe next time!")
                sys.exit()
            else:
                sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() == "map":
        location_print()
    elif action.lower() == "stats":
        show_stats(action.lower())
    elif action.lower() == "help":
        game_help(action.lower())


def player_move(myAction):
    ask = " Where would you like to move to?\n"
    print(ask)
    dest = input(" ")
    if dest in ['up', 'west']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + " You have moved to the " + destination + ".")
    myPlayer.location = destination
    location_print()


def player_examine(action): # Доделать
    if zonemap[myPlayer.location][SOLVED]:
        print(" You have already exhausted this zone.")
    else:
        # i = int(random.randrange(1, 16))
        print(" You can trigger a quest here.")
       # if i == 1:
       #     print("""
       #              ~ You saw a strange young man. He wanna to say smth to you. But your ... frightens him.
       #              ~ Maybe you should say smth to him...
       #
       #              """)
       #       something = input("<")


###### GAME FUNCTIONALITY ######

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # here handle if quest have been solved, boss defeated, explored everything, etc.

YOU = '\x1b[1;34;40m'
SYSTEM = "\x1b[1;32;40m"
DANGER = "\x1b[1;31;40m"
NPC = "\x1b[1;36;40m"
END = '\x1b[0m'

def load_game():
    os.system('cls')
    loadGame = open('savegame.txt', 'rb')
    loadValues = pickle.load(loadGame)
    myPlayer.name = loadValues[0]
    myPlayer.job = loadValues[1]
    myPlayer.maxHP = loadValues[2]
    myPlayer.maxMP = loadValues[3]
    myPlayer.maxDEF = loadValues[4]
    myPlayer.location = loadValues[5]
    myPlayer.game_over = loadValues[6]
    myPlayer.STR = loadValues[7]
    loadGame.close()
    main_game_loop()


def setup_game():
    os.system('cls')

    #### NAME COLLECTING
    cut_scene.dialog = YOU + "\n YOU: " + END + "Uhhhh...\n      What`s going on ?\n      Where am i... ?\n" + "\n"
    cut_scene.dialog_print01()
    cut_scene.dialog = SYSTEM + " SYSTEM: " + END + "Hello stranger, what`s your name?\n"
    cut_scene.dialog_print005()
    cut_scene.dialog = YOU + "\n YOU: " + END + "What`s my name ??\n      Hmm......\n"
    cut_scene.dialog_print01()

    player_name = input(" > ")
    myPlayer.name = player_name

    #### CLASS HANDLING
    cut_scene.dialog = "\n" + SYSTEM + " SYSTEM: " + END + "Hello, " + player_name + "! What`s class do you wanna to play?\n"
    cut_scene.dialog_print005()
    cut_scene.dialog = "         (You can play as a warrior, mage or ranger)\n"
    cut_scene.dialog_print005()

    player_class = input(" > ")
    valid_jobs = ['warrior', 'mage', 'ranger']
    if player_class.lower() in valid_jobs:
        myPlayer.job = player_class
        print(SYSTEM + " Initialization")
        cut_scene.dialog = (" .............\n" + END)
        cut_scene.dialog_print03()
        print("\n You now a " + player_class + "!\n")
    while player_class.lower() not in valid_jobs:
        print(" I don`t know such class....")
        player_class = input(" > ")
        if player_class.lower() in valid_jobs:
            myPlayer.job = player_class
            print(SYSTEM + " Initialization")
            cut_scene.dialog = (" .............\n" + END)
            cut_scene.dialog_print03()
            print("\n You now a " + player_class + "\n")

    ##### PLAYER STATS
    if myPlayer.job == 'warrior':
        myPlayer.maxHP = 120
        myPlayer.maxMP = 20
        myPlayer.STR = 45
        myPlayer.maxDEF = 10
        myPlayer.spels = [FireSword, blizzard, HollyShield]
    if myPlayer.job == 'mage':
        myPlayer.STR = 15
        myPlayer.maxHP = 40
        myPlayer.maxMP = 120
        myPlayer.maxDEF = 10
        myPlayer.maxDEF = 4
        myPlayer.spels = [fire, thunder, meteor, cure, cura, curaga]
    if myPlayer.job == 'ranger':
        myPlayer.STR = 70
        myPlayer.maxHP = 60
        myPlayer.maxMP = 60
        myPlayer.maxDEF = 6
        myPlayer.spels = [bloodKing, DarkDaggerTechnique]

    #### INTRODUCTION

    cut_scene.dialog = SYSTEM + "\n SYSTEM: " + END + "Welcome, " + player_name + " the " + player_class + "! " + "\n"
    cut_scene.dialog_print005()

    input("\n\n\n To start playing press enter")
    os.system('cls')
    cut_scene.dialog = SYSTEM + """ 
\n Not far from you noticed an old man. 
 You think you can get some info from him. 
 Maybe you will know where you are and what is happening here\n\n""" + END
    print(cut_scene.dialog)

    cut_scene.dialog = NPC + " Old man: " + END +"""Oh young man, you are in the kingdom of Wellock. 
          It consists of a total of 16 quarters, we are now in the Blacklake quarter i. 
          After the young princess is kidnapped by the great magician Elminster,
          the King is still looking for a brave hero who will save her from captivity
          Recently things are going very badly in this kingdom 
          A lot has happened this year, who knows what awaits us in the future ...     
"""
    cut_scene.dialog_print0025()
    input(" You > ")
    cut_scene.dialog = ("\n"+NPC + " Old man: " + END +"And remember, on the way between the quarters you can meet a lot of monsters or robbers.\n" + "\n")
    cut_scene.dialog_print0025()
    print(" ### The old man just disappeared ###\n")
    cut_scene.dialog = (DANGER+ " Strange voice: " + END, "Who knows, maybe the hero I've been waiting for so long is you... ", myPlayer.name, ", the ", myPlayer.job, "!\n")
    cut_scene.dialog_print0025()
    cut_scene.dialog = (SYSTEM + " System: " + END, "Good luck, I hope you enjoy the gameplay\n         If you don't die soon...\n         Hehehe.....\n")
    cut_scene.dialog_print0025()
    input(" You > ")


    os.system('cls')
    print("")
    print(SYSTEM + " ###################################")
    print(" ####      Ley`s start now!     ####")
    print(" ###################################" + END)
    main_game_loop()


title_screen()
