# A. Creating Words
# time limit per test1 second
# memory limit per test256 megabytes
# Matthew is given two strings a
#  and b
# , both of length 3
# . He thinks it's particularly funny to create two new words by swapping the first character of a
#  with the first character of b
# . He wants you to output a
#  and b
#  after the swap.
#
# Note that the new words may not necessarily be different.
#
# Input
# The first line contains t
#  (1≤t≤100
# )  — the number of test cases.
#
# The first and only line of each test case contains two space-separated strings, a
#  and b
# , both of length 3
# . The strings only contain lowercase Latin letters.
#
# Output
# For each test case, after the swap, output a
#  and b
# , separated by a space.
#
# Example
# inputCopy
# 6
# bit set
# cat dog
# hot dog
# uwu owo
# cat cat
# zzz zzz
# outputCopy
# sit bet
# dat cog
# dot hog
# owu uwo
# cat cat
# zzz zzz
# Solution
# Python O(N) O(1)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b = sys.stdin.readline().rstrip().split()
        sys.stdout.write(b[0] + a[1:] + ' ' + a[0] + b[1:] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(N) O(1)
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (size_t i = 0; i < t; ++i) {
        std::string a, b;
        std::cin >> a >> b;
        std::cout << b[0] << a.substr(1, a.size()) << " " << a[0] << b.substr(1, b.size()) << std::endl;
    }
}