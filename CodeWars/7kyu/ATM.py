# An ATM has banknotes of nominal values 10, 20, 50, 100, 200 and 500 dollars. You can consider that there is a large enough supply of each of these banknotes.
#
# You have to write the ATM's function that determines the minimal number of banknotes needed to honor a withdrawal of n dollars, with 1 <= n <= 1500.
#
# Return that number, or -1 if it is impossible.
#
# Good Luck!!!
#
# FUNDAMENTALSMATHEMATICSALGORITHMS
# Solution
def solve(n):
    d = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0}
    for i in d:
        while n >= i:
            d[i] = n // i
            n %= i
    if n > 0:
        return -1
    return sum(v for v in d.values())