# You will be given an array of objects representing data about developers who have signed
# up to attend the next web development meetup that you are organising. Three programming
# languages will be represented: Python, Ruby and JavaScript.
#
# Your task is to return either:
#
# true if the number of meetup participants representing any of the three programming
# languages is ** at most 2 times higher than the number of developers representing any
# of the remaining programming languages**; or
# false otherwise.
# For example, given the following input array:
#
# list1 = [
#     { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
#     { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
#     { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
#     { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
#     { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
#     { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
#     ]
# your function should return false as the number of JavaScript developers (3) is 3 times
# higher than the number of Python developers (1). It can't be more than 2 times higher
# to be regarded as language-diverse.
#
# Notes:
#
# The strings representing all three programming languages will always be formatted in
# the same way (e.g. 'JavaScript' will always be formatted with upper-case 'J' and 'S'.
# The input array will always be valid and formatted as in the example above.
# Each of the 3 programming languages will always be represented.
#
#
#
#
# This kata is part of the Coding Meetup series which includes a number of short and easy
# to follow katas which have been designed to allow mastering the use of higher-order functions.
# In JavaScript this includes methods like: forEach, filter, map, reduce, some, every, find, findIndex.
# Other approaches to solving the katas are of course possible.
#
# Here is the full list of the katas in the Coding Meetup series:
#
# Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe
#
# Coding Meetup #2 - Higher-Order Functions Series - Greet developers
#
# Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?
#
# Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer
#
# Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages
#
# Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?
#
# Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer
#
# Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?
#
# Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?
#
# Coding Meetup #10 - Higher-Order Functions Series - Create usernames
#
# Coding Meetup #11 - Higher-Order Functions Series - Find the average age
#
# Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins
#
# Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?
#
# Coding Meetup #14 - Higher-Order Functions Series - Order the food
#
# Coding Meetup #15 - Higher-Order Functions Series - Find the odd names
#
# Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details
#
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESARRAYSFUNDAMENTALSALGORITHMSSTRINGS
# Solution
from collections import Counter
def is_language_diverse(lst):
    count = Counter(map(lambda x: x["language"], lst)).values()
    return max(count) <= min(count) * 2