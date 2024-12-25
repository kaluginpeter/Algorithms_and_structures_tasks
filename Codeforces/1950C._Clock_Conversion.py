# C. Clock Conversion
# time limit per test1 second
# memory limit per test256 megabytes
# Given the time in 24-hour format, output the equivalent time in 12-hour format.
#
# 24-hour format divides the day into 24 hours from 00
#  to 23
# , each of which has 60 minutes from 00
#  to 59
# .
# 12-hour format divides the day into two halves: the first half is AM
# , and the second half is PM
# . In each half, the hours are numbered in the order 12,01,02,03,…,11
# . Each hour has 60 minutes numbered from 00
#  to 59
# .
# Input
# The first line contains a single integer t
#  (1≤t≤1440
# ) — the number of test cases.
#
# The only line of each test case contains a string s
#  of length 5
#  with format hh:mm representing a valid time in the 24-hour format. hh represents the hour from 00
#  to 23
# , and mm represents the minute from 00
#  to 59
# .
#
# The input will always be a valid time in 24-hour format.
#
# Output
# For each test case, output two strings separated by a space ("hh:mm AM" or "hh:mm PM"), which are the 12-hour equivalent to the time provided in the test case (without quotes).
#
# You should output the time exactly as indicated; in particular, you should not remove leading zeroes.
#
# Example
# InputCopy
# 11
# 09:41
# 18:06
# 12:14
# 00:59
# 00:00
# 14:34
# 01:01
# 19:07
# 11:59
# 12:00
# 21:37
# OutputCopy
# 09:41 AM
# 06:06 PM
# 12:14 PM
# 12:59 AM
# 12:00 AM
# 02:34 PM
# 01:01 AM
# 07:07 PM
# 11:59 AM
# 12:00 PM
# 09:37 PM
# C++ O(1) O(1) Greedy
#include <iostream>
#include <string>

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        std::string time;
        std::getline(std::cin, time);
        std::string h_str = time.substr(0, 2);
        std::string m_str = time.substr(3, 2);
        int h = std::stoi(h_str);
        bool past = false;

        if (h >= 12) {
            past = true;
        }
        if (h >= 13) {
            h -= 12;
        } else if (h == 0) {
            h = 12;
        }
        std::cout << (h < 10 ? "0" : "") << h << ":" << m_str << " " << (past ? "PM" : "AM") << std::endl;
    }
}

int main() {
    int t;
    std::cin >> t;
    std::cin.ignore();
    solution(t);
    return 0;
}

# Python O(1) O(1)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        h, m = sys.stdin.readline().rstrip().split(':')
        past: bool = False
        if h >= '12':
            past = True
        if h >= '13':
            h = str(int(h) - 12)
            if len(h) == 1:
                h = '0' + h
        elif int(h) == 0:
            h = '12'
        sys.stdout.write(f'{h}:{m} {"AM" if not past else "PM"}\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
