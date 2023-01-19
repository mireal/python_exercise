"""Day 5"""

"""
Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def question16():
    li = input('Enter a sequence of comma-separated numbers: ').split(',')
    square_li = []
    for x in li:
        if int(x) % 2 != 0:
            square_li.append(str(int(x) ** 2))
    print(','.join(square_li))


# question16()

"""
Question 17
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def question17():
    deposit = 0
    while True:
        operation = input('Type D for deposit or W to withdraw, then type a value. (Example: D 100): ').split()
        if operation[0] == 'D':
            deposit += int(operation[1])
        elif operation[0] == 'W':
            deposit -= int(operation[1])
        print(f'Balance: {deposit}')


question17()
