# You will be given an array of objects (associative arrays in PHP, table in COBOL) representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return an object (associative array in PHP, table in COBOL) which includes the count of each coding language represented at the meetup.
#
# For example, given the following input array:
#
# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
#     { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
#     ]
# your function should return the following object (associative array in PHP, table in COBOL):
#
# { 'C': 2, 'JavaScript': 1, 'Ruby': 1 }
# Notes:
#
# The order of the languages in the object does not matter.
# The count value should be a valid number.
# The input array will always be valid and formatted as in the example above.
#
#
#
#
# This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible.
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
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESARRAYSFUNDAMENTALSALGORITHMS
# Solution
from collections import Counter
def count_languages(lst):
    return Counter(i['language'] for i in lst)