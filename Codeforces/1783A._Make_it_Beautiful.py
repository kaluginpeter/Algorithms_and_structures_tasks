# A. Make it Beautiful
# time limit per test3 seconds
# memory limit per test512 megabytes
# An array a
#  is called ugly if it contains at least one element which is equal to the sum of all elements before it. If the array is not ugly, it is beautiful.
#
# For example:
#
# the array [6,3,9,6]
#  is ugly: the element 9
#  is equal to 6+3
# ;
# the array [5,5,7]
#  is ugly: the element 5
#  (the second one) is equal to 5
# ;
# the array [8,4,10,14]
#  is beautiful: 8≠0
# , 4≠8
# , 10≠8+4
# , 14≠8+4+10
# , so there is no element which is equal to the sum of all elements before it.
# You are given an array a
#  such that 1≤a1≤a2≤⋯≤an≤100
# . You have to reorder the elements of a
#  in such a way that the resulting array is beautiful. Note that you are not allowed to insert new elements or erase existing ones, you can only change the order of elements of a
# . You are allowed to keep the array a
#  unchanged, if it is beautiful.
#
# Input
# The first line contains one integer t
#  (1≤t≤2000
# ) — the number of test cases.
#
# Each test case consists of two lines. The first line contains one integer n
#  (2≤n≤50
# ). The second line contains n
#  integers a1,a2,…,an
#  (1≤a1≤a2≤⋯≤an≤100
# ).
#
# Output
# For each test case, print the answer as follows:
#
# if it is impossible to reorder the elements of a
#  in such a way that it becomes beautiful, print NO;
# otherwise, in the first line, print YES. In the second line, print n
#  integers — any beautiful array which can be obtained from a
#  by reordering its elements. If there are multiple such arrays, print any of them.
# Example
# InputCopy
# 4
# 4
# 3 3 6 6
# 2
# 10 10
# 5
# 1 2 3 4 5
# 3
# 1 4 4
# OutputCopy
# YES
# 3 6 3 6
# NO
# YES
# 2 4 1 5 3
# YES
# 1 4 4
# Solution
# C++ O(NlogN) O(N) HashSet Greedy Sorting
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> nums(n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &nums[j]);
        std::unordered_set<int> seen;
        for (int &num : nums) seen.insert(num);
        if (seen.size() == 1 && n > 1) std::printf("NO\n");
        else {
            std::printf("YES\n");
            std::sort(nums.begin(), nums.end(), std::greater<int>());
            int left = 0, right = n - 1;
            while (left <= right) {
                if (left && nums[left] == nums[left - 1]) {
                    std::printf("%d ", nums[right]);
                    --right;
                } else {
                    std::printf("%d ", nums[left]);
                    ++left;
                }
            }
            std::printf("\n");
        }
    }
}


int main() {
    solution();
}

# Python O(NlogN) O(N) HashSet Sorting Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        if len(set(nums)) == 1 and n > 1:
            sys.stdout.write('NO\n')
        else:
            sys.stdout.write('YES\n')
            nums.sort(reverse=True)
            left: int = 0
            right: int = n - 1
            while left <= right:
                if left and nums[left] == nums[left - 1]:
                    sys.stdout.write('{} '.format(nums[right]))
                    right -= 1
                else:
                    sys.stdout.write('{} '.format(nums[left]))
                    left += 1
            sys.stdout.write('\n')


if __name__ == '__main__':
    solution()