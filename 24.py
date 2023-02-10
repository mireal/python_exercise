"""Day 24"""

"""
Question 100
Question
You are given words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:

3
2 1 1
Hints
Make a list to get the input order and a dictionary to count the word frequency
"""


# word_dict = {}
# while True:
#     word = input('Enter a word')
#     if not word:
#         break
#     if word not in word_dict:
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
# for x in word_dict:
#     print(word_dict[x],end=' ')

"""
Question 101
Question
You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1
Hints
Count frequency with dictionary and sort by Value from dictionary Items
"""

# s = 'aabbbccde'
# freq_dict = {}
# for letter in s:
#     if letter not in freq_dict:
#         freq_dict[letter] = 1
#     else:
#         freq_dict[letter] += 1
# freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
# for x in freq_dict:
#     print(f'{x} {freq_dict[x]}')

"""
Question
Write a Python program that accepts a string and calculate the number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8
Hints
Use isdigit() and isalpha() function


"""

# s = 'Hello321Bye360'
# digits = 0
# letters = 0
# for x in s:
#     if x.isdigit():
#         digits += 1
#     elif x.isalpha():
#         letters += 1
# print(f'Digit - {digits} \nLetter - {letters}')

"""
Question 103
Question
Given a number N.Find Sum of 1 to N Using Recursion

Input

5
Output

15
Hints
Make a recursive function to get the sum
"""

#skipped