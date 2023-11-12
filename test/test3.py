
import random
import time
import sys


def d4():
    return random.randint(1,4)
def d6():
    return random.randint(1,6)
def d8():
    return random.randint(1,8)
def d10():
    return random.randint(1,10)
def d12():
    d12roll = random.randint(1,12)
    return d12roll
def d20():
    d20roll = random.randint(1,20)
    return d20roll
def d100():
    return random.randint(1,100)
print(d4())