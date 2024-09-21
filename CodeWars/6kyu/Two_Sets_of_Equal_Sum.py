# If possible, divide the integers 1,2,…,n into two sets of equal sum.
#
# Input
# A positive integer n <= 1,000,000.
#
# Output
# If it's not possible, return [ ] (Python, Javascript, Swift, Ruby) or ( ) (Python) or [ [],[] ] (Java, C#, C++, Kotlin) or None (Scala) or Nothing (Haskell).
# If it's possible, return two disjoint sets. Each integer from 1 to n must be in one of them. The integers in the first set must sum up to the same value as the integers in the second set. The sets can be returned in a tuple, list, or array, depending on language.
#
# Examples:
# For n = 8, valid answers include:
# [1, 3, 6, 8], [2, 4, 5, 7] (or [[1, 3, 6, 8], [2, 4, 5, 7]])
# [8, 1, 3, 2, 4], [5, 7, 6]
# [7, 8, 3], [6, 1, 5, 4, 2], and others.
#
# For n = 9 it is not possible. For example, try [6, 8, 9] and [1, 2, 3, 4, 5, 7], but the first sums to 23 and the second to 22. No other sets work either.
#
# Source: CSES
#
# ARRAYSALGORITHMS
# Solution
# C++
#include <vector>
#include <array>

std::array<std::vector<int>, 2> createTwoSetsOfEqualSum(int n) {
    std::array<std::vector<int>, 2> sets;
    long long total_sum = static_cast<long long>(n) * (n + 1) / 2;
    if (total_sum % 2 != 0) {
        return sets;
    }
    long long target = total_sum / 2;
    for (int num = n; num > 0; --num) {
        if (target >= num) {
            sets[0].push_back(num);
            target -= num;
        } else {
            sets[1].push_back(num);
        }
    }
    return sets;
}
# Python
def create_two_sets_of_equal_sum(n: int) -> tuple[list[int], list[int]]:
    total_sum: int = n * (n + 1) // 2
    if total_sum % 2 != 0: return []

    target: int = total_sum // 2
    set1, set2 = [], []
    for num in range(n, 0, -1):
        if target >= num:
            set1.append(num)
            target -= num
        else:
            set2.append(num)
    return (set1, set2)