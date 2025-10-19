# C. Beautiful XOR
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two integers a
#  and b
# . You are allowed to perform the following operation any number of times (including zero):
#
# choose any integer x
#  such that 0≤x≤a
#  (the current value of a
# , not initial),
# set a:=a⊕x
# . Here, ⊕
#  represents the bitwise XOR operator.
# After performing a sequence of operations, you want the value of a
#  to become exactly b
# .
#
# Find a sequence of at most 100
#  operations (values of x
#  used in each operation) that transforms a
#  into b
# , or report that it is impossible.
#
# Note that you are not required to find the minimum number of operations, but any valid sequence of at most 100
#  operations.
#
# Input
# The first line of input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ).
#
# Output
# For each test case, if it is impossible to obtain b
#  from a
#  using the allowed operations, print a single line containing −1
# .
#
# Otherwise, on the first line print a single integer k
#  (0≤k≤100
# ) — the number of operations. On the second line print k
#  integers (x1,x2,…,xk
# ) — the chosen values of x
#  in the order you apply them.
#
# If there are multiple valid sequences, you may print any one of them.
#
# Example
# InputCopy
# 6
# 9 6
# 13 13
# 292 929
# 405 400
# 998 244
# 244 353
# OutputCopy
# 2
# 7 8
# 0
# -1
# 1
# 5
# 2
# 25 779
# -1
# Note
# For the first test case,
#
# choose x=7
# , now a
#  becomes equal to 9⊕7=14
# .
# choose x=8
# , now a
#  becomes equal to 14⊕8=6
# .
# Thus, we can make a=b
# .
# For the fourth test case, choosing x=5
#  makes a=b
# .
# Solution
# C++ O(logN) O(1) Bit
#include <iostream>
#include <vector>


void solution() {
    int a, b;
    std::cin >> a >> b;
    if (a == b) {
        std::cout << "0\n";
        return;
    }
    int a_ = a, b_ = b;
    while (a_ && b_) {
        a_ >>= 1;
        b_ >>= 1;
    }
    if (b_) {
        std::cout << "-1\n";
        return;
    }
    std::vector<int> moves;

    int places = 0;
    while (a && b) {
        if ((a & 1) != (b & 1)) moves.push_back(1 << places);
        a >>= 1;
        b >>= 1;
        ++places;
    }
    while (a) {
        if (a & 1) moves.push_back(1 << places);
        ++places;
        a >>= 1;
    }

    std::cout << moves.size() << "\n";
    for (int& move : moves) std::cout << move << " ";
    std::cout << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(logN) O(1) Bit
import sys


def solution() -> None:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == b:
        sys.stdout.write('0\n')
        return
    a_: int = a
    b_: int = b
    while a_ and b_:
        a_ >>= 1
        b_ >>= 1
    if b_:
        sys.stdout.write('-1\n')
        return
    moves: list[int] = []
    places: int = 0
    while a and b:
        if (a & 1) != (b & 1): moves.append(1 << places)
        places += 1
        a >>= 1
        b >>= 1
    while a:
        if a & 1: moves.append(1 << places)
        places += 1
        a >>= 1
    sys.stdout.write('{}\n{}\n'.format(len(moves), ' '.join(map(str, moves))))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()