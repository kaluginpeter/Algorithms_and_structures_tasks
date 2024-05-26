# There is an implementation of quicksort algorithm. Your task is to fix it. All inputs are correct.
#
# See also: https://en.wikipedia.org/wiki/Quicksort
#
# SORTINGALGORITHMSFUNDAMENTALSDEBUGGING
# Solution
def quicksort(arr):
    if len(arr) < 1: return arr
    p = arr[0]
    less = [i for i in arr[1:] if i < p]
    greater = [i for i in arr[1:] if i >= p]
    return quicksort(less) + [p] + quicksort(greater)