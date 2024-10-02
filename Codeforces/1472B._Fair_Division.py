# B. Fair Division
# time limit per test2 seconds
# memory limit per test256 megabytes
# Alice and Bob received n
#  candies from their parents. Each candy weighs either 1 gram or 2 grams. Now they want to divide all candies among themselves fairly so that the total weight of Alice's candies is equal to the total weight of Bob's candies.
#
# Check if they can do that.
#
# Note that candies are not allowed to be cut in half.
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.
#
# The first line of each test case contains an integer n
#  (1≤n≤100
# ) — the number of candies that Alice and Bob received.
#
# The next line contains n
#  integers a1,a2,…,an
#  — the weights of the candies. The weight of each candy is either 1
#  or 2
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
#
# Output
# For each test case, output on a separate line:
#
# "YES", if all candies can be divided into two sets with the same weight;
# "NO" otherwise.
# You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).
#
# Example
# inputCopy
# 5
# 2
# 1 1
# 2
# 1 2
# 4
# 1 2 1 2
# 3
# 2 2 2
# 3
# 2 1 2
# outputCopy
# YES
# NO
# YES
# NO
# NO
# Note
# In the first test case, Alice and Bob can each take one candy, then both will have a total weight of 1
# .
#
# In the second test case, any division will be unfair.
#
# In the third test case, both Alice and Bob can take two candies, one of weight 1
#  and one of weight 2
# .
#
# In the fourth test case, it is impossible to divide three identical candies between two people.
#
# In the fifth test case, any division will also be unfair.
# Solution
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        weights: list = list(map(int, sys.stdin.readline().rstrip().split()))
        total_weight: int = sum(weights)

        if total_weight % 2 != 0:
            sys.stdout.write('NO\n')
            continue

        target: int = total_weight // 2
        count1: int = weights.count(1)
        count2: int = weights.count(2)

        max_2s_used: int = min(count2, target // 2)
        weight_from_2s: int = max_2s_used * 2
        remaining_weight: int = target - weight_from_2s
        sys.stdout.write(['NO', 'YES'][remaining_weight <= count1] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
