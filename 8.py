"""Day 8"""

"""
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def question22():
    words = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split()
    # words = input("Type something: ").split()
    words = sorted(words)
    unique_words = set(words)
    di = {}
    for word in unique_words:
        di[word] = words.count(word)

    for w in dict(sorted(di.items())):
        print(f"{w}:{di[w]}")

# question22()


"""
Question 23
Question:
Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p
"""

def question23():
    print(int(input('Enter a number: '))**2)

# question23()

"""
Question:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

Hints:
The built-in document method is __doc__
"""

def question24():
    """This function prints documentations of other functions"""
    name = input("Enter the name of function: ")
    func = f"print({name}.__doc__)"
    exec(func)

# question24()
# print(question24.__doc__)

"""
Question 25
Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later
"""

class Student:
    name = 'Student'

    def __init__(self, name = None):
        self.name = name

Jim = Student('Jim')
print(f'{Student.name} name is {Jim.name}')

John = Student()
John.name = "John"
print(f'{Student.name} name is {John.name}')