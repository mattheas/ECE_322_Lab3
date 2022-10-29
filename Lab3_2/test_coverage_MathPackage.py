import unittest
from MathPackage import MathPackage


class TestMathPackage(unittest.TestCase):

  def test_random_method_coverage(self):
    test_list = MathPackage.random(3, 1, 5)
    self.assertEqual(len(test_list), 3)

  def test_max_method_coverage(self):
    max_num = MathPackage.max([1,2,3])
    self.assertEqual(max_num, 3)

  def test_min_method_coverage(self):
    min_num = MathPackage.min([3,4,5])
    self.assertEqual(min_num, 3)
    

if __name__ == '__main__':
    unittest.main()
