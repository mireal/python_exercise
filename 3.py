"""day 3"""

"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words 
after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""

def question10():
    sequence = input('Enter a prompt: ').split()
    sequence = sorted(set(sequence))
    print(' '.join(sequence))

# question10()


"""
Question
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def question11():
    seq = input('Enter a prompt: ').split(',')
    for x in seq:
        if int(x, base = 2) % 5 == 0:
            print(x)


# question11()

"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def question12():
    seq = input('Enter a prompt: ').split(',')
    li = []
    for x in range(int(seq[0]), int(seq[1])):
        if int(x / 1000) % 2 == 0 and int(x / 100) % 2 == 0 and int(x / 10) % 2 == 0 and int(x) % 2 == 0:
            li.append(x)
    print(li)


# question12()


"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def question13():
    letters = 0
    digits = 0
    seq = 'hello world! 123'
    for x in list(seq):
        if str(x).isdigit():
            digits += 1
        elif str(x).isalpha():
            letters += 1
    print(f'Letters: {letters}, Digits: {digits}')

question13()