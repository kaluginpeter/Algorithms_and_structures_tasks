# Given an array of integers arr,
# return true if the number of occurrences of each value in the array is unique or false otherwise.
#
# Example 1:
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
#
# Input: arr = [1,2]
# Output: false
# Example 3:
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# Solution
class Solution(object):
    def uniqueOccurrences(self, arr):
        counter = Counter(arr).values()
        if(len(counter) == len(set(counter))): return True
        return False


# Solution 2 O(N) O(N) HashTable and HashSet
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ht: dict = {}
        for i in arr:
            ht[i] = ht.get(i, 0) + 1
        hs: set = set()
        for i in ht:
            if ht[i] in hs:
                return False
            else:
                hs.add(ht[i])
        return True
# Solution 3 O(N) O(N) HashTable
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ht: dict = {}
        for i in arr:
            ht[i] = ht.get(i, 0) + 1
        return len(ht.values()) == len(set(ht.values()))