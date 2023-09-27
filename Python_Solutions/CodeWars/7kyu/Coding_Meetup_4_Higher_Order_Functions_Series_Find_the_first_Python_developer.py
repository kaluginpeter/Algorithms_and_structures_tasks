# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising. The list is ordered according to who signed up first.
#
# Your task is to return one of the following strings:
#
# < firstName here >, < country here > of the first Python developer who has signed up; or
# There will be no Python developers if no Python developer has signed up.
# For example, given the following input array:
#
# list1 = [
#   { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
#   { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
#   { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
# ]
# your function should return Victoria, Puerto Rico.
#
# Notes:
#
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
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESARRAYSFUNDAMENTALSALGORITHMSSTRINGSREGULAR EXPRESSIONS
# Solution
def get_first_python(users):
    for user in users:
        if user['language'] == 'Python':
            return f'{user["first_name"]}, {user["country"]}'
    return 'There will be no Python developers'