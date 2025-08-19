import unittest

class TestBasics(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(True)

    def test_arithmetic(self):
        self.assertEqual(1 + 1, 2)

    def test_string_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_list_reverse(self):
        self.assertEqual([1, 2, 3][::-1], [3, 2, 1])

if __name__ == '__main__':
    unittest.main()
