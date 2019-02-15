import unittest

class Test_some_calculations(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(1 + 2, 3)

    def test_case_02(self):
        self.assertEqual(2 + 2, 4)

    def test_case_03(self):
        self.assertEqual(3 + 2, 4)

    def test_case_04(self):
        self.assertEqual(3 + 2, 6)

    def test_case_05(self):
        self.assertEqual(4 + 2, 6)


if __name__ == '__main__':
    unittest.main()