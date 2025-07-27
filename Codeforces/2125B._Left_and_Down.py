# B. Left and Down
# time limit per test2 seconds
# memory limit per test512 megabytes
# There is a robot located in the cell (a,b)
#  of an infinite grid. Misha wants to move it to the cell (0,0)
# . To do this, he has fixed some integer k
# .
#
# Misha can perform the following operation: choose two integers dx
#  and dy
#  (both from 0
#  to k
#  inclusive) and move the robot dx
#  cells to the left (in the direction of decreasing x
#  coordinate) and dy
#  cells down (in the direction of decreasing y
#  coordinate). In other words, move the robot from (x,y)
#  to (x−dx,y−dy)
# .
#
# The cost of the operation is:
#
# 1
# , if the chosen pair (dx,dy)
#  is used for the first time;
# 0
# , if the pair (dx,dy)
#  has been chosen before.
# Note that if dx≠dy
# , the pairs (dx,dy)
#  and (dy,dx)
#  are considered different.
#
# Help Misha bring the robot to the cell (0,0)
#  with minimum total cost. Note that you don't have to minimize the number of operations.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The only line of each test case contains three integers a,b
# , and k
#  (1≤a,b,k≤1018
# ).
#
# Output
# For each test case, output a single integer — the minimum total cost of operations required to move the robot to the cell (0,0)
# .
#
# Example
# InputCopy
# 4
# 3 5 15
# 2 3 1
# 12 18 8
# 9 7 5
# OutputCopy
# 1
# 2
# 1
# 2
# Note
# In the first test case, the operation (3,5)
#  can be applied once. The robot will immediately go to (0,0)
# , and the cost of the operation will be 1
# .
#
# In the second test case, the operations: (1,1)
# , (0,1)
# , and (1,1)
#  can be applied. After the first operation, the robot will be at cell (1,2)
# , after the second one — at (1,1)
# , and after the third one — at (0,0)
# . The cost of the first and second operations is 1
# , while the third is 0
# , as the pair (1,1)
#  has already been used in the first operation.
#
# In the third test case, the pair (4,6)
#  can be chosen three times in a row.
#
# In the fourth test case, the operations: (4,2)
#  and (5,5)
#  can be applied.
# Solution
# C++ O(logN) O(1) Math
#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

void solution() {
    long long a, b, k;
    cin >> a >> b >> k;
    long long g = gcd(a, b);
    if (a / g <= k && b / g <= k) cout << 1 << '\n';
    else cout << 2 << '\n';
}

int main() {
    int t;
    cin >> t;
    while (t--) solution();
}

# Python O(logN) O(1) Math
import sys
import math

def solution() -> None:
    a, b, k = map(int, sys.stdin.readline().rstrip().split())
    g: int = math.gcd(a, b)
    sys.stdout.write('{}\n'.format([2, 1][a // g <= k and b // g <= k]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()