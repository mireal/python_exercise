"""Day 11"""

"""
Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

def question38():
    tu = (1,2,3,4,5,6,7,8,9,10)
    print(tu[0:5])
    print(tu[5:10])

# question38()

"""
Question 39
Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:
Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.


"""

def question39():
    tu = (1,2,3,4,5,6,7,8,9,10)
    odds = tuple(x for x in tu if x % 2 == 0)
    print(odds)

# question39()

"""
Question 40
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""

def question40():
    yes = input(": ")
    if yes == 'yes' or yes == 'Yes' or yes == 'YES':
        print(yes.capitalize())
    else:
        print('No')

# question40()

"""
Question 41
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use lambda to define anonymous functions.
"""

def question41():
    li = [1,2,3,4,5,6,7,8,9,10]
    new_li = list(map(lambda x : x**2,li))
    print(new_li)

# question41()

"""
Question 42
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.
"""

def question42():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_li = list(map(lambda x : x**2,filter(lambda x : x%2 == 0,li)))
    print(new_li)

# question42()

"""
Question 43
Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:
Use filter() to filter elements of a list.Use lambda to define anonymous functions.
"""

def question43():
    li = list(filter(lambda x : x % 2 == 0,list(range(1,21))))
    print(li)

question43()