import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(1, -2), -1)
    # Add the following test methods to the TestCalculator class:
    def test_sub(self):
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(-4,2),-6)
    def test_mul(self):
        self.assertEqual(self.calc.multiply(3,3),9)
        self.assertEqual(self.calc.multiply(5,5),25)
    def test_div(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(15,1),15)
    def test_mod(self):
        self.assertEqual(self.calc.modulo(10,3),1)
        self.assertEqual(self.calc.modulo(9,3),0)
        
if __name__ == '__main__':
    unittest.main()