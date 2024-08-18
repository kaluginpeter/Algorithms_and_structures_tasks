# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own,
# to enjoy the process --myjinxin2015 said
#
# Description:
# Give you two number rows , columns and a string str. Returns a rows x columns table
# pattern and fill in the str(each grid fill in a char, the length of str is always less than or equals
# to the total numbers of grids):
#
# If rows = 4 and columns = 4, str = "Hello World!"
# The pattern should be a 4x4 table like this:
# +---+---+---+---+
# | H | e | l | l |   From left to right
# +---+---+---+---+
# | o |   | W | o |   and from top to bottom
# +---+---+---+---+
# | r | l | d | ! |   each row separated by "\n"
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# Some examples:
# pattern(3, 3, "codewars") should return:
# +---+---+---+
# | c | o | d |
# +---+---+---+
# | e | w | a |
# +---+---+---+
# | r | s |   |
# +---+---+---+
#
# pattern(4, 3, "Nice pattern") should return:
# +---+---+---+
# | N | i | c |
# +---+---+---+
# | e |   | p |
# +---+---+---+
# | a | t | t |
# +---+---+---+
# | e | r | n |
# +---+---+---+
#
# pattern(3, 4, "Nice pattern") should return:
# +---+---+---+---+
# | N | i | c | e |
# +---+---+---+---+
# |   | p | a | t |
# +---+---+---+---+
# | t | e | r | n |
# +---+---+---+---+
# ASCII ARTPUZZLES
# Solution
def pattern(rows, col, s):
    seperator, res, l, index = '+---'*col + '+', '', len(s), 0
    for _ in range(rows):
        res += seperator+'\n'
        for c in range(col):
            if index < l: res += f'| {s[index]} '
            else: res += '|   '
            index += 1
        res += '|\n'
    res += seperator
    return res