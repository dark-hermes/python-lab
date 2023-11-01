# Hermawan Sentyaki Sarjito
# J0403231111

import unittest
import math_operations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_operations.add(5, 5), 10)
        self.assertEqual(math_operations.add(5, -5), 0)
        self.assertEqual(math_operations.add(-5, -5), -10)
        self.assertEqual(math_operations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(5, 5), 0)
        self.assertEqual(math_operations.subtract(5, -5), 10)
        self.assertEqual(math_operations.subtract(-5, -5), 0)
        self.assertEqual(math_operations.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(math_operations.multiply(5, 5), 25)
        self.assertEqual(math_operations.multiply(5, -5), -25)
        self.assertEqual(math_operations.multiply(-5, -5), 25)
        self.assertEqual(math_operations.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(math_operations.divide(5, 5), 1)
        self.assertEqual(math_operations.divide(5, -5), -1)
        self.assertEqual(math_operations.divide(-5, -5), 1)
        self.assertEqual(math_operations.divide(0, 5), 0)
        
if __name__ == '__main__':
    unittest.main()