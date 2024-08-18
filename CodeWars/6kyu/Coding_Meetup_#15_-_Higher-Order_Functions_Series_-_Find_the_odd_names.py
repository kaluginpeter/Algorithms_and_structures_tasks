# You will be given an array of objects representing data about developers who have signed up
# to attend the next coding meetup that you are organising.
#
# Given the following input array:
#
# var list1 = [
#   { firstName: 'Aba', lastName: 'N.', country: 'Ghana', continent: 'Africa', age: 21, language: 'Python' },
#   { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
# ];
# write a function that when executed as findOddNames(list1) returns only the developers where if
# you add the ASCII representation of all characters in their first names, the result will be an odd number:
#
# [
#   { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
# ]
# Explanation of the above:
#
# Sum of ASCII codes of letters in 'Aba' is: 65 + 98 + 97 = 260 which is an even number
# Sum of ASCII codes of letters in 'Abb' is: 65 + 98 + 98 = 261 which is an odd number
# Notes:
#
# Preserve the order of the original list.
# Return an empty array [] if there is no developer with an "odd" name.
# The input array and first names will always be valid and formatted as in the example above.
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
# Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language
#
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESARRAYSFUNDAMENTALSALGORITHMSSTRINGS
# Solution
def find_odd_names(lst):
    return [i for i in lst if sum(map(ord, i["firstName"])) % 2]