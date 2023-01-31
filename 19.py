"""Day 19"""

import random


"""
Question 75
Question
Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints
Use random.randrange() to a random integer in a given range.
"""

print(random.randint(7,15))

"""
Question
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""
# import zlib
# string = "hello world!hello world!hello world!hello world!"
# string = bytes(string, 'utf-8')
# compr_str = zlib.compress(string)
# print(compr_str)
# print(zlib.decompress(compr_str))

"""
Question 77
Question
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints
Use timeit() function to measure the running time.
"""

import time

def question77():
    start = time.time()
    for x in range(100):
        x = 1 + 1
    print(f'Execution time: {time.time() - start}')

# question77()

"""
Question 78
Question
Please write a program to shuffle and print the list [3,6,7,8].

Hints
Use shuffle() function to shuffle a list.
"""

def question78():
    li = [3,6,7,8]
    random.shuffle(li)
    print(li)

# question78()

"""
Question 79
Question
Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints
Use list[index] notation to get a element from a list.
"""



def question79():
    subj = ["I", "You"]
    verb = ["Play", "Love"]
    obj = ["Hockey","Football"]
    for s in subj:
        for v in verb:
            for o in obj:
                print(f'{s} {v} {o}')

question79()