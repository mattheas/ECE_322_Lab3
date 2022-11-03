# ECE_322_Lab3

Lab 3 is an introduction to White Box testing techniques (i.e., unit testing) as well as exploring one last Black Box technique (pairwise testing). This lab uses Python3, PyCharm, unittest testing framework and allpairspy package tool. 


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

The file test_coverage_MathPackage.py uses white box testing techniques (i.e. unit tests) to provide:
- Statement coverage
- Branch coverage

This is achieved through a single unit test for each method. The methods are quite simple in nature so a single test with some generic data provided both statement and branch coverage.

The second task of part 2 is to use mocks for testing as seen in test_MathPackage.py. The task was to create a mock for each method (using @patch.object), mock a return value for one method (I chose the max method), and use the following assertinons for each mocked method:

- assert_called
- assert_called_once
- assert_called_with
- assert_called_once_with
- call_count
- call_args
- call_args_list
- method_calls



## Lab3_3:

The source file pairwise.py is given that produces an orthogonal array (using allpairspy) given inputs and the possible values inputs can take. In the lab it is asked to change the file so 3 independent variables A, B & C that can take on three possible values 0, 1 & 2. A pairwise table is then generated and in the lab report this is analyzed and compared to testing all input combinations. I reflect on the effectivness of pairwise testing as a black box testing technique, the types of errors it catches and misses, and comparing it to test cases using all possible input combinations (esentially exhaustive testing).   
