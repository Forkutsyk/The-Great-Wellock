class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxDEF = 0
        self.spels = []
        self.location = 'b2'
        self.game_over = False
        self.STR = 0
        self.HP = 0
        self.MP = 0
        self.DEF = 0


class enemy:
    def __init__(self):
        self.job = ''
        self.maxHP = 0
        self.maxMP = 0
        self.maxSTR = 0
        self.STR = 0
        self.HP = 0
        self.MP = 0
        self.status_effects = []
