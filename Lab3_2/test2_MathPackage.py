import unittest
from unittest.mock import Mock, MagicMock
from MathPackage import MathPackage


class TestCoverage(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	#myMathPackage = Mock()

	# tests provides statement/ branch coverage for methods

	def test_random_method(self):
		self.myMathPackage.random = MagicMock(return_value = [1,2,3])
		self.myMathPackage.random(3,1,3)
		self.myMathPackage.random.assert_called()
		self.myMathPackage.random.assert_called_once()
		self.myMathPackage.random.assert_called_with(3,1,3)
		

		# self.myMathPackage.random.assert_called_once()
 
	def test_max_method(self):
		print("hello")
		#self.myMathPackage.max([1, 2, 3])
		#self.myMathPackage.max.assert_called_once()

	def test_min_method(self):
		print("hello") 
		#self.myMathPackage.min([3, 4, 5])
		# self.myMathPackage.min.assert_called_once()


if __name__ == '__main__':
    unittest.main()
