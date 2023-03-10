"""Day 4"""

"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def question14():
    upper = 0
    lower = 0
    seq = input('Enter a sentence: ')
    for x in seq:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
    print(f'Upper case: {upper}, Lower case: {lower}')


# question14()

"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


"""


def question15():
    num = input("Enter a number: ")
    out = int(num * 4) + int(num * 3) + int(num * 2) + int(num)
    print(out)

# question15()
