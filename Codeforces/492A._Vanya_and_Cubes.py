# A. Vanya and Cubes
# time limit per test1 second
# memory limit per test256 megabytes
# Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, the second level must consist of 1 + 2 = 3 cubes, the third level must have 1 + 2 + 3 = 6 cubes, and so on. Thus, the i-th level of the pyramid must have 1 + 2 + ... + (i - 1) + i cubes.
#
# Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.
#
# Input
# The first line contains integer n (1 ≤ n ≤ 104) — the number of cubes given to Vanya.
#
# Output
# Print the maximum possible height of the pyramid in the single line.
#
# Examples
# inputCopy
# 1
# outputCopy
# 1
# inputCopy
# 25
# outputCopy
# 4
# Note
# Illustration to the second sample:
# Solution
# C++ O(logN) O(1) Math
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int height = 0;
    int total = 0;
    while (true) {
        int cubes_needed = (height + 1) * (height + 2) / 2;
        if (total + cubes_needed > n) {
            break;
        }
        height += 1;
        total += cubes_needed;
    }
    std::cout << height << std::endl;
}
# Python O(logN) O(1) Math
import sys

def solution(n: int) -> str:
    height: int = 0
    total: int = 0
    while True:
        cubes_needed: int = (height + 1) * (height + 2) // 2
        if total + cubes_needed > n:
            break
        height += 1
        total += cubes_needed
    return str(height)

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n) + "\n")
