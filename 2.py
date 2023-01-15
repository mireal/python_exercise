"""Day 2"""

"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple
"""


def sequence():
    seq = str(input('enter a sequence of comma-separated numbers: '))
    seq = seq.split(',')
    li = tuple(seq)
    print(seq)
    print(li)


# sequence()

"""
Question 5
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
"""


class StringMethods:

    def __init__(self):
        string = 0

    def getString(self):
        self.string = str(input('Enter text: '))

    def printString(self):
        print(self.string.upper())

a = StringMethods()
# a.getString()
# a.printString()

"""
Question 6
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value 
(for example, if the output received is 26.0, it should be printed as 26).
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from math import sqrt

def calc():
    C = 50
    H = 30
    seq = str(input('Enter a comma-separated sequence: '))
    D = seq.split(',')
    D = list(int(i) for i in D)
    print(D)
    for d in D:
        Q = sqrt((2 * C * d) / H)
        print(int(Q), end=', ')

# calc()

"""
Question 7
Question:
_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


"""