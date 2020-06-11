import sys
import time


class dialogs:
    def __init__(self):
        self.dialog = ""

    def dialog_print03(self):
        for character in self.dialog:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.3)

    def dialog_print0025(self):
        for character in self.dialog:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.025)

    def dialog_print01(self):
        for character in self.dialog:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

    def dialog_print001(self):
        for character in self.dialog:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)

    def dialog_print005(self):
        for character in self.dialog:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

    def print_classes(self):
        print("""
           ______________________________________________________________________
          |                                                                      |
          |    ooooooooo.                                                        |
          |   `888   `Y88.                                                       |
          |    888   .d88'  .oooo.   ooo. .oo.    .oooooooo  .ooooo.  oooo d8b   | 
          |    888ooo88P'  `P  )88b  `888P"Y88b  888' `88b  d88' `88b `888""8P   |
          |    888`88b.     .oP"888   888   888  888   888  888ooo888  888       |
          |    888  `88b.  d8(  888   888   888  `88bod8P'  888    .o  888       |
          |    o888o  o888o `Y888""8o o888o o888o `8oooooo.  `Y8bod8P' d888b     |
          |                                       d"     YD                      |
          |     HP: 90                           "Y88888P'                       |
          |     MP: 60                                                           |
          |     Strenght: 70                                                     |
          |     Defence: 6                                                       |
          |                                                                      |
          |______________________________________________________________________|
        """)
        print("""
            ___________________________________________________________________________________   
           |                                                                                   |  
           |    oooooo   oooooo     oooo                              o8o                      |  
           |     `888.    `888.     .8'                               `"'                      |  
           |      `888.   .8888.   .8'    .oooo.   oooo d8b oooo d8b oooo   .ooooo.  oooo d8b  |   
           |       `888  .8'`888. .8'    `P  )88b  `888""8P `888""8P `888  d88' `88b `888""8P  |  
           |        `888.8'  `888.8'      .oP"888   888      888      888  888   888  888      |  
           |         `888'    `888'      d8(  888   888      888      888  888   888  888      |  
           |          `8'      `8'       `Y888""8o d888b    d888b    o888o `Y8bod8P' d888b     |  
           |                                                                                   |  
           |    HP: 160                                                                        |  
           |    MP: 25                                                                         |  
           |    Strenght: 45                                                                   |  
           |    Defence: 15                                                                    |  
           |                                                                                   |
           |___________________________________________________________________________________|
                """)
        print("""
             _____________________________________________________    
            |                                                     |
            |    ooo        ooooo                                 |
            |    `88.       .888'                                 |
            |    8888b     d'888   .oooo.    .oooooooo  .ooooo.   |
            |     8 Y88. .P  888  `P  )88b  888' `88b  d88' `88b  |
            |     8  `888'   888   .oP"888  888   888  888ooo888  |
            |     8    Y     888  d8(  888  `88bod8P'  888    .o  |
            |    o8o        o888o `Y888""8o `8oooooo.  `Y8bod8P'  |
            |                                d"     YD            |
            |                                "Y88888P'            |   
            |   HP: 70                                            |   
            |   MP: 120                                           |   
            |   Strength: 15                                      |   
            |   Defence: 4                                        |   
            |                                                     |   
            |_____________________________________________________|   
        """)