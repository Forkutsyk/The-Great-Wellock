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

