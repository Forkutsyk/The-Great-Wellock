import random
import sys
import os

roadswrongs = 1
sproby = 0

class Quests:
    def __init__(self, parent):
        self.parent = parent
        self.quest1 = False
        self.quest2 = False
        self.home = False

    def quest_a2(self, response=None):
        if not response:
            self.parent.text.system(text=""" A stranger offers you to buy a lottery ticket.\nIf you win you will receive 25 coins. Are you interested?\nThe ticket costs 4 coins\n""")
        self.parent.text.system("Choose one of the below answers\n1. Yes\n2. No\n", txt_only=True)
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

    def quest_a3(self, response=None):
        if not response:
            self.parent.text.system(text=""" A pilgrim stops you in the street. He asks if you'll be travelling east anytime soon.\n          Also, he offers 10 coins for taking him with you\n""")
        self.parent.text.system(" Choose one of the below answers\n  1. Yes, I will take you there\n  2. No\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response in ('yes', '1'):
            self.parent.text.you(text="OK, let's go\n")
            self.parent.myPlayer.move('right')
            self.parent.myPlayer.cash += 10
            self.parent.myPlayer.xp += 50
            self.parent.text.npc(text=""" Here, take it! I suppose you will make good use of it!\n""", begin_txt='Pilgrim')
            self.parent.text.system(text=""" The pilgrim gives you the promissed 10 coins!\n""")
            self.parent.zonemap['a3']['SOLVED'] = True
        elif response in ('no', '2'):
            self.parent.text.you(text='Go away! I have more urgent business on my mind...\n')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a3(response)

    def quest_a4(self, response=None):
        def tavern():
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
                        self.parent.zonemap['a1']['SOLVED'] = True
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
                            "Yep, there are mage master Who lives somewhere in Nezeris\n            and another warrior master which lives somewhere in Blacklake\n            That's all what can I say",
                            begin_txt='The Gamer')
                        break
                    elif your_guess > number:
                        self.parent.text.npc("Nope, the number is too big\n", begin_txt='The Gamer')
                    elif your_guess < number:
                        self.parent.text.npc("No, the number is too small\n", begin_txt='The Gamer')
                    tries -= 1
                    if tries == 0:
                        self.parent.text.npc(f"It is too late {self.parent.myPlayer.name}. You lost the game\n", begin_txt='The Gamer')
                        break
            elif response == '2':
                self.parent.text.you(" If you say so.. Bye\n")
                self.parent.myPlayer.xp += 30
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                tavern()
        if not response:
            print("")
            self.parent.text.system(text=""" While having a walk through the little town you find on ground a unique and strange golden ring.\n You think that someone had to lose it here\n What do you want to do with it?\n""")
        self.parent.text.system(" Choose one of the below answers\n  1. Go to mayor's mansion to leave it there\n  2. Leave it on the ground\n  3. Take it with you\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1':
            self.parent.text.system(" You turn to a broad street leading to Mayor Habakuk's mansion\n")
            self.parent.text.npc(" Welcome traveller, what brings you to my town?\n", begin_txt='Habakuk')
            self.parent.text.you(" Good afternoon Sir! I found this ring nearby. I thought that you might know who is the owner of it\n")
            self.parent.text.npc(" Oh! Thank you very much. This belongs to my beloved daughter!\n", begin_txt='Habakuk')
            self.parent.text.npc(" Take this small gift as a 'thank you' from me.\n", begin_txt='Habakuk')
            self.parent.text.you(" Thank you\n")
            self.parent.text.system(" You receive 100 coins\n")
            self.parent.myPlayer.cash += 100
            self.parent.myPlayer.xp += 150
            self.parent.text.system(""" You are very hungry, look into the tavern, so as not to die from starving\n          1. Go to tabern\n          2. Continue the journey\n""")
            starv_danger = input(" > ")
            if starv_danger == "1":
                tavern()
            elif starv_danger == "2":
                self.parent.text.danger(""" - You've died from starvation -  """, begin_txt="SYSTEM")
                self.parent.text.system(" Reloading from the last ceckpoint\n")
                self.parent.text.system(" .................................\n", txt_only=True)
                os.system('cls')
                self.quest_a4()
        elif response == '2':
            self.parent.text.you(" Hmmm, I better leave it where it is so the one who lost it can find it\n")
            self.parent.myPlayer.xp += 30
            self.parent.text.system(""" You are very hungry, look into the tavern, so as not to die from starving\n          1. Go to tabern\n          2. Continue the journey\n""")
            starv_danger = input(" > ")
            if starv_danger == "1":
                tavern()
            elif starv_danger == "2":
                self.parent.text.danger(""" - You've died from starvation -  """, begin_txt="SYSTEM")
                self.parent.text.system(" Reloading from the last ceckpoint\n")
                self.parent.text.system(" .................................\n", txt_only=True)
                os.system('cls')
                self.quest_a4()
        elif response == '3':
            self.parent.text.you(" What a lucky day! GOLD!\n")
            self.parent.text.system(" You receive 150 coins\n")
            self.parent.myPlayer.cash += 150
            self.parent.myPlayer.xp += 10
            self.parent.text.system(""" You are very hungry, look into the tavern, so as not to die from starving\n          1. Go to tabern\n          2. Continue the journey\n""")
            starv_danger = input(" > ")
            if starv_danger == "1":
                tavern()
            elif starv_danger == "2":
                self.parent.text.danger(""" - You've died from starvation -  \n""", begin_txt="SYSTEM")
                self.parent.text.system(" Reloading from the last ceckpoint\n")
                self.parent.text.system(" .................................\n", txt_only=True)
                os.system('cls')
                self.quest_a4()
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a1(response)

    def quest_a5(self):
        self.parent.text.system(""" You can go to:\n 1.Stable\n 2.Black ice mines\n""")
        answer = input(" > ")
        print(" ")

        #### Stable quest
        if answer == '1' and self.quest1 is False:
            self.parent.text.npc(""" An owner of the stable says: he's heard strange singing in the night in his stable, but whenever he goes out to look, he doesn't find anyone.\n         If that wasn't strange enough, one morning he found scarecrows which was in a drawn circle on the porch""", begin_txt='Owner')
            response = input(""" Could you help him understand what's going on?\n 1. Yes, I will take you there\n 2. No\n""")
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
                    self.parent.text.npc(" Hmm ... this substance is also used in mines. This is not a reason to contact with the royal guard.", begin_txt='Owner')
                    self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                if choise == "2":
                    self.parent.text.npc(" You're kidding, we're on Dwarven Valley, dark ice is everywhere!\n Get out of here !\n", begin_txt='Owner')
                    self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                if choise == "3":
                    self.parent.text.npc(" Did you find it in the stable?!?! I will immediately notify the royal guards.\n Thank you very much hero\n Here is your reward\n", begin_txt='Owner')
                    self.parent.text.system(' Greeting you have got 50 xp, 20 coins\n')
                    self.parent.myPlayer.cash += 20
                    self.parent.myPlayer.xp += 50
                    self.quest1 = True
                    if self.quest2 is True:
                        self.parent.zonemap['a5']['SOLVED'] = True
                        self.parent.text.system("You`ve solved this location")
                        self.quest1 = False
                        self.quest2 = False

                elif response in ('no', '2'):
                    self.parent.text.system(""" You tell the owner to go away as you have more urgent business on your mind""")
                else:
                    self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    self.quest_a5()

        ### Mine quest
        elif answer == "2" and self.quest2 is False:
            self.parent.text.system(" You met a dwarf!\n")
            self.parent.text.npc(" The dwarf said he had a job for you\n         You look strong, could you help me with this mechanism? \n         You just need to hold on to this lever.But hold on tight, if you drop it, I will have to look for someone stronger.\n ", begin_txt='Dwarf')
            response = input(""" Could you help him ?\n   1. Yes, I will take you there\n   2. No\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                result = random.randint(1, 6)
                self.parent.myPlayer.xp += 5
                if result == 5:
                    self.parent.text.system(' You were strong enough to hold the lever!\n')
                    self.parent.text.system(' Dwarf give you your reward\n')
                    self.parent.text.system(' Greeting you have got 100 xp, 25 coins\n')
                    self.parent.myPlayer.cash += 25
                    self.parent.myPlayer.xp += 100
                    self.quest2 = True
                    if self.quest1 is True:
                        self.parent.zonemap['a5']['SOLVED'] = True
                        self.parent.text.system("You`ve solved this location")
                        self.quest1 = False
                        self.quest2 = False
                else:
                    self.parent.text.danger(' You`ve failed!\n', begin_txt='SYSTEM')
                    self.parent.text.system(" Try again later...")
            elif response in ('no', '2'):
                self.parent.text.you(text="Maybe next time\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)
        elif answer == "1" and self.quest1 is True and self.quest2 is False:
            self.parent.text.system(' You have already passed this quest, try to go to the mine')
        elif answer == "2" and self.quest1 is False and self.quest2 is True:
            self.parent.text.system(' You have already passed this quest, try to go to the stable')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a5()

    def quest_b1(self):
        self.parent.text.system(text=""" In tavern you see an old man with long beard\n""")
        self.parent.text.npc(text="""My name is Tetrex. I have been fighting all my life. Also if you pay me I can teach you some self defense technics that can help you survive in this world\n""", begin_txt='Old warrior')
        self.parent.text.you(text=f'Hello, I am {self.parent.myPlayer.name}\n It would be an honor to learn something from you\n')
        self.parent.text.npc(text="""Ok then, let us go to outside\n""", begin_txt='Old warrior')
        self.parent.text.system(text=""" After almost whole day of training you finally make it to increase you maximum HP\n""")
        self.parent.text.system(text=""" Your max HP increases by 30\n""")
        self.parent.myPlayer.maxHP += 30
        self.parent.text.npc(text="""My service is worth 50 coins\n""", begin_txt='Old warrior')
        self.parent.text.you(text="Here it is\n")
        self.parent.text.npc(text="""Thank you and good luck\n""", begin_txt='Old warrior')
        self.parent.zonemap['b1']['SOLVED'] = True

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
            print(mana_perfect)

            i = 0
            thrown_knifes = random.randint(2, 5)
            catch_chanse = 0
            print(thrown_knifes)

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
                if catch_chanse < 26:
                    y = random.randint(1, 4)
                    if y == 1:
                        print(" You catch knife1")
                        i += 1
                    else:
                        print("You didnt catch1")
                elif 25 < catch_chanse <= 50:
                    y = random.randint(1, 4)
                    if y in [1, 4]:
                        print(" You catch knife2")
                        i += 1
                    else:
                        print("You didnt catch2")
                elif 50 < catch_chanse <= 75:
                    y = random.randint(1, 4)
                    if y in [1, 2, 3]:
                        print(" You catch knife3")
                        i += 1
                    else:
                        print("You didnt catch3")
                elif 75 < catch_chanse <= 130:
                    print(" You catch knife4")
                    i += 1

            self.parent.text.npc(text="""Yo worked well. And now the last task!\n""", begin_txt='Gandalfux')
            self.parent.text.npc(text="""I want to test your courage and strength of spirit\n""", begin_txt='Gandalfux')
            self.parent.text.npc(text="""I will give you my staff, so you must pour your mana into it. And now  cross this homeless gorge. 
            Don't worry the levitation spell, I'll tell you, you just have to repeat me word for word.\n""",
                                 begin_txt='Gandalfux')
            self.parent.text.npc(text="""Ready ?\n""", begin_txt='Gandalfux')
            input(" > ")

            self.parent.text.you(text="""Ok lets start""")
            self.parent.text.npc(text="""Gaudeamus igitur\n""", begin_txt='Gandalfux')
            lev_spell_1 = input(" > ").lower()
            if lev_spell_1 != "gaudeamus igitur":
                self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
            self.parent.text.npc(text="""Juvenes dum sumus\n""", begin_txt='Gandalfux')
            lev_spell_2 = input(" > ").lower()
            if lev_spell_2 != "juvenes dum sumus":
                self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
            self.parent.text.npc(text="""Post jucundam juventutem\n""", begin_txt='Gandalfux')
            lev_spell_2 = input(" > ").lower()
            if lev_spell_2 != "post jucundam juventutem":
                self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
            self.parent.text.npc(text="""Nos habebit humus.\n""", begin_txt='Gandalfux')
            lev_spell_2 = input(" > ").lower()
            if lev_spell_2 != "nos habebit humus.":
                self.parent.text.danger('You cast the spell incorrectly and fell into the gorge\n', begin_txt='SYSTEM')
            self.parent.text.you(text="You step on the other end of the abyss\n")
            self.parent.text.npc(text="""You worked well. I think you're good enough to be my student!\n""",
                                 begin_txt='Gandalfux')

        if not response:
            self.parent.text.system(text=""" Close to a castle you meet a mage\n""")
            self.parent.text.npc(
                text="""People and other creatures call me Gandalfux. I have power over white magic\n""",
                begin_txt='Gandalfux')
            self.parent.text.you(text=f'Good day, I am {self.parent.myPlayer.name}\n Can you learn me something new?\n')
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
            self.parent.text.npc(text=f" Let go outside the town to the Gardens. I will teach you there\n",
                                 begin_txt='Gandalfux')
            self.parent.text.you(text="OK\n")
            self.parent.text.system(
                text='....After several hours of training. You start to think that this might actually not wor to learn anything from him\n')
            self.parent.text.system(f"Finally after many struggles you learn a new spell!\n", txt_only=True)
            self.parent.text.system(text='Your can now use Fire Ball special spell\n')
            self.parent.myPlayer.spells.append(self.parent.FireBall)
            self.parent.zonemap['b2']['SOLVED'] = True
        elif response in ('2', 'no'):
            self.parent.text.you(text="No, I don't think it is a good idea\n")
            self.parent.text.npc(text=f"Bye\n", begin_txt='Gandalfux')
        else:
            self.parent.text.danger('Wrong input or lack of money\n', begin_txt='SYSTEM')
            self.quest_b2(response)

    def quest_b3(self):
        def auction():
            self.parent.text.system("""\n  - On the auction - \n""", txt_only=True)
            self.parent.text.npc(" Ladies and gentlemen, and the current lot, is a house located on the edge of town\n", begin_txt='Auction leader')
            self.parent.text.npc(" The initial bet is 500 coins\n", begin_txt='Auction leader')
            ### first bet
            while True:
                self.parent.text.system("Write your bet using only nums\n", txt_only=True)
                bet = int(input(" > "))
                self.parent.text.npc(f" I hear {bet}\n", begin_txt='Auction leader')
                ### does not go further
                if bet >= 500 and bet<= 999:
                    if bet > 999:
                        self.parent.text.npc(" Greetings you won", begin_txt='Auction leader')
                        self.home = True
                        break
                    elif 500 < bet <= 999:
                        enemy_bet = random.randint(25, 100)
                        enemy_bet += bet
                        self.parent.text.npc(enemy_bet, begin_txt='Tretegors enemy')
                        self.parent.text.npc(f" I hear {enemy_bet}\n", begin_txt='Auction leader')
                else:
                    self.parent.text.system("""\n Write nums beetween 500 and 1000\n""", txt_only=True)
        if self.home == False:
            self.parent.text.system("\n  - Welcome to Absol -\n", txt_only=True)
            self.parent.text.system(""" You saw three soldiers werewolves attacking an elf\n""")
            self.parent.text.system(""" Do you wanna to help him\n    1.Yes\n    2.No\n""", txt_only=True)
            help_elf = input(" > ")
            if help_elf == "1":
                self.parent.text.danger(" Hey buddy do you know who we are?\n", begin_txt="Werewolve soldier")
                self.parent.fight_soldiers()
                self.parent.text.npc(" Oh thank you a brave hero, let me introduce myself my name is Tretogor\n", begin_txt='Tretogor')
                self.parent.text.you(f" Nice to meet Tratigor, my name is {self.parent.myPlayer.name}, now be more careful, see you\n")
                self.parent.text.npc(f" Plese, wait a minute {self.parent.myPlayer.name}! What would you like as a reward for my salvation?!\n",begin_txt='Tretogor')
                self.parent.text.you(" Thanks but I don't need anything, I'm in a hurry\n")
                self.parent.text.npc(" In that case, I have a little job for you. If you don't mind \n", begin_txt='Tretogor')
                self.parent.text.system(""" Do you wanna take the job\n    1.Yes\n    2.No\n""", txt_only=True)
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
                self.parent.text.danger(" Hey, you what are you staring ?!")
                self.text.danger(" Hey buddy do you know who we are?\n", begin_txt="Werewolve soldier")
                self.parent.fight_soldiers()
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b3()
        else:
            self.parent.text.system(""" You can rest here and train \n    1.rest\n    2.train\n""", txt_only=True)

    def quest_b4(self):
        self.parent.text.system("\n  - Welcome to Cardcaster -\n", txt_only=True)
        self.parent.text.npc("This is a charming city known for its smithies. If there would problems, do not worry, contact the guards.\n", begin_txt='Town Guardian')
        self.parent.text.system("""  You can go to:\n          1.Abandoned forge\n          2.Mysterious gorge\n""")
        answer = input(" > ")
        print(" ")

        def p_choise():
            self.parent.text.system(' What do you wanna to do:\n           1.Try to get out and teach manners, this guy\n           2.Just give up and die\n')
            answer_1 = input(" > ")

            if answer_1 == "1":
                chanse_of_GO = random.randint(1, 6)
                if chanse_of_GO == 5:
                    self.parent.text.system("Congratulations you got out of the trap\n")
                    self.parent.text.you(" Now that old man learns that it's better not to play with me\n")
                    self.parent.text.you(" Hmm and what i should to do now ?\n           1. Go to the local guards\n           2. Go to tavern to find out some ifo about him \n")
                    npc_asking =input(" > ")
                    if npc_asking == "1":
                        self.parent.text.system("You told everything to the guards, they promised to deal with him\n")
                    elif npc_asking == "2":
                        self.parent.text.you(" Maybe you know something about Abandoned forge near you tavern? \n")
                        self.parent.text.npc('Yes, it was destroyed 2 days ago because the owner was selling forbidden things.\n', begin_txt='The owner of the tavern')
                        self.parent.text.you(" And what does the owner look like, and is it possible to know where he is now \n")
                        self.parent.text.npc('it`s an ungle old man. And if you wanna i can tell you were is he hiding. \n', begin_txt='The owner of the tavern')
                        self.parent.text.system(' Few moments later...\n')
                        self.parent.text.you(" You have foud that man \n       It was a long 3 hours .... for him\n")
                        self.parent.myPlayer.maxHP += 20
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 150
                        self.parent.text.system(' Congratulations you have received 100 coins and a potion that increases health\n')
                        self.quest1 = True
                        if self.quest2 is True:
                            self.parent.zonemap['b4']['SOLVED'] = True
                            self.parent.text.system("You`ve solved this location")
                            self.quest1 = False
                            self.quest2 = False

                elif chanse_of_GO in [1, 2, 3, 4, 6]:
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
        if answer == '1' and self.quest1 is False:
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
        elif answer == '2' and self.quest2 is False:
            self.parent.text.system("""You went into a dark cave, the inhabitants say that a secret treasure is hidden here. 
         But no one don't want to say why no one has taken the treasure yet.
         Maybe it's a trap?!
""")
            self.parent.text.you("*It's too dark, maybe I should light a torch?*\n 1. Yes, i should\n 2. NO, no way\n")
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
                    self.parent.text.system(" Congratulations you have found a tresure 150 coins and a potion that increases strenghth\n ")
                    self.quest2 = True
                    if self.quest1 is True:
                        self.parent.zonemap['b4']['SOLVED'] = True
                        self.parent.text.system("You`ve solved this location")
                        self.quest1 = False
                        self.quest2 = False
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

        elif answer == "1" and self.quest1 is True and self.quest2 is False:
            self.parent.text.system(' You have already passed this quest, try to go to the gorge')
        elif answer == "2" and self.quest1 is False and self.quest2 is True:
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
                self.parent.text.system(
                    f" Choose option\n  1. Go to see the miller\n  2. Do not work\n", txt_only=True)
                response = input(" >  ")
                response = str(response).lower()
        if response == '1':
            if not action:
                self.parent.text.you(text=f"Hey, I am {self.parent.myPlayer.name}, I saw you job offer\n")
                self.parent.text.npc(text=f"Hi there\n", begin_txt='Miller')
                self.parent.text.npc(text=f"Great, how can I help you?\n", begin_txt='Miller')
            self.parent.text.system(
                f" Choose option\n1. Can you tell me more about the job?\n2. How long would I work?\n3. How much am I going to earn?\n4. OK, I want start working\n5. I have to go\n", txt_only=True)
            response = input(" >  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.you(text=f"Can you tell me more about the job?\n")
                self.parent.text.npc(text=f"I am looking for a man that can help me carrying my flour to my clients\n", begin_txt='Miller')
                self.quest_b5(response, True)
            elif response == '2':
                self.parent.text.you(text=f"2. How long would I work?\n")
                self.parent.text.npc(text=f"Only today. Until dawn\n", begin_txt='Miller')
                # TODO: to check why it crashes here
                self.quest_b5(response, True)
            elif response == '3':
                self.parent.text.you(text=f"How much am I going to earn?\n")
                self.parent.text.npc(text=f"100 coins paid after job\n", begin_txt='Miller')
                self.quest_b5(response, True)
            elif response == '4':
                self.parent.text.you(text=f"OK, I want start working?\n")
                self.parent.text.npc(text=f"Wonderfull! We can start straight away!\n", begin_txt='Miller')
                self.parent.text.system(text=""" After whole day of work you get paid by the miller. Also he lets you sleep in his mill so can recover a bit\n""")
                self.parent.myPlayer.cash += 100
                self.parent.myPlayer.HP += 25
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxMP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxMP
                self.parent.zonemap['b5']['SOLVED'] = True
            elif response == '5':
                self.parent.text.you(text=f"I have to go\n")
                self.parent.text.npc(text=f"Bye bye\n", begin_txt='Miller')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b5(response)

    def quest_c1(self):
        print(" to be continued")

    def quest_c2(self, response=None):
        raise NotImplementedError

    def quest_c3(self, response=None):
        if not response:
            self.parent.text.system(
                text=""" Welcome to the Well of Dragons \n People of this place believe dragons are indeed real creatures\n Some of the are even sure they have seen one!\n""")
        self.parent.text.system(
            " Choose one of the below answers\n  1. Go to tavern\n  2. Go to town market\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1':

            # TAVERN
            self.parent.text.system(" You walk into a crowdy place full of warriors mages and drunkards\n")
            self.parent.text.npc(" Hey there!, what are you doing in tis town?\n", begin_txt='Little John')
            self.parent.text.you(
                f" Hi, I am {self.parent.myPlayer.name}. I wanna kill Elminster, and save the princes\n")
            self.parent.text.npc(" Ah! You are lucky today. I will have a job for you!\n",
                                 begin_txt='Litte John')
            self.parent.text.you(" Keep talking\n")
            self.parent.text.npc(" The magician Elminster has many strong beasts in his possession, but the Dragon is his favorite and most powerful.\n If you kill him then you will have a better chance to kill him and save the princess.\n And we will be able to survive next winter\n", begin_txt='Litte John')
            self.parent.text.you(f" Plus you {self.parent.myPlayer.name}\n will still receive a reward for killing the dragon. You will receive 200 coins\n")
            self.parent.text.system(
                " Choose one of the below answers\n 1.  Accept the offer\n  2. Refuse\n", txt_only=True)
            response_2 = input(" >  ")
            response_2 = str(response_2).lower()
            if response_2 == '1':
                self.parent.text.you(" I will kill the monster\n")
                self.parent.fight_dragon()
                #self.parent.zonemap['c3']['SOLVED'] = True
                self.parent.myPlayer.cash += 200
                self.parent.myPlayer.xp += 250
                self.parent.text.system('You received 200 coins\n')
            elif response_2 == '2':
                self.parent.text.you(" I do not hurt animals. Even dangerous ones\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c3(response_2)
        elif response == '2':
            # TOWN MARKET
            self.parent.text.you(" Hmmm, I'm hungry. Let's buy something to eat\n")
            self.parent.text.system(
                " Choose one of the below answers\n 1. Buy an apple - 10 coins (+10HP)\n 2. Buy a piece of cake - 18 coins (+30HP)\n 3. Buy a bread - 25 coins (+50HP)\n 4. Buy piece of dried meat - 50 coins (+100HP)\n", txt_only=True)
            response_3 = input(" >  ")
            response_3 = str(response_3).lower()
            if response_3 == '1' and self.parent.myPlayer.cash >= 10:
                self.parent.text.system("You eat an apple\n", txt_only=True)
                self.parent.myPlayer.HP += 10
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '2' and self.parent.myPlayer.cash >= 18:
                self.parent.text.system("You eat a piece of cake\n", txt_only=True)
                self.parent.myPlayer.HP += 30
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '3' and self.parent.myPlayer.cash >= 25:
                self.parent.text.system("You eat a bread\n", txt_only=True)
                self.parent.myPlayer.HP += 50
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '4' and self.parent.myPlayer.cash >= 50:
                self.parent.text.system("You eat a piece of dried meat\n", txt_only=True)
                self.parent.myPlayer.HP += 100
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_c3(response_3)
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_c3(response)

    def quest_c4(self, response=None):
        if not response:
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
        self.parent.text.npc(text=f"Ah, no one gets my songs. They are so deep\n Can you then at least help me with samll amount of cash?\n", begin_txt='Jester')
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
            self.parent.zonemap['c4']['SOLVED'] = True
        elif response in ('2', 'no'):
            self.parent.myPlayer.xp += 130
            self.parent.text.you(text="No, I don't think you deserve it\n")
            self.parent.text.npc(text=f"Then Bye\n", begin_txt='Jester')
            self.parent.zonemap['c4']['SOLVED'] = True
        else:
            self.parent.text.danger('Wrong input or lack of money\n', begin_txt='SYSTEM')
            self.quest_c4(response)


