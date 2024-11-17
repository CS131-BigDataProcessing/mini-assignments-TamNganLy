import unittest
from math_functions import power
import math

class math_unittest(unittest.TestCase):
    def test_power(self):
        # Standard test case
        self.assertEqual(power(2,3),8)
        self.assertEqual(power(5,0),1)

        # Edge test case:
        self.assertEqual(power(4,0.5),2)
        self.assertEqual(power(4,-3),0.015625)
        self.assertEqual(power(4,-3),math.pow(4,-3))
        self.assertEqual(power(-4,3),math.pow(-4,3))
        self.assertEqual(power(0,3),math.pow(0,3))

if __name__ == ('__main__'):
    unittest.main