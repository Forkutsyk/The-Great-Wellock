import os
import random
import sys
import time

roadswrongs = 1
sproby = 0


class Quests:
    def __init__(self, parent):
        self.parent = parent
        self.gold_quest_a4_1 = 0
        self.heal_use = 3
        self.knife_use = 2

    def quest_a2(self, response=None):
        if not response:
            self.parent.text.system("""\n  -  Sharandar - \n""", txt_only=True)
            if self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is False:
                self.parent.text.system("""  You can go to:\n   1. Old Sharandar Ruins\n   2. The Farthest Forest \n""", txt_only=True)
            elif self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
                self.parent.text.system("""  You can go to:\n   1. Old Sharandar Ruins\n   2. The Farthest Forest\n  3.Assistant home""",
                                        txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1' and self.parent.zonemap['a2']['SOLVED1'] is False:
            self.parent.text.system(text="""A stranger offers you to buy a lottery ticket.\n         If you win you will receive 25 coins. Are you interested?\n         The ticket costs 4 coins\n""")
            self.parent.text.system(" Choose one of the below answers\n  1. Yes\n  2. No\n", txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(text="I always win! Now, take my money and give me the lottery ticket\n")
                if self.parent.myPlayer.cash >= 4:
                    self.parent.myPlayer.cash -= 4
                    self.parent.myPlayer.xp += 5
                    result = random.randint(1, 6)
                    if result == 5:
                        self.parent.text.system(' YOU WON!!!\n')
                        self.parent.text.system(' YOU GOT 25 COINS PRIZE!!!\n')
                        self.parent.myPlayer.cash += 25
                        self.parent.myPlayer.xp += 100
                        self.parent.zonemap['a2']['SOLVED1'] = True
                        if self.parent.zonemap['a2']['SOLVED2'] is True:
                            self.parent.zonemap['a2']['SOLVED'] = True
                    else:
                        self.parent.text.system(f' YOUR NUMBER: {result}\n')
                        self.parent.text.danger(' YOU LOST!!!\n', begin_txt='SYSTEM')
                else:
                    self.parent.text.system(" You don't have enough money\n")
            elif response in ('no', '2'):
                self.parent.text.you(text="Maybe next time\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a2(response)
        elif response == '2' and self.parent.zonemap['a2']['SOLVED2'] is False:
            if 'Incredible medicine' not in self.parent.myPlayer.inventory:
                print("""                                                                                           
                                                                              ,///**///                                                                
                                                                       ./.     .,,....,,**//                                                          
                                                                    .*      ..........,.,,,,*//                                                       
                                                        ./,,.,,.,****     .........,.,,,,,,,,,,*(                                                     
                                                     /      ..,......,,**..........,,,,,,,,,.........,,****/((                                        
                                                   /      ........,,,,,,, .          .,,**/     .,..........,,**/(                                    
                                                  ..     .........,,,,                 ...,,,,**...........,,,,,,,*//(                                 
                                        .(((((*   ,     ...,  ....,,           ... .......,,,,,,,*,,,,,,,,,,,,,,,,,*///(                               
                                   (    .......,*,....,,,,***,,,,            .*##....,,,,,,,,,,*,*/***,,,,,,,,,,,,,////#                              
                                 (    ....,,,,             ...,,.        ...,,##,,,..,,,,..,,,,*,,*/*******,,,,,,,,/////#                             
                                *,. ..,,***.              ....,*..... ..,****##            .,,**  ...*///****,,,,,/(//(/(                             
                                ,,,,***///.           ........,       ,*****%(            ...,,,(//,,,,////****,//(((((/(                             
                                 (**/((((*,.    .........,,,         ,*,,,/%/         .......,,,,/((*,((*///*/(((((#((//#                             
                                   (*/((#***,,.,,,,,,,,,,,.        ,**,,,#%*,   ........,,,,,,,,,,(/((((((#(####(###(//#                              
                                       //**/***,,,,,,,,,,*.. ..,,**,**,%%****,.,,,,,,,,,,,,,,,,,/(//(#############(///                               
                                           **/*//(///******//********,,*##/**///*,,,,,,,,,,,,,,,*/(((#######%%%###(//(                                 
                                           ,*///////((((((//(///,,,**,#(///((/////***,,,,**///(((/##%%%%%%%####//#                                    
                                              /////(((((((((((***,,,*((((#%&&&&%%#(((((((((((((##(((###(////#,                                        
                                               .(   ,(###(* ******,*,**,,,**,,,#####%%%%%%%%%#//#                                                     
                                             #.    *      ,///**********,,,*.#    ,#(////(#(.(                                                        
                                          /#     .      ,///////////******.#              ((     ,                                                    
                                        #             /*/////*****/////*,#.    .       ,#     .                                                       
                                     *#            /.          .//////,#.    .       ##     (                                                         
                                                    ,/          .  /////*(,   *       *#     .                                                            
                                              (,          *   ////*(,   *       #(                                                                    
                                           /(          /    ,****(*  (       .#                                                                       
                                         #/                ****// ,(                                                                                  
                                      (#                  ,*,/# #                                                                                     
                                   #/                   ,,*#,/                                                                                       
                                (#                  ,,*##                                                                                          
                              #.                   ,*%                                                                                             
                                                 ,%                                                                                               
                                             .                    """)
                self.parent.text.system("""Suddenly an incredible storm began.From an unexpected storm, 
         you decided to hide under the roots of a giant elven tree.
         - Hmm what is it?
         You smelled roasted pork. After a short search, you noticed a small hut\n""")
                self.parent.text.system(
                    """What do you think what should you do\n         1. Wait till storm is ended in the forest.\n         2. Ask the owner of the hut, wait for the storm in him. \n""")
                player_choose1 = input(" > ")
                if player_choose1 == '1':
                    self.parent.text.system("You sat under the root all day only in the evening the storm subsided, you had to sleep in the woods ...and then continued their journey\n")
                elif player_choose1 == '2':
                    self.parent.text.system("""
        You knocked on the door of the hut, and a nice sweet lady opened it for you.
        You asked to wait for a thunderstorm in their hut. You have been invited to the table.
        You spent a lot of time talking with a young ladyAnd you find out that she lives with her sick father.
        They moved to this forest to find at least some medicine for her father, because he has unknown disease.
        In search of medicine for her father, she spent 3 years in this forest.
        She told you that she had found effective herbs against her father's illness, but she needed to 
        get to the spellshop in Wyllowwood. She invited you to stay the night. 
        And in the morning to continue my journey. In the morning she asked you for a favor: \n""", txt_only= True)
                    print("""
                    
        #######################################################
        ~~~~~~   !   Bring him back from that world      ~~~~~~
        #######################################################
        |                                                     |
        | Take the herbs to the spellstore in Wyllowwod       |
        | to be processed into an effective medicine          |
        | for her father                                      |  
        |                                                     |
        |  Reward:  60 coins + Assistant-healer               |
        |                                                     |
        #######################################################
        |     1.Accept             |           2.Decline      |
        #######################################################\n""")
                    player_choose2 = input(" > ")
                    if player_choose2 == '1':
                        self.parent.text.npc("This is great news, I will be incredibly grateful for the great hero.\n", begin_txt="Young lady")
                        self.parent.myPlayer.inventory.pop(0)
                        self.parent.myPlayer.inventory.insert(0, 'Elven herbs')
                        self.parent.text.system("You have successfully come out of the woods\n")
                    elif player_choose2 == '2':
                        self.parent.text.npc("Well, no problem, I'll go myself...\n", begin_txt="Young lady")
                        self.parent.text.system("You have one last chance to prove yourself as a man(1 or 2)\n")
                        player_choose3 = input(" > ")
                        if player_choose3 == "1":
                            self.parent.text.npc("This is great news, I will be incredibly grateful for the great hero.\n",
                                                 begin_txt="Young lady")
                            self.parent.myPlayer.inventory.pop(0)
                            self.parent.myPlayer.inventory.insert(0, 'Elven herbs')
                        elif player_choose3 == "2":
                            self.parent.text.system("You have successfully come out of the woods!\n")
                        else:
                            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                            self.quest_a2()
                    else:
                        print(" here problem")
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        self.quest_a2()
                else:
                    self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    self.quest_a2()
            elif 'Incredible medicine' in self.parent.myPlayer.inventory:
                self.parent.text.system(
                    """As you approached the hut you noticed that a young lady was watering flowers near the hut
         Seeing you, the girl immediately ran up to you\n""")
                self.parent.text.npc("Did you bring medicine ?!\n", begin_txt="Young lady")
                self.parent.text.you("Yes, of course\n")
                print("""
                
        #######################################################
        ~~~~~~   !   Bring him back from that world      ~~~~~~
        #######################################################
        |                                                     |
        | You brought the young lady the medicine she         |
        |  had asked for her father. He now start recovering. |
        |  You did a great job.                               |
        |                                                     |
        |              In reward you have got:                |
        #######################################################
        |      60 coins         +       Assistant-healer      |
        #######################################################\n""")
                self.parent.myPlayer.cash += 60
                self.parent.myPlayer.inventory.pop(0)
                self.parent.myPlayer.inventory.insert(0, '-')
                self.parent.zonemap['a2']['ASISTANT-HEALER'] = True
                self.parent.zonemap['a2']['SOLVED2'] = True
                if self.parent.zonemap['a2']['SOLVED1'] is True:
                    self.parent.zonemap['a2']['SOLVED'] = True
        elif response == '3' and self.parent.zonemap['a2']['SOLVED3'] is False and self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
            self.parent.text.system("""\n  -  Assistant abandoned home - \n""", txt_only=True)
            self.parent.text.you("So, do you remember where is it ?\n")
            self.parent.text.npc("Emmm, nope\n")
            self.parent.text.you("Ok, lets find it\n")
            tresure = False
            while tresure is not True:
                assistant_home = ['Bedroom', 'Back yard', 'Kitchen', 'Pantry']
                treasure_place = random.choice(assistant_home)
                self.parent.text.system("""  Where do you wanna to go?\n   1. Bedroom\n   2. Back yard\n  3. Kitchen\n  4. Pantry\n""",
                                        txt_only=True)
                treasure_search = input(" > ")
                Bedroom = False
                Back_yard = False
                Kitchen = False
                Pantry = False
                if treasure_search == "1" and Bedroom is False:
                    treasure_search1 = "Bedroom"
                    if treasure_search1 == treasure_place:
                        self.parent.text.npc("Yep, i found it!")
                        self.parent.text.you("Great !")
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        break
                    else:
                        Bedroom = True
                        self.parent.text.npc("Hmm, maybe in other place")
                elif treasure_search == "2" and Back_yard is False:
                    treasure_search2 = "Back yard"
                    if treasure_search2 == treasure_place:
                        self.parent.text.npc("Yep, i found it!")
                        self.parent.text.you("Great !")
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        break
                    else:
                        Back_yard = True
                        self.parent.text.npc("Hmm, maybe in other place")
                elif treasure_search == "3" and Kitchen is False:
                    treasure_search3 = "Kitchen"
                    if treasure_search3 == treasure_place:
                        self.parent.text.npc("Yep, i found it!")
                        self.parent.text.you("Great !")
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        break
                    else:
                        Kitchen = True
                        self.parent.text.npc("Hmm, maybe in other place")
                elif treasure_search == "4" and Pantry is False:
                    treasure_search4 = "Pantry"
                    if treasure_search4 == treasure_place:
                        self.parent.text.npc("Yep, i found it!")
                        self.parent.text.you("Great !")
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        break
                    else:
                        Pantry = True
                        self.parent.text.npc("Hmm, maybe in other place")
                else:
                    self.parent.text.you("We have seen here or wrong input")

        elif response == '3' and self.parent.zonemap['a2']['SOLVED3'] is True and self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
            self.parent.text.system(' You have already passed this quest, try to go somewhere else')
        elif response == '1' and self.parent.zonemap['a2']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the Forest')
        elif response == '2' and self.parent.zonemap['a2']['SOLVED2'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the Ruins')

    def quest_a3(self, response=None):
        if not response:
            self.parent.text.system("""\n  -  House of a Thousand Faces - \n""", txt_only=True)
            self.parent.text.system(""" You can go to:\n  1. Billie Jo Tavern\n  2. Local informant\n""", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1' and self.parent.zonemap['a3']['SOLVED1'] is False:
            self.parent.text.system(text=""" A pilgrim stops you in the street. He asks if you'll be travelling east anytime soon.\n          Also, he offers 10 coins for taking him with you\n""")
            print("""
            
        #######################################################
        ~~~~~~          !  Journey to the east           ~~~~~~
        #######################################################
        |                                                     |
        |    The pilgrim asked you to accompany him to east   |
        |                                                     |  
        |                                                     |
        |  Reward:  10 coins                                  |
        |                                                     |
        #######################################################
        |     1.Accept             |         2.Decline        |
        #######################################################\n
                                        """)
            response = input(" >  ")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(text="OK, let's go\n")
                self.parent.myPlayer.move('right')
                self.parent.myPlayer.cash += 10
                self.parent.myPlayer.xp += 50
                self.parent.text.npc(text=""" Here, take it! I suppose you will make good use of it!\n""", begin_txt='Pilgrim')
                print("""
                
        #######################################################
        ~~~~~~          !  Journey to the east           ~~~~~~
        #######################################################
        |                       DONE                          |
        |    The pilgrim asked you to accompany him to east   |
        |                                                     |  
        |                                                     |
        #######################################################
        |                    +10 coins                        |
        #######################################################\n
                                                    """)
                self.parent.text.system(text=""" The pilgrim gives you the promissed 10 coins!\n""")
                self.parent.zonemap['a3']['SOLVED1'] = True
                if self.parent.zonemap['a3']['SOLVED2'] is True:
                    self.parent.zonemap['a3']['SOLVED'] = True
            elif response in ('no', '2'):
                self.parent.text.you(text='Go away! I have more urgent business on my mind...\n')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a3(response)
        elif response == '1' and self.parent.zonemap['a3']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to Local informant')
        elif response == '2' and "Warrior medicine" not in self.parent.myPlayer.inventory and self.parent.zonemap['a3']['SOLVED2'] is False:
            self.parent.text.npc("Khe khe...\n")
            self.parent.text.system("You noticed a man lying on the ground\n")
            self.parent.text.system("Chose what do you wanna to do:\n         1. Come to help get up\n         2. Go past\n")
            help_stranger = input(" > ")
            if help_stranger == '1':
                self.parent.text.system("You help him get up and ask if something happened\n")
                self.parent.text.npc(
"""Oh no no, I'm sorry I used to be the same warrior as you,
           only in the recent battle I was very seriously wounded.
           colleagues threw me at will. And now I'm bleeding in these streets ... And I'm getting ready to die\n""")
                print("""
                
        #######################################################
        ~~~~~~    !   Give a hero a second chanse        ~~~~~~
        #######################################################
        |                                                     |
        | You met a warrior with a serious injury.            |
        | If you cure him he will be grateful to you          |
        | for the rest of his life                            |
        |                                                     |
        |  Reward: + Assistant-warrior                        |
        |                                                     |
        #######################################################
        |     1.Accept             |           2.Decline      |
        #######################################################\n""")
                save_a_hero = input(" > ")
                if save_a_hero == "1":
                    self.parent.text.you("We need to hurry until his condition not get worse\n")
                elif save_a_hero == "2":
                    self.parent.text.you("Meh...."
                                         "")
        elif response == '2' and "Warrior medicine" in self.parent.myPlayer.inventory and self.parent.zonemap['a3']['SOLVED2'] is False:
            self.parent.text.you("Thank God he is still alive\n")
            self.parent.text.system("You gave the warrior medicine, and they instantly healed his wounds\n")
            self.parent.myPlayer.inventory.pop(12)
            self.parent.myPlayer.inventory.insert(12, '-')
            self.parent.text.npc("I offer my life for my salvation.\n")
            print("""
            
        #######################################################
        ~~~~~~    !   Give a hero a second chanse        ~~~~~~
        #######################################################
        |                                                     |
        | You met a warrior with a serious injury.            |
        | If you cure him he will be grateful to you          |
        | for the rest of his life                            |
        |                                                     |
        |  For his rescuing he ofers you his life.            |
        |  He would helps you in battles                      |
        |                                                     |
        #######################################################
        |               +  Assistant-warrior                  |
        #######################################################\n""")

            self.parent.zonemap['a3']['ASISTANT-WARRIOR'] = True
            self.parent.zonemap['a3']['SOLVED2'] = True
            if self.parent.zonemap['a3']['SOLVED1'] is True:
                self.parent.zonemap['a3']['SOLVED'] = True
            self.parent.text.npc("Master, I have one question")
            print("""

                    #############################################################
                    ~~~~~~           !   Memories of the past              ~~~~~~
                    #############################################################
                    |                                                           |
                    | Before embarking on the path of a warrior, your assistant |
                    | went through a lot. And all things related to the past    |
                    | are hidden in the former house.                           |
                    |                                                           |
                    | The assistant asks you to go back there                   |   
                    | and pick up something                                     |
                    |                                                           |
                    |  Reward: You can take all the money that is there         |                                     
                    |                                                           |
                    #############################################################
                    |         1. Accept           |           2. Decline        |
                    #############################################################\n""")
            memories_of_past = input(" > ")
            if memories_of_past == "1":
                self.parent.text.you("Where is it ?")
                self.parent.text.npc("Not far from here, in the west. In the town Sharandar")
            elif memories_of_past == "2":
                self.parent.text.you("I`m sorry but no, we have to save the kingdom")
        elif response == '2' and self.parent.zonemap['a3']['SOLVED2'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to Billie Jo tavern\n')

    def quest_a4(self):
        def tavern():
            self.parent.text.system(
                """ You are very hungry, look into the tavern, so as not to die from starving\n          1. Go to tavern\n          2. Continue the journey\n""")
            starv_danger = input(" > ")
            if starv_danger == "1":
                print(' ')
                self.parent.text.system("You have found one tavern nearby\n")
            elif starv_danger == "2":
                self.parent.text.danger(""" - You've died from starvation -  \n""", begin_txt="SYSTEM")
                self.parent.text.system(" Reloading from the last checkpoint\n")
                self.parent.myPlayer.cash -= self.gold_quest_a4_1
                self.parent.zonemap['a4']['SOLVED1'] = False
                self.parent.text.system(" .................................\n", txt_only=True)
                os.system('cls')
                self.quest_a4()
            print(' ')
            self.parent.text.system(
                text=""" In a local tavern you spot a man wearing black cloak sitting in shady corner.\n          You approach him\n""")
            self.parent.text.npc(f" Hello {self.parent.myPlayer.name}\n", begin_txt='The Gamer')
            self.parent.text.you(" HHhow you know my name?!\n")
            self.parent.text.npc(f" Let's say... I know much...\n             For example I know you will lose a guessing game with me!\n", begin_txt='The Gamer')
            self.parent.text.you(" Wait a minute how to play the game ?\n")
            self.parent.text.npc(" It is very simple, I will guess a number between 1 and 42 and will have guess it in several tries\n", begin_txt='The Gamer')
            self.parent.text.you(" Sounds easy\n")
            self.parent.text.system(
                " Choose one of the below answers\n  1. Pfff. I can win with you. Let's play\n  2. I'm out.. Bye\n",
                txt_only=True)

            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.you("Pfff not possible. Let us have a quick round\n")
                tries = 5
                number = random.randint(1, 42)
                print(number)
                while True:
                    self.parent.text.npc("Guess a number between 1 and 42?\n", begin_txt='The Gamer')
                    your_guess = input(" >  ")
                    try:
                        your_guess = int(your_guess)
                    except:
                        continue
                    if your_guess == number:
                        self.parent.text.npc("Wow! You won!. Take your money and come back again\n", begin_txt='The Gamer')
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        self.parent.zonemap['a4']['SOLVED2'] = True
                        if self.parent.zonemap['a4']['SOLVED1'] is True:
                            self.parent.zonemap['a4']['SOLVED'] = True
                        self.parent.text.npc(
                            "And if you really want to defeat Elminster and save the princess, you need to increase the fighting force\n",
                            begin_txt='The Gamer')
                        self.parent.text.you(" Wwhat?!\n       How do you know it?!\n")
                        self.parent.text.you(" Hah well okay never mind, how can I do that?\n")
                        self.parent.text.npc(
                            "You can go to Stronghold and buy something in the guild shop or...\n            Go to the masters\n",
                            begin_txt='The Gamer')
                        self.parent.text.you("Masters?\n")
                        self.parent.text.npc(
                            "Yep, there are mage master Who lives somewhere in Nezeris\n            and another warrior master which lives somewhere in Blacklake\n            That's all what can I say\n",
                            begin_txt='The Gamer')
                        return
                    elif your_guess > number:
                        self.parent.text.npc("Nope, the number is too big\n", begin_txt='The Gamer')
                    elif your_guess < number:
                        self.parent.text.npc("No, the number is too small\n", begin_txt='The Gamer')
                        tries -= 1
                    if tries == 0:
                        self.parent.text.npc(f"It is too late {self.parent.myPlayer.name}. You lost the game\n", begin_txt='The Gamer')
                        return
                self.parent.text.system("You ate quietly. And then continued your journey\n")
                return
            elif response == '2':
                self.parent.text.you(" If you say so.. Bye\n")
                self.parent.myPlayer.xp += 30
                self.parent.text.system("You ate quietly. And then continued your journey\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                if self.parent.zonemap['a4']['SOLVED2'] is not True:
                    tavern()

        if self.parent.zonemap['a4']['SOLVED1'] is True and self.parent.zonemap['a4']['SOLVED2'] is False:
            tavern()

        if self.parent.zonemap['a4']['SOLVED1'] is False:
            print("")
            self.parent.text.system(text=""" While having a walk through the little town you find on ground a unique and strange golden ring.\n          You think that someone had to lose it here\n          What do you want to do with it?\n""")
            self.parent.text.system(" Choose one of the below answers\n  1. Go to mayor's mansion to leave it there\n  2. Leave it on the ground\n  3. Take it with you\n", txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                print(' ')
                self.parent.text.system(" You turn to a broad street leading to Mayor Habakuk's mansion\n")
                self.parent.text.npc(" Welcome traveller, what brings you to my town?\n", begin_txt='Habakuk')
                self.parent.text.you(" Good afternoon Sir! I found this ring nearby. I thought that you might know who is the owner of it\n")
                self.parent.text.npc(" Oh! Thank you very much. This belongs to my beloved daughter!\n", begin_txt='Habakuk')
                self.parent.text.npc(" Take this small gift as a 'thank you' from me.\n", begin_txt='Habakuk')
                self.parent.text.you(" Thank you\n")
                self.parent.text.system(" You receive 100 coins\n")
                self.parent.myPlayer.cash += 100
                self.gold_quest_a4_1 = 100
                self.parent.myPlayer.xp += 150
                self.parent.zonemap['a4']['SOLVED1'] = True
                tavern()
            elif response == '2':
                print(' ')
                self.parent.text.you(" Hmmm, I better leave it where it is so the one who lost it can find it\n")
                self.parent.myPlayer.xp += 30
                self.parent.zonemap['a4']['SOLVED1'] = True
                tavern()
            elif response == '3':
                print(' ')
                self.parent.text.you(" What a lucky day! GOLD!\n")
                self.parent.text.system(" You receive 150 coins\n")
                self.parent.myPlayer.cash += 150
                self.gold_quest_a4_1 = 150
                self.parent.myPlayer.xp += 10
                self.parent.zonemap['a4']['SOLVED1'] = True
                tavern()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a4()

    def quest_a5(self):
        print(' ')
        self.parent.text.system(
            text=""" - Welcome to Icespire Peak -\n""")
        self.parent.text.system(""" You can go to:\n  1.Stable\n  2.Black ice mines\n""",txt_only=True)
        answer = input(" > ")
        print(" ")

        #### Stable quest
        if answer == '1' and self.parent.zonemap['a5']['SOLVED1'] is False:
            self.parent.text.npc(""" An owner of the stable says: he's heard strange singing in the night in his stable, but whenever he goes out to look, he doesn't find anyone.\n         If that wasn't strange enough, one morning he found scarecrows which was in a drawn circle on the porch""", begin_txt='Owner')
            print("""
            
        #######################################################
        ~~~~~~       !  The mystery of the stable        ~~~~~~
        #######################################################
        |                                                     |
        | Help owner find out what's going on in the stable   |
        |                                                     |  
        |                                                     |
        |  Reward:  ????????                                  |
        |                                                     |
        #######################################################
        |     1.Accept             |         2.Decline        |
        #######################################################\n""")
            response = input(" > ")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(" * going to the stable * \n")
                self.parent.text.system(""" In the stable you found 3 things that can be associated with the dark cult:
           1. A dark substance that is mostly used by the dark cult in rituals
           2. Pieces of dark ice - used by the dark cult in rituals
           3. A piece of anarchist cloth - which is used by the dark cult to sew their clothes
           What will you show the owner to persuade him to turn to the royal guard ?
           (you have 1 attempt)\n """)
                choise = input(" > ")
                if choise == "1":
                    self.parent.text.npc(" Hmm ... this substance is also used in mines. This is not a reason to contact with the royal guard.\n", begin_txt='Owner')
                    self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                elif choise == "2":
                    self.parent.text.npc("You're kidding, we're on Dwarven Valley, dark ice is everywhere!\n        Get out of here !\n", begin_txt='Owner')
                    self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                elif choise == "3":
                    self.parent.text.npc("Did you find it in the stable?!?! I will immediately notify the royal guards.\n        Thank you very much hero\n        Here is your reward\n", begin_txt='Owner')
                    print("""
        #######################################################
        ~~~~~~       !  The mystery of the stable        ~~~~~~
        #######################################################
        |                      DONE                           |
        | Most likely, the dark cult uses its territory       |
        | as a gathering place. You did a great job!          |  
        |                                                     |
        |                                                     |
        #######################################################
        |                    +20 coins                        |
        #######################################################\n""")
                    self.parent.text.system(' Greeting you have got 50 xp, 20 coins\n')
                    self.parent.myPlayer.cash += 20
                    self.parent.myPlayer.xp += 50
                    self.parent.zonemap['a5']['SOLVED1'] = True
                    if self.parent.zonemap['a5']['SOLVED2'] is True:
                        self.parent.zonemap['a5']['SOLVED'] = True

                elif response in ('no', '2'):
                    self.parent.text.system(""" You tell the owner to go away as you have more urgent business on your mind""")
                else:

                    self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    self.quest_a5()

        ### Mine quest
        elif answer == "2" and self.parent.zonemap['a5']['SOLVED2'] is False:
            self.parent.text.system(" You met a dwarf!\n")
            self.parent.text.npc(" The dwarf said he had a job for you\n         You look strong, could you help me with this mechanism? \n         You just need to hold on to this lever.But hold on tight, if you drop it, I will have to look for someone stronger.\n ", begin_txt='Dwarf')
            response = input(""" Could you help him ?\n   1. Yes, I will take you there\n   2. No\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                tryies = 3
                while tryies != 0:
                    result = random.randint(1, 6)
                    self.parent.myPlayer.xp += 5
                    if result == 5:
                        self.parent.text.system('You were strong enough to hold the lever!\n')
                        self.parent.text.system('Dwarf give you your reward\n')
                        self.parent.text.system('Greeting you have got 100 xp, 25 coins\n')
                        self.parent.myPlayer.cash += 25
                        self.parent.myPlayer.xp += 100
                        self.parent.zonemap['a5']['SOLVED2'] = True
                        if self.parent.zonemap['a5']['SOLVED1'] is True:
                            self.parent.zonemap['a5']['SOLVED'] = True
                        break
                    else:
                        self.parent.text.danger(' You`ve failed!\n', begin_txt='SYSTEM')
                        tryies -= 1
                        if tryies != 0:
                            self.parent.text.system("Dwarf wanna try again. What did you say? (write 'yes' or 'no')\n")
                            sugestion = input(' > ')
                            if sugestion == "yes":
                                self.parent.text.you("Yep lets go\n")
                            elif sugestion == "no":
                                self.parent.text.npc("Well, thank you for trying\n", begin_txt="Dwarf")
                                break
                            else:
                                self.parent.text.npc("Well, thank you for trying\n", begin_txt="Dwarf")
                                break
                        if tryies == 0:
                            self.parent.text.system("Maybe next time!\n")

            elif response in ('no', '2'):
                self.parent.text.you(text="Maybe next time\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a5()
        elif answer == "1" and self.parent.zonemap['a5']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the mine')
        elif answer == "2" and self.parent.zonemap['a5']['SOLVED2'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the stable')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a5()

    def quest_b1(self):
        def desert_quest():
            self.parent.text.system("""\n  - Desert of despair  - \n""", txt_only=True)
            self.parent.text.system("""After a long journey, you decided to rest under a withered tree\n""")
            self.parent.text.you("WHAT ?!\n")
            self.parent.text.danger("""Suddenly, you begin falling into the sand\n""", begin_txt='SYSTEM')
            self.parent.text.system("You must try to pull yourself to the tree with the help of magic\n")
            self.parent.text.system(" Press enter till you do not pull out yourself\n", txt_only=True)
            player_tryies = 0
            awailble_pulls = random.randint(1, 10)
            while player_tryies != awailble_pulls:
                input(" > ")
                player_tryies += 1
            self.parent.text.you("Heh where did this old man send me?\n")
            self.parent.text.you("There is literally nothing here...\n")
            self.parent.text.you("I'd better go back to him and tell him everything I think about him\n")
        def waterfall_quest():
            self.parent.text.system("""\n  - Waterfall of life and death  - \n""", txt_only=True)
            self.parent.text.system(text=""" Try to look out, maybe you find something interesting...(write look)\n""")
            input(" > ")
            self.parent.text.system(text=""" You noticed an unusual glow behind the waterfall. 
          Most likely there is something behind the waterfall,
          however ... It is a waterfall of life and death, if I will enter the water I can die. What should i do ?\n""")

            self.parent.text.system(text="""\n  1. Just go through the waterfall, maybe I would be lucky\n  2. Cover yourself with your light cloak, and hope for the best\n  3. Stop and think more\n""",
                txt_only=True)
            player_choose4 = input(" > ")
            if player_choose4 == "1":
                chanse_to_die = random.randint(1, 2)
                if chanse_to_die == 1:
                    self.parent.text.danger(' Luck is not on your side, you died just by going into the water\n',begin_txt='SYSTEM')
                    self.parent.text.system(" Reloading from the last checkpoint\n")
                    self.parent.text.system(" .................................\n", txt_only=True)
                    os.system('cls')
                    self.quest_b1()
                else:
                    self.parent.text.system(""" luck on your side, you went through the waterfall without consequences\n""",txt_only=True)
                    self.parent.text.system("Behind the waterfall was a cave it was incredibly dark there, but there were 3 swords that shone slightly\n")
                    self.parent.text.system(
                        text=""" Wich one you wanna take ?\n  1. Sword inlaid with gems\n  2. Incredibly light and sharp one-handed sword\n  3. Rusty iron sword\n""",
                        txt_only=True)
                    player_choose5 = input(" > ")
                    if player_choose5 in ['1', '2']:
                        self.parent.text.system(text=""" You have taken the knife and went to the master""")
                        self.parent.text.npc(
                            text=""" You are very inattentive, I will not help you and leave this trinket to yourself, it is a useless thing.\n""",
                            begin_txt='Old warrior')
                    elif player_choose5 == "3":
                        self.parent.text.system(text=""" You have taken the knife and went to the master\n""")
                        self.parent.text.npc(text=""" Very well, either you listened to me well, or you have a pure spirit.
                        Unfortunately, I can do little to help you. However, this sword will definitely help you.
                        Yes, maybe he looks like an ordinary rusty sword. However, this sword is cursed, it will help you cope with an incredible amount of light opponents.
                        This rust is the blood of the dead from this sword, which because of the curses cannot be washed away.
                        I also will show you how to increse you endurance.\n""",
                                             begin_txt='Old warrior')
                        self.parent.myPlayer.maxHP += 30
                        self.parent.myPlayer.xp += 50
                        self.parent.text.system(
                            """After a whole day of hard training, you managed to increase your HP for 30, and learnd how to use the Abyssal sword""",
                            txt_only=True)
                        self.parent.zonemap['b1']['SOLVED'] = True
                    else:
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        self.quest_b1()
            elif player_choose4 == "2":
                self.parent.text.danger(' It was a terrible plan, you died just by going into the water\n',begin_txt='SYSTEM')
                self.parent.text.system(" Reloading from the last ceckpoint\n")
                self.parent.text.system(" .................................\n", txt_only=True)
                os.system('cls')
                self.quest_b1()
            elif player_choose4 == "3":
                self.parent.text.system(text=""" After a long search you found nothing\n""")
                time.sleep(3)
                self.parent.text.system(text=""" You wanted to go back, but noticed a small gorge    
          You decide to go in and see what's inside
          Behind the waterfall was a cave it was incredibly dark there, but there were 3 swords that shone slightly\n""")
                self.parent.text.you(" Which of them is the one I need, the old man almost did not describe it...\n")
                self.parent.text.system(text=""" Wich one you wanna take ?\n  1. Sword inlaid with gems\n  2. Incredibly light and sharp one-handed sword\n  3. Rusty iron sword\n""", txt_only=True)
                player_choose5 = input(" > ")
                if player_choose5 in ['1', '2']:
                    self.parent.text.system(text=""" You have taken the knife and went to the master\n""")
                    self.parent.text.npc(text=""" You are very inattentive, I will not help you and leave this trinket to yourself, it is a useless thing.\n""", begin_txt='Old warrior')
                elif player_choose5 == "3":
                    self.parent.text.system(text=""" You have taken the knife and went to the master\n""")
                    self.parent.text.npc(text=""" Very well, either you listened to me well, or you have a pure spirit.
               Unfortunately, I can do little to help you. However, this sword will definitely help you.
               Yes, maybe he looks like an ordinary rusty sword. However, this sword is cursed, it will help you cope with an incredible amount of light opponents.
               This rust is the blood of the dead from this sword, which because of the curses cannot be washed away.
               I also will show you how to increse you endurance.\n""", begin_txt='Old warrior')
                    self.parent.myPlayer.inventory.pop(4)
                    self.parent.myPlayer.inventory.insert(4, "Abyssal sword")
                    self.parent.myPlayer.maxHP += 30
                    self.parent.myPlayer.xp += 50
                    self.parent.text.system(""" After a whole day of hard training, you managed to increase your HP for 30, and learnd how to use the Abyssal sword\n""", txt_only=True)
                    self.parent.zonemap['b1']['SOLVED'] = True
                else:
                    self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    self.quest_b1()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b1()

        self.parent.text.system(text=""" In tavern you see an old man with long beard\n""")
        self.parent.text.npc(text="""My name is Tetrex. What do you want ?\n""", begin_txt='Old warrior')
        self.parent.text.you(text=f"Hello, I am {self.parent.myPlayer.name} I've met one guy he said that you can help me become stronger\n")
        self.parent.text.npc(text=""" Hmm interesting...But first you have to prove to me that you are worthy of my time\n""", begin_txt='Old warrior')
        self.parent.text.system(text=""" What will you answer the old warrior\n           1. I'm ready for anything to defeat Elminster\n           2. Quest? again ? Meeeh\n           3. Ignoring to drink the beer of the old master\n""")
        player_choose1 = input(" > ")

        if player_choose1 == "1":
            self.parent.text.npc(text=""" Very good young man, You had to bring me the Abyssal sword...\n""", begin_txt='Old warrior')
            self.parent.text.you(text="Okay, and where is he?\n")
            self.parent.text.npc(text=""" I don`t know... try to search in the desert of despair\n""", begin_txt='Old warrior')
            self.parent.text.system(text=""" So you will go to the desert of despair?\n           1. Yep\n           2. Nope, i will not go anywhere. I will not be completed this quest ...\n""")
            player_choose2 = input(" > ")
            if player_choose2 == "1":
                desert_quest()
                print(" ")
                self.parent.text.you("There is literally nothing there...only a lot of quicksands \n")
                self.parent.text.npc(text=""" Hmm , in general there at least two more places where it is possible to find this sword\n""",
                    begin_txt='Old warrior')
                self.parent.text.system(
                    text="""\n  1.Swamp of walking snakes\n  2.Waterfall of life and death \n""", txt_only=True)
                bad_road = input(" > ")
                if bad_road == "1":
                    self.parent.snakes_fight()
                    self.parent.text.you("Okay, there's only one place left\n")
                    waterfall_quest()
                elif bad_road == "2":
                    waterfall_quest()
            elif player_choose2 == "2":
                self.parent.text.npc(text=""" Alright, alright I'm just kidding....It is known only two places where it can be\n""", begin_txt='Old warrior')
                self.parent.text.system(text="""\n  1.Swamp of walking snakes\n  2.Waterfall of life and death \n""", txt_only=True)
                player_choose3 = input(" > ")
                if player_choose3 == "1":
                    self.parent.snakes_fight()
                    self.parent.text.you("Okay, there's only one place left\n")
                    waterfall_quest()
                elif player_choose3 == "2":
                    waterfall_quest()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b1()
        elif player_choose1 == "2":
            self.parent.text.npc(text=""" Well, it's your choice\n""", begin_txt='Old warrior')
        elif player_choose1 == "3":
            self.parent.master_fight()
            self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            self.quest_b1()
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_b1()

    def quest_b2(self, response=None):
        def tasks():
            self.parent.text.npc(text="""First I want to check your stock of mana\n""", begin_txt='Gandalfux')
            self.parent.text.npc(text="""You have to use mana to stop these knives that I will throw at you\n""",
                                 begin_txt='Gandalfux')
            mana_perfect = 0

            if 10 < self.parent.myPlayer.maxMP < 25:
                self.parent.text.npc(
                    text="""You have small stock of mana, if you fail next task I'll kick you out of here \n""",
                    begin_txt='Gandalfux')
                mana_perfect = 1
            elif 25 < self.parent.myPlayer.maxMP < 80:
                mana_perfect = 2
                self.parent.text.npc(text="""You have midle stock of mana, hmm.... \n""", begin_txt='Gandalfux')
            elif 80 < self.parent.myPlayer.maxMP < 200:
                self.parent.text.npc(text="""You have large stock of mana, very good, сommendable ! \n""",
                                     begin_txt='Gandalfux')
                mana_perfect = 3
            elif self.parent.myPlayer.maxMP > 200:
                mana_perfect = 4
                self.parent.text.npc(text="""Whaaat, i cant see the end of your stock. You are a real genius\n""",
                                     begin_txt='Gandalfux')

            i = 0
            thrown_knifes = random.randint(2, 8)
            failed = int((thrown_knifes/2)+2)
            catch_chanse = 0
            print(thrown_knifes)
            print(failed)
            self.parent.text.system(
                """Press ENTER to catch the knife! Press as fast as you can , or you won't catch a knife\n""")
            while i != thrown_knifes:
                print(" Catch")
                if mana_perfect == 1:
                    catch_chanse = 25
                elif mana_perfect == 2:
                    catch_chanse = 50
                elif mana_perfect == 3:
                    catch_chanse = 75
                elif mana_perfect == 4:
                    catch_chanse = 120
                exit = input(" > ")
                if exit == "exit":
                    self.quest_b2()
                if failed != 0:
                    if catch_chanse < 26:
                        y = random.randint(1, 4)
                        if y == 1:
                            print(" You catch knife")
                            i += 1
                            print(i)
                        else:
                            print("You didn`t catch")
                            failed -= 1
                            print(failed)
                    elif 25 < catch_chanse <= 50:
                        y = random.randint(1, 4)
                        if y in [1, 4]:
                            print(" You catch knife")
                            i += 1
                            print(i)
                        else:
                            print("You didn`t catch")
                            failed -= 1
                            print(failed)
                    elif 50 < catch_chanse <= 75:
                        y = random.randint(1, 4)
                        if y in [1, 2, 3]:
                            print(" You catch knife")
                            i += 1
                            print(i)
                        else:
                            print("You didnt catch")
                            failed -= 1
                            print(failed)
                    elif 75 < catch_chanse <= 130:
                        print(" You catch knife")
                        i += 1
                elif failed == 0:
                    self.parent.text.npc(text="""You failed\n""",
                                         begin_txt='Gandalfux')
                    self.quest_b2(response)
                    break
            if failed != 0:
                self.parent.text.npc(text="""Yo worked well. And now the last task!\n""", begin_txt='Gandalfux')
                self.parent.text.npc(text="""I want to test your courage and strength of spirit\n""", begin_txt='Gandalfux')
                self.parent.text.npc(text="""I will give you my staff, so you must pour your mana into it. And now  cross this homeless gorge. 
            Don't worry the levitation spell, I'll tell you, you just have to repeat me word for word.\n""",
                                     begin_txt='Gandalfux')
                self.parent.text.npc(text="""Ready ?\n""", begin_txt='Gandalfux')
                input(" > ")

                self.parent.text.you(text="""Ok lets start\n""")
                self.parent.text.npc(text="""Gaudeamus igitur\n""", begin_txt='Gandalfux')
                spell_1 = False
                spell_2 = False
                spell_3 = False
                spell_4 = False
                lev_spell_1 = input(" > ").lower()
                if lev_spell_1 != "gaudeamus igitur":
                    self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
                    self.parent.text.system(" Reloading from the last ceckpoint\n")
                    self.parent.text.system(" .................................\n", txt_only=True)
                    os.system('cls')
                    self.quest_b2()
                elif lev_spell_1 == "gaudeamus igitur":
                    self.parent.text.npc(text="""Juvenes dum sumus\n""", begin_txt='Gandalfux')
                    lev_spell_2 = input(" > ").lower()
                    if lev_spell_2 != "juvenes dum sumus":
                        self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
                        self.parent.text.system(" Reloading from the last ceckpoint\n")
                        self.parent.text.system(" .................................\n", txt_only=True)
                        os.system('cls')
                        self.quest_b2()
                    elif lev_spell_2 == "juvenes dum sumus":
                        self.parent.text.npc(text="""Post jucundam juventutem\n""", begin_txt='Gandalfux')
                        lev_spell_3 = input(" > ").lower()
                        if lev_spell_3 != "post jucundam juventutem":
                            self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
                            self.parent.text.system(" Reloading from the last ceckpoint\n")
                            self.parent.text.system(" .................................\n", txt_only=True)
                            os.system('cls')
                            self.quest_b2()
                        elif lev_spell_3 == "post jucundam juventutem":
                            self.parent.text.npc(text="""Nos habebit humus\n""", begin_txt='Gandalfux')
                            lev_spell_4 = input(" > ").lower()
                            if lev_spell_4 != "nos habebit humus":
                                self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
                                self.parent.text.system(" Reloading from the last ceckpoint\n")
                                self.parent.text.system(" .................................\n", txt_only=True)
                                os.system('cls')
                                self.quest_b2()
                            elif lev_spell_4 == "nos habebit humus":
                                self.parent.text.you(text="You step on the other end of the abyss\n")
                                self.parent.text.npc(text="""You worked well. I think you're good enough to be my student!\n""",
                                                     begin_txt='Gandalfux')
                                self.parent.zonemap['a2']['SOLVED1'] = True

        if not response:
            self.parent.text.system(text=""" Close to a castle you meet a mage\n""")
            self.parent.text.npc(
                text="""People and other creatures call me Gandalfux. I have power over white magic\n""",
                begin_txt='Gandalfux')
            self.parent.text.you(text=f'Good day, I am {self.parent.myPlayer.name}\n      Can you learn me something new?\n')
            self.parent.text.npc(
                text="""If you want me to teach you, you have to prove that you are worthy of it. You must successfully complete 2 of my tasks and not die\n""",
                begin_txt='Gandalfux')
        self.parent.text.system(
            f" Choose answer\n  1. Yes, i'll do that\n  2. No, thanks\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response in ('1', 'yes'):
            self.parent.text.you(text="Yes\n")
            tasks()
            if self.parent.zonemap['a2']['SOLVED1'] is True:
                self.parent.text.npc(text=f" Let go outside the town to the Gardens. I will teach you there\n",
                                     begin_txt='Gandalfux')
                self.parent.text.you(text="OK\n")
                self.parent.text.system(
                    text='....After several hours of training. You start to think that this might actually not wor to learn anything from him\n')
                self.parent.text.system(f" Finally after many struggles you learn a new spell!\n", txt_only=True)
                self.parent.text.system(text='Your can now use Fire Ball special spell\n')
                self.parent.myPlayer.spells.append(self.parent.FireBall)
                self.parent.zonemap['b2']['SOLVED'] = True
                self.parent.text.system(
                """
                During training, you find out that Elminster is a former student of Gandelfux. He told you that 
                the magician Elminster uses high-quality magic in his territory, which creates a barrier around the castle, 
                and that without a special object (something like a map) it is almost impossible to get there.
                Also, that the magician Elminster performed a ritual that incredibly increases his armor, so he advised to 
                visit Cardcaster and find a secret treasure there.  There should be a staff that removes the effect of the ritual.
                """, txt_only=True)
            else:
                self.parent.text.npc(text=f" Train your mana and than come back\n",
                                     begin_txt='Gandalfux')
        elif response in ('2', 'no'):
            self.parent.text.you(text="No, I don't think it is a good idea\n")
            self.parent.text.npc(text=f"Bye\n", begin_txt='Gandalfux')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_b2(response)

    def quest_b3(self):
        def auction():
            self.parent.text.system("""\n  - On the auction - \n""", txt_only=True)
            print("")
            self.parent.text.npc(" Ladies and gentlemen, and the current lot, is a house located on the edge of town\n", begin_txt='Auction leader')
            self.parent.text.npc(" The initial bet is 500 coins\n", begin_txt='Auction leader')
            auction_lasts = False
            ### first bet
            while auction_lasts is False:
                self.parent.text.system(" Write your bet using only nums\n", txt_only=True)
                bet = int(input(" > "))
                self.parent.text.npc(f" I hear {bet}\n\n", begin_txt='Auction leader')

                if 500 < bet <= 1000:

                    if bet > 990:
                        self.parent.text.npc(" Greetings you won\n", begin_txt='Auction leader')
                        print("""
            #######################################################
            ~~~~~~       !  The elf has a job for you        ~~~~~~
            #######################################################
            |                     DONE                            |
            | The elf wants to thank you for salvation,           |   
            | and offers you a job.                               |
            |                                                     |  
            |                                                     |
            #######################################################
            |  + Your own home where you can relax or exercise    |
            #######################################################\n""")
                        self.parent.zonemap['b3']['HOME'] = True
                        break

                    elif 500 < bet <= 990:
                        enemy_bet = random.randint(25, 100)
                        enemy_bet += bet
                        if enemy_bet > 1000:
                            enemy_bet = 990
                        self.parent.text.npc(f"{enemy_bet}\n", begin_txt='Tretegors enemy')
                        self.parent.text.npc(f" I hear {enemy_bet}\n", begin_txt='Auction leader')
                else:
                    self.parent.text.system("""\n Write nums beetween 500 and 1000\n""", txt_only=True)
        if self.parent.zonemap['b3']['HOME'] is False:
            self.parent.text.system("\n  - Welcome to Absol -\n", txt_only=True)
            self.parent.text.system(""" You saw three soldiers werewolves attacking an elf\n""")
            self.parent.text.system(""" Do you wanna to help him\n    1. Yes\n    2. No\n""", txt_only=True)
            help_elf = input(" > ")
            if help_elf == "1":
                self.parent.text.danger(" Hey buddy do you know who we are?\n", begin_txt="Werewolve soldier")
                self.parent.fight_soldiers()
                self.parent.text.npc(" Oh thank you a brave hero, let me introduce myself my name is Tretogor\n", begin_txt='Tretogor')
                self.parent.text.you(f" Nice to meet Tratigor, my name is {self.parent.myPlayer.name}, now be more careful, see you\n")
                self.parent.text.npc(f" Please, wait a minute {self.parent.myPlayer.name}! What would you like as a reward for my salvation?!\n", begin_txt='Tretogor')
                self.parent.text.you(" Thanks but I don't need anything, I'm in a hurry\n")
                self.parent.text.npc(" In that case, I have a little job for you. If you don't mind \n", begin_txt='Tretogor')
                print("""
                           #######################################################
                           ~~~~~~       !  The elf has a job for you        ~~~~~~
                           #######################################################
                           |                                                     |
                           | The elf wants to thank you for salvation,           |   
                           | and offers you a job.                               |
                           |                                                     |  
                           |  Reward:  ????????                                  |
                           |                                                     |
                           #######################################################
                           |        1.Accept          |         2.Decline        |
                           #######################################################\n""")
                elf_work = input(" > ")
                if elf_work == "1":
                    self.parent.text.npc(""" I have one sworn enemy who always bothers me, and even now he had sent Elminster’s soldiers to kill me.
            Tonight will be an auction at which the house will be raffled off. He is very important to him(Tretegor’s enemy), 
            but I can not stay at the auction, I now need to go to another city.
            Therefore, I suggest you bargain instead of me. Here you have the money, 
            and if you manage to win the auction, you can leave this house for yourself as a gift.\n""", begin_txt='Tretogor')
                    self.parent.text.system(""" You received 1000 coins\n""")
                    auction()
                elif elf_work == "2":
                    self.parent.text.npc(" Well, as you wish, thank you again for the rescuing\n", begin_txt='Tretogor')
            elif help_elf == "2":
                self.parent.text.you(" Meeeh, this does not concern me\n")
                self.parent.text.danger(" Hey, you what are you staring ?!", begin_txt="Werewolve soldier")
                self.parent.text.danger(" If you do not want problems pay 25 coins\n", begin_txt="Werewolve soldier")
                self.parent.text.system(""" Choose what do you wanna say\n    1.Yes, off course, i`m sorry\n    2.Ignore\n    3. Who said that i do not wanna ?""")
                player_answer = input(" > ")
                if player_answer == '1':
                    self.parent.myPlayer.cash -= 25
                    self.parent.text.danger(" Good boy, now run while you can!\n", begin_txt="Werewolve soldier")
                elif player_answer in ['2', '3']:
                    self.parent.text.danger(" Hey buddy do you know who we are?\n", begin_txt="Werewolve soldier")
                    self.parent.fight_soldiers()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b3()
        else:
            self.parent.text.system("""\n  - Welcome to your home - \n""", txt_only=True)
            self.parent.text.system(""" What do you wanna to do\n    1. Go to rest\n    2. Train\n    3. Go out\n""", txt_only=True)
            house_choise = input(" > ")
            if house_choise == "1":
                sleep_quality = ['great', 'so-so', 'bad']
                mood = random.choice(sleep_quality)
                if mood == 'great':
                    self.parent.myPlayer.regenaration_mana()
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                    self.parent.text.system(""" Congratulations, you slept well you completely recovered!\n""", txt_only=True)
                    self.quest_b3()
                elif mood == 'so-so':
                    self.parent.myPlayer.regenaration_mana()
                    self.parent.myPlayer.heal()
                    self.parent.text.system(""" You haven't slept well you recovered full mana, and some health points \n""", txt_only=True)
                    self.quest_b3()
                elif mood == 'bad':
                    self.parent.myPlayer.regenaration_mana()
                    self.parent.text.system(""" You  slept bad but you recovered mana\n""", txt_only=True)
                    self.quest_b3()
                elif self.parent.myPlayer.HP == self.parent.myPlayer.maxHP and self.parent.myPlayer.MP == self.parent.myPlayer.maxMP:
                    self.parent.text.system("""You rested well\n""", txt_only=True)
                    self.quest_b3()
            elif house_choise == "2":
                self.parent.text.system(""" Which type of training do you wanna to do ?\n       1.practice punches   2.Train spells   3.Meditation\n""")
                training_chanse = random.randint(1, 100)
                training_choose = input(" > ")
                if training_choose == "3":
                    if training_chanse < 10:
                        self.parent.myPlayer.maxHP += 2
                        self.parent.text.system(""" Congratulations you have improved your health\n""", txt_only=True)
                    else:
                        self.parent.text.system("""You did not succeed\n""", txt_only=True)
                        self.quest_b3()
                elif training_choose == "2":
                    self.parent.text.system(""" Repeat the spell to practice\n""", txt_only=True)
                    spellbook = ['Parseltongue', 'Metamorphmagi', 'Seers', 'Legilimency', 'Apparition ',
                                 'Occlumency ', 'Posteriori','Avada Kedavra', 'Crucio', 'Imperio', 'Inferius ',
                                 'Horcrux', 'Portraits', ]
                    false_spell = 0
                    i = 0
                    while i != 7:
                        train_mana = random.choice(spellbook)
                        print(train_mana)
                        player_spell = input(" > ")
                        if false_spell == 3:
                            self.parent.text.system(""" You failed your training\n """)
                            break
                        elif i == 6:
                            self.parent.myPlayer.MP += 5
                            self.parent.text.system(""" Congratulations you successfully ended  your training and uped MP\n""")
                            break
                        elif i != 6 and player_spell == train_mana:
                            self.parent.text.system(""" You have successfully cast a spell\n""")
                            i += 1
                        elif player_spell != train_mana:
                            self.parent.text.system(""" You`ve made mistake!\n""")
                            false_spell += 1

                elif training_choose == "1":
                    if training_chanse < 10:
                        self.parent.myPlayer.maxHP += 2
                        self.parent.text.system(""" Congratulations you have improved your health\n""", txt_only=True)
                    else:
                        self.parent.text.system("""You did not succeed\n""", txt_only=True)
                        self.quest_b3()
            elif house_choise == "3":
                self.parent.text.system('Have a nice day!\n')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b3()

    def quest_b4(self):
        self.parent.text.system("\n  - Welcome to Cardcaster -\n", txt_only=True)
        self.parent.text.npc("This is a charming city known for its smithies. If there would problems, do not worry, contact the guards.\n", begin_txt='Town Guardian')
        self.parent.text.system(""" You can go to:\n  1.Abandoned forge\n  2.Mysterious gorge\n""",txt_only=True)
        answer = input(" > ")
        print(" ")

        def p_choise():
            self.parent.text.system(' What do you wanna to do:\n           1.Try to get out and teach manners, this guy\n           2.Just give up and die\n')
            answer_1 = input(" > ")

            if answer_1 == "1":
                chanse_of_GO = random.randint(1, 6)
                if chanse_of_GO == 6:
                    self.parent.text.system("Congratulations you got out of the trap\n")
                    self.parent.text.you(" Now that old man learns that it's better not to play with me\n")
                    self.parent.text.you(" Hmm and what i should to do now ?\n           1. Go to the local guards\n           2. Go to tavern to find out some info about him \n")
                    npc_asking =input(" > ")
                    if npc_asking == "1":
                        self.parent.text.system("You told everything to the guards, they promised to deal with him\n")
                        self.parent.zonemap['b4']['SOLVED1'] = True

                        if self.parent.zonemap['b4']['SOLVED2'] is True:
                            self.parent.zonemap['b4']['SOLVED'] = True
                    elif npc_asking == "2":
                        self.parent.text.you(" Maybe you know something about Abandoned forge near you tavern? \n")
                        self.parent.text.npc('Yes, it was destroyed 2 days ago because the owner was selling forbidden things.\n', begin_txt='The owner of the tavern')
                        self.parent.text.you(" And what does the owner look like, and is it possible to know where he is now \n")
                        self.parent.text.npc('it`s an ungly old man. And if you wanna i can tell you were is he hiding. \n', begin_txt='The owner of the tavern')
                        self.parent.text.system(' Few moments later...\n')
                        self.parent.text.you(
                            " You have foud that man \n       It was a long 3 hours .... for him\n       I also find out that Elminster's possession is a former school of magic\n       And that old Howards school map can be found in the vicinity of Bricklewhite\n")
                        self.parent.myPlayer.maxHP += 20
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 150
                        self.parent.text.system(' Congratulations you have received 100 coins and a potion that increases health\n')
                        self.parent.zonemap['b4']['SOLVED1'] = True

                        if self.parent.zonemap['b4']['SOLVED2'] is True:
                            self.parent.zonemap['b4']['SOLVED'] = True
                    else:
                        p_choise()

                elif chanse_of_GO in range(1,5):
                    self.parent.text.system("You didn't succeed, try again\n")
                    p_choise()

            elif answer_1 == "2":
                chanse_1 = random.randint(1, 3)
                if chanse_1 == 1:
                    self.parent.text.system(" *clatter*\n", begin_txt='STRANGE SOUNDS')
                    self.parent.text.you(" Hey, I'm over here, please help me get out of here\n")
                    self.parent.text.system(" You're lucky. You were saved by the royal guards\n")
                elif chanse_1 == 2:
                    self.parent.text.system(" Thieves heard your screams, they decided to shoot you and pick up your things\n")
                    self.parent.text.danger("You're dead !\n", begin_txt='SYSTEM')
                    sys.exit()
                elif chanse_1 == 3:
                    self.parent.text.danger(" You died of starvation !\n", begin_txt="SYSTEM")
                    sys.exit()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                p_choise()

        def randome_rode():
            true_road = []
            moves = ['^', '<', '>']
            for i in range(4):
                true_road.append(random.choice(moves))
            return true_road

        def get_road():
            player_road = []
            guess_road = input(" Give the path you want to go(^, <, >), do not separate, do not add other signs:  \n")
            for i in range(len(guess_road)):
                player_road.append(guess_road[i])
            return player_road

        def check():
            global sproby
            global roadswrongs
            true_road = randome_rode()
            print(true_road)
            while roadswrongs != 0 and sproby < 10:
                roadswrongs = 0
                player_road = get_road()
                for i in range(0, 4):
                    if player_road[i] in true_road:
                        if player_road[i] == true_road[i]:
                            print(" This part of the road is safe: ", format(player_road[i]), "On the ", i + 1, " place.\n")
                        else:
                            print(" Hmm, I have to use this part of the road elsewhere: ", format(player_road[i]), "On the ", i + 1, " place.\n")
                            roadswrongs += 1
                    else:
                        print(" If I go like that, I'll probably die: ", format(player_road[i]), "On the ", i + 1," place.\n")
                        roadswrongs += 1
                sproby += 1
            return true_road

        #### Forge quest b4
        if answer == '1' and self.parent.zonemap['b4']['SOLVED1'] is False:
            self.parent.text.npc(""" Within is my granddaughter, could you save her?\n """, begin_txt='OWNER')
            self.parent.text.system( """        Choose one of the below answers\n          1. Yes, I will save her\n          2. No, I'm sorry\n""", txt_only=True)
            response = input(" > ")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(" Yes, I will save her\n")
                self.parent.text.you(" * going to the forge *\n")
                self.parent.text.you(" The smithy is small, but I don't see anyone here\n", begin_txt='YOU(thoughts)')
                self.parent.text.you("Although, stop, I see something ....\n", begin_txt='YOU(thoughts)')
                self.parent.text.danger('\n', begin_txt=':~CRACK~')
                self.parent.text.you(" Aaaaaaa...\n\n")
                self.parent.text.system("You have fallen into a deep pit\n")
                self.parent.text.danger(' Ahahaa, your generous heart will destroy you ...\n         Accept your destiny and die like an animal\n', begin_txt='OWNER')
                self.parent.text.danger('*clatter....*\n')
                p_choise()
            elif response in ('no', '2'):
                self.parent.text.you(" I'm sorry i can't help you\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b4()

        #### Gorge quest b4
        elif answer == '2' and self.parent.zonemap['b4']['SOLVED2'] is False:
            self.parent.text.system("""You went into a dark cave, the inhabitants say that a secret treasure is hidden here.
         This is the treasure about which master was talking.
         But no one don't want to say why no one has taken the treasure yet.
         Maybe it's a trap?!
""")
            self.parent.text.you("*It's too dark, maybe I should light a torch?*\n      1. Yes, i should\n      2. NO, no way\n")
            response = input(" > ")
            response = str(response).lower()
            if response == '1':
                global sproby
                global roadswrongs
                last = check()
                if roadswrongs == 0:
                    self.parent.text.you(" I think this road will be safe, worth a try\n")
                    self.parent.myPlayer.STR += 13
                    self.parent.myPlayer.cash += 150
                    self.parent.myPlayer.xp += 150
                    self.parent.text.system(" Congratulations you have found a tresure 150 coins,magic staff and a potion that increases strength\n ")
                    self.parent.zonemap['b4']['SOLVED2'] = True
                    self.parent.myPlayer.inventory.pop(8)
                    self.parent.myPlayer.inventory.insert(8, 'Antimagic staff')
                    if self.parent.zonemap['b4']['SOLVED1'] is True:
                        self.parent.zonemap['b4']['SOLVED'] = True
                else:
                    print(" Unfortunately you have made too many mistakes, the correct way is:  ", last)
            elif response == '2':
                self.parent.text.you(" Ohhh it's too dark, I can't see anything.\n", begin_txt='YOU(thoughts)')
                self.parent.text.danger(" *teeth grinding* \n")
                self.parent.text.you(" Maybe, still i have to light a torch\n", begin_txt='YOU(thoughts)')
                self.parent.text.you("*light a torch*\n")
                self.parent.text.danger("*Gets a sword*\n\n", begin_txt='Falmer, which you have stepped on the foot')
                self.parent.text.system(' You almost died, this cave is full of falmers. You managed to escape, but you get a few wounds\n')
                self.parent.myPlayer.HP -= 30
                self.parent.text.system('You got 30 damage\n')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b4()

        elif answer == "1" and self.parent.zonemap['b4']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the gorge')
        elif answer == "2" and self.parent.zonemap['b4']['SOLVED2'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the forge')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_b4()

    def quest_b5(self, response=None, action=False):
        if not action:
            if not response:
                self.parent.text.system(text=""" When you walk to market in the morning you see on a wall a pinned leaflet\n""")
                self.parent.text.system(text=""" It looks like local miller looks for an employee\n""")
                self.parent.text.system(text=""" This could be an occasion for quick money\n""")
                print("""
                #######################################################
                ~~~~~~~~       !   Work for the day            ~~~~~~~~
                #######################################################
                |                                                     |
                |  You have found booklet about a job                 |  
                |  Do you want to take on this job?                   |
                |                                                     |
                |  Reward:  ????????????????                          |
                |                                                     |
                #######################################################
                |     1.Go to miller       |           2.Go away      |
                #######################################################\n""")
                response = input(" >  ")
                response = str(response).lower()
        if response == '1':
            if not action:
                self.parent.text.you(text=f"Hey, I am {self.parent.myPlayer.name}, I saw you job offer\n")
                self.parent.text.npc(text=f"Hi there\n", begin_txt='Miller')
                self.parent.text.npc(text=f"Great, how can I help you?\n", begin_txt='Miller')
            self.parent.text.system(
                f" Choose option\n  1. Can you tell me more about the job?\n  2. How long would I work?\n  3. How much am I going to earn?\n  4. OK, I want start working\n  5. I have to go\n", txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.you(text=f"Can you tell me more about the job?\n")
                self.parent.text.npc(text=f"I am looking for a man that can help me carrying my flour to my clients\n", begin_txt='Miller')
                self.quest_b5('1', True)
            elif response == '2':
                self.parent.text.you(text=f"2. How long would I work?\n")
                self.parent.text.npc(text=f"Only today. Until dawn\n", begin_txt='Miller')
                self.quest_b5('1', True)
            elif response == '3':
                self.parent.text.you(text=f"How much am I going to earn?\n")
                self.parent.text.npc(text=f"100 coins paid after job\n", begin_txt='Miller')
                self.quest_b5('1', True)
            elif response == '4':
                self.parent.text.you(text=f"OK, I want start working!\n")
                self.parent.text.npc(text=f"Wonderfull! We can start straight away!\n", begin_txt='Miller')
                self.parent.text.system(text=""" After whole day of work you get paid by the miller. Also he lets you sleep in his mill so can recover a bit\n""")
                self.parent.myPlayer.cash += 100
                self.parent.myPlayer.HP += 25
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxMP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxMP
                    print("""
            #######################################################
            ~~~~~~~~       !   Work for the day            ~~~~~~~~
            #######################################################
            |                     DONE                            |
            |  You have found booklet about a job                 |  
            |                                                     |
            |   You have worked hard and earned a reward          |
            |                                                     |
            #######################################################
            |                   + 100 coins                       |
            #######################################################\n""")
                self.parent.zonemap['b5']['SOLVED'] = True
            elif response == '5':
                self.parent.text.you(text=f"I have to go\n")
                self.parent.text.npc(text=f"Bye bye\n", begin_txt='Miller')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b5()
        elif response == '2':
            self.parent.text.system("Pff i don't need this")
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_b5(response)

    # i need to add this  to quests b5
    def peepers_game(self):
        self.parent.text.system("To your surprise, you noticed a large group of people who were constantly shouting and laughing\n")
        self.parent.text.system(
            " Do you want to come and find out what happened there?\n  1.Yes\n  2.Nope\n",txt_only=True)
        group_of_people = input(" > ")
        if group_of_people == "1":
            self.parent.text.you("Lest1s see...")
            self.parent.text.system("You have noticed a strange situation, people are playing peepers with a one-eyed dwarf")
            self.parent.text.npc("Hey everybody look another player has come")
            print("""

                    #######################################################
                    ~~~~~~          !  Champion in peepers           ~~~~~~
                    #######################################################
                    |                                                     |
                    |    You were offered to play peepers with            |
                    |     a one-eyed gnome. What answer will you give?    |
                    |                                                     |
                    |  Reward:  30 coins                                  |
                    |                                                     |
                    #######################################################
                    #######################################################\n""")
            self.parent.text.system(
                " Choose how you answer\n  1.Hmm, what are the rules\n 2.No, i just come to see\n", txt_only=True)
            join_game = input(" > ")
            if join_game == "1":
                self.parent.text.npc("In general, you sit in front of Tandibrad and you look into each other's eyes.\n Who can not stand and blinks, the loser. Tandibrad has already won 11 times in a row, can you win it?")
                win_chanse = random.randint(1, 100)
                if win_chanse > 85:
                    self.parent.text.npc("Hmm, strangely, they have been looking at each other for so long.")
                    self.parent.text.npc("Interesting who will lose....")
                    print("""

                                       #######################################################
                                       ~~~~~~          !  Champion in peepers           ~~~~~~
                                       #######################################################
                                       |                       Done                          |
                                       |    You were offered to play peepers with            |
                                       |     a one-eyed gnome.                               |
                                       |      You won !!! Now you are the current champion   |
                                       |                                                     |
                                       |  Reward:  30 coins                                  |
                                       |                                                     |
                                       #######################################################
                                       |           Congratulations you`ve won + 30 coins     |      
                                       #######################################################\n""")
                    self.parent.myPlayer.cash += 30
                elif win_chanse <= 85:
                    self.parent.text.npc("Hmm, strangely, they have been looking at each other for so long.")
                    self.parent.text.npc("Hmm, interesting who will lose")
                    self.parent.text.you("Ahhh I`ve lost. He is a strong opponent")
            elif join_game == "2":
                self.parent.text.npc("Oh well okay...")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                peepers_game()
        elif group_of_people == "2":
            self.parent.text.you("Meeeeh")
            self.parent.text.you("You`ve continued your journey!")
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            peepers_game()
    # i need to add this ^ to quests b5

    def quest_c1(self):
        print(" ")
        self.parent.text.system("""\n  -  Wyllowwood - \n""", txt_only=True)
        print(' ')
        self.parent.text.system(""" You can go to:\n  1. Wyllowwood lake\n  2. Spellshop\n""",txt_only=True)
        player_choise1 = input(" > ")
        if player_choise1 == "1" and self.parent.zonemap['c1']['SOLVED1'] is False:

            self.parent.text.npc("Hello young man, maybe you want to take part in a fishing tournament?\n", begin_txt="Mr.Fishman")
            self.parent.text.you("But what do I benefit from this?\n")
            self.parent.text.npc("If you take prize place you will receive a cash prize, and taking 1st place you will get another special item\n", begin_txt="Mr.Fishman")
            print("""
                    ###########################################
                    ~~~~~~       Fishing tournament      ~~~~~~
                    ###########################################
                    |                                         |
                    | 1 place - 150 coins + mysterious object |
                    | 2 place - 100 coins                     |
                    | 3 place - 75 coins                      |
                    |                                         |
                    |                                         |
                    ###########################################
                    |     1.Accept      |      2.Decline      |
                    ###########################################\n""")
            player_choise2 = input(" > ")
            if player_choise2 == "1":
                self.parent.text.npc(" Let the tournament starts\n", begin_txt="Mr.Fishman")
                self.parent.text.system(""" Okay now you have 3 attempts to catch a fish, if you are sure that you have the biggest fish enter 'accept',
          if you want to try again enter 'again'. After the third attempt, the tournament ends, and the results for the last fish caught will be counted.
          To start fishing write 'catch'
      
          ! Attention when you type 'again' you release the previous caught fish, and catch a new one. 
          ! You probably won't be able to return the fish you caught before.\n""")
                some = input(" > ")
                player_choise3 = some
                i = 0
                first_catch = False
                fishname = ['Magikarp', 'Golden Habus', 'Shadow Needle', 'Silver tench', 'Crystal sturgeon']
                final_fish = 0
                age = ''
                final_fish_name = ''
                while i != 3:
                    your_fish = random.randint(100, 500)
                    if player_choise3 == "catch" and first_catch is False:
                        final_fish_name = random.choice(fishname)
                        if your_fish < 250:
                            age = " Hmm it's maybe only baby fish"
                        elif 250 < your_fish <= 480:
                            age = " Hmm it's maybe only teen fish"
                        elif 480 < your_fish <= 500:
                            age = " Oh, great fish, I think you can take 1st place with her"
                        print("""

                                                                                        @@@@@@@@@@@.    
                                          #@@                             &@@@@@%    @@@@@@@@@#         
                                           &@@                        @@@@@@@@@@@@@@@@@@@@@@            
                                            @@@                     @@(     (@@@@@@@@@@@@@@             
                                            @@@                                  (@@@@@@@@@             
                                            &@@                                    &@@@@@@@             
                                            @@@                                     @@@@@@@             
                                           *@@                                      @@@@@@@             
                                          .@@                                       @@@@@@@             
                                         @@@                                       @@@@@@@@             
                                       .@@@                                        @@@@@@@@             
                                      @@@                                        (@@@@@@@@@             
                                    @@@                                         @@@@@@@@@@@             
                                   @@@                       @@               @@@@@@@@@@@@              
                                 @@@                       @@@@            @@@@@@@@@@@@@@@              
                               @@@*                      &@@@@@       @@@@@@@@@@@@@@@@@@@               
                              @@@                       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                             @@@                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                            @@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                            @@@                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                            @@@             @@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                            ,@@           @@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@        @@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
                              @@@     @@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@         .@              
                               @@@*  @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@                            
                                 @@@@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@@@@@                               
                                   &@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@                                  
                                      *@@@@@@@@@@@@@@@@@@@@  @@@@                                       
                                           (@@@@@@@@@@@@@@@                                             

                                                """)
                        self.parent.text.system(f"Congratulations, you have caught {final_fish_name} in the size of {your_fish}, {age}\n")
                        first_catch = True
                        final_fish = your_fish
                        i += 1
                        self.parent.text.system(" You wanna try again?\n")
                        player_choise3 = input(" > ")
                    elif player_choise3 == 'again':
                        final_fish_name = random.choice(fishname)
                        if your_fish < 250:
                            age = " Hmm it's maybe only baby fish"
                        elif 250 < your_fish <= 480:
                            age = " Hmm it's maybe only teen fish"
                        elif 480 < your_fish <= 500:
                            age = " Oh, great fish, I think you can take 1st place with her"
                        print("""
                                                                                            
                                                                @@@@@@@@@@@.    
                  #@@                             &@@@@@%    @@@@@@@@@#         
                   &@@                        @@@@@@@@@@@@@@@@@@@@@@            
                    @@@                     @@(     (@@@@@@@@@@@@@@             
                    @@@                                  (@@@@@@@@@             
                    &@@                                    &@@@@@@@             
                    @@@                                     @@@@@@@             
                   *@@                                      @@@@@@@             
                  .@@                                       @@@@@@@             
                 @@@                                       @@@@@@@@             
               .@@@                                        @@@@@@@@             
              @@@                                        (@@@@@@@@@             
            @@@                                         @@@@@@@@@@@             
           @@@                       @@               @@@@@@@@@@@@              
         @@@                       @@@@            @@@@@@@@@@@@@@@              
       @@@*                      &@@@@@       @@@@@@@@@@@@@@@@@@@               
      @@@                       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
     @@@                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
    @@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
    @@@                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
    @@@             @@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
    ,@@           @@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
     @@@        @@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
      @@@     @@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@         .@              
       @@@*  @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@                            
         @@@@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@@@@@                               
           &@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@                                  
              *@@@@@@@@@@@@@@@@@@@@  @@@@                                       
                   (@@@@@@@@@@@@@@@                                             
                                     
                        """)
                        self.parent.text.system(f"Congratulations, you have caught {final_fish_name} in the size of {your_fish}, {age}\n")
                        i += 1
                        final_fish = your_fish
                        if i != 3:
                            self.parent.text.system(" You wanna try again ?\n")
                            player_choise3 = input(" > ")
                    elif player_choise3 == "accept":
                        print("""

                                                                                        @@@@@@@@@@@.    
                                          #@@                             &@@@@@%    @@@@@@@@@#         
                                           &@@                        @@@@@@@@@@@@@@@@@@@@@@            
                                            @@@                     @@(     (@@@@@@@@@@@@@@             
                                            @@@                                  (@@@@@@@@@             
                                            &@@                                    &@@@@@@@             
                                            @@@                                     @@@@@@@             
                                           *@@                                      @@@@@@@             
                                          .@@                                       @@@@@@@             
                                         @@@                                       @@@@@@@@             
                                       .@@@                                        @@@@@@@@             
                                      @@@                                        (@@@@@@@@@             
                                    @@@                                         @@@@@@@@@@@             
                                   @@@                       @@               @@@@@@@@@@@@              
                                 @@@                       @@@@            @@@@@@@@@@@@@@@              
                               @@@*                      &@@@@@       @@@@@@@@@@@@@@@@@@@               
                              @@@                       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                             @@@                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                            @@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                            @@@                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                            @@@             @@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                            ,@@           @@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@        @@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
                              @@@     @@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@         .@              
                               @@@*  @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@                            
                                 @@@@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@@@@@                               
                                   &@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@                                  
                                      *@@@@@@@@@@@@@@@@@@@@  @@@@                                       
                                           (@@@@@@@@@@@@@@@                                             

                                                """)
                        self.parent.text.system(f"Congratulations, your result {final_fish_name} in the size of {final_fish}\n")
                        break
                    else:
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')

                places = 3
                fisherman1 = random.randint(200, 480)
                fisherman2 = random.randint(200, 480)
                fisherman3 = random.randint(200, 480)
                print(fisherman1)
                print(fisherman2)
                print(fisherman3)

                while places != 0:
                    if fisherman1 > fisherman2 and fisherman1 > fisherman3 and fisherman1 > final_fish:
                        self.parent.text.system(f"Best result is: {fisherman1}\n")
                        places -= 1
                        if fisherman2 > fisherman3 and fisherman2 > final_fish:
                            self.parent.text.system(f"Second place is: {fisherman2}\n")
                            places -= 1
                            if fisherman3 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                                self.parent.text.npc("Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n", begin_txt="Mr.Fishman")
                            elif final_fish > fisherman3:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 150
                        elif fisherman3 > fisherman2 and fisherman3 > final_fish:
                            self.parent.text.system(f"Second result is: {fisherman3}\n")
                            places -= 1
                            if fisherman2 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                                self.parent.text.npc("Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n", begin_txt="Mr.Fishman")
                            elif final_fish > fisherman3:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 75
                        elif final_fish > fisherman2 and final_fish > fisherman3:
                            self.parent.text.system(f"Second place is: {final_fish}\n")
                            self.parent.text.npc(
                                "Not bad young man, here is your 100 coins for the 2 place\n",
                                begin_txt="Mr.Fishman")
                            self.parent.myPlayer.cash += 100
                            self.parent.myPlayer.xp += 100
                            places -= 1
                            if fisherman3 > fisherman2:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                            elif fisherman2 > fisherman3:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                    elif fisherman2 > fisherman1 and fisherman2 > fisherman3 and fisherman2 > final_fish:
                        self.parent.text.system(f"Best result is: {fisherman2}\n")
                        places -= 1
                        if fisherman1 > fisherman3 and fisherman1 > final_fish:
                            self.parent.text.system(f"Second place is: {fisherman1}\n")
                            places -= 1
                            if fisherman3 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                                self.parent.text.npc(
                                    "Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n",
                                    begin_txt="Mr.Fishman")
                            elif final_fish > fisherman3:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 150
                        elif fisherman3 > fisherman1 and fisherman3 > final_fish:
                            self.parent.text.system(f"Second result is: {fisherman3}\n")
                            places -= 1
                            if fisherman2 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                                self.parent.text.npc(
                                    "Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n",
                                    begin_txt="Mr.Fishman")
                            elif final_fish > fisherman2:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 75
                        elif final_fish > fisherman2 and final_fish > fisherman3:
                            self.parent.text.system(f"Second place is: {final_fish}\n")
                            self.parent.text.npc(
                                "Not bad young man, here is your 100 coins for the 2 place\n",
                                begin_txt="Mr.Fishman")
                            self.parent.myPlayer.cash += 100
                            self.parent.myPlayer.xp += 100
                            places -= 1
                            if fisherman1 > fisherman3:
                                self.parent.text.system(f"Third place is: {fisherman1}\n")
                                places -= 1
                            elif fisherman3 > fisherman1:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                    elif fisherman3 > fisherman1 and fisherman3 > fisherman2 and fisherman3 > final_fish:
                        self.parent.text.system(f"Best result is: {fisherman3}\n")
                        places -= 1
                        if fisherman2 > fisherman1 and fisherman2 > final_fish:
                            self.parent.text.system(f"Second place is: {fisherman2}\n")
                            places -= 1
                            if fisherman1 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman1}\n")
                                places -= 1
                                self.parent.text.npc(
                                    "Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n",
                                    begin_txt="Mr.Fishman")
                            elif final_fish > fisherman1:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 150
                        elif fisherman1 > fisherman2 and fisherman1 > final_fish:
                            self.parent.text.system(f"Second result is: {fisherman1}\n")
                            places -= 1
                            if fisherman2 > final_fish:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                                self.parent.text.npc(
                                    "Sorry you didn't get into the top 3, come again, maybe next time you'll be luckier\n",
                                    begin_txt="Mr.Fishman")
                            elif final_fish > fisherman2:
                                self.parent.text.system(f"Third place is: {final_fish}\n")
                                self.parent.text.npc(
                                    "Not bad young man, here is your 75 coins for the 3 place\n",
                                    begin_txt="Mr.Fishman")
                                places -= 1
                                self.parent.myPlayer.cash += 75
                                self.parent.myPlayer.xp += 75
                        elif final_fish > fisherman2 and final_fish > fisherman1:
                            self.parent.text.system(f"Second place is: {final_fish}\n")
                            self.parent.text.npc(
                                "Not bad young man, here is your 100 coins for the 2 place\n",
                                begin_txt="Mr.Fishman")
                            self.parent.myPlayer.cash += 100
                            self.parent.myPlayer.xp += 100
                            places -= 1
                            if fisherman1 > fisherman2:
                                self.parent.text.system(f"Third place is: {fisherman1}\n")
                                places -= 1
                            elif fisherman2 > fisherman1:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                    elif final_fish > fisherman1 and final_fish > fisherman2 and final_fish > fisherman3:
                        self.parent.text.system(f"Best result is: {final_fish}\n")
                        self.parent.text.npc(""" My sincere congratulations, you won this tournament, here are the promised 150 coins     
        and 2 throwing knives that are impossible to miss and that always inflict the same damage, despite the enemy's armor\n""",
                            begin_txt="Mr.Fishman")
                        self.parent.myPlayer.cash += 150
                        self.parent.myPlayer.xp += 150
                        self.parent.myPlayer.inventory.pop(1)
                        self.parent.myPlayer.inventory.pop(2)
                        self.parent.myPlayer.inventory.insert(1, 'Throwing knife')
                        self.parent.myPlayer.inventory.insert(2, 'Throwing knife')
                        self.parent.zonemap['c1']['SOLVED1'] = True

                        places -= 1
                        if fisherman1 > fisherman2 and fisherman1 > fisherman3:
                            self.parent.text.system(f"Second place is: {fisherman1}\n")
                            places -= 1
                            if fisherman2 > fisherman3:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
                            elif fisherman3 > fisherman2:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                        elif fisherman2 > fisherman1 and fisherman2 > fisherman3:
                            self.parent.text.system(f"Second result is: {fisherman2}\n")
                            places -= 1
                            if fisherman1 > fisherman3:
                                self.parent.text.system(f"Third place is: {fisherman1}\n")
                                places -= 1
                            elif fisherman3 > fisherman1:
                                self.parent.text.system(f"Third place is: {fisherman3}\n")
                                places -= 1
                        elif fisherman3 > fisherman1 and fisherman3 > fisherman2:
                            self.parent.text.system(f"Second place is: {fisherman3}\n")
                            places -= 1
                            if fisherman1 > fisherman2:
                                self.parent.text.system(f"Third place is: {fisherman1}\n")
                                places -= 1
                            elif fisherman2 > fisherman1:
                                self.parent.text.system(f"Third place is: {fisherman2}\n")
                                places -= 1
        elif player_choise1 == "2":
            print("""
        #######################################################
        ~~~~~~~~             SPELL SHOP                ~~~~~~~~
        #######################################################
        |              What do you wanna to do ?              |
        |   1. Refactor something                             |
        |   2. Do a spell                                     |
        |                                                     |
        #######################################################
        #######################################################\n""")
            player_conversation = input(" > ")
            if player_conversation == "1":
                if 'Elven herbs' in self.parent.myPlayer.inventory:
                    self.parent.text.npc("What do you need a hero?\n")
                    self.parent.text.you("I have these herbs, I heard that you can help me, turn them into medicine.\n")
                    self.parent.text.npc("Let`s see what can i do...\n")
                    self.parent.myPlayer.inventory.pop(0)
                    self.parent.myPlayer.inventory.insert(0, "Incredible medicine")
                    self.parent.text.npc("Here you are, the best what can i do\n")
                    self.parent.text.you("Thanks!\n")
                if 'Fiery flower' in self.parent.myPlayer.inventory:
                    self.parent.text.npc("What do you need a hero?\n")
                    self.parent.text.you("I have these flower, i heard that you can help me, turn them into medicine.\n")
                    self.parent.text.npc("Let`s see what can i do...\n")
                    self.parent.myPlayer.inventory.pop(12)
                    self.parent.myPlayer.inventory.insert(12, "Warrior medicine")
                    self.parent.text.npc("Here you are, the best what can i do\n")
                    self.parent.text.you("Thanks!\n")
                else:
                    self.parent.text.system("You do not have nothing what to refactor!")
            elif player_conversation == "2":
                i = 3
                if 'Heal grass' in self.parent.myPlayer.inventory and i != 0:
                    if i == 3:
                        self.parent.text.npc("What do you need a hero?\n")
                        self.parent.text.you("I have these heal grass, i heard that you can help me, turn them into medicine.\n")
                        self.parent.text.npc("Let`s see what can i do...\n")
                        self.parent.myPlayer.inventory.pop(5)
                        self.parent.myPlayer.inventory.insert(5, "Heal pousion")
                        self.parent.text.npc("Here you are, the best what can i do\n")
                        self.parent.text.you("Thanks!\n")
                        i -= 1
                    if i == 2:
                        self.parent.text.npc("What do you need a hero?\n")
                        self.parent.text.you(
                            "I have these heal grass, i heard that you can help me, turn them into medicine.\n")
                        self.parent.text.npc("Let`s see what can i do...\n")
                        self.parent.myPlayer.inventory.pop(6)
                        self.parent.myPlayer.inventory.insert(6, "Heal pousion")
                        self.parent.text.npc("Here you are, the best what can i do\n")
                        self.parent.text.you("Thanks!\n")
                        i -= 1
                    if i == 1:
                        self.parent.text.npc("What do you need a hero?\n")
                        self.parent.text.you(
                            "I have these heal grass, i heard that you can help me, turn them into medicine.\n")
                        self.parent.text.npc("Let`s see what can i do...\n")
                        self.parent.myPlayer.inventory.pop(7)
                        self.parent.myPlayer.inventory.insert(7, "Heal pousion")
                        self.parent.text.npc("Here you are, the best what can i do\n")
                        self.parent.text.you("Thanks!\n")
                        i -= 1
                if 'Heal grass' not in self.parent.myPlayer.inventory:
                    self.parent.text.you("I dont have anything...")
        elif player_choise1 == "1" and self.parent.zonemap['c1']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to the spellshop if you have something to refactor')

    def quest_c2(self):
        def chicken_find():
            fear_count = 0
            while fear_count != 100:
                random_chicken = random.randint(1, 3)
                if random_chicken == 1:
                    print(' ')
                    print("""                                
                                                                   @@   @@      
                                                                    @@@@@@@@@   
               @@@@                                             @@@@@@@@@@@@    
           #@@@@@@@@@                                        @@@@@@@@   @@@@@@   
    @@@@@@@@@@@@@@@@@@*                                     @@@@@@@@@@@@@@@@@@@@@)
 @@@@@@@@@@@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@@@.   
  @@@@@@@@@@@@@@@@@@@@@@@@/                               @@@@@@@@@@@@@@@@      
      .@@@@@@@@@@@@@@@@@@@@@@.                          *@@@@@@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@@@@   
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       
                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,             
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                   
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@*                     
                                       @@@@@@@@@@@@@@@@@@                       
                                          @@@@@@@@@@@@@                         
                                           #@@@@@@@                             
                                             @@@@@@                             
                                             *@@@@@                             
                                        .@@@@@@@@@@@@@@@                        
                                      @@@@@@@@@@@@*@@@@@@@@@@                   
                                            @@@&                         \n""")
                    self.parent.text.you("Haha, find one. I hope she has no owner\n")
                    finded_chicken = random.randint(3, 11)
                    self.parent.text.you(
                        f"Okay even if you have an owner I won't take a lot of feathers, Only {finded_chicken}\n")
                    fear_count += finded_chicken
                    if fear_count > 100:
                        fear_count = 100
                    if fear_count != 100:
                        self.parent.text.you(f"Okay, і already have {fear_count}, i need to find the next one\n")
                        input(" > ")

                elif random_chicken == 2:
                    print(' ')
                    self.parent.text.you("Okay maybe this gentleman will help me\n")
                    self.parent.text.system(" What do you wanna tell him?\n   1.Greetings, can i ask you about help\n   2.Do you have a chicken\n",txt_only=True)
                    player_conversation1 = input(" > ")
                    if player_conversation1 == "1":
                        self.parent.text.you("Greetings, can i ask you about help\n")
                        self.parent.text.npc("I think so, but what can I do to help a young warrior\n",begin_txt="Peasant")
                        self.parent.text.you("I only need a couple of feathers if you have a chicken\n")
                        self.parent.text.npc("So of course I can help you\n", begin_txt="Peasant")
                        print("""                                
                                                                                          @@   @@      
                                                                                           @@@@@@@@@   
                                      @@@@                                             @@@@@@@@@@@@    
                                  #@@@@@@@@@                                        @@@@@@@@   @@@@@@   
                           @@@@@@@@@@@@@@@@@@*                                     @@@@@@@@@@@@@@@@@@@@@)
                        @@@@@@@@@@@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@@@.   
                         @@@@@@@@@@@@@@@@@@@@@@@@/                               @@@@@@@@@@@@@@@@      
                             .@@@@@@@@@@@@@@@@@@@@@@.                          *@@@@@@@@@@@@@@@@@@     
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@    
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@@@@   
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,             
                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                   
                                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@*                     
                                                              @@@@@@@@@@@@@@@@@@                       
                                                                 @@@@@@@@@@@@@                         
                                                                  #@@@@@@@                             
                                                                    @@@@@@                             
                                                                    *@@@@@                             
                                                               .@@@@@@@@@@@@@@@                        
                                                             @@@@@@@@@@@@*@@@@@@@@@@                   
                                                                   @@@&                         """)
                        finded_chicken = random.randint(8, 17)
                        self.parent.text.npc(
                            f"I hope this amount will help you somehow, give you {finded_chicken} feathers\n", begin_txt="Peasant")
                        fear_count += finded_chicken
                        if fear_count > 100:
                            fear_count = 100
                        self.parent.text.you(f"Okay, і already have {fear_count}, i need to find the next one\n")
                        input(" > ")
                    elif player_conversation1 == "2":
                        self.parent.text.you("Do you have a chicken?\n")
                        self.parent.text.npc("Emm, what ?\n",
                                             begin_txt="Peasant")
                        self.parent.text.you("Oh, forgive me for my rudeness. I just need a few feathers, if you have a chicken, could you help me?\n")
                        self.parent.text.npc("Heh, ok i will help you\n", begin_txt="Peasant")
                        print("""                                
                                                                                                                  @@   @@      
                                                                                                                   @@@@@@@@@   
                                                              @@@@                                             @@@@@@@@@@@@    
                                                          #@@@@@@@@@                                        @@@@@@@@   @@@@@@   
                                                   @@@@@@@@@@@@@@@@@@*                                     @@@@@@@@@@@@@@@@@@@@@)
                                                @@@@@@@@@@@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@@@.   
                                                 @@@@@@@@@@@@@@@@@@@@@@@@/                               @@@@@@@@@@@@@@@@      
                                                     .@@@@@@@@@@@@@@@@@@@@@@.                          *@@@@@@@@@@@@@@@@@@     
                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@    
                                                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@@@@   
                                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
                                                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       
                                                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                                                                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,             
                                                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                   
                                                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@*                     
                                                                                      @@@@@@@@@@@@@@@@@@                       
                                                                                         @@@@@@@@@@@@@                         
                                                                                          #@@@@@@@                             
                                                                                            @@@@@@                             
                                                                                            *@@@@@                             
                                                                                       .@@@@@@@@@@@@@@@                        
                                                                                     @@@@@@@@@@@@*@@@@@@@@@@                   
                                                                                           @@@&                         """)
                        finded_chicken = random.randint(4, 13)
                        self.parent.text.npc(
                            f"Here you are!, give you {finded_chicken} feathers\n", begin_txt="Peasant")
                        fear_count += finded_chicken
                        if fear_count > 100:
                            fear_count = 100
                        if fear_count != 100:
                            self.parent.text.you(f"Okay, і already have {fear_count}, i need to find the next one\n")
                            input(" > ")
                    else:
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')

                elif random_chicken == 3:
                    print(' ')
                    self.parent.text.you(
                        "I'm sorry, I see you have chickens, could you help me and give me some feathers?\n")
                    self.parent.text.npc(
                        "Yes, of course, but I'm too busy. Go pluck as much as you need\n", begin_txt="Peasant")
                    self.parent.text.you("Thank you good man\n")
                    self.parent.text.system("""
                    The chicken has started to run away from you, try to catch it when it stops.  
                    Write 'wait' when it goig to fly, or bites grains.
                    Write 'catch' when she is distracted\n """, txt_only=True)

                    chicken_catch = False
                    while chicken_catch is False:
                        chicken_moves = random.randint(1, 3)
                        if chicken_moves == 1:
                            self.parent.text.you("Oh no, she is going to fly\n")
                            player_conversation2 = input(" > ")
                            if player_conversation2 == "catch":
                                self.parent.text.system(""" Hey hey , catch her when she is distracted \n""",
                                                        txt_only=True)
                            elif player_conversation2 == "wait":
                                self.parent.text.system("""Right choise\n""", txt_only=True)
                            else:
                                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        elif chicken_moves == 2:
                            self.parent.text.you("Hmm, she bites the grain\n")
                            player_conversation2 = input(" > ")
                            if player_conversation2 == "catch":
                                self.parent.text.system(""" Hey hey , catch her when she is distracted """,
                                                        txt_only=True)
                            elif player_conversation2 == "wait":
                                self.parent.text.system("""Right choise\n""",
                                                        txt_only=True)
                            else:
                                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        elif chicken_moves == 3:
                            self.parent.text.you("She is distracted!\n")
                            player_conversation2 = input(" > ")
                            if player_conversation2 == "catch":
                                catch_chanse = random.randint(1, 4)
                                if catch_chanse in [1, 2 ,3]:
                                    self.parent.text.system("""Yes, you caught her !!!""",
                                                            txt_only=True)
                                    print("""                                
                                                                                                                              @@   @@      
                                                                                                                               @@@@@@@@@   
                                                                          @@@@                                             @@@@@@@@@@@@    
                                                                      #@@@@@@@@@                                        @@@@@@@@   @@@@@@   
                                                               @@@@@@@@@@@@@@@@@@*                                     @@@@@@@@@@@@@@@@@@@@@)
                                                            @@@@@@@@@@@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@@@.   
                                                             @@@@@@@@@@@@@@@@@@@@@@@@/                               @@@@@@@@@@@@@@@@      
                                                                 .@@@@@@@@@@@@@@@@@@@@@@.                          *@@@@@@@@@@@@@@@@@@     
                                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@    
                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@@@@   
                                                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
                                                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       
                                                                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,             
                                                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                   
                                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@*                     
                                                                                                  @@@@@@@@@@@@@@@@@@                       
                                                                                                     @@@@@@@@@@@@@                         
                                                                                                      #@@@@@@@                             
                                                                                                        @@@@@@                             
                                                                                                        *@@@@@                             
                                                                                                   .@@@@@@@@@@@@@@@                        
                                                                                                 @@@@@@@@@@@@*@@@@@@@@@@                   
                                                                                                       @@@&                         """)
                                    chicken_catch = True
                                elif catch_chanse == 4:
                                    self.parent.text.system("""Oh no she broke free!!!\n""",
                                                            txt_only=True)
                            elif player_conversation2 == "wait":
                                self.parent.text.system("""You had to catch her in that moment !!!""",
                                                        txt_only=True)
                            else:
                                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    finded_chicken = random.randint(8, 17)
                    self.parent.text.npc(
                        f"I hope this amount will help you somehow, {finded_chicken} feathers\n", begin_txt="Peasant")
                    fear_count += finded_chicken
                    if fear_count > 100:
                        fear_count = 100
                    if fear_count != 100:
                        self.parent.text.you(f"Okay, і already have {fear_count}, i need to find the next one\n")
                        input(" > ")

        self.parent.text.npc("""Hey hey buddy, did you know that the wizard Elminster has a real dragon?
        and that this dragon often flies into the valley of dragons for fun or to eat something \n""",begin_txt="Frank")
        self.parent.text.you("So what?\n")
        self.parent.text.npc("Have you ever wondered how they fly?\n", begin_txt="Frank")
        if "Dragon heart" in self.parent.myPlayer.inventory:
            self.parent.text.you("""No, I don't know, but the dragon you're talking about i has already killed him 
      І`m busy a little, i had info that i can find a map that i need here \n""")
            self.parent.text.npc("Whaaat ?! No waaay....If so, you would have the dragon's heart with you\n")
            self.parent.text.you("Yep have one\n")
            self.parent.text.npc("*The sound of a drooping jaw*\n")
            self.parent.text.npc("What map do you say you need ?\n")
            self.parent.text.you("Old map of the former school of magicians Howard\n")
            self.parent.text.npc("Do you wanna trade? I'll get you a card and you'll give me dragon heart.\n")
            self.parent.text.system("Do you wanna trade with him ?\n      1.Yes\n      2.Nope\n")
            heart_trade = input(" > ")
            if heart_trade == "1":
                self.parent.text.you("Alright !\n")
                self.parent.myPlayer.inventory.pop(11)
                self.parent.myPlayer.inventory.insert(11, "-")
                self.parent.myPlayer.inventory.pop(10)
                self.parent.myPlayer.inventory.insert(10, "Ancient map of Howard")
                self.parent.text.npc("It's nice to deal with you!")
        elif "Dragon heart" not in self.parent.myPlayer.inventory:
            self.parent.text.you("""No, I'm not very interested in dragons
      І`m busy a little, i had info that i can find a map that i need here\n""")
            self.parent.text.npc("What map do you say you need ?\n", begin_txt="Frank")
            self.parent.text.you("Old map of the former school of magicians Howard\n")
            self.parent.text.npc("I can get it for you, if you'll done my request\n\n",begin_txt="Frank")
            print("""
                                    #######################################################
                                    ~~~~~~          !  Flight like a bird?           ~~~~~~
                                    ~~~~~~~~~~~~       No, like a DRAGON !!    ~~~~~~~~~~~~
                                    #######################################################
                                    |                                                     |
                                    | Frank wants to learn to fly, but not like a bird,   |
                                    | like a DRAGON!                                      |
                                    | Help him make a costume for flights                 |
                                    |                                                     |  
                                    |     I found everything needed for the costume,      |
                                    |     but i do not have yet 100 feathers              |
                                    |                                                     |
                                    |  Reward:  35 coins   +  Ancient map of Howard       |
                                    |                                                     |
                                    #######################################################
                                    |     1.Accept             |         2.Decline        |
                                    #######################################################\n""")
            player_choose2 = input(" > ")
            if player_choose2 == "1":
                self.parent.text.you("Okay, I'll go look elsewhere")
                time.sleep(3)
                chicken_find()
                time.sleep(3)
                print(" ")
                self.parent.text.you("Hi, here are your feathers\n")
                self.parent.text.npc("Great, great, great. Give it to me\n", begin_txt="Frank")
                print("""
                        #######################################################
                        ~~~~~~          !  Flight like a bird?           ~~~~~~
                        ~~~~~~~~~~~~       No, like a DRAGON !!    ~~~~~~~~~~~~
                        #######################################################
                        |                      Done!                          |
                        | Frank wants to learn to fly, but not like a bird,   |
                        | like a DRAGON!                                      |
                        | Help him make a costume for flights                 |
                        |                                                     |
                        #######################################################
                        |     35 coins           |   Ancient map of Howard    |
                        #######################################################\n
                                           """)
                self.parent.myPlayer.cash += 35
                self.parent.zonemap['c2']['SOLVED'] = True
                self.parent.myPlayer.inventory.pop(10)
                self.parent.myPlayer.inventory.insert(10, 'Ancient map of Howard')

            elif player_choose2 == "2":
                print("As you wish!\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c2()

    def quest_c3(self):
        print(' ')
        self.parent.text.system(text=""" - Welcome to the Well of Dragons -\n""")
        self.parent.text.system(
            " Choose one of the below answers\n  1. Go to tavern\n  2. Go to town market\n  3. Get out\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1' and self.parent.zonemap['c3']['SOLVED1'] is False:

            # TAVERN
            print(' ')
            self.parent.text.system(" You walk into a crowdy place full of warriors mages and drunkards\n")
            self.parent.text.npc(" Hey there!, what are you doing in tis town?\n", begin_txt='Little John')
            self.parent.text.you(
                f" Hi, I am {self.parent.myPlayer.name}. I wanna kill Elminster, and save the princes\n")
            self.parent.text.npc(" Ah! You are lucky today. I will have a job for you!\n",
                                 begin_txt='Litte John')
            self.parent.text.you(" Keep talking\n")
            self.parent.text.npc("The magician Elminster has many strong beasts in his possession, but the Dragon is his favorite and most powerful.\n             If you kill him then you will have a better chance to kill him and save the princess.\n             And we will be able to survive next winter\n", begin_txt='Litte John')
            self.parent.text.you(f" Plus you {self.parent.myPlayer.name} will still receive a reward for killing the dragon. You will receive 200 coins\n")
            print("""
        #######################################################
        ~~~~~~~~~         !  Dragon killer            ~~~~~~~~~
        #######################################################
        |                                                     |
        |  Kill the dragon that terrorizes the whole valley.  |
        |  Residents will thank you generously                |  
        |                                                     |
        |  Reward:  200 coins   +  Rare item                  |
        |                                                     |
        #######################################################
        |     1.Accept             |         2.Decline        |
        #######################################################\n""")
            response_2 = input(" >  ")
            response_2 = str(response_2).lower()
            if response_2 == '1':
                self.parent.text.you(" I will kill the monster\n")
                self.parent.fight_dragon()
                if self.parent.myPlayer.HP < 0:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                    self.quest_c3()
                elif self.parent.myPlayer.HP > 0:
                    print("""
            #######################################################
            ~~~~~~~~~         !  Dragon killer            ~~~~~~~~~
            #######################################################
            |                                                     |
            |  Kill the dragon that terrorizes the whole valley.  |
            |  Residents will thank you generously                |  
            |                                                     |
            |                                                     |
            #######################################################
            |        + 200 coins        + Dragon Heart            |
            #######################################################\n""")
                    self.parent.myPlayer.cash += 200
                    self.parent.myPlayer.xp += 250
                    self.parent.myPlayer.inventory.pop(11)
                    self.parent.myPlayer.inventory.insert(11, 'Dragon heart')
                    self.parent.zonemap['c3']['SOLVED1'] = True
                    self.parent.text.system('You received 200 coins, and dragon heart\n')
            elif response_2 == '2':
                self.parent.text.you(" I do not hurt animals. Even dangerous ones\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c3()
        elif response == '2' and self.parent.zonemap['c3']['SOLVED2'] is False:
            self.parent.text.npc("Good afternoon, young man, did you know that you were cursed?\n",begin_txt="Shona")
            self.parent.text.you("Whaaaat !?!?\n")
            self.parent.text.npc("If you do not remove this curse, you may die soon\n", begin_txt="Shona")
            self.parent.text.you("And how do I take it off\n")
            self.parent.text.npc("Play one game with me, if you manage to win, I will help you for free. However, if you lose you will have to pay for help 50 coins\n", begin_txt="Shona")
            print("""
            
                                #######################################################
                                ~~~~~~              !  Gambler                   ~~~~~~
                                #######################################################
                                |                                                     |
                                |    You know you're cursed. Do you want to play      |
                                |    with Shona so she can take it of the curse       |
                                |    for free?                                        |
                                |                                                     |
                                |  Reward:  Shona will take off the curse for free    |
                                |                                                     |
                                #######################################################
                                |         1. Yes           |         2. Nope          |
                                #######################################################\n""")
            player_choise = input(" > ")
            if player_choise == "1":
                self.parent.text.npc("""The rules are simple. We will play the times.I drag a card then you drag a card.
        Bigger card win. Whoever wins 2 attempts wins 
        When you would be ready, press enter\n""",begin_txt="Shona")
                input(" > ")
                self.parent.text.you("Allright, lets get it\n")
                attempts = 3
                you = 0
                shon = 0
                while attempts != 0:
                    if shon >= 2:
                        self.parent.text.npc("Hurray i have won\n", begin_txt="Shona")
                        self.parent.text.npc("So if you want to take off this curse, pay 50 \n", begin_txt="Shona")
                        self.parent.text.system(
                            " Choose \n  1. Pay to take off the curse\n  2. Do not pay\n",
                            txt_only=True)
                        curse_choose = input(" > ")
                        if curse_choose == '1':
                            self.parent.myPlayer.cash -= 50
                            self.parent.text.system("You have been deceived, by the thief\n")
                            self.parent.zonemap['c3']['SOLVED2'] = True
                            break
                        elif curse_choose == '2':
                            self.parent.text.you("Nooope\n")
                            break
                    elif you == 2:
                        self.parent.text.npc("WHAT !?\n",begin_txt="Shona")
                        self.parent.text.you("Hurray i have won\n")
                        self.parent.text.you("So do what you promised\n")
                        self.parent.text.npc("Do you seriously believe this ??\n", begin_txt="Shona")
                        self.parent.text.system("  1.Either you pay me what you promised or I call a guard\n  2.Get out of here while you can\n",txt_only=True)
                        robber_fate = input(" > ")
                        if robber_fate == '1':
                            self.parent.text.npc("Okay, I just wanted to play with someone\n", begin_txt="Shona")
                            self.parent.myPlayer.cash += 50
                            self.parent.myPlayer.xp += 50
                            self.parent.zonemap['c3']['SOLVED2'] = True
                            break
                        elif robber_fate == '2':
                            self.parent.text.npc("Okay, just don't call them", begin_txt="Shona")
                            self.parent.myPlayer.xp += 100
                            self.parent.zonemap['c3']['SOLVED2'] = True
                            break
                    elif shon <= 2:
                        cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'Joker']
                        your_card = random.choice(cards)
                        if your_card == 'Joker':
                            cards.pop(9)
                        shon_card = random.choice(cards)
                        print(f" ~ You`ve get {your_card}\n")
                        print(f" ~ Shon gets {shon_card}\n")
                        if your_card == '6':
                            if shon_card == '6':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            elif shon_card == 'A':
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1

                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == '7':
                            if shon_card == '6':
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == '7':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == '8':
                            if shon_card in ['6', '7']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == '8':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == '9':
                            if shon_card in ['6', '7', '8']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == '9':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == '10':
                            if shon_card in ['6', '7', '8', '9']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == '10':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == 'J':
                            if shon_card in ['6', '7', '8', '9', '10']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == 'J':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == 'Q':
                            if shon_card in ['6', '7', '8', '9', '10', 'J']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == 'Q':
                                self.parent.text.system("You got the same cards\n")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                shon += 1
                                attempts -= 1
                        elif your_card == 'K':
                            if shon_card in ['6', '7', '8', '9', '10', 'J', 'Q']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == 'K':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == 'K':
                            if shon_card in ['6', '7', '8', '9', '10', 'J', 'Q']:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                            elif shon_card == 'K':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            else:
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                        elif your_card == 'A':
                            if shon_card == 'A':
                                self.parent.text.system("You got the same cards\n")
                                input("To play next one press Enter")
                            elif shon_card == 'Joker':
                                self.parent.text.system("Shon won this attempt\n")
                                input("To play next one press Enter")
                                shon += 1
                                attempts -= 1
                            else:
                                self.parent.text.system("You won this attempt\n")
                                input("To play next one press Enter")
                                attempts -= 1
                                you += 1
                        else:
                            self.parent.text.system("You won this attempt\n")
                            input("To play next one press Enter")
                            attempts -= 1
                            you += 1
                            cards.insert(9, 'Joker')
        elif response == '2' and self.parent.zonemap['c3']['SOLVED2'] is True:
            # TOWN MARKET
            self.parent.text.you(" Hmmm, I'm hungry. Let's buy something to eat\n")
            self.parent.text.system(
                " Choose one of the below answers\n 1. Buy an apple - 10 coins (+10HP)\n 2. Buy a piece of cake - 18 coins (+30HP)\n 3. Buy a bread - 25 coins (+50HP)\n 4. Buy piece of dried meat - 50 coins (+100HP)\n", txt_only=True)
            response_3 = input(" >  ")
            response_3 = str(response_3).lower()
            if response_3 == '1' and self.parent.myPlayer.cash >= 10:
                self.parent.text.system("You eat an apple\n", txt_only=True)
                self.parent.myPlayer.HP += 10
                self.parent.myPlayer.cash -= 10
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '2' and self.parent.myPlayer.cash >= 18:
                self.parent.text.system("You eat a piece of cake\n", txt_only=True)
                self.parent.myPlayer.HP += 30
                self.parent.myPlayer.cash -= 18
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '3' and self.parent.myPlayer.cash >= 25:
                self.parent.text.system("You eat a bread\n", txt_only=True)
                self.parent.myPlayer.HP += 50
                self.parent.myPlayer.cash -= 25
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '4' and self.parent.myPlayer.cash >= 50:
                self.parent.text.system("You eat a piece of dried meat\n", txt_only=True)
                self.parent.myPlayer.HP += 100
                self.parent.myPlayer.cash -= 50
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c3()
        elif response == "3":
            self.parent.text.system("Have a nice day !\n")
        elif response == '1' and self.parent.zonemap['c3']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to town market\n')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_c3()

    def quest_c4(self, response=None):
        if not response:
            print(' ')
            self.parent.text.system(
                text=""" - Welcome to the Yarlford -\n""")
            self.parent.text.system(""" You can go to:\n  1. City center\n  2. Grass meadow\n  3. Get out\n""", txt_only=True)
        player_choose = input(" > ")
        if player_choose == "1" and self.parent.zonemap['c4']['SOLVED1'] is False:
            self.parent.text.system(text=""" You meet a funny person on your way\n""")
            self.parent.text.npc(text="""Hey buddy, I'm a local jester.\n""", begin_txt='Jester')
            self.parent.text.you(text='Oh great... can you just let me go and leave me alone?\n')
            self.parent.text.npc(text="""No. Can I go with you? Please. I have no idea how to fight BUT\n""", begin_txt='Jester')
            self.parent.text.npc(text="""I know how to sing!\n""", begin_txt='Jester')
            self.parent.text.you(text="Please don't..\n")
            self.parent.text.npc(text="""Let us make a deal. If my song will be great enough for you, you will take me as your companion. Do you agree?\n""", begin_txt='Jester')
            self.parent.text.you(text="Hmm I guess there is no other way to get rid of you.. so yes\n")

            self.parent.text.system(
                f" Choose next sentence\n  1. Oh {self.parent.myPlayer.name} the Great warrior\n  2. Oh valley of plenty\n  3. Once upon a time\n",
                txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.npc(text=f"Oh {self.parent.myPlayer.name} the Great warrior\n", begin_txt='Jester')
            elif response == '2':
                self.parent.text.npc(text=f"Oh valley of plenty\n", begin_txt='Jester')
            elif response == '3':
                self.parent.text.npc(text=f"Once upon a time\n", begin_txt='Jester')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c4(response)

            self.parent.text.system(
                f" Choose next sentence\n  1. The weather is so nice yesterday!\n  2. {self.parent.myPlayer.name} and his best companiooon\n  3. Who let the dogs out?!\n",
                txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.npc(text=f"The weather is so nice yesterday!\n", begin_txt='Jester')
            elif response == '2':
                self.parent.text.npc(text=f"{self.parent.myPlayer.name} and his best companiooon\n", begin_txt='Jester')
            elif response == '3':
                self.parent.text.npc(text=f"Who let the dogs out?!\n", begin_txt='Jester')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c4(response)

            self.parent.text.system(
                f" Choose next sentence\n  1. Roses are red\n  2. La la lalala\n  3. Pam pa ram pam pam\n",
                txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.npc(text=f"Roses are red\n", begin_txt='Jester')
            elif response == '2':
                self.parent.text.npc(text=f"La la lalala\n", begin_txt='Jester')
            elif response == '3':
                self.parent.text.npc(text=f"Pam pa ram pam pam\n", begin_txt='Jester')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c4(response)
            self.parent.text.you(text="OK STOP, please\n")
            self.parent.text.npc(text=f"Do you like it my lord?\n", begin_txt='Jester')
            self.parent.text.you(text="It was the worst thing I have ever heard\n")
            self.parent.text.npc(text=f"Ah, no one gets my songs. They are so deep\n         Can you then at least help me with samll amount of cash?\n", begin_txt='Jester')
            self.parent.text.system(
                f" Choose answer\n  1. Yes (-10 coins)\n  2. No\n",
                txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response in ('1', 'yes') and self.parent.myPlayer.cash >= 10:
                self.parent.myPlayer.cash -= 10
                self.parent.myPlayer.xp += 150
                self.parent.text.you(text="Yes, here you go\n")
                self.parent.text.npc(text=f"Thank you my lord\n", begin_txt='Jester')
                self.parent.text.system(text='Your give 10 coins')
                self.parent.zonemap['c4']['SOLVED1'] = True
            elif response in ('2', 'no'):
                self.parent.myPlayer.xp += 130
                self.parent.text.you(text="No, I don't think you deserve it\n")
                self.parent.text.npc(text=f"Then Bye\n", begin_txt='Jester')
                self.parent.zonemap['c4']['SOLVED1'] = True
            else:
                self.parent.text.danger('Wrong input or lack of money\n', begin_txt='SYSTEM')
                self.quest_c4(response)
        elif player_choose == "2":
            print(" ")
            self.parent.text.system("Welcome to the meadow here you can find a lot various herbs and even you have chanse to find fiery flower\n         (write 'search' or write 'end')\n")
            find_grass = True
            i = 0
            while find_grass is not False:
                sujestion = input(" > ")
                if sujestion == "search":
                    found_chanse = random.randint(0, 100)
                    if found_chanse <= 75:
                        self.parent.text.system(" You couldnt find anything !\n")
                    elif 75 < found_chanse <= 95:
                        if '-' in self.parent.myPlayer.inventory:
                            if i == 0:
                                self.parent.text.you("hooray i found heal grass, it would , help me to do heal potion\n")
                                self.parent.myPlayer.inventory.pop(5)
                                self.parent.myPlayer.inventory.insert(5, 'Heal grass')
                                i += 1
                            elif i == 1:
                                self.parent.text.you("hooray i found heal grass, it would , help me to do heal potion\n")
                                self.parent.myPlayer.inventory.pop(6)
                                self.parent.myPlayer.inventory.insert(6, 'Heal grass')
                                i += 1
                            elif i == 2:
                                self.parent.text.you("hooray i found heal grass, it would , help me to do heal potion\n")
                                self.parent.myPlayer.inventory.pop(7)
                                self.parent.myPlayer.inventory.insert(7, 'Heal grass')
                                i += 1
                            else:
                                self.parent.text.you("It`s to heavy, i cant take anymore heal grass\n")
                    elif 95 < found_chanse <= 100 and "Fiery flower" not in self.parent.myPlayer.inventory:
                        self.parent.text.you("No way! I found fiery flower! And strange jewelry \n")
                        self.parent.myPlayer.inventory.pop(10)
                        self.parent.myPlayer.inventory.insert(10, 'Strange Jewelery')
                        self.parent.myPlayer.inventory.pop(12)
                        self.parent.myPlayer.inventory.insert(12, 'Fiery flower')
                    else:
                        self.parent.text.you("Its not my day...\n")
                elif sujestion == "end":
                    find_grass = False

            #### STOLEN JEWELRY
            if 'Strange Jewelery' in self.parent.myPlayer.inventory:
                print(" ")
                print("""
        ###########################################################################################
        ###########################################################################################
        |                                                                                         |
        |    !!!  Warning                                                                         |                    
        |   !!! An unexpected quest. The result of this quest will show whether you will survive  |
        |                                                                                         | 
        ###########################################################################################
        ###########################################################################################\n""")
                self.parent.text.npc("Good afternoon, could you show me everything you have?\n", begin_txt="Royal guard")
                self.parent.text.you("Why i should to do that ?\n")
                self.parent.text.npc("We know it was you who stole the jewelry\n              Either you voluntarily show what you have, or we will immediately take you to the grate\n",
                                        begin_txt="Royal guard")
                self.parent.text.system(
                    " Choose:\n  1. Run\n  2. Stay and show\n",
                    txt_only=True)
                jewelery_show = input(" > ")
                if jewelery_show == '1':
                    available_locations = ['Boar trail', 'Fairies cave', "Shepherd's columns", 'Foggy forest']
                    guard_searches = random.choice(available_locations)
                    self.parent.text.system(
                        """You successfully escaped from the guard in heavy armor.
         BUT You will be searched, so you need to hide somewhere for the night and then run away somewhere\n""")
                    print("""

            #######################################################
            ~~~~~~  !  Quieter than water, lower than grass  ~~~~~~
            #######################################################
            |                                                     |
            |   They want to accuse you of a crime you did not    |
            |   commit. Choose a place where they will not find   |
            |   you.                                              |
            |                                                     |
            |                                                     |
            #######################################################
            #######################################################\n""")
                    self.parent.text.system(
                        " Choose were do you wanna stay\n  1.Boar trail\n  2.Fairies cave\n  3.Shepherd's columns\n  4.Foggy forest\n",
                        txt_only=True)
                    hide_place = input(" > ")
                    if hide_place == '1':
                        your_place = 'Boar trail'
                        if your_place == guard_searches:
                            self.parent.text.danger("They founded you\n", begin_txt="SYSTEM")
                            print("""
                                       /%/@&@%@&&%%###%
                                      @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                      ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                       &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                       ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                       %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                       (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                       /*%%&%%&@(((//////////////((@&%&#   
                                       *(%%&&%&@#####((((((((((((#@@%#&% 
                                       (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                       %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                       #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                       (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                       (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                       /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                       %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                       ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                       #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                       #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                       (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                       %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                       %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                       ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                       /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                         &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                         &&&&&&@.  ..  .   .  .. &&@%&&%    
                                         &&%%%&% ..  ..  .. ..  %@@@&&%%
                                         &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                         &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                         &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                         &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                         &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                        .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
             @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                     &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                       @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                      %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  
                      
                      
        oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
         `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
          `888. .8'   888      888  888       8        888      888  888   888          888      888 
           `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
            `888'     888      888  888       8        888      888  888   888    "     888      888 
             888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
            o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   
                                                                                           
                     You were convicted and executed for a crime you did not commit  \n""")
                            sys.exit()
                        else:
                            self.parent.myPlayer.inventory.pop(10)
                            self.parent.myPlayer.inventory.insert(10, '-')
                            self.parent.zonemap['c4']['SOLVED2'] = True
                            self.parent.text.system("You successfully waited for the night. The guards must have thought that you lost, and been killed by wild beasts\n")
                    elif hide_place == '2':
                        your_place = 'Fairies cave'
                        if your_place == guard_searches:
                            self.parent.text.danger("They founded you\n", begin_txt="SYSTEM")
                            print("""
                                                       /%/@&@%@&&%%###%
                                                      @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                                      ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                                       &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                                       ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                                       %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                                       (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                                       /*%%&%%&@(((//////////////((@&%&#   
                                                       *(%%&&%&@#####((((((((((((#@@%#&% 
                                                       (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                                       %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                                       #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                                       (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                                       (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                                       /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                                       %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                                       ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                                       #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                                       #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                                       (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                                       %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                                       %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                                       ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                                       /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                                         &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                                         &&&&&&@.  ..  .   .  .. &&@%&&%    
                                                         &&%%%&% ..  ..  .. ..  %@@@&&%%
                                                         &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                                         &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                                         &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                                         &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                                         &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                                        .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
                             @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                                @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                                     &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                                       @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                                      %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  


                        oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
                         `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
                          `888. .8'   888      888  888       8        888      888  888   888          888      888 
                           `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
                            `888'     888      888  888       8        888      888  888   888    "     888      888 
                             888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
                            o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   

                                     You were convicted and executed for a crime you did not commit  \n""")
                            sys.exit()
                        else:
                            self.parent.myPlayer.inventory.pop(10)
                            self.parent.myPlayer.inventory.insert(10, '-')
                            self.parent.zonemap['c4']['SOLVED2'] = True
                            self.parent.text.system("You successfully waited for the night. The guards must have thought that you lost, and been killed by wild beasts\n")
                    elif hide_place == '3':
                        your_place = "Shepherd's columns"
                        if your_place == guard_searches:
                            self.parent.text.danger("They founded you\n", begin_txt="SYSTEM")
                            print("""
                                                       /%/@&@%@&&%%###%
                                                      @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                                      ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                                       &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                                       ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                                       %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                                       (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                                       /*%%&%%&@(((//////////////((@&%&#   
                                                       *(%%&&%&@#####((((((((((((#@@%#&% 
                                                       (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                                       %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                                       #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                                       (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                                       (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                                       /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                                       %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                                       ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                                       #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                                       #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                                       (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                                       %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                                       %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                                       ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                                       /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                                         &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                                         &&&&&&@.  ..  .   .  .. &&@%&&%    
                                                         &&%%%&% ..  ..  .. ..  %@@@&&%%
                                                         &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                                         &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                                         &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                                         &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                                         &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                                        .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
                             @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                                @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                                     &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                                       @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                                      %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  


                        oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
                         `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
                          `888. .8'   888      888  888       8        888      888  888   888          888      888 
                           `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
                            `888'     888      888  888       8        888      888  888   888    "     888      888 
                             888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
                            o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   

                                     You were convicted and executed for a crime you did not commit  \n""")
                            sys.exit()
                        else:
                            self.parent.myPlayer.inventory.pop(10)
                            self.parent.myPlayer.inventory.insert(10, '-')
                            self.parent.zonemap['c4']['SOLVED2'] = True
                            self.parent.text.system("You successfully waited for the night. The guards must have thought that you lost, and been killed by wild beasts\n")
                    elif hide_place == '4':
                        your_place = 'Foggy forest'
                        if your_place == guard_searches:
                            self.parent.text.danger("They founded you\n", begin_txt="SYSTEM")
                            print("""
                                                       /%/@&@%@&&%%###%
                                                      @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                                      ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                                       &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                                       ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                                       %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                                       (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                                       /*%%&%%&@(((//////////////((@&%&#   
                                                       *(%%&&%&@#####((((((((((((#@@%#&% 
                                                       (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                                       %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                                       #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                                       (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                                       (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                                       /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                                       %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                                       ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                                       #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                                       #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                                       (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                                       %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                                       %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                                       ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                                       /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                                         &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                                         &&&&&&@.  ..  .   .  .. &&@%&&%    
                                                         &&%%%&% ..  ..  .. ..  %@@@&&%%
                                                         &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                                         &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                                         &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                                         &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                                         &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                                        .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
                             @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                                @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                                     &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                                       @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                                      %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  


                        oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
                         `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
                          `888. .8'   888      888  888       8        888      888  888   888          888      888 
                           `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
                            `888'     888      888  888       8        888      888  888   888    "     888      888 
                             888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
                            o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   

                                     You were convicted and executed for a crime you did not commit  \n""")
                            sys.exit()
                        else:
                            self.parent.myPlayer.inventory.pop(10)
                            self.parent.myPlayer.inventory.insert(10, '-')
                            self.parent.zonemap['c4']['SOLVED2'] = True
                            self.parent.text.system("You successfully waited for the night. The guards must have thought that you lost, and been killed by wild beasts\n")
                elif jewelery_show == '2':
                    print("""
                                                           /%/@&@%@&&%%###%
                                                          @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                                          ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                                           &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                                           ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                                           %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                                           (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                                           /*%%&%%&@(((//////////////((@&%&#   
                                                           *(%%&&%&@#####((((((((((((#@@%#&% 
                                                           (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                                           %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                                           #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                                           (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                                           (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                                           /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                                           %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                                           ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                                           #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                                           #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                                           (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                                           %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                                           %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                                           ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                                           /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                                             &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                                             &&&&&&@.  ..  .   .  .. &&@%&&%    
                                                             &&%%%&% ..  ..  .. ..  %@@@&&%%
                                                             &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                                             &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                                             &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                                             &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                                             &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                                            .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
                                 @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                                    @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                                         &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                                           @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                                          %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  


                            oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
                             `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
                              `888. .8'   888      888  888       8        888      888  888   888          888      888 
                               `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
                                `888'     888      888  888       8        888      888  888   888    "     888      888 
                                 888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
                                o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   

                                         You were convicted and executed for a crime you did not commit  \n""")
                    sys.exit()
                else:
                    print("""
                                                                               /%/@&@%@&&%%###%
                                                                              @%%&%%&%@@%%&&&%&%%&&@%%##%%&%%&%%%.    
                                                                              ((@@%&%&@&%%%&&%&#%&&%&%@&&&&%%%#&% 
                                                                               &%&&&%%%@.  ..  /(% .  .. @@@&%&#%  
                                                                               ((&&%%%%@.  ..  &(&/.  .. @@@&%&&#   
                                                                               %(%%%&%%@ ..  .#&(%. ..  .@%&%&&@/
                                                                               (@%%%&&&&#((((((((/(((((((##@%&&%,  
                                                                               /*%%&%%&@(((//////////////((@&%&#   
                                                                               *(%%&&%&@#####((((((((((((#@@%#&% 
                                                                               (#&%%&&&@%%%%%%%###### .. &@@%%%%  
                                                                               %(%%%&%%@%%%%%%%%.  .  .. &@@%%%%  
                                                                               #(%%#&&%@###  ..  .. ..  .@@&%%&%
                                                                               (@&%%&%&@.  ..  ..  .  .. &@@%%&&    
                                                                               (/&&%&%%@.  ..  .   .  .. @@@%%%%   
                                                                               /%&&%%%%@ ..  ..  .. ..  .&@&%%&#
                                                                               %/&%#%%&@.  ..  ..  .  .. %@@%%#%    
                                                                               ##%%#%%&@.  ..  ..  .  .. &@&%%#%    
                                                                               #(%&%%&&@ ..  ..  .. ..  .&@&%%&%
                                                                               #(&@&&%@@.  ..  ..  .  .. &@&#%&#  
                                                                               (%@@&&%&@.  ..  .   .  .. @@&%%#%   
                                                                               %*&&%&&&@ ..  ..  .. ..  .@@&%%#%
                                                                               %(%%%&%%@.  ..  ..  .  .. @@@#%%%  
                                                                               ###&&&&&@.  ..  ..  .  .. @&&%%%% 
                                                                               /(%&&&&&@ ..  ..  .. ..   &&@&&%%
                                                                                 &&%&&&@.  ..  ..  .  .. @@@%%&% 
                                                                                 &&&&&&@.  ..  .   .  .. &&@%&&%    
                                                                                 &&%%%&% ..  ..  .. ..  %@@@&&%%
                                                                                 &&%%%%#&& ..  ..  .  ..@@@@%%%%   
                                                                                 &&&%%&%&  ..  ..  .  ..#@@@%&%& 
                                                                                 &&&%%%&&&.  ..  .. ..,(%@@@&%&%
                                                                                 &&&%&%&&&&@.  ..  /*&&%&@@@&&&%  
                                                                                 &%&%%&@&&&&%&&&&&%%&%.,#%@%&%&%  
                                                                                .&&&%%#@.,,,&@&&&&%%%,,,*@@@&%@%,
                                                     @                      ###&@@@.,//&@@&&&@@&&@&@@&@%&@#(,*****    
                                                        @&.   .  ......,..#%#&@#@@&&@@&@@&%%&&&@@@&&&&@@%%#&#%%@#,
                                                             &@............###&@@@&@&&@@@&@&&%@@@%@%@@%###((//,,,.
                                                               @@,,,,,,,,,(##@@&@&@&@@@@####(((((((////****,,*,.,,    
                                                              %@@&&&&&@#(/((////////**/************,,*,,,,..,,....  


                                                oooooo   oooo   .oooooo.   ooooo     ooo      oooooooooo.   ooooo oooooooooooo oooooooooo.   
                                                 `888.   .8'   d8P'  `Y8b  `888'     `8'      `888'   `Y8b  `888' `888'     `8 `888'   `Y8b  
                                                  `888. .8'   888      888  888       8        888      888  888   888          888      888 
                                                   `888.8'    888      888  888       8        888      888  888   888oooo8     888      888 
                                                    `888'     888      888  888       8        888      888  888   888    "     888      888 
                                                     888      `88b    d88'  `88.    .8'        888     d88'  888   888       o  888     d88' 
                                                    o888o      `Y8bood8P'     `YbodP'         o888bood8P'   o888o o888ooooood8 o888bood8P'   

                                                             You were convicted and executed for a crime you did not commit  \n""")
                    sys.exit()
            if self.parent.zonemap['c4']['SOLVED2'] is False:
                self.parent.text.system("Not a bad place, I may come back here someday...\n")
        elif player_choose == "3":
            self.parent.text.system("Have a nice day !\n")
        elif player_choose == "1" and self.parent.zonemap['c4']['SOLVED1'] is True:
            self.parent.text.system(' You have already passed this quest, try to go to town market\n')

    def quest_c5(self):

        def boss_fight_harder():
            print(" ")
            self.parent.text.you(
                text='I am finally here, and I will finally be able to free this region from this tyrant\n')
            self.parent.text.system(" You have opened the hall door\n")
            self.parent.text.danger(
        """Interesting, interesting .... Another pig came to play !\n       Well, show our guest what hospitality is\n""",begin_txt="Elminster")
            if "Abyssal sword" in self.parent.myPlayer.inventory:
                self.parent.text.danger("Whaat ?!? Abyssal sword ??\n",begin_txt="Elminster")
                self.parent.text.system("You have kiled every sodsiers\n")
            if "Abyssal sword" not in self.parent.myPlayer.inventory:
                self.parent.boss_soldiers_harder()
            self.parent.text.danger(
                """You not only dare to appear on my territory, but also killed my warriors.
            Well, nothing, I'll take care of you, and then call other soldiers and destroy Wellock.\n""",
                begin_txt="Elminster")
            print("""
                                ###########################################
                                ~~~~~~        Final boss fight       ~~~~~~
                                ###########################################
                                |                                         |
                                | Defeat the Elmister, and return         |
                                | the princes to the kingdom              |
                                |                                         |
                                |     The fate of the whole kingdom       |
                                |              lies on you                |
                                |                                         |
                                ###########################################
                                ###########################################\n""")
            defeated = False
            boss_hp = 900
            boss_def = 90
            while defeated is not True:
                if boss_hp != 0:
                    boss_atempt = 2
                    while boss_atempt != 0:
                        boss_atack = random.randint(1, 3)
                        if boss_atack == 1:
                            self.parent.text.system("He cast a spell on you, try to dodge!(write 'dodge')\n")
                            player_dodge_choose = input(" > ")
                            if player_dodge_choose == "dodge":
                                player_dodge = random.randint(1, 5)
                                if player_dodge in [1, 2, 3]:
                                    self.parent.text.system("You have successfully dodged!\n")
                                    boss_atempt -= 1
                                elif player_dodge == 4:
                                    self.parent.text.system("You dodged badly and received part of the damage\n")
                                    self.parent.myPlayer.HP -= 10
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                                elif player_dodge == 5:
                                    self.parent.text.system("You failed with dodging and received whole damage\n")
                                    self.parent.myPlayer.HP -= 25
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                            else:
                                self.parent.text.system("You failed with dodging and received whole damage\n")
                                self.parent.myPlayer.HP -= 25
                                self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                boss_atempt -= 1
                        if boss_atack == 2:
                            self.parent.text.system("He begins to cast spells, interrupt him until he not finished(write 'broke')\n")
                            player_interupt_choose = input(" > ")
                            if player_interupt_choose == "broke":
                                player_interupt = random.randint(1, 5)
                                if player_interupt in [1, 2, 3]:
                                    self.parent.text.system("You have successfully broke his caste\n")
                                    boss_atempt -= 1
                                elif player_interupt == 4:
                                    self.parent.text.system("You did not manage to stop him, but you jumped in a moment and therefore get only part of the damage\n")
                                    self.parent.myPlayer.HP -= 18
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                                elif player_interupt == 5:
                                    self.parent.text.system("You failed to stop him and received a spell right in the face\n")
                                    self.parent.myPlayer.HP -= 30
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                            else:
                                self.parent.text.system(
                                    "You failed to stop him and received a spell right in the face\n")
                                self.parent.myPlayer.HP -= 30
                                self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                boss_atempt -= 1
                        if boss_atack == 3:
                            self.parent.text.system("He summoned 5 soldiers, but they look weak\n")
                            self.parent.fight_boss_soldiers()
                            boss_atempt -= 1
                    boss_atempt = 2
                    self.parent.text.you("Haha apparently he needs time to recover mana, this is my chance!\n")
                    player_choise = False
                    while player_choise is False:
                        self.parent.text.system(" How do you want to attack?\n   1. Beat\n   2. Spell\n   3. Use an item\n   4. Heal\n", txt_only=True)
                        player_atempt = input(" > ")
                        if player_atempt == "1":
                            if "Antimagic staff" not in self.parent.myPlayer.inventory:
                                if self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is False:
                                    print(self.parent.zonemap['a3']['ASISTANT-WARRIOR'])
                                    damage = self.parent.myPlayer.STR
                                    damage -= boss_def
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print("here 1")
                                    print(boss_hp)
                                    player_choise = True
                                elif self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
                                    damage = self.parent.myPlayer.STR
                                    damage += 45
                                    damage -= boss_def
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print("here 2")
                                    print(boss_hp)
                                    player_choise = True
                            elif "Antimagic staff" in self.parent.myPlayer.inventory:
                                if self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is False:
                                    damage = self.parent.myPlayer.STR
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print(boss_hp)
                                    player_choise = True
                                elif self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
                                    damage = self.parent.myPlayer.STR
                                    damage += 45
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print(boss_hp)
                                    player_choise = True
                        elif player_atempt == "2":
                            if "Antimagic staff" not in self.parent.myPlayer.inventory:
                                if self.parent.myPlayer.job == "mage":
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
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "3":
                                        if self.parent.myPlayer.MP >= 80:
                                            self.parent.myPlayer.MP -= 80
                                            damage = 120
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "4":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 62
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "5":
                                        if self.parent.myPlayer.MP >= 32:
                                            self.parent.myPlayer.MP -= 32
                                            damage = 70
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "6":
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 120
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                ### warrior spels
                                elif self.parent.myPlayer.job == 'warrior':
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
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 35
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 50
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                #### ranger spels
                                elif self.parent.myPlayer.job == 'ranger':
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
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 70
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 45
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                            elif "Antimagic staff" in self.parent.myPlayer.inventory:
                                if self.parent.myPlayer.job == "mage":
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
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "3":
                                        if self.parent.myPlayer.MP >= 80:
                                            self.parent.myPlayer.MP -= 80
                                            damage = 120
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "4":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 62
                                            boss_hp -= damage
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "5":
                                        if self.parent.myPlayer.MP >= 32:
                                            self.parent.myPlayer.MP -= 32
                                            damage = 70
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "6":
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 120
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    ### warrior spels
                                elif self.parent.myPlayer.job == 'warrior':
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
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 35
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 50
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    #### ranger spels
                                elif self.parent.myPlayer.job == 'ranger':
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
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 70
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 45
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                        elif player_atempt == "3":
                            self.parent.text.system("Which element do you want to use?\n")
                            if "Heal pousion" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 1. Heal pousion\n", txt_only=True)
                            if "Throwing knife" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 2. Throwing knife\n", txt_only=True)
                            if "Antimagic staff" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 3. Antimagic staff\n", txt_only=True)

                            elment_choose = input(" > ")
                            if elment_choose == "1":
                                if self.heal_use == 3:
                                    self.parent.myPlayer.inventory.pop(5)
                                    self.parent.myPlayer.inventory.insert(5, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    print(self.parent.myPlayer.HP)
                                    self.heal_use -= 1
                                    player_choise = True
                                elif self.heal_use == 2:
                                    self.parent.myPlayer.inventory.pop(6)
                                    self.parent.myPlayer.inventory.insert(6, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.heal_use -= 1
                                    print(self.parent.myPlayer.HP)
                                    player_choise = True
                                elif self.heal_use == 1:
                                    self.parent.myPlayer.inventory.pop(7)
                                    self.parent.myPlayer.inventory.insert(7, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.heal_use -= 1
                                    print(self.parent.myPlayer.HP)
                                    player_choise = True
                            elif elment_choose == "2":
                                if self.knife_use == 2:
                                    self.parent.myPlayer.inventory.pop(2)
                                    self.parent.myPlayer.inventory.insert(2, '-')
                                    boss_hp -= 50
                                    print(boss_hp)
                                    self.knife_use -= 1
                                    player_choise = True
                                elif self.knife_use == 1:
                                    self.parent.myPlayer.inventory.pop(3)
                                    self.parent.myPlayer.inventory.insert(3, '-')
                                    boss_hp -= 50
                                    print(boss_hp)
                                    self.knife_use -= 1
                                    player_choise = True
                            elif elment_choose == "3":
                                boss_def = 0
                                print(boss_def)
                                self.parent.text.system(" Elminster do not have defense anymore\n", txt_only=True)
                                player_choise = True
                            else:
                                self.parent.text.system("You have no items you can use\n")
                        elif player_atempt == "4":
                            if self.parent.zonemap['a2']['ASISTANT-HEALER'] is False:
                                self.parent.myPlayer.HP += random.randrange(10, 40)
                                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP and self.parent.myPlayer.MP >= 10:
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.parent.myPlayer.MP -= 9
                                else:
                                    print(" You have not enoght mana or you health is full")
                            elif self.parent.zonemap['a2']['ASISTANT-HEALER'] is True:
                                print(self.parent.zonemap['a2']['ASISTANT-HEALER'])
                                self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                self.parent.myPlayer.MP = self.parent.myPlayer.maxMP
                            self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                        elif player_atempt == "exit":
                            self.quest_c5()
                if boss_hp == 0:
                    defeated = True
                    self.parent.final_titles()

        def boss_fight():
            print(" ")
            self.parent.text.you(
                text='I am finally here, and I will finally be able to free this region from this tyrant\n')
            self.parent.text.system(" You have opened the hall door\n")
            self.parent.text.danger(
        """Interesting, interesting .... Another pig came to play !\n       Well, show our guest what hospitality is\n""",begin_txt="Elminster")
            self.parent.text.you("They wont come to help you\n")
            self.parent.text.danger(
                """You not only dare to appear on my territory, but also killed my warriors.
            Well, nothing, I'll take care of you, and then call other soldiers and destroy Wellock.\n""",
                begin_txt="Elminster")
            print("""
                                ###########################################
                                ~~~~~~        Final boss fight       ~~~~~~
                                ###########################################
                                |                                         |
                                | Defeat the Elmister, and return         |
                                | the princes to the kingdom              |
                                |                                         |
                                |     The fate of the whole kingdom       |
                                |              lies on you                |
                                |                                         |
                                ###########################################
                                ###########################################\n""")
            defeated = False
            boss_hp = 900
            boss_def = 90
            while defeated is not True:
                if boss_hp != 0:
                    boss_atempt = 2
                    while boss_atempt != 0:
                        boss_atack = random.randint(1, 3)
                        if boss_atack == 1:
                            self.parent.text.system("He cast a spell on you, try to dodge!(write 'dodge')\n")
                            player_dodge_choose = input(" > ")
                            if player_dodge_choose == "dodge":
                                player_dodge = random.randint(1, 5)
                                if player_dodge in [1, 2, 3]:
                                    self.parent.text.system("You have successfully dodged!\n")
                                    boss_atempt -= 1
                                elif player_dodge == 4:
                                    self.parent.text.system("You dodged badly and received part of the damage\n")
                                    self.parent.myPlayer.HP -= 10
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                                elif player_dodge == 5:
                                    self.parent.text.system("You failed with dodging and received whole damage\n")
                                    self.parent.myPlayer.HP -= 25
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                            else:
                                self.parent.text.system("You failed with dodging and received whole damage\n")
                                self.parent.myPlayer.HP -= 25
                                self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                boss_atempt -= 1
                        if boss_atack == 2:
                            self.parent.text.system("He begins to cast spells, interrupt him until he not finished(write 'broke')\n")
                            player_interupt_choose = input(" > ")
                            if player_interupt_choose == "broke":
                                player_interupt = random.randint(1, 5)
                                if player_interupt in [1, 2, 3]:
                                    self.parent.text.system("You have successfully broke his caste\n")
                                    boss_atempt -= 1
                                elif player_interupt == 4:
                                    self.parent.text.system("You did not manage to stop him, but you jumped in a moment and therefore get only part of the damage\n")
                                    self.parent.myPlayer.HP -= 18
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                                elif player_interupt == 5:
                                    self.parent.text.system("You failed to stop him and received a spell right in the face\n")
                                    self.parent.myPlayer.HP -= 30
                                    self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                    boss_atempt -= 1
                            else:
                                self.parent.text.system(
                                    "You failed to stop him and received a spell right in the face\n")
                                self.parent.myPlayer.HP -= 30
                                self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                                boss_atempt -= 1
                        if boss_atack == 3:
                            self.parent.text.system("He summoned 5 soldiers, but they look weak\n")
                            self.parent.fight_boss_soldiers()
                            boss_atempt -= 1
                    boss_atempt = 2
                    self.parent.text.you("Haha apparently he needs time to recover mana, this is my chance!\n")
                    player_choise = False
                    while player_choise is False:
                        self.parent.text.system(" How do you want to attack?\n   1. Beat\n   2. Spell\n   3. Use an item\n   4. Heal\n", txt_only=True)
                        player_atempt = input(" > ")
                        if player_atempt == "1":
                            if "Antimagic staff" not in self.parent.myPlayer.inventory:
                                if self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is False:
                                    print(self.parent.zonemap['a3']['ASISTANT-WARRIOR'])
                                    damage = self.parent.myPlayer.STR
                                    damage -= boss_def
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print("here 1")
                                    print(boss_hp)
                                    player_choise = True
                                elif self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
                                    damage = self.parent.myPlayer.STR
                                    damage += 45
                                    damage -= boss_def
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print("here 2")
                                    print(boss_hp)
                                    player_choise = True
                            elif "Antimagic staff" in self.parent.myPlayer.inventory:
                                if self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is False:
                                    damage = self.parent.myPlayer.STR
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print(boss_hp)
                                    player_choise = True
                                elif self.parent.zonemap['a3']['ASISTANT-WARRIOR'] is True:
                                    damage = self.parent.myPlayer.STR
                                    damage += 45
                                    boss_hp -= damage
                                    if boss_hp < 0:
                                        boss_hp = 0
                                    print(boss_hp)
                                    player_choise = True
                        elif player_atempt == "2":
                            if "Antimagic staff" not in self.parent.myPlayer.inventory:
                                if self.parent.myPlayer.job == "mage":
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
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "3":
                                        if self.parent.myPlayer.MP >= 80:
                                            self.parent.myPlayer.MP -= 80
                                            damage = 120
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "4":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 62
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "5":
                                        if self.parent.myPlayer.MP >= 32:
                                            self.parent.myPlayer.MP -= 32
                                            damage = 70
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "6":
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 120
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                ### warrior spels
                                elif self.parent.myPlayer.job == 'warrior':
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
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 35
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 50
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                #### ranger spels
                                elif self.parent.myPlayer.job == 'ranger':
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
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 70
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 45
                                            damage -= boss_def
                                            if damage < 0:
                                                damage = 0
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                            elif "Antimagic staff" in self.parent.myPlayer.inventory:
                                if self.parent.myPlayer.job == "mage":
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
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 60
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "3":
                                        if self.parent.myPlayer.MP >= 80:
                                            self.parent.myPlayer.MP -= 80
                                            damage = 120
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "4":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 62
                                            boss_hp -= damage
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "5":
                                        if self.parent.myPlayer.MP >= 32:
                                            self.parent.myPlayer.MP -= 32
                                            damage = 70
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "6":
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 120
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    ### warrior spels
                                elif self.parent.myPlayer.job == 'warrior':
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
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 35
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 25:
                                            self.parent.myPlayer.MP -= 25
                                            damage = 50
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    #### ranger spels
                                elif self.parent.myPlayer.job == 'ranger':
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
                                        if self.parent.myPlayer.MP >= 50:
                                            self.parent.myPlayer.MP -= 50
                                            damage = 70
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                                    elif telling == "2":
                                        if self.parent.myPlayer.MP >= 20:
                                            self.parent.myPlayer.MP -= 20
                                            damage = 45
                                            boss_hp -= damage
                                            player_choise = True
                                        else:
                                            print(" You have not enough mana points")
                        elif player_atempt == "3":
                            self.parent.text.system("Which element do you want to use?\n")
                            if "Heal pousion" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 1. Heal pousion\n", txt_only=True)
                            if "Throwing knife" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 2. Throwing knife\n", txt_only=True)
                            if "Antimagic staff" in self.parent.myPlayer.inventory:
                                self.parent.text.system(" 3. Antimagic staff\n", txt_only=True)

                            elment_choose = input(" > ")
                            if elment_choose == "1":
                                if self.heal_use == 3:
                                    self.parent.myPlayer.inventory.pop(5)
                                    self.parent.myPlayer.inventory.insert(5, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    print(self.parent.myPlayer.HP)
                                    self.heal_use -= 1
                                    player_choise = True
                                elif self.heal_use == 2:
                                    self.parent.myPlayer.inventory.pop(6)
                                    self.parent.myPlayer.inventory.insert(6, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.heal_use -= 1
                                    print(self.parent.myPlayer.HP)
                                    player_choise = True
                                elif self.heal_use == 1:
                                    self.parent.myPlayer.inventory.pop(7)
                                    self.parent.myPlayer.inventory.insert(7, '-')
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.heal_use -= 1
                                    print(self.parent.myPlayer.HP)
                                    player_choise = True
                            elif elment_choose == "2":
                                if self.knife_use == 2:
                                    self.parent.myPlayer.inventory.pop(2)
                                    self.parent.myPlayer.inventory.insert(2, '-')
                                    boss_hp -= 50
                                    print(boss_hp)
                                    self.knife_use -= 1
                                    player_choise = True
                                elif self.knife_use == 1:
                                    self.parent.myPlayer.inventory.pop(3)
                                    self.parent.myPlayer.inventory.insert(3, '-')
                                    boss_hp -= 50
                                    print(boss_hp)
                                    self.knife_use -= 1
                                    player_choise = True
                            elif elment_choose == "3":
                                boss_def = 0
                                print(boss_def)
                                self.parent.text.system(" Elminster do not have defense anymore\n", txt_only=True)
                                player_choise = True
                            else:
                                self.parent.text.system("You have no items you can use\n")
                        elif player_atempt == "4":
                            if self.parent.zonemap['a2']['ASISTANT-HEALER'] is False:
                                self.parent.myPlayer.HP += random.randrange(10, 40)
                                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP and self.parent.myPlayer.MP >= 10:
                                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                    self.parent.myPlayer.MP -= 9
                                else:
                                    print(" You have not enoght mana or you health is full")
                            elif self.parent.zonemap['a2']['ASISTANT-HEALER'] is True:
                                print(self.parent.zonemap['a2']['ASISTANT-HEALER'])
                                self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
                                self.parent.myPlayer.MP = self.parent.myPlayer.maxMP
                            self.parent.text.system(f"You have left: {self.parent.myPlayer.HP}\n", txt_only=True)
                        elif player_atempt == "exit":
                            self.quest_c5()
                if boss_hp == 0:
                    defeated = True
                    self.parent.final_titles()


        print(""" 
        
     .----------------. 
    | .--------------. |
    | |      _       | |
    | |     | |      | |  Hero, be careful, if you are not confident in your abilities, 
    | |     | |      | |  return to other locations and gain strength.
    | |     | |      | |  Mage Elminster is a tough opponent. 
    | |     |_|      | |  Take on this quest, only if you have collected all the things you need.
    | |     (_)      | |
    | '--------------' |
     '-----------------' \n""")
        self.parent.text.system(" Choose one of the below answers\n  1. Go straight to castle\n  2. Walk on the outer territory\n  3. Go to gain strength\n", txt_only=True)
        final_bose = input(" > ")
        if final_bose == "1":
            boss_fight_harder()
        elif final_bose == "2":
            if "Ancient map of Howard" in self.parent.myPlayer.inventory:
                self.parent.text.system(
                    "You approached to the drawbridge. You had no choice but to walk across the bridge\n")
                self.parent.text.danger("You were noticed by 3 guards\n", begin_txt="SYSTEM")
                self.parent.fight_soldiers()
                self.parent.text.system("You have successfully cleared the bridge\n")
                self.parent.text.you("I think I could clear the surrounding area from the soldiers\n")
                storage_fight_done = False
                training_fight_done = False
                port_fight_done = False
                boss_fight_done = False
                while storage_fight_done is not True or training_fight_done is not True or port_fight_done is not True or boss_fight_done is not True:
                    self.parent.text.system(
                        """ Where are you going to go now?       
      1. Storage
      2. Training hall
      3. Port
      4. Main hall (probably Elminster here)\n""", begin_txt=True)
                    conversation_loop = input(" > ")
                    if conversation_loop == "1":
                        if storage_fight_done is False:
                            self.parent.storage_fight()
                            storage_fight_done = True
                        elif storage_fight_done is not False:
                            self.parent.text.system("You`ve cleared this part\n")
                    elif conversation_loop == "2":
                        if training_fight_done is False:
                            self.parent.training_fight()
                            training_fight_done = True
                        elif storage_fight_done is not False:
                            self.parent.text.system("You`ve cleared this part\n")
                    elif conversation_loop == "3":
                        if port_fight_done is False:
                            self.parent.port_fight()
                            port_fight_done = True
                        elif storage_fight_done is not False:
                            self.parent.text.system("You`ve cleared this part\n")
                    elif conversation_loop == "4":
                        if storage_fight_done is not True or training_fight_done is not True or port_fight_done is not True:
                            boss_fight_harder()
                            break
                        elif storage_fight_done is True and training_fight_done is True and port_fight_done is True:
                            boss_fight()
                            break
                    else:
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        self.quest_c5()
            elif "Ancient map of Howard" not in self.parent.myPlayer.inventory:
                i = 0
                while i < 78:
                    chanse_get_lost = random.randint(0, 100)
                    i = chanse_get_lost
                    self.parent.text.danger("You have lost !\n     -write 'look' to find way\n     -write 'give up' if you do not whant to fight\n")
                    destiny = input(" > ")
                    if destiny == "look":
                        self.parent.text.system("You continued to search\n")
                    elif destiny == "give up":
                        self.parent.text.system("You have accepted your destiny\n")
                        sys.exit()
                self.parent.text.system("You are lucky to cross the magic barrier\n")
                random_road = random.randint(1, 4)
                if random_road == 1:
                    self.parent.text.you(" Finally i get out, what is that -____-\n")
                    self.parent.text.you("I think I could clear the surrounding area from the soldiers\n")
                    self.parent.text.npc("Hey, what are you doing here ???\n", begin_txt="soldier")
                    self.parent.text.npc("It doesn't matter if he die anyway\n", begin_txt="soldier")
                    self.parent.storage_fight()
                    self.parent.text.you("Huh, I did it, let's move on to the next building\n")
                    self.parent.training_fight()
                    self.parent.text.you("Huh, I did it, there is one more and finally to the main dish of the day\n")
                    self.parent.port_fight()
                    boss_fight()
                elif random_road == 2:
                    self.parent.text.you(" Finally i get out, what is that -____-\n")
                    self.parent.text.you("I think I could clear the surrounding area from the soldiers\n")
                    self.parent.text.npc("Hey, what are you doing here ???\n", begin_txt="soldier")
                    self.parent.text.npc("It doesn't matter if he die anyway\n", begin_txt="soldier")
                    self.parent.training_fight()
                    self.parent.text.you("Huh, I did it, let's move on to the next building\n")
                    self.parent.port_fight()
                    self.parent.text.you("Huh, I did it, there is one more and finally to the main dish of the day\n")
                    self.parent.storage_fight()
                    boss_fight()
                elif random_road == 3:
                    self.parent.port_fight()
                    self.parent.text.you(" Finally i get out, what is that -____-\n")
                    self.parent.text.you("I think I could clear the surrounding area from the soldiers\n")
                    self.parent.text.npc("Hey, what are you doing here ???\n", begin_txt="soldier")
                    self.parent.text.npc("It doesn't matter if he die anyway\n", begin_txt="soldier")
                    self.parent.port_fight()
                    self.parent.text.you("Huh, I did it, let's move on to the next building\n")
                    self.parent.storage_fight()
                    self.parent.text.you("Huh, I did it, there is one more and finally to the main dish of the day\n")
                    self.parent.training_fight()
                    boss_fight()
                elif random_road == 4:
                    boss_fight()
        elif final_bose == "3":
            print(" Good choise!\n")
