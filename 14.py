"""Day 14"""

"""
Question 51
Question
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.
"""

def question51():
    try:
        return 5/0
    except ZeroDivisionError:
        print('Division by zero')
    except:
        print('Error!')

# question51()

"""
Question 52
Question
Define a custom exception class which takes a string message as attribute.

Hints
To define a custom exception, we need to define a class inherited from Exception.
"""

class CustomException(Exception):
    """My custom exception"""
    def __init__(self, string):
        self.string = string

    def exc(self):
        try:
            raise CustomException('Error!')
        except CustomException as ex:
            print(ex)

# err = CustomException('e')
# print(err.exc())

"""
Question 53
Question
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use \w to match letters.
"""

import re
def question53():
    mail = input('Enter a mail address: ')
    expr = r'(\w*?)@'
    name = re.findall(expr, mail)
    print(name[0])

question53()