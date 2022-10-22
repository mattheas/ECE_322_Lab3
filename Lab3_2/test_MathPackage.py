import unittest
from unittest.mock import Mock
from MathPackage import MathPackage


class TestCoverage(unittest.TestCase):

    # create a mock obj
    mock_math_obj = Mock()
    mock_math_obj = MathPackage

    def test_random_method(self):
        print("hello")
        # statement coverage should be simple, simply call method w/ parameters
        # branch coverage is also satisfied since no if() statements

    def test_max_method(self):
        print("hello")
        # statement coverage should be simple, simply call method w/ parameters
        # branch coverage is also satisfied since by finding max the if statement should be true at least
        # once and false at least once IF the list with more than ONE element is passed

    def test_min_method(self):
        print("hello")
        # statement coverage should be simple, simply call method w/ parameters
        # branch coverage is also satisfied since by finding min the if statement should be true at least
        # once and false at least once IF the list with more than ONE element is passed


if __name__ == '__main__':
    unittest.main()
