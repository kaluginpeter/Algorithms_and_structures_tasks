# In Germany we have "LOTTO 6 aus 49". That means that 6 of 49 numbers are drawn as winning combination.
# There is also a "Superzahl", an additional number, which can increase your winning category.
#
# In this kata you have to write two methods.
#
# def number_generator():
#
# def check_for_winning_category(your_numbers, winning_numbers):
# The first method is for drawing the lottery numbers.
# You have to create an array with 7 random numbers. 6 from these are from 1 - 49.
# Of course every number may only occur once.
# And the 7th number is the "Superzahl". A number from 0 - 9. This number is independent from the first six numbers.
# The first 6 numbers have to be in ascending order.
#
# A result could be:
# 4, 9, 17, 22, 25, 35, 0
# Or:
# 4, 18, 22, 34, 41, 44, 4
#
# The second method should check a given number against the winning combination and have to return the winning category:
#
# 1  - 6 numbers and Superzahl match
# 2  - 6 numbers match
# 3  - 5 numbers and Superzahl match
# 4  - 5 numbers match
# 5  - 4 numbers and Superzahl match
# 6  - 4 numbers match
# 7  - 3 numbers and Superzahl match
# 8  - 3 numbers match
# 9  - 2 numbers and Superzahl match
# -1 - if the numbers do not match any of the rules above
#
#
# Have fun coding it and please don't forget to vote and rank this kata! :-)
#
# I have created other katas. Have a look if you like coding and challenges.
#
# MATHEMATICSALGORITHMS
# Solution
import random
def number_generator():
    ans: list = [random.randint(1, 49) for i in range(6)]
    return sorted(ans) + [random.randint(0, 9)]

def check_for_winning_category(your_numbers, winning_numbers):
    count: int = sum(i in winning_numbers[:6] for i in your_numbers[:6])
    top: int = your_numbers[-1] == winning_numbers[-1]
    if count == 6: return 1 if top else 2
    elif count == 5: return 3 if top else 4
    elif count == 4: return 5 if top else 6
    elif count == 3: return 7 if top else 8
    elif count == 2: return 9 if top  else -1
    return -1