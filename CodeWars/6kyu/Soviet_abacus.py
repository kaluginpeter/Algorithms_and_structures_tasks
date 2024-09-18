# Soviet abacus
# In the recent past, when calculators were not so common, the abacus was used to calculate prices
# Your task is to learn how to use them
#
# You will receive a matrix as input
# Size of matrix: 9x6
# Cost of a row:
# 1 = 0.01 (or 1 cent/penny)
# 2 = 0.1 (or 10 cents/pennies)
# 3 = 1
# 4 = 10
# 5 = 100
# 6 = 1000
# Each row has its own price (the price is indicated above). To get 1230 - you need to have 3 beads on the left on the 4th row, 2 beads on the 5th row and 1 bead on the 6th row. It is necessary to take into account only the consecutive beads on the left
#
# Because floating-point numbers should not be used for monetary amounts, as we want exact results, you will return a Decimal.
#
# Trivia: this abacus design was popular in the USSR.
#
# Example:
# First:
# [
#     [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0],
# ] -> 1.3
#
# Second:
# [
#     [1, 0, 0, 1, 1, 1, 0, 0, 0],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0, 0, 0, 0, 0],
# ] -> 1203.11
#
# Third:
# [
#     [1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0],
# ] -> 3214.36
# ALGORITHMSMATRIX
# Solution
from decimal import Decimal

def abacus(abacus_rows: list[list[int]]) -> Decimal:
    amount: dict[int, int] = {1: 0.01, 2: 0.1, 3: 1, 4: 10, 5: 100, 6: 1000}
    result: int = 0
    for i in range(1, 7):
        move: bool = False
        for module in range(9):
            if abacus_rows[i - 1][module] == 0:
                result += module * amount[i]
                move = True
                break
        if not move and abacus_rows[i - 1][-1] == 1:
            result += 9 * amount[i]
    return Decimal(str(result)).quantize(Decimal('0.01'))