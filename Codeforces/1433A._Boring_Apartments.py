# A. Boring Apartments
# time limit per test1 second
# memory limit per test256 megabytes
# There is a building consisting of 10 000
#  apartments numbered from 1
#  to 10 000
# , inclusive.
#
# Call an apartment boring, if its number consists of the same digit. Examples of boring apartments are 11,2,777,9999
#  and so on.
#
# Our character is a troublemaker, and he calls the intercoms of all boring apartments, till someone answers the call, in the following order:
#
# First he calls all apartments consisting of digit 1
# , in increasing order (1,11,111,1111
# ).
# Next he calls all apartments consisting of digit 2
# , in increasing order (2,22,222,2222
# )
# And so on.
# The resident of the boring apartment x
#  answers the call, and our character stops calling anyone further.
#
# Our character wants to know how many digits he pressed in total and your task is to help him to count the total number of keypresses.
#
# For example, if the resident of boring apartment 22
#  answered, then our character called apartments with numbers 1,11,111,1111,2,22
#  and the total number of digits he pressed is 1+2+3+4+1+2=13
# .
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤36
# ) — the number of test cases.
#
# The only line of the test case contains one integer x
#  (1≤x≤9999
# ) — the apartment number of the resident who answered the call. It is guaranteed that x
#  consists of the same digit.
#
# Output
# For each test case, print the answer: how many digits our character pressed in total.
#
# Example
# inputCopy
# 4
# 22
# 9999
# 1
# 777
# outputCopy
# 13
# 90
# 1
# 66
# Solution Math
# Python O(logN) O(1)
import sys


def solution(t:int) -> None:
    for _ in range(t):
        x: int = int(sys.stdin.readline().rstrip())
        remainder: int = 0
        module: int = 0
        while x:
            remainder = x % 10
            x //= 10
            module += 1
        acc: int = 0
        for digit in range(1, module + 1):
            acc += digit
        sys.stdout.write(str(10 * (remainder - 1) + acc) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
# C++ O(logN) O(1)
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int x;
        std::cin >> x;
        int remainder = 1;
        int module = 0;
        while (x) {
            remainder = x % 10;
            x /= 10;
            module++;
        }
        int acc = 0;
        for (int digit = 1; digit <= module; ++digit) {
            acc += digit;
        }
        std::cout << (10 * (remainder - 1)) + acc << std::endl;
    }
}