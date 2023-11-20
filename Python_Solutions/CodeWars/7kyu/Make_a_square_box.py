# Easy; Make a box
# Given a number as a parameter (between 2 and 30), return an array containing strings which form a box.
# Like this:
#
# n = 5
#
# [
#   '-----',
#   '-   -',
#   '-   -',
#   '-   -',
#   '-----'
# ]
# n = 3
#
# [
#   '---',
#   '- -',
#   '---'
# ]
# STRINGSARRAYSASCII ARTALGORITHMS
# Solution
def box(n):
    l = []
    for i in range(n):
        if i in {0, n -1}:
            l.append('-' * n)
        else:
            l.append('-' + ' ' * (n - 2) + '-')
    return l