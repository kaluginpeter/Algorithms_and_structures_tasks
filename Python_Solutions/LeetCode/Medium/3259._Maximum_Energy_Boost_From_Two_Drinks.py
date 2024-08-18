# You are given two integer arrays energyDrinkA and energyDrinkB of the same length n by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.
#
# You want to maximize your total energy boost by drinking one energy drink per hour. However, if you want to switch from consuming one energy drink to the other, you need to wait for one hour to cleanse your system (meaning you won't get any energy boost in that hour).
#
# Return the maximum total energy boost you can gain in the next n hours.
#
# Note that you can start consuming either of the two energy drinks.
#
#
#
# Example 1:
#
# Input: energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]
#
# Output: 5
#
# Explanation:
#
# To gain an energy boost of 5, drink only the energy drink A (or only B).
#
# Example 2:
#
# Input: energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]
#
# Output: 7
#
# Explanation:
#
# To gain an energy boost of 7:
#
# Drink the energy drink A for the first hour.
# Switch to the energy drink B and we lose the energy boost of the second hour.
# Gain the energy boost of the drink B in the third hour.
#
#
# Constraints:
#
# n == energyDrinkA.length == energyDrinkB.length
# 3 <= n <= 105
# 1 <= energyDrinkA[i], energyDrinkB[i] <= 105
# Solution Dynamic Programming O(N) O(N)
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n: int = len(energyDrinkA)

        dpA: list[int] = [0] * n
        dpB: list[int] = [0] * n

        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        dpA[1] = max(energyDrinkA[0], energyDrinkA[0] + energyDrinkA[1])
        dpB[1] = max(energyDrinkB[0], energyDrinkB[0] + energyDrinkB[1])

        for i in range(2, n):
            dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-2] + energyDrinkA[i])
            dpB[i] = max(dpB[i-1] + energyDrinkB[i], dpA[i-2] + energyDrinkB[i])

        return max(dpA[n-1], dpB[n-1])