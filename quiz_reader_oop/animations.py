#add imports
import os
import time
from math import floor

#add class
class Animation:
        #add __init__ to make the speed of the animations customizable
        def __init__(self, speed=0.03):
                self.speed = speed

        #def spec print
        def spec_print(self, text, new_line=False):
                for character in text:
                        print(character, end="", flush=True)
                        time.sleep(self.speed)
                if new_line:
                        print("")

        #def animated center
        def animated_center(self, text):
                center = os.get_terminal_size().columns
                arrows = 1
                duration = 6
                max_arrows = 3
                print("\033[H\033[J", end="")

                while duration > 0:
                    space = floor(center / 2) - (floor(len(text) / 2) + 1 + max_arrows)
                    spacer = " " * space
                    print(spacer + f"{('>' * arrows) + ' ' * (max_arrows - arrows)} {text} {' ' * (max_arrows - arrows) + ('<' * arrows)}" + spacer, end="\033[H", flush=True)
                    time.sleep(0.1)
                    duration -= 0.1
                    arrows += 1

                    if arrows > max_arrows:
                            spaces = 0
                            arrows = max_arrows
                            time.sleep(0.3)
                            duration -= 0.3

                            while arrows != 0:
                                    spaces += 1
                                    arrows -= 1
                                    print(spacer + f"{' ' * spaces + '>' * arrows} {text} {'<' * arrows + ' ' * spaces}" + spacer, end="\033[H", flush=True)
                                    time.sleep(0.1)
                                    duration -= 0.1

                            time.sleep(0.3)
                            duration -= 0.3

                print("\033[H\033[J", end="")
