import unittest
from mybisect import Polynomial
from mybisect import MyBisect


class TestMyBisect(unittest.TestCase):

    # initialize Polynomial and MyBisect objects
    test_polynomial_obj = Polynomial(1, -1)
    test_mybisect_obj = MyBisect(test_polynomial_obj)
    test_mybisect_obj1 = MyBisect(1, test_polynomial_obj)

    def test_mybisect_statement_coverage_1(self):
        root_val = self.test_mybisect_obj.run(0, 3)
        self.assertTrue(0.98 <= root_val <= 1.02)

    def test_mybisect_branch_coverage_1(self):
        with self.assertRaises(ValueError):
            self.test_mybisect_obj.run(4, 5)

    def test_mybisect_branch_coverage_2(self):
        with self.assertRaises(ValueError):
            self.test_mybisect_obj1.run(-10, 10)


if __name__ == '__main__':
    unittest.main() 
