# B. Lasers
# time limit per test2 seconds
# memory limit per test256 megabytes
# There is a 2D-coordinate plane that ranges from (0,0)
#  to (x,y)
# . You are located at (0,0)
#  and want to head to (x,y)
# .
#
# However, there are n
#  horizontal lasers, with the i
# -th laser continuously spanning (0,ai)
#  to (x,ai)
# . Additionally, there are also m
#  vertical lasers, with the i
# -th laser continuously spanning (bi,0)
#  to (bi,y)
# .
#
# You may move in any direction to reach (x,y)
# , but your movement must be a continuous curve that lies inside the plane. Every time you cross a vertical or a horizontal laser, it counts as one crossing. Particularly, if you pass through an intersection point between two lasers, it counts as two crossings.
#
# For example, if x=y=2
# , n=m=1
# , a=[1]
# , b=[1]
# , the movement can be as follows:
#
#
# What is the minimum number of crossings necessary to reach (x,y)
# ?
#
# Input
# The first line contains t
#  (1≤t≤104
# )  — the number of test cases.
#
# The first line of each test case contains four integers n
# , m
# , x
# , and y
#  (1≤n,m≤2⋅105,2≤x,y≤109
# ).
#
# The following line contains n
#  integers a1,a2,…,an
#  (0<ai<y
# )  — the y-coordinates of the horizontal lasers. It is guaranteed that ai>ai−1
#  for all i>1
# .
#
# The following line contains m
#  integers b1,b2,…,bm
#  (0<bi<x
# )  — the x-coordinates of the vertical lasers. It is guaranteed that bi>bi−1
#  for all i>1
# .
#
# It is guaranteed that the sum of n
#  and m
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output the minimum number of crossings necessary to reach (x,y)
# .
#
# Example
# InputCopy
# 2
# 1 1 2 2
# 1
# 1
# 2 1 100000 100000
# 42 58
# 32
# OutputCopy
# 2
# 3
# Solution
# C++ O(N + M) O(1) Greedy
#include <iostream>
#include <vector>


void solution() {
    int n, m, x ,y;
    std::cin >> n >> m >> x >> y;
    std::vector<int> vertical(m, 0), horizontal(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> horizontal[i];
    for (size_t i = 0; i < m; ++i) std::cin >> vertical[i];
    int output = 0;
    for (const int &laser : horizontal) {
        if (laser <= y) ++output;
        else break;
    }
    for (const int&laser : vertical) {
        if (laser <= x) ++output;
        else break;
    }
    std::cout << output << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# C++ O(N + M) O(1) Greedy
import sys


def solution() -> None:
    n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
    horizontal: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    vertical: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    output: int = 0
    for laser in horizontal:
        if laser <= y: output += 1
        else: break
    for laser in vertical:
        if laser <= x: output += 1
        else: break
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()