from generator.wordlist import wordlist
from random import randint

def generate(password=''):
    for i in range(4):
        password += wordlist[randint(0,19999)]
        if i is not 3:
            password += ' '
    return password