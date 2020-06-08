
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
ZONENAME = 'ZONENAME'
DESCRIPTION = 'description'
SOLVED = 'SOLVED'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 }
zonemap = {
    'a0': {
        ZONENAME: 'Docks',
        DESCRIPTION: " The initial location is the main port of the kingdom of Wellock. You mysteriously appeared at this location. The port is most of the infrastructure of the kingdom.",
        'SOLVED': False,
        UP: "a3",
        DOWN: "0",
        LEFT: "1",
        RIGHT: "1"
    },
    'a3': {
        ZONENAME: 'House of a Thousand Faces',
        DESCRIPTION: " Area with taverns where you can eat and stay overnight. It is better not to walk here in the evening.",
        'SOLVED': False,
        UP: "b3",
        DOWN: "a0",
        LEFT: "a2",
        RIGHT: "a4"
    },
    'a2': {
        ZONENAME: 'Sharandar',
        DESCRIPTION: " The ancient Feywild homeland of the Iliyanbruen elves.",
        'SOLVED': False,
        UP: "b2",
        DOWN: "1",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'a1': {
        ZONENAME: 'Stronghold',
        DESCRIPTION: " Area with castles of large guilds.",
        'SOLVED': False,
        UP: "b1",
        DOWN: "1",
        LEFT: "2",
        RIGHT: "a2"
    },
    'a4': {
        ZONENAME: 'Dwarven Valley',
        DESCRIPTION: """ Dwarven Valley, has been corrupted by dwarves from the Hammerstone dig up black ice, 
 and the long dead barbarians who once served Akar Kessell rise once more to wage war in the name of their undying master.""",
        'SOLVED': False,
        UP: "b4",
        DOWN: "1",
        LEFT: "a3",
        RIGHT: "a5"
    },
    'a5': {
        ZONENAME: 'Icespire Peak',
        DESCRIPTION: " The place of origin of black ice extracted by dwarves. Dangerous place, it seems that here can survive or very skilled heroes, or very stupid",
        'SOLVED': False,
        UP: "b5",
        DOWN: "1",
        LEFT: "a4",
        RIGHT: "3"
    },
    'b1': {
        ZONENAME: 'Blacklake',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "c1",
        DOWN: "a1",
        LEFT: "2",
        RIGHT: "b2"
    },
    'b2': {
        ZONENAME: 'Nezeris',
        DESCRIPTION: " ",
        'SOLVED': False,
        UP: "c2",
        DOWN: "a2",
        LEFT: "b1",
        RIGHT: "b3"
    },
    'b3': {
        ZONENAME: 'Absol',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "c3",
        DOWN: "a3",
        LEFT: "b2",
        RIGHT: "b4"
    },
    'b4': {
        ZONENAME: 'Cardcaster',
        DESCRIPTION: " Cardcaster is built into the side of a mountain, and is known for having tough warriors. The ruler is fair and just, respected by the populace. ",
        'SOLVED': False,
        UP: "c4",
        DOWN: "a4",
        LEFT: "b3",
        RIGHT: "b5"
    },
    'b5': {
        ZONENAME: 'Arahead',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "c5",
        DOWN: "a5",
        LEFT: "b4",
        RIGHT: "3"
    },
    'c1': {
        ZONENAME: 'Wyllowwood',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "4",
        DOWN: "b1",
        LEFT: "2",
        RIGHT: "c2"
    },
    'c2': {
        ZONENAME: 'Brickell Whyte',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "4",
        DOWN: "b2",
        LEFT: "c1",
        RIGHT: "c3"
    },
    'c3': {
        ZONENAME: 'The Well of Dragons ',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "4",
        DOWN: "b3",
        LEFT: "c2",
        RIGHT: "c4"
    },
    'c4': {
        ZONENAME: 'The Yarlford',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "4",
        DOWN: "b4",
        LEFT: "c3",
        RIGHT: "c5"
    },
    'c5': {
        ZONENAME: 'The final town',
        DESCRIPTION: "",
        'SOLVED': False,
        UP: "4",
        DOWN: "b5",
        LEFT: "c4",
        RIGHT: "3"
    }
}

