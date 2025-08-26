# A. Redstone?
# time limit per test1 second
# memory limit per test256 megabytes
#
# Steve stumbled upon a collection of n
#  gears, where gear i
#  has ai
#  teeth, and he wants to arrange them into a row.
#
# After he arranges them, Steve will spin the leftmost gear at a speed of 1
#  revolution per second. For each of the other gears, let x
#  be the number of teeth it has, y
#  be the number of teeth of the gear to its left, and z
#  be the speed the gear to its left spins at. Then, its speed will be yx⋅z
#  revolutions per second.
#
# Steve considers the contraption satisfactory if the rightmost gear spins at a speed of 1
#  revolution per second. Determine whether Steve can rearrange the gears into a satisfactory contraption.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the number of gears Steve has.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (2≤ai≤100
# ) — the number of teeth of each gear.
#
# Output
# For each test case, print "YES" if Steve can rearrange the gears in a satisfactory way, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 2
# 5 5
# 4
# 6 3 6 9
# 2
# 2 3
# 7
# 30 10 12 10 10 9 18
# 5
# 2 4 8 16 32
# OutputCopy
# YES
# YES
# NO
# YES
# NO
# Note
# In the first test case, the second gear will always spin at speed 55⋅1=1
#  revolution per second, so any arrangement is satisfactory.
#
# In the second test case, one possible arrangement is [6,3,9,6]
# . Then:
#
# The second gear spins at speed 63⋅1=2
#  revolutions per second.
# The third gear spins at speed 39⋅2=23
#  revolutions per second.
# The fourth spins at speed 96⋅23=1
#  revolution per second.
# Since the rightmost gear spins at a speed of 1
#  revolution per second, the arrangement is satisfactory.
# In the third test case, neither of the possible arrangements [2,3]
#  and [3,2]
#  are satisfactory.
# Solution
# C++ O(N) O(D) HashMap
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> hashmap(101, 0);
    bool isValid = false;
    for (int i = 0; i < n; ++i) {
        int gear;
        std::cin >> gear;
        ++hashmap[gear];
        if (hashmap[gear] > 1) isValid = true;
    }
    std::cout << (isValid ? "YES" : "NO") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(D) HashMap
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    hashmap: list[int] = [0] * 101
    is_valid: bool = False
    for _ in range(n):
        gear: int = next(nums)
        hashmap[gear] += 1
        if hashmap[gear] > 1: is_valid = True
    sys.stdout.write('{}\n'.format(['NO', 'YES'][is_valid]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline())
    for _ in range(t): solution()