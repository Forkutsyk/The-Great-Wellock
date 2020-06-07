import random


class Quests:
    def __init__(self, parent):
        self.parent = parent
        self.something = True

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
                    self.parent.text.danger(' YOU LOST!!!\n', begin_txt='SYSTEM')
            else:
                self.parent.text.system(" You don't have enough money\n")
        elif response in ('no', '2'):
            self.parent.text.you(text="Maybe next time\n")
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a2(response)

    def quest_a1(self, response=None):
        if not response:
            self.parent.text.system(text=""" While having a walk through the little town you find on ground a unique and strange golden ring.\n You think that someone had to lose it here\n What do you want to do with it?\n""")
        self.parent.text.system("Choose one of the below answers\n 1. Go to mayor's mansion to leave it there\n 2. Leave it on the ground\n 3. Take it with you\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1':
            self.parent.text.system(" You turn to a broad street leading to Mayor Habakuk's mansion\n")
            self.parent.text.npc(" Welcome traveller, what brings you to my town?\n", begin_txt='Habakuk')
            self.parent.text.you(" Good afternoon Sir! I found this ring nearby. I thought that you might know who is the owner of it\n")
            self.parent.text.npc(" Oh! Thank you very much. This belongs to my beloved daughter!\n", begin_txt='Habakuk')
            self.parent.text.npc(" Take this small gift as a 'thank you' from me.", begin_txt='Habakuk')
            self.parent.text.you(" Thank you\n")
            self.parent.text.system(" You receive 100 coins\n")
            self.parent.myPlayer.cash += 100
            self.parent.myPlayer.xp += 150
            self.parent.zonemap['a1']['SOLVED'] = True
        elif response == '2':
            self.parent.text.you(" Hmmm, I better leave it where it is so the one who lost it can find it\n")
            self.parent.myPlayer.xp += 30
            self.parent.zonemap['a1']['SOLVED'] = True
        elif response == '3':
            self.parent.text.you(" What a lucky day! GOLD!\n")
            self.parent.text.system(" You receive 150 coins\n")
            self.parent.myPlayer.cash += 150
            self.parent.myPlayer.xp += 10
            self.parent.zonemap['a1']['SOLVED'] = True
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a1(response)

    def quest_b3(self, response=None):
        if not response:
            self.parent.text.system(text=""" In a local tavern you spot a man wearing black cloak sitting in shady corner.\nYou approach him\n""")
            self.parent.text.npc(f" Hello {self.parent.myPlayer.name}?\n", begin_txt='The Gamer')
            self.parent.text.you(" HHhow you know my name?!\n")
            self.parent.text.npc(f" Let's say... I know much...\n For example I know you will lose a guessing game with me!\n", begin_txt='The Gamer')
        self.parent.text.system("Choose one of the below answers\n1. Pfff. I can win with you. Let's play\n2. I'm out.. Bye\n3. How to play the game?\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1':
            self.parent.text.you("Pfff not possible. Let us have a quick round\n")
            tries = 5
            number = random.randint(1, 42)
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
                    self.parent.zonemap['b3']['SOLVED'] = True
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
        elif response == '3':
            self.parent.text.you(" How to play the game?\n")
            self.parent.text.npc(" It is very simple, I will guess a number between 1 and 42 and will have guess it in several tries\n", begin_txt='The Gamer')
            self.parent.text.you(" Sounds easy\n")
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_b3(response)

    def quest_a5(self):
        self.parent.text.system(""" You can go to:\n 1.Stable\n 2.Black ice mines\n""")
        answer = input(" > ")
        print(" ")

        #### Stable quest
        if answer == '1' and self.stablequest == False:
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
                    self.parent.text.system(' Greeting you have got 50 xp, 20 coins')
                    self.parent.myPlayer.cash += 20
                    self.parent.myPlayer.xp += 50
                    self.stablequest = True
                elif response in ('no', '2'):
                    self.parent.text.system(""" You tell the owner to go away as you have more urgent business on your mind""")
                else:
                    self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                    self.quest_a5()

        ### Mine quest
        elif answer == "2" and self.minequest == False:
            self.parent.text.system(" You met a dwarf!\n")
            self.parent.text.npc(" The dwarf said he had a job for you\nYou look strong, could you help me with this mechanism? \n You just need to hold on to this lever.But hold on tight, if you drop it, I will have to look for someone stronger.\n ", begin_txt='Dwarf')
            response = input(""" Could you help him ?\n 1. Yes, I will take you there\n 2. No\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                result = random.randint(1, 6)
                self.parent.myPlayer.xp += 5
                if result == 5:
                    self.parent.text.system(' You were strong enough to hold the lever!\n')
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
        elif answer == "1" and self.stablequest == True and self.minequest == False:
            self.parent.text.system(' You have already passed this quest, try to go to the mine')
        elif answer == "2" and self.stablequest == False and self.minequest == True:
            self.parent.text.system(' You have already passed this quest, try to go to the stable')
        elif answer in ['1', '2'] and self.stablequest == True and self.minequest == True:
            self.parent.zonemap['a5']['SOLVED'] = True
            self.parent.text.system(' You have already passed all quests, try to go to location')
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a5()

    ### parts of b4
    def randome_rode(self):
        true_road = []
        moves = ['^', '<', '>']
        for i in range(4):
            true_road.append(random.choice(moves))
            return true_road

    def get_road(self):
        player_road = []
        guess_road = input(" Give the path you want to go(^, <, >), do not separate, do not add other signs:  ")
        for i in range(len(guess_road)):
            player_road.append(guess_road[i])
            return player_road

    def check(self):
        global sproby
        global roadswrongs
        true_road = randome_rode()
        print(true_road)
        while roadswrongs != 0 and sproby < 10:  # ( i think stops here  :(  )
            roadswrongs = 0
            player_road = get_road()
            for i in range(0, 4):
                if player_road[i] in true_road:

                    if player_road[i] == true_road[i]:
                        print(" This part of the road is safe: ", format(player_road[i]), "On the ", i + 1, " place.")
                    else:
                        print(" Hmm, I have to use this part of the road elsewhere: ", format(player_road[i]),
                              "On the ", i + 1, " place.")
                        roadswrongs += 1
                else:
                    print(" If I go like that, I'll probably die: ", format(player_road[i]), "On the ", i + 1,
                          " place.")
                    roadswrongs += 1
            sproby += 1
        return true_road

    def quest_b4(self):
        self.parent.text.system("""You can go to:\n          1.Abandoned forge\n          2.Mysterious gorge\n""")
        answer = input(" > ")
        print(" ")

        #### Forge quest b4
        if answer == '1':
            self.parent.text.npc(""" Within is my granddaughter, could you save her?\n """, begin_txt='OWNER')
            response = input("""        Choose one of the below answers\n          1. Yes, I will save her\n          2. No, I'm sorry\n""")
            response = str(response).lower()
            if response in ('yes', '1'):
                self.parent.text.you(" * going to the forge *")
                self.parent.text.you(" The smithy is small, but I don't see anyone here", begin_txt='YOU(thoughts)')
                self.parent.text.you("Although, stop, I see something ....\n", begin_txt='YOU(thoughts)')
                self.parent.text.danger('\n', begin_txt=':~CRACK~')
                self.parent.text.you(" Aaaaaaa...\n")
                self.parent.text.system("You have fallen into a deep pit\n")
                self.parent.text.danger(' Ahahaa, your generous heart will destroy you ...\n         Accept your destiny and die like an animal\n', begin_txt='OWNER')
                self.parent.text.danger('*clatter....*\n')
                self.parent.text.system(' What do you wanna to do:\n           1.Try to get out and teach manners, this guy\n           2.Just give up and die\n')
                choise = input(" > ")
                if choise == "1":
                    i = False
                    while i == False:
                        try:
                            chanse = random.randint(1, 6)
                            if chanse == 5:
                                self.parent.text.system("Congratulations you got out of the trap\n")
                                i = True
                            else:
                                self.parent.text.system("You didn't succeed, try again\n")
                                self.parent.text.system(
                                    ' What do you wanna to do:\n           1.Try to get out and teach manners, this guy\n           2.Just give up and die\n')
                                p_choise()
                        except:
                            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                            p_choise()

                if choise == "2":
                    self.parent.text.npc(" You're kidding, we're on Dwarven Valley, dark ice is everywhere!\n Get out of here !\n", begin_txt='Owner')
                    self.parent.text.danger('You`ve failed !\n', begin_txt='SYSTEM')
                if choise == "3":
                    self.parent.text.npc(" Did you find it in the stable?!?! I will immediately notify the royal guards.\n Thank you very much hero\n Here is your reward\n",begin_txt='Owner')
                    self.parent.text.system(' Greeting you have got 50 xp, 20 coins')
                    self.parent.myPlayer.cash += 20
                    self.parent.myPlayer.xp += 50
                    self.stablequest = True
                elif response in ('no', '2'):
                    self.parent.text.system(""" You tell the owner to go away as you have more urgent business on your mind""")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b4()

        #### Gorge quest b4
        elif answer == '2':
            self.parent.text.system("""You went into a dark cave, the inhabitants say that a secret treasure is hidden here. 
         But no one don't want to say why no one has taken the treasure yet.
         Maybe it's a trap?!""")
            self.parent.text.you("*It's too dark, maybe I should light a torch?*\n 1. Yes, i should\n 2. NO, no way\n")
            response = input(" > ")
            response = str(response).lower()
            if response == '1':
                roadswrongs = 1
                sproby = 0
                def check():
                    global sproby
                    global roadswrongs
                    true_road = self.randome_rode()
                    print(true_road)
                    while roadswrongs != 0 and sproby < 10: #( i think stops here  :(  )
                        roadswrongs = 0
                        player_road = self.get_road()
                        for i in range(0, 4):
                            if player_road[i] in true_road:
                                if player_road[i] == true_road[i]:
                                    print(" This part of the road is safe: ", format(player_road[i]), "On the ", i + 1, " place.")
                                else:
                                    print(" Hmm, I have to use this part of the road elsewhere: ", format(player_road[i]), "On the ", i + 1, " place.")
                                    roadswrongs += 1
                            else:
                                print(" If I go like that, I'll probably die: ", format(player_road[i]), "On the ", i + 1, " place.")
                                roadswrongs += 1
                        sproby += 1
                    return true_road
                last = check()
                if roadswrongs == 0:
                    print(" I think this road will be safe, worth a try")
                else:
                    print(" Unfortunately you have made too many mistakes, the correct way is:  ", last)
            elif response == '2':
                self.parent.text.you(" Ohhh it's too dark, I can't see anything.\n", begin_txt='YOU(thoughts)')
                self.parent.text.danger(" *teeth grinding* ")
                self.parent.text.you(" Maybe, still i have to light a torch", begin_txt='YOU(thoughts)')
                self.parent.text.you("*light a torch*\n")
                self.parent.text.danger("*Gets a sword*\n\n", begin_txt='Falmer, which you have stepped on the foot')
                self.parent.text.system(' You almost died, this cave is full of falmers. You managed to escape, but you get a few wounds\n')
                self.parent.myPlayer.HP -= 30
                self.parent.text.system('You got 30 damage\n')
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_b4()

    def quest_c3(self, response=None):
        if not response:
            self.parent.text.system(
                text=""" Welcome to the Well of Dragons \n People of this place believe dragons are indeed real creatures\n Some of the are even sure they have seen one!\n""")
        self.parent.text.system(
            "Choose one of the below answers\n 1. Go to tavern\n 2. Go to town market\n", txt_only=True)
        response = input(" >  ")
        response = str(response).lower()
        if response == '1':

            # TAVERN
            self.parent.text.system(" You walk into a crowdy place full of warriors mages and drunkards\n")
            self.parent.text.npc(" Hey there!, what are you doing in tis town?\n", begin_txt='Little John')
            self.parent.text.you(
                f" Hi, I am {self.parent.myPlayer.name}. I think adventures are my destination\n")
            self.parent.text.npc(" Ah! You are lucky today. I will have a job for you!\n",
                                 begin_txt='Litte John')
            self.parent.text.you(" Keep talking\n")
            self.parent.text.npc(" A Dragon is kiling our cattle this year. If you make it to kill him we will be able to survive next winter\n", begin_txt='Litte John')
            self.parent.text.you(" Hah, but you have something to reward me the pleasure of killing a Dragon right??\n")
            self.parent.text.you(f" Do not worry {self.parent.myPlayer.name}\n You will receive 200 coins\n")
            self.parent.text.system(
                "Choose one of the below answers\n 1. Accept the offer\n 2. Refuse\n", txt_only=True)
            response_2 = input(" >  ")
            response_2 = str(response_2).lower()
            if response_2 == '1':
                self.parent.text.you(" I will kill the monster\n")
                self.parent.fight_dragon()
                self.parent.zonemap['c3']['SOLVED'] = True
                self.parent.myPlayer.cash += 200
                self.parent.myPlayer.xp += 250
                self.parent.text.system('You received 200 coins\n')
            elif response_2 == '2':
                self.parent.text.you(" I do not hurt animals. Even dangerous ones\n")
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a1(response_2)
        elif response == '2':
            # TOWN MARKET
            self.parent.text.you(" Hmmm, I'm hungry. Let's buy something to eat\n")
            self.parent.text.system(
                "Choose one of the below answers\n 1. Buy an apple (+10HP)\n 2. Buy a piece of cake (+30HP)\n3. Buy a bread (+50HP)\n4. Buy piece of dried meat (+100HP)\n", txt_only=True)
            response_3 = input(" >  ")
            response_3 = str(response_3).lower()
            if response_3 == '1':
                self.parent.text.system("You eat an apple\n", txt_only=True)
                self.parent.myPlayer.HP += 10
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '2':
                self.parent.text.system("You eat a piece of cake\n", txt_only=True)
                self.parent.myPlayer.HP += 30
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '3':
                self.parent.text.system("You eat a bread\n", txt_only=True)
                self.parent.myPlayer.HP += 50
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            elif response_3 == '4':
                self.parent.text.system("You eat a piece of dried meat\n", txt_only=True)
                self.parent.myPlayer.HP += 100
                if self.parent.myPlayer.HP > self.parent.myPlayer.maxHP:
                    self.parent.myPlayer.HP = self.parent.myPlayer.maxHP
            else:
                self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
                self.quest_a1(response_3)
        #elif response in ['1',' 2'] and quest1 == True and quest2 == True:
            #self.parent.zonemap['c3']['SOLVED'] = True
        else:
            self.parent.text.danger('Wrong input\n', begin_txt='SYSTEM')
            self.quest_a1(response)
