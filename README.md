# ECE_322_Lab3



## Lab3_1:

The file mybisect.py is given. It is a program that attempts to find the root of a function f(x) between a given interval. 

The file test_mybisect.py uses white box testing techniques (i.e. unit tests) to provide:
- Statement coverage
- Branch coverage
- Execution each loop body at least twice (enter the loop and repeat)

The test cases are written using the python unittest testing framework assertion statements. A self-illustrated Control
Flow Graph is used to determine if the aforementioned coverage is met. 



## Lab3_2:

Source file MathPackage.py is given. It is a class that provides three methods, one method to generate an array of random numbers, a method to find the maxiumum value in an array, and a method to find the miniumum value in an array.

The file test_MathPackage.py uses white box testing techniques (i.e. unit tests) to provide:
- Statement coverage
- Branch coverage

The test cases are written using a Mock object. For the second set of test cases each method in MathPackage.py is mocked (using @patch.object) instead of the entire object and the following assertions are used for each method:

- assert_called
- assert_called_once
- assert_called_with
- assert_called_once_with
- call_count
- call_args
- call_args_list
- method_calls

Furthermore the return value of one method is mocked (I chose the max method)
