# Task
# You are given a string s.
#
# Let us call a substring of s with 2 or more adjacent identical letters a group (such as "aa", "bbb", "cccc"...).
#
# Let us call a substring of s with 2 or more adjacent groups a big group (such as "aabb","bbccc"...).
#
# Your task is to count the number of big groups in the given string.
#
# Examples
# "ccccoodeffffiiighhhhhhhhhhttttttts" => 3
#
# The groups are "cccc", "oo", "ffff", "iii", "hhhhhhhhhh", "ttttttt".
#
# The big groups are "ccccoo", "ffffiii", "hhhhhhhhhhttttttt".
#
# "gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp" => 2
#
# The big groups are :
#
# "xxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmm" and "tttttttlllll"
#
# "soooooldieeeeeer" => 0
#
# There is no big group.
#
# Input/Output
# [input] string s
#
# A string of lowercase Latin letters.
#
# [output] an integer
#
# The number of big groups.
#
# ALGORITHMS
# Solution
def repeat_adjacent(st):
    count: int = 0
    lst: list = list()
    el, count_el = None, 0
    for i in st:
        if el is None:
            el, count_el = i, 1
        elif el == i:
            count_el += 1
        else:
            if count_el == 1:
                if len(lst) > 1:
                    count += 1
                lst.clear()
            else:
                lst.append(count_el)
            el, count_el = i, 1
    if count_el > 1:
        lst.append(count_el)
    if len(lst) > 1:
        count += 1
    return count