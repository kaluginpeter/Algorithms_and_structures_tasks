# You will be given a sequence of objects (associative arrays in PHP) representing data about
# developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if all of the following continents / geographic zones will be represented by at least one
# developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
# false otherwise.
# For example, given the following input array:
#
# list1 =  [
#   { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
#   { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
#   { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
#   { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
#   ]
# your function should return true as there is at least one developer from the required 5 geographic zones.
#
# Notes:
#
# The input array and continent names will always be valid and formatted as in the list above for example 'Africa'
# will always start with upper-case 'A'.
#
#
#
#
# This kata is part of the Coding Meetup series which includes a number of short and
# easy to follow katas which have been designed to allow mastering the use of higher-order functions.
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
def all_continents(lst):
    return len(set(i["continent"] for i in lst)) == 5