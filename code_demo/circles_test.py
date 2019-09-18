import unittest
from math import pi

from code_demo.circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test Area when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)

        
