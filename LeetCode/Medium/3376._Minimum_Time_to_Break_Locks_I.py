# Bob is stuck in a dungeon and must break n locks, each requiring some amount of energy to break. The required energy for each lock is stored in an array called strength where strength[i] indicates the energy needed to break the ith lock.
#
# To break a lock, Bob uses a sword with the following characteristics:
#
# The initial energy of the sword is 0.
# The initial factor X by which the energy of the sword increases is 1.
# Every minute, the energy of the sword increases by the current factor X.
# To break the ith lock, the energy of the sword must reach at least strength[i].
# After breaking a lock, the energy of the sword resets to 0, and the factor X increases by a given value K.
# Your task is to determine the minimum time in minutes required for Bob to break all n locks and escape the dungeon.
#
# Return the minimum time required for Bob to break all n locks.
#
#
#
# Example 1:
#
# Input: strength = [3,4,1], K = 1
#
# Output: 4
#
# Explanation:
#
# Time	Energy	X	Action	Updated X
# 0	0	1	Nothing	1
# 1	1	1	Break 3rd Lock	2
# 2	2	2	Nothing	2
# 3	4	2	Break 2nd Lock	3
# 4	3	3	Break 1st Lock	3
# The locks cannot be broken in less than 4 minutes; thus, the answer is 4.
#
# Example 2:
#
# Input: strength = [2,5,4], K = 2
#
# Output: 5
#
# Explanation:
#
# Time	Energy	X	Action	Updated X
# 0	0	1	Nothing	1
# 1	1	1	Nothing	1
# 2	2	1	Break 1st Lock	3
# 3	3	3	Nothing	3
# 4	6	3	Break 2nd Lock	5
# 5	5	5	Break 3rd Lock	7
# The locks cannot be broken in less than 5 minutes; thus, the answer is 5.
#
#
#
# Constraints:
#
# n == strength.length
# 1 <= n <= 8
# 1 <= K <= 10
# 1 <= strength[i] <= 106
# Solution
# Python O(N!) O(1) Permutations
import itertools

class Solution:
    def time_needed(self, wall: int, energy: int) -> int:
        return wall // energy + int(wall % energy != 0)

    def findMinimumTime(self, strength: List[int], K: int) -> int:
        n: int = len(strength)
        min_time: int = float('inf')
        for perm in itertools.permutations(strength):
            time_spent: int = 0
            current_energy: int = 1
            for wall_strength in perm:
                time_spent += self.time_needed(wall_strength, current_energy)
                current_energy += K
            min_time = min(min_time, time_spent)
        return min_time if min_time != float('inf') else -1