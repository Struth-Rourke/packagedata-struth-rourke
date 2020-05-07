import unittest

from newpandaspackage.my_mod import enlarge

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(enlarge(5), 50)
        self.assertEqual(enlarge('oops'), 0)



if __name__ == '__main__':
    unittest.main()