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
		self.myMathPackage.random.call_args == ()
		
		# call to mock method
		self.myMathPackage.random(3,1,3)
		
		# assertion statements
		self.myMathPackage.random.assert_called()
		self.myMathPackage.random.assert_called_once()
		self.myMathPackage.random.assert_called_with(3,1,3)
		self.myMathPackage.random.assert_called_once_with(3,1,3)
		self.assertEqual(self.myMathPackage.random.call_count, 1)
		self.assertEqual(self.myMathPackage.random.call_args, ((3,1,3),) )
		
		#call to mock method
		self.myMathPackage.random(5,1,100)
		
		# assertion statements
		expected_args = [((3,1,3),), ((5,1,100),)]
		self.assertEqual(self.myMathPackage.random.call_args_list, expected_args)
		#expected_calls = ['call.random()', 'call.random()']
		#self.assertEqual(self.myMathPackage.random.method_calls, expected_calls)
		


class TestMockMaxMethod(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	
	@patch.object(MathPackage, 'max')
	def test_max_method(self, mock_max):
		mock_max.return_value = 5


class TestMockMinMethod(unittest.TestCase):

	# create a MathPackage obj and turn it into a mock object
	myMathPackage = MathPackage()
	
	@patch.object(MathPackage, 'min')
	def test_max_method(self, mock_min):
		print("HELLO min")
		mock_min.return_value = 1



if __name__ == '__main__':
    unittest.main()
