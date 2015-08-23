__author__ = 'mukul'

from unittest import TestCase

from utils import number_utils


class NumberUtilTest(TestCase):

    def test_isDivisibleByFiveReturnsTrue(self):
        self.assertTrue( number_utils.isDivisibleByFive(5))
        self.assertTrue( number_utils.isDivisibleByFive(655))
        self.assertTrue( number_utils.isDivisibleByFive(280))

    def test_isDivisibleByFiveReturnsFalse(self):
        self.assertFalse( number_utils.isDivisibleByFive(6))
        self.assertFalse( number_utils.isDivisibleByFive(657))
        self.assertFalse( number_utils.isDivisibleByFive(289))


    def test_isDivisibleByThreeReturnsTrue(self):
        self.assertTrue( number_utils.isDivisibleByThree(6))
        self.assertTrue( number_utils.isDivisibleByThree(15))
        self.assertTrue( number_utils.isDivisibleByThree(0))

    def test_isDivisibleByThreeReturnsFalse(self):
        self.assertFalse( number_utils.isDivisibleByThree(10))
        self.assertFalse( number_utils.isDivisibleByThree(11))
        self.assertFalse( number_utils.isDivisibleByThree(16))

    def test_isDivisibleByFifteenReturnsTrue(self):
        self.assertTrue( number_utils.isDivisibleByFifteen(30))
        self.assertTrue( number_utils.isDivisibleByFifteen(15))
        self.assertTrue( number_utils.isDivisibleByFifteen(120))

    def test_isDivisibleByFifteenReturnsFalse(self):
        self.assertFalse( number_utils.isDivisibleByFifteen(9))
        self.assertFalse( number_utils.isDivisibleByFifteen(3))
        self.assertFalse( number_utils.isDivisibleByFifteen(20))
