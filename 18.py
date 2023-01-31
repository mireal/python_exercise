"""Day 18"""
import random
"""
Question 70
Question
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
"""

def question70():
    return random.choice(list(x for x in range(0,11) if x % 2 == 0))

print(question70())

"""
Question 71
Question
Please write a program to output a random number, which is divisible by 5 and 7, 
between 10 and 150 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
"""

def question71():
    return random.choice(list(x for x in range(10,151) if x % 5 == 0 and x % 7 == 0))

print(question71())

"""
Question 72
Question
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

def question72():
    return random.sample(range(100,201), 5)

print(question72())

"""
Question 73
Question
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

print(random.sample(list(x for x in range(100,201) if x % 2 == 0), 5))

"""
Question 74
Question
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

print(random.sample(list(x for x in range(1,1001) if x % 5 == 0 and x % 7 == 0), 5))