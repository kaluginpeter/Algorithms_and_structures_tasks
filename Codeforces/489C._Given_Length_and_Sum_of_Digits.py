# C. Given Length and Sum of Digits...
# time limit per test1 second
# memory limit per test256 megabytes
# You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.
#
# Input
# The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.
#
# Output
# In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).
#
# Examples
# InputCopy
# 2 15
# OutputCopy
# 69 96
# InputCopy
# 3 0
# OutputCopy
# -1 -1
# Solution
# C++ O(M) O(M) Math
#include <iostream>
#include <vector>

int main() {
    long long m, s;
    std::cin >> m >> s;

    // Edge cases
    if (s == 0) {
        if (m == 1) {
            std::cout << "0 0" << std::endl;  // The only number of length 1 with sum 0 is 0
        } else {
            std::cout << "-1 -1" << std::endl; // Impossible to have a valid number
        }
        return 0;
    }

    if (s > 9 * m) {
        std::cout << "-1 -1" << std::endl; // Impossible to have a valid number
        return 0;
    }

    // Construct the largest number
    std::vector<int> largest(m, 0);
    long long remaining_sum = s;

    for (int i = 0; i < m; ++i) {
        for (int digit = 9; digit >= 0; --digit) {
            if (remaining_sum - digit >= 0 && remaining_sum - digit <= 9 * (m - i - 1)) {
                largest[i] = digit;
                remaining_sum -= digit;
                break;
            }
        }
    }

    // Construct the smallest number
    std::vector<int> smallest(m, 0);
    remaining_sum = s;

    for (int i = 0; i < m; ++i) {
        for (int digit = (i == 0 ? 1 : 0); digit <= 9; ++digit) {
            if (remaining_sum - digit >= 0 && remaining_sum - digit <= 9 * (m - i - 1)) {
                smallest[i] = digit;
                remaining_sum -= digit;
                break;
            }
        }
    }

    // Output the results
    for (int digit : smallest) {
        std::cout << digit;
    }
    std::cout << " ";

    for (int digit : largest) {
        std::cout << digit;
    }
    std::cout << std::endl;

    return 0;
}

# Python O(M) O(M) Math
import sys


def find_smallest_and_largest(m: int, s: int) -> str:
    if s == 0:
        if m == 1:
            return "0 0"
        else:
            return "-1 -1"

    if s > 9 * m:
        return "-1 -1"

    largest = []
    remaining_sum = s

    for i in range(m):
        for digit in range(9, -1, -1):
            if remaining_sum - digit >= 0 and remaining_sum - digit <= 9 * (m - i - 1):
                largest.append(digit)
                remaining_sum -= digit
                break

    smallest = []
    remaining_sum = s
    for i in range(m):
        for digit in range(1 if i == 0 else 0, 10):
            if remaining_sum - digit >= 0 and remaining_sum - digit <= 9 * (m - i - 1):
                smallest.append(digit)
                remaining_sum -= digit
                break

    smallest_number = ''.join(map(str, smallest))
    largest_number = ''.join(map(str, largest))

    return f"{smallest_number} {largest_number}"


if __name__ == '__main__':
    m, s = map(int, input().split())
    sys.stdout.write(find_smallest_and_largest(m, s))