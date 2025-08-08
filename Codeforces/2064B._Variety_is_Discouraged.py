# B. Variety is Discouraged
# time limit per test1.5 seconds
# memory limit per test256 megabytes
# Define the score of an arbitrary array b
#  to be the length of b
#  minus the number of distinct elements in b
# . For example:
#
# The score of [1,2,2,4]
#  is 1
# , as it has length 4
#  and only 3
#  distinct elements (1
# , 2
# , 4
# ).
# The score of [1,1,1]
#  is 2
# , as it has length 3
#  and only 1
#  distinct element (1
# ).
# The empty array has a score of 0
# .
# You have an array a
# . You need to remove some non-empty contiguous subarray from a
#  at most once.
#
# More formally, you can do the following at most once:
#
# pick two integers l
# , r
#  where 1≤l≤r≤n
# , and
# delete the contiguous subarray [al,…,ar]
#  from a
#  (that is, replace a
#  with [a1,…,al−1,ar+1,…,an]
# ).
# Output an operation such that the score of a
#  is maximum; if there are multiple answers, output one that minimises the final length of a
#  after the operation. If there are still multiple answers, you may output any of them.
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of testcases.
#
# The first line of each testcase contains an integer n
#  (1≤n≤2⋅105
# ) — the length of the array a
# .
#
# The second line of each testcase contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ).
#
# The sum of n
#  across all testcases does not exceed 2⋅105
# .
#
# Output
# For each testcase, if you wish to not make a move, output 0
# .
#
# Otherwise, output two integers l
#  and r
#  (1≤l≤r≤n
# ), representing the left and right bound of the removed subarray.
#
# The removed subarray should be chosen such that the score is maximized, and over all such answers choose any of them that minimises the final length of the array.
#
# Example
# InputCopy
# 3
# 1
# 1
# 5
# 1 1 1 1 1
# 4
# 2 1 3 2
# OutputCopy
# 1 1
# 0
# 2 3
# Note
# In the first testcase, we have two options:
#
# do nothing: the score of [1]
#  is 1−1=0
# .
# remove the subarray with l=1
# , r=1
# : we remove the only element, and we get an empty array with score 0
# .
# Therefore, the maximum score possible is 0
# . However, since we need to additionally minimise the final length of the array, we must output the second option with l=r=1
# . Note that the first option of doing nothing is incorrect, since it has a longer final length.
# In the second testcase, no subarray is selected, so after which a
#  is still [1,1,1,1,1]
# . This has length 5
#  and 1
#  distinct element, so it has a score of 5−1=4
# . This can be proven to be a shortest array which maximises the score.
#
# In the third testcase, the subarray selected is [2,1,3,2]
# , after which a
#  becomes [2,2]
# . This has length 2
#  and 1
#  distinct element, so it has a score of 2−1=1
# . This can be proven to be a shortest array which maximises the score.
# Solution
# C++ O(N) O(N) SlidingWindow
#include <iostream>
#include <vector>
#include <unordered_map>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    std::unordered_map<int, int> hashmap;
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
        ++hashmap[nums[i]];
    }

    int left = 0;
    int output = 0, outputL = -1, outputR = 0;
    for (int right = 0; right < n; ++right) {
        if (hashmap[nums[right]] > 1) {
            if (right - left > output) {
                output = right - left;
                outputL = left + 1;
                outputR = right;
            }
            left = right + 1;
        }
    }
    if (n - left > output) {
        outputL = left + 1;
        outputR = n;
    }
    if (outputL == -1) std::cout << "0\n";
    else std::printf("%d %d\n", outputL, outputR);
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) HashMap
import sys



def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    hashmap: dict[int, int] = dict()
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    left: int = 0
    output: int = 0
    output_left: int = -1
    output_right: int = 0
    for right in range(n):
        if hashmap[nums[right]] > 1:
            if right - left > output:
                output = right - left
                output_left = left + 1
                output_right = right
            left = right + 1
    if n - left > output:
        output_left = left + 1
        output_right = n
    if output_left == -1:
        sys.stdout.write('0\n')
    else:
        sys.stdout.write('{} {}\n'.format(output_left, output_right))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()