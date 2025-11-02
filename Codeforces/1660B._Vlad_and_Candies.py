# B. Vlad and Candies
# time limit per test1 second
# memory limit per test256 megabytes
# Not so long ago, Vlad had a birthday, for which he was presented with a package of candies. There were n
#  types of candies, there are ai
#  candies of the type i
#  (1≤i≤n
# ).
#
# Vlad decided to eat exactly one candy every time, choosing any of the candies of a type that is currently the most frequent (if there are several such types, he can choose any of them). To get the maximum pleasure from eating, Vlad does not want to eat two candies of the same type in a row.
#
# Help him figure out if he can eat all the candies without eating two identical candies in a row.
#
# Input
# The first line of input data contains an integer t
#  (1≤t≤104
# ) — the number of input test cases.
#
# The following is a description of t
#  test cases of input, two lines for each.
#
# The first line of the case contains the single number n
#  (1≤n≤2⋅105
# ) — the number of types of candies in the package.
#
# The second line of the case contains n
#  integers ai
#  (1≤ai≤109
# ) — the number of candies of the type i
# .
#
# It is guaranteed that the sum of n
#  for all cases does not exceed 2⋅105
# .
#
# Output
# Output t
#  lines, each of which contains the answer to the corresponding test case of input. As an answer, output "YES" if Vlad can eat candy as planned, and "NO" otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 6
# 2
# 2 3
# 1
# 2
# 5
# 1 6 2 4 3
# 4
# 2 2 2 1
# 3
# 1 1000000000 999999999
# 1
# 1
# OutputCopy
# YES
# NO
# NO
# YES
# YES
# YES
# Note
# In the first example, it is necessary to eat sweets in this order:
#
# a candy of the type 2
# , it is the most frequent, now a=[2,2]
# ;
# a candy of the type 1
# , there are the same number of candies of the type 2
# , but we just ate one, now a=[1,2]
# ;
# a candy of the type 2
# , it is the most frequent, now a=[1,1]
# ;
# a candy of the type 1
# , now a=[0,1]
# ;
# a candy of the type 2
# , now a=[0,0]
#  and the candy has run out.
# In the second example, all the candies are of the same type and it is impossible to eat them without eating two identical ones in a row.
#
# In the third example, first of all, a candy of the type 2
#  will be eaten, after which this kind will remain the only kind that is the most frequent, and you will have to eat a candy of the type 2
#  again.
# Solution
# C++ O(NlogN + N) O(1) Sorting
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    if (n == 1) {
        std::cout << (nums.back() == 1 ? "YES" : "NO") << "\n";
        return;
    }
    std::cout << (nums[n - 1] - nums[n - 2] <= 1 ? "YES" : "NO") << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN + N) O(1) Sorting
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    if n == 1:
        sys.stdout.write('{}\n'.format(['NO', 'YES'][nums[0] == 1]))
        return
    sys.stdout.write('{}\n'.format(['NO', 'YES'][nums[-1] - nums[-2] <= 1]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()