"""Day 12"""

"""
Question 44
Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list. Use lambda to define anonymous functions.
"""


def question44():
    li = list(map(lambda x : x ** 2 ,list(range(1,21))))
    print(li)

# question44()

"""
Question 45
Question:
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.
"""

class American:
    @staticmethod
    def printNationality():
        print('American')

person = American
person.printNationality()

"""
Question 46
Question:
Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*
"""

class American:
    pass
class NewYorker(American):
        pass

american = American
newyorker = NewYorker
print(american, newyorker)