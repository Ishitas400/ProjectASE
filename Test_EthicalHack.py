# unit test case
import unittest


class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        EnteredPassword = "nnjjhgs"
        ListedPassword = "gnjjhgs"
        # error message in case if test case got failed
        message = "First  and second passwords are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(EnteredPassword, ListedPassword, message)


# unit test case
import unittest


class TestHack(unittest.TestCase):
    # test function to test equality of two value
    def test_positive(self):
        EnteredPassword = "abcdefg"
        ListedPassword = "abcdefg"
        # error message in case if test case got failed
        info = "First  and second passwords are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(EnteredPassword, ListedPassword, info)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
