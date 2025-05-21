# B. Bad Boy
# time limit per test1 second
# memory limit per test256 megabytes
# Riley is a very bad boy, but at the same time, he is a yo-yo master. So, he decided to use his yo-yo skills to annoy his friend Anton.
#
# Anton's room can be represented as a grid with n
#  rows and m
#  columns. Let (i,j)
#  denote the cell in row i
#  and column j
# . Anton is currently standing at position (i,j)
#  in his room. To annoy Anton, Riley decided to throw exactly two yo-yos in cells of the room (they can be in the same cell).
#
# Because Anton doesn't like yo-yos thrown on the floor, he has to pick up both of them and return back to the initial position. The distance travelled by Anton is the shortest path that goes through the positions of both yo-yos and returns back to (i,j)
#  by travelling only to adjacent by side cells. That is, if he is in cell (x,y)
#  then he can travel to the cells (x+1,y)
# , (x−1,y)
# , (x,y+1)
#  and (x,y−1)
#  in one step (if a cell with those coordinates exists).
#
# Riley is wondering where he should throw these two yo-yos so that the distance travelled by Anton is maximized. But because he is very busy, he asked you to tell him.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.
#
# The only line of each test case contains four integers n
# , m
# , i
# , j
#  (1≤n,m≤109
# , 1≤i≤n
# , 1≤j≤m
# ) — the dimensions of the room, and the cell at which Anton is currently standing.
#
# Output
# For each test case, print four integers x1
# , y1
# , x2
# , y2
#  (1≤x1,x2≤n
# , 1≤y1,y2≤m
# ) — the coordinates of where the two yo-yos should be thrown. They will be thrown at coordinates (x1,y1)
#  and (x2,y2)
# .
#
# If there are multiple answers, you may print any.
#
# Example
# InputCopy
# 7
# 2 3 1 1
# 4 4 1 2
# 3 5 2 2
# 5 1 2 1
# 3 1 3 1
# 1 1 1 1
# 1000000000 1000000000 1000000000 50
# OutputCopy
# 1 2 2 3
# 4 1 4 4
# 3 1 1 5
# 5 1 1 1
# 1 1 2 1
# 1 1 1 1
# 50 1 1 1000000000
# Note
# Here is a visualization of the first test case.
# Solution
# C++ O(1) O(1) Math Greedy
#include <iostream>
#include <cmath>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int iter = 0; iter < t; ++iter) {
        int n, m, i, j;
        std::scanf("%d %d %d %d", &n, &m, &i, &j);
        long long case1 = (
            std::abs(i - 1) + std::abs(j - 1)
            + (n - 1) + (m - 1)
        );
        long long case2 = std::abs(i - 1) + std::abs(m - j) + std::abs(n - 1) + std::abs(m - 1);
        if (case1 >= case2) std::printf("%d %d %d %d\n", 1, 1, n, m);
        else std::printf("%d %d %d %d\n", 1, m, n, 1);

    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m, i, j = map(int, sys.stdin.readline().rstrip().split())
        case1: int = abs(i - 1) + abs(j - 1) + abs(n - 1) + abs(m - 1)
        case2: int = abs(i - 1) + abs(m - j) + abs(n - 1) + abs(m - 1)
        if case1 >= case2:
            sys.stdout.write('{} {} {} {}\n'.format(1, 1, n, m))
        else:
            sys.stdout.write('{} {} {} {}\n'.format(1, m, n, 1))


if __name__ == '__main__':
    solution()