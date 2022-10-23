import unittest
from unittest.mock import Mock, patch
from MathPackage import MathPackage


class TestCoverage(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	myMathPackage = Mock()

	# tests provides statement/ branch coverage for methods

	def test_random_method_coverage(self):
		self.myMathPackage.random(3, 1, 5)
		self.myMathPackage.random.assert_called_once()

	def test_max_method_coverage(self):
		self.myMathPackage.max([1, 2, 3])
		self.myMathPackage.max.assert_called_once() 

	def test_min_method_coverage(self):
		self.myMathPackage.min([3, 4, 5])
		self.myMathPackage.min.assert_called_once()


class TestMockRandomMethod(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	#myMathPackage = Mock()

	# tests mock each method

	@patch.object(MathPackage, 'random')
	def test_random_method(self, mock_random):
		mock_random.return_value = [1,2,3]

		self.myMathPackage.random(3,1,3)
		self.myMathPackage.random.assert_called()
		self.myMathPackage.random.assert_called_once()
		self.myMathPackage.random.assert_called_with(3,1,3)
		self.myMathPackage.random.assert_called_once_with(3,1,3)


class TestMockMaxMethod(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	
	@patch.object(MathPackage, 'max')
	def test_max_method(self, mock_max):
		print("HELLO max")
		mock_max.return_value = 5
		#self.myMathPackage.max([1, 2, 3])
		#self.myMathPackage.max.assert_called_once()
		

class TestMockMinMethod(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	
	@patch.object(MathPackage, 'min')
	def test_max_method(self, mock_min):
		print("HELLO min")
		mock_min.return_value = 1
		#self.myMathPackage.max([1, 2, 3])
		#self.myMathPackage.max.assert_called_once()


if __name__ == '__main__':
    unittest.main()
