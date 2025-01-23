# A. Primary Task
# time limit per test1 second
# memory limit per test256 megabytes
# Dmitry wrote down t
#  integers on the board, and that is good. He is sure that he lost an important integer n
#  among them, and that is bad.
#
# The integer n
#  had the form 10^x
#  (x≥2
# ), where the symbol '^
# ' denotes exponentiation.. Something went wrong, and Dmitry missed the symbol '^
# ' when writing the important integer. For example, instead of the integer 105
# , he would have written 105
# , and instead of 1019
# , he would have written 1019
# .
#
# Dmitry wants to understand which of the integers on the board could have been the important integer and which could not.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤104
# ) — the number of integers on the board.
#
# The next t
#  lines each contain an integer a
#  (1≤a≤10000
# ) — the next integer from the board.
#
# Output
# For each integer on the board, output "YES" if it could have been the important integer and "NO" otherwise.
#
# You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 7
# 100
# 1010
# 101
# 105
# 2033
# 1019
# 1002
# OutputCopy
# NO
# YES
# NO
# YES
# NO
# YES
# NO
# Solution
# C++ O(1) O(1) Greedy
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string n;
        std::cin >> n;
        std::cout << (n.size() >= 3 && n[0] == '1' && n[1] == '0' && ((n[2] == '1' && n.size() > 3) || (n[2] != '0' && n[2] != '1'))? "YES" : "NO") << "\n";
    }
}


int main () {
    solution();
}

# Python O(1) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        sys.stdout.write(['NO', 'YES'][len(n) >= 3 and n.startswith('10') and ((n[2] == '1' and len(n) > 3) or (n[2] not in '01'))] + '\n')


if __name__ == '__main__':
    solution()