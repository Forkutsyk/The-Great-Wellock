import random


class Quests:
    def __init__(self, parent):
        self.parent = parent

    def quest_a3(self):
        def conversation_loop(response=None):
            if not response:
                print(""" A pilgrim stops you in the street. He asks if you'll be travelling east anytime soon.\nAlso, he offers 10 coins for taking him with you""")
            response = input(""" Choose one of the below answers\n1. Yes, I will take you there\n2. No\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.myPlayer.move('right')
                self.parent.myPlayer.cash += 10
                self.parent.myPlayer.xp += 50
                print(""" The pilgrim gives you the promissed 10 coins!""")
            elif response in ('no', '2'):
                print(""" You tell the pilgrim to go away as you have more urgent business on your mind""")
            else:
                print(' Wrong input')
                conversation_loop(response)
        conversation_loop()

    def quest_a2(self):
        def conversation_loop(response=None):
            if not response:
                print(""" A stranger offers you to buy a lottery ticket.\nIf you win you will receive 25 coins. Are you interested?\nThe ticket costs 4 coins""")
            response = input("""
                        Choose one of the below answers\n1. Yes\n2. No\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                if self.parent.myPlayer.cash >= 4:
                    self.parent.myPlayer.cash -= 4
                    self.parent.myPlayer.xp += 5
                    result = random.randint(1, 10)
                    if result == 10:
                        print(""" YOU WON!!!""")
                        print(""" YOU GOT 25 COINS PRIZE!!!""")
                        self.parent.myPlayer.cash += 25
                        self.parent.myPlayer.xp += 100
                    else:
                        print(""" YOU LOST!!!""")
                else:
                    print(" You don't have enough money")
            elif response in ('no', '2'):
                print(""" You tell the pilgrim to go away as you have more urgent business on your mind""")
            else:
                print('Wrong input')
                conversation_loop(response)

        conversation_loop()

    def quest_a5(self):
        def conversation_loop(response=None):
            if not response:
                print("""Yo u can go to:\n 1.Stable\n 2.Black ice mines""")
                answer = input(" > ")
                if answer == "1":
                    print(""" A owner of the stable says he's heard strange singing in the night in his stable, but whenever he goes out to look, he doesn't find anyone.\n If that wasn't strange enough, one morning he found scarecrows which was in a drawn circle on the porch""")
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

