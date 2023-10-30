# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
#
# Return the array after sorting it.
#
#
#
# Example 1:
#
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
# Example 2:
#
# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
#
#
# Constraints:
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 104
# Solution 1 list
class Solution(object):
    def sortByBits(self, arr):
        d, ans = [], []
        for i in arr:
            d.append((i, bin(i).count('1')))
        for i in range(len(d)):
            top, val = float('inf'), float('inf')
            for j in d:
                if j[1] < top:
                    val, top = j[0], j[1]
                elif j[1] == top:
                    if j[0] < val:
                        val, top = j[0], j[1]
            ans.append(val)
            d.remove((val, top))
        return ans
# Solution 2 Hashtable
class Solution(object):
    def sortByBits(self, arr):
        d, ans = {}, []
        for i in arr:
            d[i] = d.get(i, 0) + 1
        while d:
            top, val = float('inf'), float('inf')
            for j in d:
                x = bin(j).count('1')
                if x < top:
                    val, top = j, x
                elif x == top:
                    if j < val:
                        val, top = j, x
            d[val] -= 1
            if d[val] == 0:
                del d[val]
            ans.append(val)
        return ans
# Solution 3 Math with bits
class Solution(object):
    def sortByBits(self, arr):
        for i in range(len(arr)):
            arr[i] += bin(arr[i]).count('1') * 10001
        arr.sort()
        for i in range(len(arr)):
            arr[i] = arr[i] % 10001
        return arr