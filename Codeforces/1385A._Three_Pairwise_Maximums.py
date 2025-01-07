# A. Three Pairwise Maximums
# time limit per test1 second
# memory limit per test256 megabytes
# You are given three positive (i.e. strictly greater than zero) integers x
# , y
#  and z
# .
#
# Your task is to find positive integers a
# , b
#  and c
#  such that x=max(a,b)
# , y=max(a,c)
#  and z=max(b,c)
# , or determine that it is impossible to find such a
# , b
#  and c
# .
#
# You have to answer t
#  independent test cases. Print required a
# , b
#  and c
#  in any (arbitrary) order.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤2⋅104
# ) — the number of test cases. Then t
#  test cases follow.
#
# The only line of the test case contains three integers x
# , y
# , and z
#  (1≤x,y,z≤109
# ).
#
# Output
# For each test case, print the answer:
#
# "NO" in the only line of the output if a solution doesn't exist;
# or "YES" in the first line and any valid triple of positive integers a
# , b
#  and c
#  (1≤a,b,c≤109
# ) in the second line. You can print a
# , b
#  and c
#  in any order.
# Example
# InputCopy
# 5
# 3 2 3
# 100 100 100
# 50 49 49
# 10 30 20
# 1 1000000000 1000000000
# OutputCopy
# YES
# 3 2 1
# YES
# 100 100 100
# NO
# NO
# YES
# 1 1 1000000000
# Solution
# C++ O(1) O(1) Math
#include <iostream>
#include <algorithm>

void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int x, y, z;
        std::cin >> x >> y >> z;

        // We can construct a, b, c as follows
        int a = std::min(x, y);
        int b = std::min(x, z);
        int c = std::min(y, z);

        // Check if max conditions hold
        if (std::max(a, b) == x && std::max(a, c) == y && std::max(b, c) == z) {
            std::cout << "YES\n";
            std::cout << a << " " << b << " " << c << "\n";
        } else {
            std::cout << "NO\n";
        }
    }
}

int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        a: inb = min(x, y)
        b: int = min(x, z)
        c: int = min(y, z)
        if max(a, b) == x and max(a, c) == y and max(b, c) == z:
            sys.stdout.write('YES\n')
            sys.stdout.write(f'{a} {b} {c}\n')
        else:
            sys.stdout.write('NO\n')


if __name__ == '__main__':
    solution()
