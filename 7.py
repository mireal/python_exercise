"""Day 7"""

"""
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
Hints:
Consider use class, function and comprehension.
"""

class question20:
    def div_by_7(self, n):
        for x in range(0,n + 1):
            if x % 7 == 0:
                yield x

# n = int(input('Enter a number: '))
# func = question20()
# for x in func.div_by_7(n):
#     print(x)

"""
Question:
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input.
Here distance indicates to euclidean distance.Import math module to use sqrt function.
"""
from math import sqrt

def question21():
    position = [0,0]
    while True:
        move = input("Enter direction and number of steps: ").split()
        if not move:
            break
        if move[0] == 'UP':
            position[0] += int(move[1])
        elif move[0] == 'DOWN':
            position[0] -= int(move[1])
        elif move[0] == 'LEFT':
            position[1] += int(move[1])
        elif move[0] == 'RIGHT':
            position[1] -= int(move[1])
    distance = int(round(sqrt((position[0]**2)+(position[1]**2))))
    print(distance)

# question21()