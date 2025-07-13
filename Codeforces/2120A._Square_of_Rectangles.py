# A. Square of Rectangles
# time limit per test1 second
# memory limit per test256 megabytes
# Aryan is an ardent lover of squares but a hater of rectangles (Yes, he knows all squares are rectangles). But Harshith likes to mess with Aryan. Harshith gives Aryan three rectangles of sizes l1×b1
# , l2×b2
# , and l3×b3
#  such that l3≤l2≤l1
#  and b3≤b2≤b1
# . Aryan, in order to defeat Harshith, decides to arrange these three rectangles to form a square such that no two rectangles overlap and the rectangles are aligned along edges. Rotating rectangles is not allowed. Help Aryan determine if he can defeat Harshith.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# Each test case contains a single line with 6
#  space-separated integers l1,b1,l2,b2,l3
# , and b3
#  (1≤l3≤l2≤l1≤100
# , 1≤b3≤b2≤b1≤100
# ) — the dimensions of the three rectangles.
#
# Output
# For each testcase, print "YES" if the rectangles can be arranged to form a square; otherwise, "NO".
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 100 100 10 10 1 1
# 5 3 5 1 5 1
# 2 3 1 2 1 1
# 8 5 3 5 3 3
# 3 3 3 3 2 1
# OutputCopy
# NO
# YES
# YES
# NO
# NO
# Note
# In the second test case, the three rectangles 5×3
# , 5×1
# , and 5×1
#  can be arranged as follows to form a square.
#
#
# In the fourth test case, it can be proven that the rectangles can't be arranged to form a square with the given constraints.
# Solution
# C++ O(1) O(1) Math
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

bool check(int l1, int b1, int l2, int b2, int l3, int b3) {
    long long total_area = (long long)l1 * b1 + (long long)l2 * b2 + (long long)l3 * b3;
    long long s = round(sqrt(total_area));
    if (s * s != total_area) return false;
    if (l1 == s) {
        long long remaining_height = s - b1;
        if (remaining_height > 0) {
            if (b2 == b3 && b2 == remaining_height && l2 + l3 == s) return true;
            if (l2 == s && l3 == s && b2 + b3 == remaining_height) return true;
        }
    }

    if (b1 == s) {
        long long remaining_width = s - l1;
        if (remaining_width > 0) {
            if (l2 == l3 && l2 == remaining_width && b2 + b3 == s) return true;
            if (b2 == s && b3 == s && l2 + l3 == remaining_width) return true;
        }
    }
    return false;
}

void solution() {
    int l1, b1, l2, b2, l3, b3;
    cin >> l1 >> b1 >> l2 >> b2 >> l3 >> b3;
    if (check(l1, b1, l2, b2, l3, b3) ||
        check(l2, b2, l1, b1, l3, b3) ||
        check(l3, b3, l1, b1, l2, b2)) cout << "YES\n";
    else cout << "NO\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) solution();
    return 0;
}

# Python O(1) O(1) Math
import sys

def check(l1: int, b1: int, l2: int, b2: int, l3: int, b3: int) -> bool:
    total_area: int = l1 * b1 + l2 * b2 + l3 * b3
    s: int = round(total_area**.5)
    if s * s != total_area: return False
    if l1 == s:
        remaining_height: int = s - b1
        if remaining_height > 0:
            if b2 == b3 and b2 == remaining_height and l2 + l3 == s: return True
            if l2 == s and l3 ==s and b2 + b3 == remaining_height: return True
    if b1 == s:
        remaining_width = s - l1
        if remaining_width > 0:
            if l2 == l3 and l2 == remaining_width and b2 + b3 == s: return True
            if b2 == s and b3 == s and l2 + l3 == remaining_width: return True
    return False

def solution() -> None:
    l1, b1, l2, b2, l3, b3 = map(int, sys.stdin.readline().rstrip().split())
    if check(l1, b1, l2, b2, l3, b3) or check(l2, b2, l1, b1, l3, b3) or check(l3, b3, l1, b1, l2, b2):
        sys.stdout.write('YES\n')
    else: sys.stdout.write('NO\n')

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()