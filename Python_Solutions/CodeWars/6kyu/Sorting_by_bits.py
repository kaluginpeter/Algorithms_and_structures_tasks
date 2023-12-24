# In this kata you're expected to sort an array of 32-bit integers in ascending order of the number of on bits they have.
#
# E.g Given the array [7, 6, 15, 8]
#
# 7 has 3 on bits (000...0111)
# 6 has 2 on bits (000...0110)
# 15 has 4 on bits (000...1111)
# 8 has 1 on bit (000...1000)
# So the array in sorted order would be [8, 6, 7, 15].
#
# In cases where two numbers have the same number of bits, compare their real values instead.
#
# E.g between 10 (...1010) and 12 (...1100), they both have the same number of on bits '2' but the integer 10 is less than 12 so it comes first in sorted order.
#
# Your task is to write a function that takes an array of integers and sort them as described above.
#
# Note: your solution has to sort the array in place.
#
# Example:
#
# [3, 8, 3, 6, 5, 7, 9, 1]   =>    [1, 8, 3, 3, 5, 6, 9, 7]
# LOGICARRAYSALGORITHMSDATA STRUCTURESFUNDAMENTALSBITSBINARYSORTING
# Solution 1 - Using sort
def sort_by_bit(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
# Solution 2 -Bubble sort
def sort_by_bit(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            top = bin(arr[j])[2:].count('1')
            x = bin(arr[j + 1])[2:].count('1')
            if top > x:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif top == x:
                m = min(arr[j], arr[j + 1])
                m_ind = j if arr[j] == m else j + 1
                arr[j], arr[j + 1] = arr[m_ind], arr[j if j != m_ind else j + 1]