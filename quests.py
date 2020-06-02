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
                print('Wrong input')
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
            elif response in ('no', '2'):
                print(""" You tell the pilgrim to go away as you have more urgent business on your mind""")
            else:
                print('Wrong input')
                conversation_loop(response)
        conversation_loop()
