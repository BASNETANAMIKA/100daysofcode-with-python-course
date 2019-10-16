import itertools
from time import sleep
import random

colour = "red green orange".split()

rotation = itertools.cycle(colour)


def light_rotation(rotation):
    for colour in rotation:
        if colour == "red":
            print("stop - the color is red")
            sleep(random.randint(3,7))
        elif colour == "orange":
            print("caution!!")
            sleep(random.randint(3,7))
        else:
            print("GO")
            sleep(random.randint(3,7))

if __name__=='__main__':
    light_rotation(rotation)
