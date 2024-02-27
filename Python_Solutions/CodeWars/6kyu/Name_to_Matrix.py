# Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array).
#
# You will need to add periods (.) to the end of the name if necessary, to turn it into a matrix.
#
# If the name has a length of 0, return "name must be at least one letter"
#
# Examples
# "Bill" ==> [ ["B", "i"],
#              ["l", "l"] ]
#
# "Frank" ==> [ ["F", "r", "a"],
#               ["n", "k", "."],
#               [".", ".", "."] ]
# STRINGSARRAYSALGORITHMSMATRIX
# Solution
def matrixfy(st):
    if not st:
        return 'name must be at least one letter'
    n: int = 1
    while n * n < len(st):
        n += 1
    ans: list = list()
    indx: int = 0
    for i in range(n):
        top: list = list()
        for j in range(n):
            if indx == len(st):
                top.append('.')
            else:
                top.append(st[indx])
                indx += 1
        ans.append(top)
    return ans