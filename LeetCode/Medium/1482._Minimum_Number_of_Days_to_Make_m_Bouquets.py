# You are given an integer array bloomDay, an integer m and an integer k.
#
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
#
#
#
# Example 1:
#
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
# Example 2:
#
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
# Example 3:
#
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.
#
#
# Constraints:
#
# bloomDay.length == n
# 1 <= n <= 105
# 1 <= bloomDay[i] <= 109
# 1 <= m <= 106
# 1 <= k <= n
# Solution Binary Search O(NlogN) O(1)
class Solution:
    def check(
            self, current_day: int, upper_boundary: int,
            needed_flowers_for_bouquet: int,
            needed_bouquets: int, days: list[int]
    ) -> bool:
        length_of_bouquet, count_bouquets = 0, 0
        current_index: int = 0
        while current_index < upper_boundary:
            while current_index < upper_boundary and days[current_index] <= current_day:
                length_of_bouquet += 1
                if length_of_bouquet == needed_flowers_for_bouquet:
                    count_bouquets += 1
                    length_of_bouquet = 0
                current_index += 1
            if current_index < upper_boundary and days[current_index] > current_day:
                length_of_bouquet = 0
            if count_bouquets >= needed_bouquets:
                return True
            current_index += 1
        return count_bouquets >= needed_bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n: int = len(bloomDay)
        if m * k > n:
            return - 1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            middle: int = (left + right) >> 1
            if self.check(middle, n, k, m, bloomDay):
                right = middle
            else:
                left = middle + 1
        return left