__author__ = 'mukul'

'''
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can use any language.
'''
from utils.number_utils import isDivisibleByFifteen, isDivisibleByFive, isDivisibleByThree

def print_numbers_crackle_way(start, last_number):

    for number in range(start, last_number+1):
        if isDivisibleByFifteen(number):
            print 'CracklePop'
        elif isDivisibleByThree(number):
            print 'Crackle'
        elif isDivisibleByFive(number):
            print 'Pop'
        else :
            print number

if __name__ == '__main__':
    print_numbers_crackle_way(1, 100)

