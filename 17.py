"""Day 17"""

"""
Question
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints
Use "assert expression" to make assertion.
"""

def question65():
    li = [2,4,6,8]
    for x in li:
        assert x % 2 == 0

# question65()

"""
Question 66
Question
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:

38
Hints
Use eval() to evaluate an expression.
"""

def question66():
    expr = input('Enter a math expression: ')
    print(eval(expr))

# question66()

"""
Question 67
Question
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.

Hints
Use if/elif to deal with conditions.
"""
# skipped
def question67(search):
    li = [1,2,3,4,5]
    for i,x in enumerate(li):
        if x == search:
            print(f'Index of given item is {i}')

# question67(3)

"""
Question 68
Question
Please generate a random float where the value is between 10 and 100 using Python module.

Hints
Use random.random() to generate a random float in [0,1].
"""

# import random
# randfloat = random.uniform(10,100)
# print(randfloat)

"""
Question 69
Question
Please generate a random float where the value is between 5 and 95 using Python module.

Hints
Use random.random() to generate a random float in [0,1].

"""

import random
randfloat = random.uniform(5,95)
print(randfloat)