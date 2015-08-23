__author__ = 'Mukul'

def isDivisibleByFive(number):
    if number%5 == 0:
        return True
    return False

def isDivisbleByThree(number):
    if number%3 == 0:
        return True
    return False

def isDivisibleByFifteen(number):
    if isDivisbleByThree(number) and isDivisibleByFive(number):
        return True
    return False
