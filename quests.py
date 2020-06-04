import random


class Quests:
    def __init__(self, parent):
        self.parent = parent
        self.stablequest = False
        self.minequest = False

    def quest_a3(self):
        def conversation_loop(response=None):
            if not response:
                self.parent.text.system(
                    text=""" A pilgrim stops you in the street. He asks if you'll be travelling east anytime soon.\nAlso, he offers 10 coins for taking him with you\n""")
            self.parent.text.system(" Choose one of the below answers\n1. Yes, I will take you there\n2. No\n",
                                    txt_only=True)
            response = input(">  ")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(text="OK, let's go\n")
                self.parent.myPlayer.move('right')
                self.parent.myPlayer.cash += 10
                self.parent.myPlayer.xp += 50
                self.parent.text.npc(text=""" Here, take it! I suppose you will make good use of it!\n""",
                                     begin_txt='Pilgrim')
                self.parent.text.system(text=""" The pilgrim gives you the promissed 10 coins!\n""")
            elif response in ('no', '2'):
                self.parent.text.you(text='Go away! I have more urgent business on my mind...\n')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)

        conversation_loop()

    def quest_a2(self):
        def conversation_loop(response=None):
            if not response:
                self.parent.text.system(
                    text=""" A stranger offers you to buy a lottery ticket.\nIf you win you will receive 25 coins. Are you interested?\nThe ticket costs 4 coins\n""")
            self.parent.text.system("Choose one of the below answers\n1. Yes\n2. No\n", txt_only=True)
            response = input(">  ")
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
                    else:
                        self.parent.text.danger(' YOU LOST!!!\n', begin_txt='SYSTEM')
                else:
                    self.parent.text.system(" You don't have enough money\n")
            elif response in ('no', '2'):
                self.parent.text.you(text="Maybe next time\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)

        conversation_loop()

    def quest_a1(self):
        def conversation_loop(response=None):
            if not response:
                self.parent.text.system(
                    text=""" While having a walk through the little town you find on ground a unique and strange golden ring.\nYou think that someone had to lose it here\nWhat do you want to do with it?\n""")
            self.parent.text.system(
                "Choose one of the below answers\n1. Go to mayor's mansion to leave it there\n2. Leave it on the ground\n3. Take it with you\n",
                txt_only=True)
            response = input(">  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.system(" You turn to a broad street leading to Mayor Habakuk's mansion\n")
                self.parent.text.npc(" Welcome traveller, what brings you to my town?\n", begin_txt='Habakuk')
                self.parent.text.you(
                    " Good afternoon Sir! I found this ring nearby. I thought that you might know who is the owner of it\n")
                self.parent.text.npc(" Oh! Thank you very much. This belongs to my beloved daughter!\n",
                                     begin_txt='Habakuk')
                self.parent.text.npc(" Take this small gift as a 'thank you' from me.", begin_txt='Habakuk')
                self.parent.text.you(" Thank you\n")
                self.parent.text.system(" You receive 100 coins\n")
                self.parent.myPlayer.cash += 100
                self.parent.myPlayer.xp += 150
            elif response == '2':
                self.parent.text.you(" Hmmm, I better leave it where it is so the one who lost it can find it\n")
                self.parent.myPlayer.xp += 30
            elif response == '3':
                self.parent.text.you(" What a lucky day! GOLD!\n")
                self.parent.text.system(" You receive 150 coins\n")
                self.parent.myPlayer.cash += 150
                self.parent.myPlayer.xp += 10
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)

        conversation_loop()

    def quest_b3(self):
        def conversation_loop(response=None):
            if not response:
                self.parent.text.system(
                    text=""" In a local tavern you spot a man wearing black cloak sitting in shady corner.\nYou approach him\n""")
                self.parent.text.npc(f" Hello {self.parent.myPlayer.name}?\n", begin_txt='The Gamer')
                self.parent.text.you(" HHhow you know my name?!\n")
                self.parent.text.npc(
                    f" Let's say... I know much...\n For example I know you will lose a guessing game with me!\n",
                    begin_txt='The Gamer')

            self.parent.text.system(
                "Choose one of the below answers\n1. Pfff. I can win with you. Let's play\n2. I'm out.. Bye\n3. How to play the game?\n",
                txt_only=True)
            response = input(">  ")
            response = str(response).lower()
            if response == '1':
                self.parent.text.you(" Pfff not possible. Let us have a quick round\n")
                tries = 5
                number = random.randint(1, 42)
                while True:
                    self.parent.text.npc("Guess a number between 1 and 42?\n", begin_txt='The Gamer')
                    your_guess = input(">  ")
                    try:
                        your_guess = int(your_guess)
                    except:
                        continue
                    if your_guess == number:
                        self.parent.text.npc("Wow! You won!. Take your money and come back again\n",
                                             begin_txt='The Gamer')
                        self.parent.myPlayer.cash += 100
                        self.parent.myPlayer.xp += 100
                        break
                    elif your_guess > number:
                        self.parent.text.npc("Nope, the number is too big\n", begin_txt='The Gamer')
                    elif your_guess < number:
                        self.parent.text.npc("No, the number is too small\n", begin_txt='The Gamer')
                    tries -= 1
                    if tries == 0:
                        self.parent.text.npc(f"It is too late {self.parent.myPlayer.name}. You lost the game\n",
                                             begin_txt='The Gamer')
                        break
            elif response == '2':
                self.parent.text.you(" If you say so.. Bye\n")
                self.parent.myPlayer.xp += 30
            elif response == '3':
                self.parent.text.you(" How to play the game?\n")
                self.parent.text.npc(
                    f" It is very simple, I will guess a number between 1 and 42 and will have guess it in several tries\n",
                    begin_txt='The Gamer')
                self.parent.text.you(" Sounds easy\n")
                conversation_loop(response)
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)

        conversation_loop()

    def quest_a5(self):
        def conversation_loop(response=None):
            if not response:
                print(""" You can go to:\n 1.Stable\n 2.Black ice mines""")
                answer = input(" > ")

                #### Stable quest
                if answer == '1' and self.stablequest == False:
                    print(""" An owner of the stable says: he's heard strange singing in the night in his stable, but whenever he goes out to look, he doesn't find anyone.\n If that wasn't strange enough, one morning he found scarecrows which was in a drawn circle on the porch""")
                    response = input(""" Could you help him understand what's going on?\n 1. Yes, I will take you there\n 2. No\n""")
                    response = str(response).lower()
                    if response in ('yes', '1'):
                        print(" YOU: * going to the stable *")
                        print(""" In the stable you found 3 things that can be associated with the dark cult:
  1. A dark substance that is mostly used by the dark cult in rituals
  2. Pieces of dark ice - used by the dark cult in rituals
  3. A piece of anarchist cloth - which is used by the dark cult to sew their clothes
  What will you show the owner to persuade him to turn to the royal guard ?
  (you have 1 attempt) """)
                        choise = input(" > ")
                        if choise == "1":
                            print(" Owner: Hmm ... this substance is also used in mines. This is not a reason to contact with the royal guard.")
                            self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                        if choise == "2":
                            print(" Owner: You're kidding, we're on Dwarven Valley, dark ice is everywhere!\n Get out of here !\n")
                            self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                        if choise == "3":
                            print(" Owner: Did you find it in the stable?!?! I will immediately notify the royal guards.\n Thank you very much hero\n Here is your reward")
                            self.parent.text.system(' Greeting you have got 50 xp, 20 coins')
                            self.parent.myPlayer.cash += 20
                            self.parent.myPlayer.xp += 50
                            self.stablequest = True
                    elif response in ('no', '2'):
                        print(""" You tell the owner to go away as you have more urgent business on your mind""")
                    else:
                        print(' Wrong input')
                        conversation_loop(response)

                 #### Mine Quest ill change it soon ( very similar to the quest on the a1
                elif answer == "2" and self.minequest == False:
                    print(" You met a dwarf!")
                    print(" The dwarf said he had a job for you\n He said he had lost an important tool on the outskirts, could you find for him his tool?\n if you succeed, he will reward you generously ")
                    response = input(""" Could you help him ?\n 1. Yes, I will take you there\n 2. No\n""")
                    response = str(response).lower()
                    if response in ('yes', '1'):
                        result = random.randint(1, 6)
                        self.parent.myPlayer.xp += 5
                        if result == 5:
                            self.parent.text.system(' YOU FIND IT!!!\n')
                            self.parent.text.system(' Dwarf give you your reward\n')
                            self.parent.text.system(' Greeting you have got 100 xp, 25 coins')
                            self.parent.myPlayer.cash += 25
                            self.parent.myPlayer.xp += 100
                            self.minequest = True
                        else:
                            self.parent.text.danger(' You`ve failed!\n', begin_txt='SYSTEM')
                    elif response in ('no', '2'):
                        self.parent.text.you(text="Maybe next time\n")
                    else:
                        self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                        conversation_loop(response)
                elif self.stablequest == True and self.minequest == False:
                    pself.parent.text.system(' You have already passed this quest, try to go to the mine')
                elif self.stablequest == False and self.minequest == True:
                    pself.parent.text.system(' You have already passed this quest, try to go to the stable')
                elif self.stablequest == True and self.minequest == True:
                    pself.parent.text.system(' You have already passed all quests, try to go to location')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                conversation_loop(response)

        conversation_loop()

