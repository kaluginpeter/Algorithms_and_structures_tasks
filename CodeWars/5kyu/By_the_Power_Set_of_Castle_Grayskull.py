# Write a function that returns all of the sublists of a list/array.
#
# Example:
#
# �
# �
# �
# �
# �
# (
# [
# 1
# ,
# 2
# ,
# 3
# ]
# )
# ;
# =
# >
# [
# [
# ]
# ,
# [
# 1
# ]
# ,
# [
# 2
# ]
# ,
# [
# 1
# ,
# 2
# ]
# ,
# [
# 3
# ]
# ,
# [
# 1
# ,
# 3
# ]
# ,
# [
# 2
# ,
# 3
# ]
# ,
# [
# 1
# ,
# 2
# ,
# 3
# ]
# ]
# power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# For more details regarding this, see the power set entry in wikipedia.
#
# MATHEMATICSALGORITHMS
# Solution
def power(a):
    subsets: list = [[]]
    for i in a:
        for idx in range(len(subsets)):
            subsets.append(subsets[idx] + [i])
    return subsets