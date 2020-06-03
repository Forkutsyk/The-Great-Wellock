import random


class Quests:
    def __init__(self, parent):
        self.parent = parent

    def quest_a3(self):
        def conversation_loop(response=None):
            if not response:
                self.parent.text.system(text=""" A pilgrim stops you in the street. He asks if you'll be travelling east anytime soon.\nAlso, he offers 10 coins for taking him with you\n""")
            response = input(""" Choose one of the below answers\n1. Yes, I will take you there\n2. No\n""")
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
                self.parent.text.system(text=""" A stranger offers you to buy a lottery ticket.\nIf you win you will receive 25 coins. Are you interested?\nThe ticket costs 4 coins\n""")
            response = input("""Choose one of the below answers\n1. Yes\n2. No\n""")
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

    def quest_a5(self):
        def conversation_loop(response=None):
            if not response:
                print("""Yo u can go to:\n 1.Stable\n 2.Black ice mines""")
                answer = input(" > ")
                if answer == "1":
                    print(""" An owner of the stable says he's heard strange singing in the night in his stable, but whenever he goes out to look, he doesn't find anyone.\n If that wasn't strange enough, one morning he found scarecrows which was in a drawn circle on the porch""")
                    response = input(""" Could you help him understand what's going on?\n 1. Yes, I will take you there\n 2. No\n""")
                    response = str(response).lower()
                    if response in ('yes', '1'):
                        print(" ")
                    elif response in ('no', '2'):
                        print(""" You tell the farmer to go away as you have more urgent business on your mind""")
                    else:
                        print(' Wrong input')
                        conversation_loop(response)
                elif answer == "2":
                    print("...")

        conversation_loop()

