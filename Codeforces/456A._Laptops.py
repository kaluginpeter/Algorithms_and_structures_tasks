# A. Laptops
# time limit per test1 second
# memory limit per test256 megabytes
# One day Dima and Alex had an argument about the price and quality of laptops. Dima thinks that the more expensive a laptop is, the better it is. Alex disagrees. Alex thinks that there are two laptops, such that the price of the first laptop is less (strictly smaller) than the price of the second laptop but the quality of the first laptop is higher (strictly greater) than the quality of the second laptop.
#
# Please, check the guess of Alex. You are given descriptions of n laptops. Determine whether two described above laptops exist.
#
# Input
# The first line contains an integer n (1 ≤ n ≤ 105) — the number of laptops.
#
# Next n lines contain two integers each, ai and bi (1 ≤ ai, bi ≤ n), where ai is the price of the i-th laptop, and bi is the number that represents the quality of the i-th laptop (the larger the number is, the higher is the quality).
#
# All ai are distinct. All bi are distinct.
#
# Output
# If Alex is correct, print "Happy Alex", otherwise print "Poor Alex" (without the quotes).
#
# Examples
# inputCopy
# 2
# 1 2
# 2 1
# outputCopy
# Happy Alex
# Solution
# Python O(NLogN) O(1) Two Pointers Sorting
import sys


def solution() -> str:
    n: int = int(sys.stdin.readline().rstrip())
    tablets: list = []
    for _ in range(n):
        price, quality = map(int, sys.stdin.readline().rstrip().split())
        tablets.append((price, quality))
    tablets.sort()
    left: int = 0
    for right in range(1, n):
        if tablets[right][0] > tablets[left][0] and tablets[right][1] < tablets[left][1]:
            return 'Happy Alex'
        left += 1
    return 'Poor Alex'


if __name__ == '__main__':
    sys.stdout.write(solution())

# C++ O(NlogN) O(1) Two Pointers Sorting
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> tablets;
    for (int i = 0; i < n; ++i) {
        int price, quality;
        std::cin >> price >> quality;
        tablets.push_back({price, quality});
    }
    std::sort(tablets.begin(), tablets.end());
    std::size_t left = 0;
    for (size_t right = 1; right < tablets.size(); ++right) {
        if (tablets[right].first > tablets[left].first && tablets[left].second > tablets[right].second) {
            std::cout << "Happy Alex" << std::endl;
            return 0;
        }
        ++left;
    }
    std::cout << "Poor Alex" << std::endl;
}