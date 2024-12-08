# B. Sereja and Suffixes
# time limit per test1 second
# memory limit per test256 megabytes
# Sereja has an array a, consisting of n integers a1, a2, ..., an. The boy cannot sit and do nothing, he decided to study an array. Sereja took a piece of paper and wrote out m integers l1, l2, ..., lm (1 ≤ li ≤ n). For each number li he wants to know how many distinct numbers are staying on the positions li, li + 1, ..., n. Formally, he want to find the number of distinct numbers among ali, ali + 1, ..., an.?
#
# Sereja wrote out the necessary array elements but the array was so large and the boy was so pressed for time. Help him, find the answer for the described question for each li.
#
# Input
# The first line contains two integers n and m (1 ≤ n, m ≤ 105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105) — the array elements.
#
# Next m lines contain integers l1, l2, ..., lm. The i-th line contains integer li (1 ≤ li ≤ n).
#
# Output
# Print m lines — on the i-th line print the answer to the number li.
#
# Examples
# InputCopy
# 10 10
# 1 2 3 4 1 2 3 4 100000 99999
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# OutputCopy
# 6
# 6
# 6
# 6
# 6
# 5
# 4
# 3
# 2
# 1
# Solution
# C++ O(N) O(N) HashSet
#include <iostream>
#include <unordered_set>
#include <vector>


void solution(int& n, int& m, std::vector<int>& nums) {
    std::unordered_set<int> hashset;
    std::vector<int> suffixArray(n, 0);
    for (int idx = n - 1; idx >= 0; --idx) {
        hashset.insert(nums[idx]);
        suffixArray[idx] = hashset.size();
    }
    for (int i = 0; i < m; ++i) {
        int l;
        std::cin >> l;
        std::cout << suffixArray[l - 1] << "\n";
    }
}


int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<int> nums;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    solution(n, m, nums);
}

# Python O(N) O(N) HashSet
import sys


def solution(n: int, m: int, nums: list) -> None:
    suffix_array: list = [0] * n
    hashset: set = set()
    for idx in range(n - 1, -1, -1):
        hashset.add(nums[idx])
        suffix_array[idx] = len(hashset)
    for _ in range(m):
        l: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(str(suffix_array[l - 1]) + '\n')


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, m, nums)
