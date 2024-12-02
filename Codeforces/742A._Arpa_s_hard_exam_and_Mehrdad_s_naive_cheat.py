# A. Arpa’s hard exam and Mehrdad’s naive cheat
# time limit per test1 second
# memory limit per test256 megabytes
# There exists an island called Arpa’s land, some beautiful girls live there, as ugly ones do.
#
# Mehrdad wants to become minister of Arpa’s land. Arpa has prepared an exam. Exam has only one question, given n, print the last digit of 1378n.
#
#
# Mehrdad has become quite confused and wants you to help him. Please help, although it's a naive cheat.
#
# Input
# The single line of input contains one integer n (0  ≤  n  ≤  109).
#
# Output
# Print single integer — the last digit of 1378n.
#
# Examples
# InputCopy
# 1
# OutputCopy
# 8
# InputCopy
# 2
# OutputCopy
# 4
# Note
# In the first example, last digit of 13781 = 1378 is 8.
#
# In the second example, last digit of 13782 = 1378·1378 = 1898884 is 4.
# Solution
# Python O(1) O(1) Math
import sys


def solution(n: int) -> None:
    if n == 0:
        sys.stdout.write('1\n')
    else:
        last_digit_cycle = [6, 8, 4, 2]
        sys.stdout.write(str(last_digit_cycle[n % 4]) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    solution(n)

# C++ O(1) O(1) Math
#include <iostream>
#include <vector>


void solution(int n) {
    if (n == 0) {
        std::cout << 1 << "\n";
    } else {
        std::vector<int> lastDigit = {6, 8, 4, 2};
        std::cout << lastDigit[n % 4] << "\n";
    }
}

int main() {
    int n;
    std::cin >> n;
    solution(n);
}