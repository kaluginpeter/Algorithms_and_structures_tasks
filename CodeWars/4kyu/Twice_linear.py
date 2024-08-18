# Consider a sequence u where u is defined as follows:
#
# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
#
# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
#
# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
#
# Example:
# dbl_linear(10) should return 22
#
# Note:
# Focus attention on efficiency
#
# MATHEMATICSALGORITHMS
# Solution
import heapq
def dbl_linear(n):
    u_set = {1}
    u_heap = [1]
    for _ in range(n):
        smallest = heapq.heappop(u_heap)
        y = 2 * smallest + 1
        z = 3 * smallest + 1
        if y not in u_set:
            u_set.add(y)
            heapq.heappush(u_heap, y)
        if z not in u_set:
            u_set.add(z)
            heapq.heappush(u_heap, z)
    return heapq.heappop(u_heap)