# A. Lineland Mail
# time limit per test3 seconds
# memory limit per test256 megabytes
# All cities of Lineland are located on the Ox coordinate axis. Thus, each city is associated with its position xi — a coordinate on the Ox axis. No two cities are located at a single point.
#
# Lineland residents love to send letters to each other. A person may send a letter only if the recipient lives in another city (because if they live in the same city, then it is easier to drop in).
#
# Strange but true, the cost of sending the letter is exactly equal to the distance between the sender's city and the recipient's city.
#
# For each city calculate two values ​​mini and maxi, where mini is the minimum cost of sending a letter from the i-th city to some other city, and maxi is the the maximum cost of sending a letter from the i-th city to some other city
#
# Input
# The first line of the input contains integer n (2 ≤ n ≤ 105) — the number of cities in Lineland. The second line contains the sequence of n distinct integers x1, x2, ..., xn ( - 109 ≤ xi ≤ 109), where xi is the x-coordinate of the i-th city. All the xi's are distinct and follow in ascending order.
#
# Output
# Print n lines, the i-th line must contain two integers mini, maxi, separated by a space, where mini is the minimum cost of sending a letter from the i-th city, and maxi is the maximum cost of sending a letter from the i-th city.
#
# Examples
# InputCopy
# 4
# -5 -2 2 7
# OutputCopy
# 3 12
# 3 9
# 4 7
# 5 12
# InputCopy
# 2
# -1 1
# OutputCopy
# 2 2
# 2 2
# Solution
# C++ O(N) O(1) Math Greedy
#include <iostream>
#include <vector>
#include <cstdint>


void solution() {
    int n;
    std::scanf("%d", &n);
    std::vector<int> cities;
    for (int i = 0; i < n; ++i) {
        int city;
        std::scanf("%d", &city);
        cities.push_back(city);
    }
    for (int i = 0; i < n; ++i) {
        long long left = INT64_MAX, right = INT64_MIN;
        if (!i) left = cities[i + 1] - cities[i];
        else if (i + 1 == n) left = cities[i] - cities[i - 1];
        else left = std::min(cities[i + 1] - cities[i], cities[i] - cities[i - 1]);

        if (!i) right = cities[n - 1] - cities[i];
        else if (i + 1 == n) right = cities[i] - cities[0];
        else right = std::max(cities[i] - cities[0], cities[n - 1] - cities[i]);
        std::printf("%lld %lld\n", left, right);
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Math Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    cities: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        left: int = 0
        right: int = 0
        if not i:
            left = cities[i + 1] - cities[i]
            right = cities[n - 1] - cities[i]
        elif i + 1 == n:
            left = cities[i] - cities[i - 1]
            right = cities[i] - cities[0]
        else:
            left = min(cities[i + 1] - cities[i], cities[i] - cities[i - 1])
            right = max(cities[n - 1] - cities[i], cities[i] - cities[0])
        sys.stdout.write('{} {}\n'.format(left, right))


if __name__ == '__main__':
    solution()