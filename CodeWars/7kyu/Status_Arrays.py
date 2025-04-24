# The status of each element of an array of integers can be determined by its position in the array and the value of the other elements in the array. The status of an element E in an array of size N is determined by adding the position P, 0 <= P < N, of the element in the array to the number of array elements in the array that are less than E.
#
# For example, consider the array containing the integers: 6 9 3 8 2 3 1. The status of the element 8 is 8 because its position is 3 and there are 5 elements in the array that are less than 8.
#
# You will return the elements of the original array from low to high status order. In the event there is a tie for status of two or more elements, you will output them in order of appearance in the array.
#
# EXAMPLE:
#
# status([6, 9, 3, 8, 2, 3, 1]) = [6, 3, 2, 1, 9, 3, 8]
# ArraysAlgorithms
# Solution
import heapq
def status(nums):
    min_heap: list[int] = []
    for i in range(len(nums)):
        status: int = i + sum(num < nums[i] for num in nums)
        heapq.heappush(min_heap, (status, i))
    output: list[int] = []
    while min_heap:
        output.append(nums[heapq.heappop(min_heap)[1]])
    return output