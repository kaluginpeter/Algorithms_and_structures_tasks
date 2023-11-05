# Given an integer array arr of distinct integers and an integer k.
#
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
#
# Return the integer which will win the game.
#
# It is guaranteed that there will be a winner of the game.
#
#
#
# Example 1:
#
# Input: arr = [2,1,3,5,4,6,7], k = 2
# Output: 5
# Explanation: Let's see the rounds of the game:
# Round |       arr       | winner | win_count
#   1   | [2,1,3,5,4,6,7] | 2      | 1
#   2   | [2,3,5,4,6,7,1] | 3      | 1
#   3   | [3,5,4,6,7,1,2] | 5      | 1
#   4   | [5,4,6,7,1,2,3] | 5      | 2
# So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
# Example 2:
#
# Input: arr = [3,2,1], k = 10
# Output: 3
# Explanation: 3 will win the first 10 rounds consecutively.
#
#
# Constraints:
#
# 2 <= arr.length <= 105
# 1 <= arr[i] <= 106
# arr contains distinct integers.
# 1 <= k <= 109
# Solution 1 - Speed O(N) / Memory O(1)
class Solution(object):
    def getWinner(self, arr, k):
        top, count = arr[0], 0
        for i in range(1, len(arr)):
            if arr[i] > top:
                top, count = arr[i], 0
            count += 1
            if count == k:
                break
        return top
# Solution 2 - Speed O(N) / Memory O(N * N)
class Solution(object):
    def getWinner(self, arr, k):
        if k >= len(arr):
            return max(arr)
        from collections import defaultdict
        d = defaultdict(int)
        while True:
            x, y = arr[0], arr[1]
            if x > y:
                d[x] += 1
                arr.append(arr.pop(1))
            else:
                d[y] += 1
                arr.append(arr.pop(0))
            if d[arr[0]] == k:
                return arr[0]