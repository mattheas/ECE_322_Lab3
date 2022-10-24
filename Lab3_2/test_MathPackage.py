import unittest
from unittest.mock import Mock, patch
from MathPackage import MathPackage

  
class TestMathPackage(unittest.TestCase):

  # create a MathPackage obj and turn it into a mock object
  myMathPackage = MathPackage()

  # tests mock each method

  @patch.object(MathPackage, 'random')
  def test_random_method(self, mock_random):
    print("HELLO random")
    mock_random.return_value = [1,2,3]
    mock_random.call_args == ()

    # call to mock method
    mock_random(3,1,3)

    # assertion statements
    mock_random.assert_called()
    mock_random.assert_called_once()
    mock_random.assert_called_once()
    mock_random.assert_called_with(3,1,3)
    mock_random.assert_called_once_with(3,1,3)
    self.assertEqual(mock_random.call_count, 1)
    self.assertEqual(mock_random.call_args, ((3,1,3),) )

    #call to mock method
    mock_random(5,1,100)

    # assertion statements
    expected_args = [((3,1,3),), ((5,1,100),)]
    self.assertEqual(mock_random.call_args_list, expected_args)
    
    #expected_calls = ['call.random()', 'call.random()']
    #self.assertEqual(self.myMathPackage.random.method_calls, expected_calls)
    
    print(mock_random.method_calls)
    
  @patch.object(MathPackage, 'max')
  def test_max_method(self, mock_max):
    mock_max.return_value = 5
    print("HELLO max")
    # MOCK A RETURN VALUE HERE
    
  @patch.object(MathPackage, 'min')
  def test_min_method(self, mock_min):
    print("HELLO min")
    mock_min.return_value = 1
    
    
  # create a MathPackage obj and turn it into a mock object
  mockMathObj = MathPackage()
  mockMathObj = Mock()

  # tests provides statement/ branch coverage for methods

  def test_random_method_coverage(self):
    self.mockMathObj.random(3, 1, 5)
    self.mockMathObj.random.assert_called_once()
    print("HELLO cov1")

  def test_max_method_coverage(self):
    self.mockMathObj.max([1, 2, 3])
    self.mockMathObj.max.assert_called_once() 
    print("HELLO cov2")

  def test_min_method_coverage(self):
    self.mockMathObj.min([3, 4, 5])
    self.mockMathObj.min.assert_called_once()  
    print("HELLO cov3")
    

if __name__ == '__main__':
    unittest.main()
