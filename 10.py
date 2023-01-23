"""Day 10"""

"""
Question 31
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

"""

def question31():
    di = {}
    for num in range(1,21):
        di[num] = num ** 2
    return di

# print(question31())

"""
Question 32
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the keys only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""

def question32():
    di = {}
    for num in range(1, 21):
        di[num] = num ** 2
    print(di.keys())

# question32()

"""
Question 33
Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
"""

def question33():
    li = list(x ** 2 for x in range(1,21))
    print(li)

# question33()

"""
Question 34
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.
Use list.append() to add values into a list.Use [n1:n2] to slice a list
"""

def question34():
    li = list(x ** 2 for x in range(1, 21))
    print(li[0:5])

# question34()

"""
Question 35
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
"""

def question35():
    li = list(x ** 2 for x in range(1, 21))
    li.reverse()
    print(li[0:5])

# question35()

"""
Question 36
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.

Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
"""

def question36():
    li = list(x ** 2 for x in range(1, 21))
    print(li[5:])

# question36()

"""
Question 37
Question:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.
Main Author's Solution: Python 2
"""

def question37():
    li = list(x ** 2 for x in range(1, 21))
    print(tuple(li))

question37()