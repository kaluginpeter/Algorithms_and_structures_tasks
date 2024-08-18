# You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Given the following input array:
#
# list1 = [
#   { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
#   { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
#   { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
#   { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
# ]
# Write a function that returns the array sorted alphabetically by the programming language. In case there are some developers that code in the same language, sort them alphabetically by the first name:
#
# [
#   { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
#   { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" },
#   { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
#   { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" }
# ]
# Notes:
#
# The input array will always be valid and formatted as in the example above.
# The array does not include developers coding in the same language and sharing the same name.
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
# Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language
#
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESARRAYSFUNDAMENTALSALGORITHMSSORTING
# Solution
def sort_by_language(arr):
	return sorted(arr, key=lambda x: (x["language"], x["first_name"]))