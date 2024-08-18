# Write
#
# function wordStep(str)
# that takes in a string and creates a step with that word.
#
# E.g
#
# wordStep('SNAKES SHOE EFFORT TRUMP POTATO') ===
#
# [['S','N','A','K','E','S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ','E','F','F','O','R','T',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','U',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' '],
#  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','P','O','T','A','T','O']]
# Every word will end with the character that the next word will start with.
# You will start top left of the array and end bottom right. All cells that
# are not occupied by a letter needs to be a space ' '
#
# ALGORITHMS
# Solution
def word_step(s):
    wo = s.split(" ")
    l, h = (sum(len(j) - 1 for j in wo[i::2]) + 1 for i in range(2))
    arr = [[" " for i in range(l)] for j in range(h)]
    l = [0, 0]
    for i, w in enumerate(wo):
        for j, c in enumerate(w):
            l[i % 2] += 1 if j else 0
            arr[l[1]][l[0]] = c
    return arr