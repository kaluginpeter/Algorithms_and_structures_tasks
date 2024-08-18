# You are given two positive integer arrays nums and target, of the same length.
#
# In a single operation, you can select any
# subarray
#  of nums and increment or decrement each element within that subarray by 1.
#
# Return the minimum number of operations required to make nums equal to the array target.
#
#
#
# Example 1:
#
# Input: nums = [3,5,1,2], target = [4,6,2,4]
#
# Output: 2
#
# Explanation:
#
# We will perform the following operations to make nums equal to target:
# - Increment nums[0..3] by 1, nums = [4,6,2,3].
# - Increment nums[3..3] by 1, nums = [4,6,2,4].
#
# Example 2:
#
# Input: nums = [1,3,2], target = [2,1,4]
#
# Output: 5
#
# Explanation:
#
# We will perform the following operations to make nums equal to target:
# - Increment nums[0..0] by 1, nums = [2,3,2].
# - Decrement nums[1..1] by 1, nums = [2,2,2].
# - Decrement nums[1..1] by 1, nums = [2,1,2].
# - Increment nums[2..2] by 1, nums = [2,1,3].
# - Increment nums[2..2] by 1, nums = [2,1,4].
#
#
#
# Constraints:
#
# 1 <= nums.length == target.length <= 105
# 1 <= nums[i], target[i] <= 108
# General idea:
# For minimize operations we should choose maximum subarray contain integers with same needed operations. For definition of subarray we can use sliding window approach. Lets define a "way"* (using first element of array) and iterate from entire array of needed differences. At each iteration check:
# If current number "way"* not equal with "way"* of our subarray, we should make all needed numbers in subarray positive(for simplify work of helper function) and calculatate needed operations on that subarray. Then move left pointer to current right pointer and define new "way"*
# If current number "way"* same as in subarray, just continue iterating, meaning increasing our subarray
# After end of loop we should check array on case where our subarray have all same opeartions and our subarray size is the same as length of array. Meaning that sliding window increases all iteration
# *way = boolean, define integer either negative or positive.
#
# Helper funcion idea
# Function will take 3 arguments: array(meaning our subarray), left and right pointers definding length of current subarray(sliding window)
# For making minimum operations we need choose maximum consecutive inegers(subarray) that not separate with 0. Then recursive call for current subarray with less boundary pointers.
# Example:
# 1) [2, 1, 2] -> we can use subarray with size equal of array size, because all numbers need to descrease to zero(for this we creating all number positive in main function, before calling helper function)
# 2) [1, 0, 1] -> we cannot use subarray with length of array, because our integers seprated with zero, so we use number at index 0
# 3) [0, 0, 1] -> we only can use subarray contain integer with number at index 2
# We need only 3 operation to make all numbers in subarray equal to 0
# If left pointer more than right - return 0, because it means that our subarray have 0 length
# Create a local right pointer for definding new sliding window. Iterate from until local_right pointer less than global right pointer.- - In loop create second loop with condition: "until local right pointer less that global right pointer and current integer not equal to 0". At each iteration of inner loop, choosing minimum element that can be use for operations(because see at example code above, we cant swapp all integers at 2 operations, because number at index 1 have value 1 and its less than value of her neighbours. So it means that minimum value will separate our subarray on two subarrays)
# After ending inner loop we should check that minimum value extist(it means that we found subarray) and if it is, we should subtract minimum value from all integers in subarray and add minimum_value to total needed operation, make minimum_value on infinity and add to total needed operation recursive call for our subarray with boundaries: left to local right poniter.
# At the end of each iteration in outer loop, just increase our local right pointer
# After the end of outer loop check on case where we our subarray already have all similar integers without zeros. Like [1, 2, 3, 4] and length of our current subarray is 4, thats equals to array length. Calculate minimum operations by adding minimum value to total needed operation, then subtract minimum value from all integers in subarray and add result of recursive call(with boundaries: left to local_right + 1 because we iterate until local_right less than global right) to total needed operations
# Note:
# While subtracting minimum value from all integers in subarray, we should keep in mind that each integer can't be less that 0
# Similar problem:
# 1526
#
# Complexity
# Time complexity: O(N**2)
# Space complexity: O(N)
# Code
class Solution:
    def needed_operations(self, arr: list[int], left: int, right: int) -> int:
        operations: int = 0
        if left > right: return operations # our subarray have 0 length

        local_right: int = left
        min_value: int = float('inf') # Define minimum value that we can use to minimuze total operations
        while local_right < right:
            # Create second loop until we can increase sliding window
            while local_right < right and arr[local_right] != 0:
                min_value = min(min_value, arr[local_right])
                local_right += 1
            # If subarray exist
            if min_value != float('inf'):
                # Subtract minimum value from all numbers in subarray
                arr[left:local_right] = [max(x - min_value, 0) for x in arr[left:local_right]]
                operations += min_value
                min_value = float('inf')
                # Create recursive call to count how many operations needed perform on subarray
                operations += self.needed_operations(arr, left, local_right)

            local_right += 1 # Move our sliding window length
        # Case where subarray can be same size as array length
        if min_value != float('inf'):
            arr[left:local_right + 1] = [max(x - min_value, 0) for x in arr[left:local_right + 1]]
            operations += min_value # Minimum number that we can choose to minimize operations
            # Caclulate needed operations on our subarray by recursive call
            operations += self.needed_operations(arr, left, local_right + 1)

        return operations

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        needed: list[int] = [i_nums - i_target for i_nums, i_target in zip(nums, target)]
        operations: int = 0
        left: int = 0
        way: bool = needed[left] > 0 # Define current way of subarray
        for right in range(len(nums)):
            current_way: bool = needed[right] > 0 # Way of current element
            if current_way != way:
                # Makes all integers positive for simplify logic of helper function
                needed[left:right] = [abs(i) for i in needed[left:right]]
                # Calculate how many operations we need make on our subarray
                operations += self.needed_operations(needed, left, right)

                left = right # Move left pointer to right
                way = current_way # Take current way of number to new current way of subarray
        # Case where our subarray can be same size as array length
        needed[left:len(nums)] = [abs(i) for i in needed[left:len(nums)]]
        operations += self.needed_operations(needed, left, len(nums))

        return operations
