__author__ = 'Mukul'


def isDivisibleByFive(number):
    """

    :rtype : bool
    """
    if number%5 == 0:
        return True
    return False

def isDivisibleByThree(number):
    """

    :rtype : bool
    """
    if number%3 == 0:
        return True
    return False

def isDivisibleByFifteen(number):
    """

    :rtype : bool
    """
    if isDivisibleByThree(number) and isDivisibleByFive(number):
        return True
    return False

