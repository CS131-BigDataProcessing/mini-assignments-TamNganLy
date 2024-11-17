import unittest
from math_functions import divide

class math_unittest(unittest.TestCase):
    def test_divide(self):
        # Standard test case
        self.assertEqual(divide(10,4),2.5)
        self.assertEqual(divide(10,2),5)
        self.assertEqual(divide(0,2),0)
        self.assertEqual(divide(-10,2),-5)
        self.assertEqual(divide(10,-2),-5)
        self.assertEqual(divide(-10,-2),5)

        # Edge test case
        self.assertEqual(divide(10,0),"The divisor cannot be 0")


if __name__ == ('__main__'):
    unittest.main