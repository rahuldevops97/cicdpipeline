import unittest

def add_numbers(num1, num2):
    return num1 + num2

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -4)
        self.assertEqual(result, -6)

    def test_add_mixed_numbers(self):
        result = add_numbers(2, -7)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()
