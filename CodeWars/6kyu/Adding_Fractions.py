# In most languages, division immediately produces decimal values, and therefore, adding two fractions gives a decimal result:
#
# (1/2) + (1/4) #=> 0.75
# But what if we want to be able to add fractions and get a fractional result?
#
# (1/2) + (1/4) #=> 3/4
# Task:
# Your job here is to implement a function, add_fracs that takes any number of fractions (positive OR negative) as strings, and yields the exact fractional value of their sum in simplest form. If the sum is greater than one (or less than negative one), it should return an improper fraction. If there are no arguments passed, (add_fracs()), return an empty string. Inputs will always be valid fractions, and the output should also be a string. If the result is an integer, like '2/1', just return '2'. Input numerators (but NOT denominators) can be zero.
#
# How the function will be called:
# add_fracs(any_number_of_fractions1, any_number_of_fractions2, any_number_of_fractions3, ...) #=> a fraction as a string
# Some examples (see example test cases for more):
# add_fracs() #=> ""
# add_fracs("1/2") #=> "1/2"
# add_fracs("1/2", "1/4") #=> "3/4"
# add_fracs("1/2", "3/4") #=> "5/4"
# add_fracs("2/4", "6/4", "4/4") #=> "3"
# add_fracs("2/3", "1/3", "4/6") #=> "5/3"
# add_fracs("-2/3", "5/3", "-4/6") #=> "1/3"
# If there are any issues with the description, test cases or anything else, please do let me know by commenting or marking an issue. Otherwise, make sure to rank and mark as ready. Enjoy!
#
# Also check out my other creations — Split Without Loss, Random Integers, Implement String#transpose, Implement Array#transpose!, Arrays and Procs #1, and Arrays and Procs #2
#
# Fundamentals
# Solution
from math import lcm


def add_fracs(*args) -> str:
    output: str = ''
    if not args: return output
    cur_ratio: list[int, int] = None
    for ratio in args:
        num, den = map(int, ratio.split('/'))
        if cur_ratio is None:
            cur_ratio = [num, den]
        else:
            common: int = lcm(cur_ratio[1], den)
            new_num: int = cur_ratio[0] * (common // cur_ratio[1]) + num * (common // den)
            cur_ratio = [new_num, common]
    d: int = 2
    while d <= cur_ratio[1]:
        if cur_ratio[0] % d != 0 or cur_ratio[1] % d != 0:
            d += 1
            continue
        cur_ratio[0] //= d
        cur_ratio[1] //= d
    if not cur_ratio[0]:
        return '0'
    elif cur_ratio[1] == 1:
        return str(cur_ratio[0])
    return '/'.join(map(str, cur_ratio))
