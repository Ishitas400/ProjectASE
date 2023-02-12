# Python code to demonstrate working of unittest
import unittest


class TestUppLow(unittest.TestCase):

    def setUp(self):
        pass



    # Returns True if the string is in upper case.
    def test_upper(self):
        self.assertEqual('abcdefg'.upper(), 'ABCDEFG')

    # Returns TRUE if the string password is in uppercase
    # otherwise returns False.
    def test_isupp(self):
        self.assertTrue('ABCDEFG'.isupper())
        self.assertFalse('abcdefg'.isupper())

if __name__ == '__main__':
 unittest.main()



