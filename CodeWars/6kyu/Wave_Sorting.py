# A list of integers is sorted in “Wave” order if alternate items are not less than their immediate neighbors (thus the other alternate items are not greater than their immediate neighbors).
#
# Thus, the array [4, 1, 7, 5, 6, 2, 3] is in Wave order because 4 >= 1, then 1 <= 7, then 7 >= 5, then 5 <= 6, then 6 >= 2, and finally 2 <= 3.
#
# The wave-sorted lists has to begin with an element not less than the next, so [1, 4, 5, 3] is not sorted in Wave because 1 < 4
#
# Your task is to implement a function that takes a list of integers and sorts it into wave order in place; your function shouldn't return anything.
#
# Note:
#
# The resulting array shouldn't necessarily match anyone in the tests, a function just checks if the array is now wave sorted.
# ALGORITHMSARRAYSLOGICSORTING
# Solution
def wave_sort(a):
    a.sort(reverse=True)
    n: int = len(a)
    n = n // 2 + 1 if n % 2 != 0 else n // 2
    ans: list = []
    left, right = 0, n
    while right < len(a):
        ans.append(a[left])
        ans.append(a[right])
        left, right = left + 1, right + 1
    if left != n:
        ans.append(a[left])
    for i in range(len(a)):
        a[i] = ans[i]