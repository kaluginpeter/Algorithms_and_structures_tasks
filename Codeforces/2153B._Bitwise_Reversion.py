# B. Bitwise Reversion
# time limit per test1.5 seconds
# memory limit per test256 megabytes
#
# You are given three non-negative integers x
# , y
#  and z
# . Determine whether there exist three non-negative integers a
# , b
#  and c
#  satisfying the following three conditions:
#
# a&b=x
# b&c=y
# a&c=z
# where &
#  denotes the bitwise AND operation.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first and only line of each test case contains three integers x
# , y
#  and z
#  (0≤x,y,z≤109
# ) — the target values of a&b
# , b&c
#  and a&c
# , respectively.
#
# Output
# For each test case, output "YES" if there exists three non-negative integers a
# , b
# , and c
#  satisfying the above conditions, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 1 1 1
# 3 2 6
# 4 8 12
# 9 10 12
# 12730 3088 28130
# OutputCopy
# YES
# YES
# NO
# YES
# NO
# Note
# In the first test case, a=3
# , b=5
# , and c=9
#  satisfies the condition as 3&5=1
# , 5&9=1
# , and 3&9=1
# .
#
# In the second test case, a=7
# , b=3
# , and c=22
#  satisfies the condition as 7&3=3
# , 3&22=2
# , and 7&22=6
# .
#
# In the third test case, it can be proven that there are no three non-negative integers a
# , b
# , and c
#  such that a&b=4
# , b&c=8
# , and a&c=12
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int x, y, z;
    std::cin >> x >> y >> z;
    std::cout << ((( x & y & ~z) || (x & z & ~y) || (~x & z & y))? "NO" : "YES") << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(1) O(1) Math
import sys

def solution() -> None:
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('{}\n'.format(['YES', 'NO'][bool((x & y & ~z) or (x & z & ~y) or (~x & z & y))]))

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()