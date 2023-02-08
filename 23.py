"""Day 23"""

"""
Question 95
Question
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5
Then, the output of the program should be:

5
Hints
Make the scores unique and then find 2nd best number
"""

# li = []
# while True:
#     num = input('Enter a number: ')
#     if not num:
#         break
#     li.append(int(num))
# li = list(set(li))
# print(li[-2])

"""
Question 96
Question
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Hints
Use wrap function of textwrap module
"""

# from textwrap import wrap
# string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# for x in wrap(string,4):
#     print(x)

"""
uestion 97
Question
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
Hints
First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.
"""

# import string
# SIZE = 3
# letters = string.ascii_lowercase
#
# rag = '-'.join(letters[:SIZE])
# rag2 = rag[::-1]
# rag2 = rag2[:len(rag2)-1]
# center = rag2+rag
# counter = 1
# li = []
# for x in range(SIZE - 1):
#     lines = '-' * (counter + 1)
#     ragstr = rag2[:len(rag2)-counter]
#     rev_rag = ragstr[::-1]
#     ragline = lines+ragstr+rev_rag[1:len(rag2)-1]+lines
#     li.append(ragline)
#     counter += 2
#
# fullrag = list(reversed(li)) + [center] + li
# for x in fullrag:
#     print(x)

"""
Question 98
Question
You are given a date. Your task is to find what the day is on that date.

Input

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

08 05 2015
Output

Output the correct day in capital letters.

WEDNESDAY
Hints
Use weekday function of calender module
"""

# from calendar import weekday, day_name
# date = '08 05 2015'
# MM,DD,YYYY = map(int,date.split())
# print(day_name[weekday(YYYY,MM,DD)].upper())

"""
Question 99
Question
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

4
2 4 5 9
4
2 4 11 12
Output

Output the symmetric difference integers in ascending order, one per line.

5
9
11
12
Hints
Use '^' to make symmetric difference operation.
"""
# from random import randint
#
# N = 4
# N_int = list(randint(1,20) for _ in range(N))
# N_list = set(map(int,N_int))
#
# M = 4
# M_int = list(randint(1,20) for _ in range(M))
# M_list = set(map(int,M_int))
#
# sym = list(sorted(N_list^M_list))
# for x in sym:
#     print(x)