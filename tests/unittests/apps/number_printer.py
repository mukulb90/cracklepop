__author__ = 'mukul'

from unittest import TestCase

from apps.number_printer import print_numbers_crackle_way


class NumberPrinterTest(TestCase):

    def test_number_printer(self):
        print_numbers_crackle_way(1, 100)