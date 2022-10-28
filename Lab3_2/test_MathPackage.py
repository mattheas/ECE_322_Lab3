import unittest
from unittest.mock import Mock, patch
from MathPackage import MathPackage

  
class TestMathPackage(unittest.TestCase):

  # create a MathPackage obj
  myMathPackage = MathPackage()

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
    mock_random.assert_called_with(3,1,3)
    mock_random.assert_called_once_with(3,1,3)
    self.assertEqual(mock_random.call_count, 1)
    self.assertEqual(mock_random.call_args, ((3,1,3),) )

    #call to mock method
    mock_random(5,1,100)

    # assertion statements
    expected_args = [((3,1,3),), ((5,1,100),)]
    self.assertEqual(mock_random.call_args_list, expected_args)
    self.assertEqual(mock_random.method_calls, [])
    
  @patch.object(MathPackage, 'max')
  def test_max_method(self, mock_max):
    mock_max.return_value = 5
    print("HELLO max")
    
    mock_max.call_args == ()

    # call to mock method
    mock_max([3,1,3])

    # assertion statements
    mock_max.assert_called()
    mock_max.assert_called_once()
    mock_max.assert_called_with([3,1,3])
    mock_max.assert_called_once_with([3,1,3])
    self.assertEqual(mock_max.call_count, 1)
    self.assertEqual(mock_max.call_args.args, ([3,1,3],))

    #call to mock method
    mock_max([5,6,7])

    # assertion statements
    self.assertEqual(mock_max.call_args_list[0].args, ([3,1,3],))
    self.assertEqual(mock_max.call_args_list[1].args, ([5,6,7],))
    self.assertEqual(mock_max.method_calls, [])
    
    myMockMathPackage = Mock()
    myMockMathPackage.max.return_value = 10 
    self.assertEqual(myMockMathPackage.max(), 10)
    
    
  @patch.object(MathPackage, 'min')
  def test_min_method(self, mock_min):
    print("HELLO min")
    mock_min.return_value = 1
    
    

if __name__ == '__main__':
    unittest.main()
