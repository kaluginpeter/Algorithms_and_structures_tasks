# B. Worms
# time limit per test1 second
# memory limit per test256 megabytes
# It is lunch time for Mole. His friend, Marmot, prepared him a nice game for lunch.
#
# Marmot brought Mole n ordered piles of worms such that i-th pile contains ai worms. He labeled all these worms with consecutive integers: worms in first pile are labeled with numbers 1 to a1, worms in second pile are labeled with numbers a1 + 1 to a1 + a2 and so on. See the example for a better understanding.
#
# Mole can't eat all the worms (Marmot brought a lot) and, as we all know, Mole is blind, so Marmot tells him the labels of the best juicy worms. Marmot will only give Mole a worm if Mole says correctly in which pile this worm is contained.
#
# Poor Mole asks for your help. For all juicy worms said by Marmot, tell Mole the correct answers.
#
# Input
# The first line contains a single integer n (1 ≤ n ≤ 105), the number of piles.
#
# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 103, a1 + a2 + ... + an ≤ 106), where ai is the number of worms in the i-th pile.
#
# The third line contains single integer m (1 ≤ m ≤ 105), the number of juicy worms said by Marmot.
#
# The fourth line contains m integers q1, q2, ..., qm (1 ≤ qi ≤ a1 + a2 + ... + an), the labels of the juicy worms.
#
# Output
# Print m lines to the standard output. The i-th line should contain an integer, representing the number of the pile where the worm labeled with the number qi is.
#
# Examples
# inputCopy
# 5
# 2 7 3 4 9
# 3
# 1 25 11
# outputCopy
# 1
# 5
# 3
# Note
# For the sample input:
#
# The worms with labels from [1, 2] are in the first pile.
# The worms with labels from [3, 9] are in the second pile.
# The worms with labels from [10, 12] are in the third pile.
# The worms with labels from [13, 16] are in the fourth pile.
# The worms with labels from [17, 25] are in the fifth pile.
# Solution
# Python O(MlogN) O(N) Binary Search
import sys


def binary_search(target: int, nums: list) -> int:
    left: int = 0
    right: int = len(nums) // 2 - 1
    while left <= right:
        middle: int = left + (right - left) // 2
        low: int = nums[2 * middle]
        high: int = nums[2 * middle + 1]
        if low <= target <= high:
            return middle + 1
        if target < low:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    prev_worm: int = 0
    worms: list = []
    for worm in map(int, sys.stdin.readline().rstrip().split()):
        worms.append(prev_worm + 1)
        prev_worm += worm
        worms.append(prev_worm)
    m: int = int(sys.stdin.readline().rstrip())
    for query in map(int, sys.stdin.readline().rstrip().split()):
        sys.stdout.write(str(binary_search(query, worms)) + '\n')


if __name__ == '__main__':
    solution()

# C++ O(MlogN) O(N) Binary Search
#include <iostream>
#include <vector>

int binary_search(int target, std::vector<int>& nums) {
    int left = 0;
    int right = nums.size() / 2 - 1;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        int low = nums[2 * middle];
        int high = nums[2 * middle + 1];
        if (target >= low && target <= high) {
            return middle + 1;
        }
        if (target < low) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> worms;
    int prev_worm = 0;
    for (int j = 0; j < n; ++j) {
        int worm;
        std::cin >> worm;
        worms.push_back(prev_worm + 1);
        prev_worm += worm;
        worms.push_back(prev_worm);
    }
    int m;
    std::cin >> m;
    for (int j = 0; j < m; ++j) {
        int query;
        std::cin >> query;
        std::cout << binary_search(query, worms) << std::endl;
    }
}