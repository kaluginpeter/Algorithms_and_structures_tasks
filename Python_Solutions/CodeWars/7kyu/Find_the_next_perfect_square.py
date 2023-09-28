# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
#
# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square
# ALGEBRAFUNDAMENTALS
# Solution
def find_next_square(sq):
    perfect_sq = sq ** .5
    if perfect_sq.is_integer():
        return (perfect_sq + 1) ** 2
    else:
        return -1