# Given a list r, return how long it would take a tunnel boring machine to excavate a tunnel through r.
#
# r is a list that contain the following sections made of combinations of the following:
#
# Very hard rock []: this section takes 60 minutes to excavate
# Hard Rock {}: this section takes 50 minutes to excavate
# Somewhat Hard Rock (): this section takes 40 minutes to excavate
# Somewhat Soft Rock ||: this section takes 30 minutes to excavate
# Soft Rock ::: this section takes 20 minutes to excavate
# Broken Rock   : this section only needs to be cleared (see below)
# After every 3 sections it excavates, the machine needs to stop for 30 minutes so workers can remove the excavated rock.
#
# Notes:
# The returned time should be in minutes
# 'r' may contain sections with only one half. Example: [ should equal 30
# Examples
# tunnel_digging(['()', ')']) # returns 60
# tunnel_digging([': ', '  ', ': ']) # returns 50
# tunnel_digging(['|)', '{ ', '{ ', '|]', '{ ', ' }']) # returns 240
# tunnel_digging(['( ', '()', '(}', '[]', '{ ', '{ ']) # returns 275
# tunnel_digging(['  ', '{ ', '[ ', '[)', '[}']) # returns 190
# tunnel_digging(['{ ', ' }', '[}', ': ', '[ ', ':|']) # returns 230
# FUNDAMENTALS
# Solution
def tunnel_digging(r):
    ht: dict[str, int] = {
        '[': 30, ']': 30, '{': 25, '}': 25,
        '(': 20, ')': 20, '|': 15, ':': 10,
        ' ': 0,
    }
    total: int = 0
    moves: int = 0
    for move in r:
        for char in move:
            total += ht.get(char)
        moves += 1
        if moves % 3 == 0:
            total += 30
    return total