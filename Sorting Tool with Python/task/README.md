Description
This project is called Sorting Tool, but, so far, you still haven’t really sorted the elements of the user input. Let's add a number-sorting mechanism to the program and provide an appropriate command-line argument to use this function.

The new optional -sortIntegers argument indicates that the input numbers should be sorted.

Objectives
Update the parsing of command-line arguments to support the number sorting option.

If the -sortIntegers argument is provided, ignore the other arguments and output two lines: the first containing the total number of numbers in the input, and the second containing all of the input numbers in ascending order.

If the -sortIntegers argument is not provided, the behavior of the program should be the same as in the previous stage.

Example
Run configuration example:

python main.py -sortIntegers