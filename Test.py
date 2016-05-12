"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)


# Test cases
print (get_fib(1))
print (get_fib(9))
print (get_fib(11))
print (get_fib(0))
var = input("please enter a number to calculate fibonacci: ")
print ("fibonacci of", var,"is", get_fib(int(var)))