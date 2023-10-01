# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.
#
# For example:
#
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []
# FUNDAMENTALS
# Solution
def solution(nums):
    if not nums:
        return []
    nums.sort()
    return nums