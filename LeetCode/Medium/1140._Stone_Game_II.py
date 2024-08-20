# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
#
#
#
# Example 1:
#
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
# Example 2:
#
# Input: piles = [1,2,3,4,5,100]
# Output: 104
#
#
# Constraints:
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 104
# Solution Dynamic Programming O(N**3) O(N**2)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n: int = len(piles)

        suffix_sum: list[int] = [0] * n
        suffix_sum[-1] = piles[-1]
        for idx in range(n - 2, -1, -1):
            suffix_sum[idx] = piles[idx] + suffix_sum[idx + 1]

        dp: list[list[int]] = [[0] * (n + 1) for _ in range(n)]

        for idx in range(n - 1, -1, -1):
            for possible_m in range(1, n + 1):
                # Case when we can get all remaining stones
                if idx + (2 * possible_m) >= n:
                    dp[idx][possible_m] = suffix_sum[idx]
                    continue
                for x in range(1, (2 * possible_m) + 1):
                    dp[idx][possible_m] = max(
                        dp[idx][possible_m],
                        suffix_sum[idx] - dp[idx + x][max(possible_m, x)]
                    )

        return dp[0][1]