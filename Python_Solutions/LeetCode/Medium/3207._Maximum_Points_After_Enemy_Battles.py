# You are given an integer array enemyEnergies denoting the energy values of various enemies.
#
# You are also given an integer currentEnergy denoting the amount of energy you have initially.
#
# You start with 0 points, and all the enemies are unmarked initially.
#
# You can perform either of the following operations zero or multiple times to gain points:
#
# Choose an unmarked enemy, i, such that currentEnergy >= enemyEnergies[i]. By choosing this option:
# You gain 1 point.
# Your energy is reduced by the enemy's energy, i.e. currentEnergy = currentEnergy - enemyEnergies[i].
# If you have at least 1 point, you can choose an unmarked enemy, i. By choosing this option:
# Your energy increases by the enemy's energy, i.e. currentEnergy = currentEnergy + enemyEnergies[i].
# The enemy i is marked.
# Return an integer denoting the maximum points you can get in the end by optimally performing operations.
#
#
#
# Example 1:
#
# Input: enemyEnergies = [3,2,2], currentEnergy = 2
#
# Output: 3
#
# Explanation:
#
# The following operations can be performed to get 3 points, which is the maximum:
#
# First operation on enemy 1: points increases by 1, and currentEnergy decreases by 2. So, points = 1, and currentEnergy = 0.
# Second operation on enemy 0: currentEnergy increases by 3, and enemy 0 is marked. So, points = 1, currentEnergy = 3, and marked enemies = [0].
# First operation on enemy 2: points increases by 1, and currentEnergy decreases by 2. So, points = 2, currentEnergy = 1, and marked enemies = [0].
# Second operation on enemy 2: currentEnergy increases by 2, and enemy 2 is marked. So, points = 2, currentEnergy = 3, and marked enemies = [0, 2].
# First operation on enemy 1: points increases by 1, and currentEnergy decreases by 2. So, points = 3, currentEnergy = 1, and marked enemies = [0, 2].
# Example 2:
#
# Input: enemyEnergies = [2], currentEnergy = 10
#
# Output: 5
#
# Explanation:
#
# Performing the first operation 5 times on enemy 0 results in the maximum number of points.
#
#
#
# Constraints:
#
# 1 <= enemyEnergies.length <= 105
# 1 <= enemyEnergies[i] <= 109
# 0 <= currentEnergy <= 109

# Solution Greedy Sorting O(NlogN) O(1)
# General idea
# For solving this problem "greedy" approach will enough.
#
# Firstly - sorting array in ascending order
# Until array is not empty, at each iteration we have 3 conditions in decision tree:
# If first(smallest) element small or equal than our energy - choose them. Increase point by whole part of energy that can be wasted on this element. Current energy value will be equal remainder of dividing by module (currentEnergy by module cost_energy_element)
# If we have at least 1 point - just choose last(biggest) element. Increase current energy and pop element form array
# If we don't have enough point to choose element - we just should break loop
# Return collected points
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(1)
# Code
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        points: int = 0
        while enemyEnergies:
            if currentEnergy >= enemyEnergies[0]:
                points += currentEnergy // enemyEnergies[0]
                currentEnergy %= enemyEnergies[0]
            elif points > 0:
                currentEnergy += enemyEnergies.pop()
            else: break
        return points
    
# Solution Greedy O(N) O(1)
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        minimum_value: int = min(enemyEnergies)
        total_possible_energy: int = currentEnergy + sum(enemyEnergies) - minimum_value
        if currentEnergy < minimum_value: return 0
        return total_possible_energy // minimum_value