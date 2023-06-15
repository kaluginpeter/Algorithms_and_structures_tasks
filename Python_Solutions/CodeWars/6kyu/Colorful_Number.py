# Problem
# Determine whether a positive integer number is colorful or not.
#
# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different;
# whereas 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] have 6 twice.
#
# So take all consecutive subsets of digits, take their product and ensure all the products are different.
#
# Examples
# 263  -->  true
# 236  -->  false
# ALGORITHMS
# Solution
def colorful(number):
    l = []
    for x in str(number): l.append(int(x))
    for y in range(len(l) - 1):
        temp = l[y] * l[y + 1]
        l.append(temp)
    return len(set(l)) == len(l)