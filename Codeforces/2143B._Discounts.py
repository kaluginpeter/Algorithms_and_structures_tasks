# B. Discounts
# time limit per test1 second
# memory limit per test256 megabytes
# You want to buy n
#  products with prices a1,a2,…,an
# . You can either:
#
# buy product i
#  individually, paying ai
#  coins, or
# use a discount voucher to buy it as part of a group purchase.
# You have k
#  discount vouchers with values b1,b2,…,bk
# . A voucher of value x
#  allows you to select exactly x
#  products and pay only for the x−1
#  most expensive ones, as such, you can consider that the cheapest product in the group is free. Each product can be included in at most one discount group, even if it is not the free one. Also, any single voucher can be used at most one single time.
#
# What is the minimum total cost required to purchase all n
#  products?
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line contains two integers n
#  and k
#  (1≤n,k≤2⋅105
# ) —the number of products and the number of available discount vouchers.
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the prices of the products.
#
# The third line contains k
#  integers b1,b2,…,bk
#  (1≤bi≤n
# ) — the values of the discount vouchers.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# , and the sum of k
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# Print t
#  lines. The i
# -th line should contain the answer for the i
# -th test case — the minimum total cost required to purchase all products in that test case.
#
# Example
# InputCopy
# 5
# 5 3
# 18 3 7 2 9
# 3 1 1
# 6 1
# 1 2 6 3 3 4
# 5
# 2 3
# 1 1
# 2 2 2
# 1 1
# 10
# 1
# 5 3
# 99 99 999 999 123
# 2 1 4
# OutputCopy
# 10
# 17
# 1
# 0
# 1197
# Note
# In the first test case, you can apply the first discount to products 2, 3, and 4. You will pay for the two most expensive ones (3 and 7 coins) and get the cheapest one for free, resulting in a cost of 3+7=10
#  coins. Then, apply the second and third discounts to products 1 and 5, getting both for free. The total cost is 10
#  coins.
#
# In the second test case, you can use the single discount on products 2, 3, 4, 5, and 6. Among them, the cheapest is product 2 (costing 2 coins), which you get for free. You pay for the remaining products: 1+6+3+3+4=17
#  coins in total.
#
# In the third test case, only one discount is available. You can use it on both products, getting the cheaper one for free and paying 1
#  coin for the other.
# Solution
# C++ O(NlogN + MlogM + N + M) O(1) TwoPointers Sorting
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n, k;
    std::cin >> n >> k;
    std::vector<int> nums(n, 0), vauchers(k, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    for (size_t i = 0; i < k; ++i) std::cin >> vauchers[i];
    std::sort(nums.begin(), nums.end(), std::greater<int>());
    std::sort(vauchers.begin(), vauchers.end());
    size_t i = 0, j = 0;
    long long output = 0;
    while (i < n || j < k) {
        if (i == n) break;
        if (j == k) {
            output += nums[i];
            ++i;
            continue;
        }
        for (size_t d = i; d < std::min(n, i + vauchers[j] - 1); ++d) output += nums[d];
        i += vauchers[j];
        ++j;
    }
    std::cout << output << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN + MlogM + N + M) O(1) Sorting TwoPointers
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()), reverse=True)
    vauchers: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    i: int = 0
    j: int = 0
    output: int = 0
    while i < n or j < k:
        if i == n: break
        elif j == k:
            output += nums[i]
            i += 1
            continue
        for d in range(i, min(n, i + vauchers[j] - 1)): output += nums[d]
        i += vauchers[j]
        j += 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()