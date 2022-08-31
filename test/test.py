import unittest

from code import add, difference, multiply, division


class TestAdd(unittest.TestCase):
    def test_integer_addition(self):
        self.assertEqual(add(5, 6), 11)

    def test_double_addition(self):
        self.assertEqual(add(5.5, 6.2), 11.7)

    def test_unequal(self):
        self.assertNotEqual(add(2, 3), 6)


class TestDifference(unittest.TestCase):
    def test_integer_difference(self):
        self.assertEqual(difference(5, 6), -1)

    def test_double_difference(self):
        self.assertEqual(difference(9.7, 2.1), 7.6)

    def test_unequal(self):
        self.assertNotEqual(difference(2, 3), 0)


class TestMultiply(unittest.TestCase):
    def test_integer_multiplication(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_double_multiplication(self):
        self.assertEqual(multiply(5.5, 6.2), 34.1)

    def test_unequal(self):
        self.assertNotEqual(multiply(2, 3), 5)


class TestDivision(unittest.TestCase):
    def test_integer_division(self):
        self.assertEqual(division(9, 3), 3.0)

    def test_double_division(self):
        self.assertEqual(division(8.4, 2.1), 4.0)

    def test_unequal(self):
        self.assertNotEqual(division(2, 3), 0.7)


if __name__ == '__main__':
    unittest.main()
