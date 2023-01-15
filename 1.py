"""Day 1"""

"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method.
"""
def numbers():
    for ind, num in enumerate(range(2000, 3200)):
        if num % 7 == 0 and num % 5 != 0:
            if (ind + 2) % 10 == 0:
                print(num)
            else:
                print(num, end=' ,')

# numbers()

""" 
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def factorial():
    num = int(input('Enter a positive integer: '))
    fact = 1
    for num in range(1, num + 1):
        fact = fact * num
        print(fact, end=' ,')

# factorial()

"""
Question:
With a given integral number n, write a program to generate a dictionary that contains
(i, i x i) such that is an integral number between 1 and n (both included).
 and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()
"""

def num_dict():
    n = int(input('Enter a positive integer: '))
    di = {}
    for i in range(1,n+1):
        di[i] = i*i
    print(di)

num_dict()