# Consider having a cow that gives a child every year from her fourth
# year of life on and all her subsequent children do the same.
#
# After n years how many cows will you have?
#
# countCows(0); // should equal 1
# countCows(1); // should equal 1
# countCows(3); // should equal 2
# countCows(4); // should equal 3
# countCows(10);// should equal 28
# Return null if n is not an integer.
#
# Note: Assume all the cows are alive after n years.
#
# MATHEMATICSPUZZLES
# Solution
def count_cows(n):
    if not isinstance(n, int): return None
    return count_cows(n-1) + count_cows(n-3) if n > 2 else 1