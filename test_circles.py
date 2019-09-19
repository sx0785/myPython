#https://docs.python.org/3/library/unittest.html

from circles import circle_area
import unittest
from math import pi

class TestCirclesArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi * 2.1**2)
    
    def test_values(self):
        self.assertRaises(ValueError, circle_area,-2)

    def test_types(self):
        self.assertRaises(TypeError,circle_area,3+5j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"radius")
    
