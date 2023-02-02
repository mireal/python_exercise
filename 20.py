"""Day 20"""

"""
Question 80
Question
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

Hints
Use list comprehension to delete a bunch of element from a list.
"""

# li = [5,6,77,45,22,12,24]
# li = [x for  x in li if x % 2 != 0]
# print(li)

"""
Question 81
Question
By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
"""

# li =[12,24,35,70,88,120,155]
# li = [x for  x in li if x % 5 != 0 and x % 7 != 0]
# print(li)

"""
Question 82
Question
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
"""

# li = [12,24,35,70,88,120,155]
# print(li[1::2])

"""
Question 83
Question
By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
"""
#
# li = [12,24,35,70,88,120,155]
# li = [x for ind,x in enumerate(li) if ind + 1 not in [2,3,4]]
# print(li)

"""
Question 84
Question
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints
Use list comprehension to make an array.
"""

li = [[ [0 for x in range(8)] for y in range(5)] for z in range(3)]
print(li)