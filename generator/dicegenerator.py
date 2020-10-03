from generator.diceware import dicelist
from random import randint

def diceware(password=''):
    for i in range(4):
        password += dicelist[dice()]
        if i is not 3:
            password += ' '
    return password

def dice(dice=''):
    for i in range(5):
        dice += str(randint(1,6))
    return dice