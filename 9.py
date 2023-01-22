"""Day 9"""

"""
Question 26
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
"""

def question26(num1,num2):
    return num1+num2

# print(question26(2,3))

"""
Question 27
Question:
Define a function that can convert a integer into a string and print it in console.

Hints:
Use str() to convert a number to string.
"""

def question27(num):
    print(str(num))

# question27(6)

"""
Question 28
Question:
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

Hints:
Use int() to convert a string to integer.
"""

def question28(num1,num2):
    return int(num1) + int(num2)

# print(question28('2','6'))

"""
Question 29
Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:
Use + sign to concatenate the strings.
"""

def question29(str1,str2):
    return str1 + str2

# print(question29('blue','berry'))

"""
Question 30
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.

Hints:
Use len() function to get the length of a string.
"""

def question30(str1,str2):
    if len(str1) == len(str2):
        print(str1)
        print(str2)
    elif len(str1) > len(str2):
        print(str1)
    else: print(str2)

# question30('apple', 'berry')