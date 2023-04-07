# file name must be start with test followed by folder name which we want to test i.e test_(filename)
import unittest
# from unittest import TestCase                      # both import are same
from calc_unit_testing import addtion,subtraction,multiplication,division,OutputWillBeZero,is_balanced,InvalidInput

class TestCalc(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(addtion(10,20),30)
        self.assertEqual(addtion(5,10),15)
        self.assertEqual(addtion(-5, 10), 5)
        self.assertEqual(addtion(-5, -5), -10)
        self.assertEqual(addtion(5, -10), -5)

    def test_sub_function(self):
        self.assertEqual(subtraction(2,1),1)
        self.assertEqual(subtraction(4,5),-1)
        self.assertEqual(subtraction(-5,6),-11)
        self.assertEqual(subtraction(-5,-6),1)
        self.assertEqual(subtraction(7,-9),16)

    def test_div_function(self):
        self.assertEqual(division(10,2),5)
        self.assertEqual(division(10, 2),5.0)
        self.assertEqual(division(10,-1),-10)
        self.assertRaises((ZeroDivisionError),division,10,0)

    def test_mul_function(self):
        self.assertEqual(multiplication(10,20),200)
        self.assertEqual(multiplication(-1,10),-10)
        self.assertEqual(multiplication(-1,-2),2)
        self.assertRaises((OutputWillBeZero),multiplication,10,0)

    def test_is_balanced(self):
        self.assertTrue(is_balanced("((){}[])"))
        self.assertFalse(is_balanced("((){}[])(({["))
        self.assertFalse(is_balanced("(((((((()))))))){{{{{{{{{}"))
        self.assertFalse(is_balanced("((({{{))}}}}))))))))))"))
        self.assertFalse(is_balanced("(){}[]("))
        self.assertRaises((InvalidInput),is_balanced,"123698553574")


if __name__ == '__main__':
    unittest.main()