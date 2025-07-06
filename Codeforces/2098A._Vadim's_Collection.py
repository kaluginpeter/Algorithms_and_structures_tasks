# A. Vadim's Collection
# time limit per test1 second
# memory limit per test256 megabytes
# We call a phone number a beautiful if it is a string of 10
#  digits, where the i
# -th digit from the left is at least 10−i
# . That is, the first digit must be at least 9
# , the second at least 8
# , …
# , with the last digit being at least 0
# .
#
# For example, 9988776655 is a beautiful phone number, while 9099999999 is not, since the second digit, which is 0
# , is less than 8
# .
#
# Vadim has a beautiful phone number. He wants to rearrange its digits in such a way that the result is the smallest possible beautiful phone number. Help Vadim solve this problem.
#
# Please note that the phone numbers are compared as integers.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The only line of each test case contains a single string s
#  of length 10
# , consisting of digits. It is guaranteed that s
#  is a beautiful phone number.
#
# Output
# For each test case, output a single string of length 10
#  — the smallest possible beautiful phone number that Vadim can obtain.
#
# Example
# InputCopy
# 4
# 9999999999
# 9988776655
# 9988776650
# 9899999999
# OutputCopy
# 9999999999
# 9876556789
# 9876567890
# 9899999999
# Note
# In the first test case, for the first phone number 9999999999, regardless of the rearrangement of digits, the same phone number is obtained.
#
# In the second test case, for the phone number 9988776655, it can be proven that 9876556789 is the smallest phone number that can be obtained by rearranging the digits.
# Solution
# C++ O(log10(10) + 10*10) O(10) HashMap Greedy
#include <iostream>
#include <string>
#include <array>


void solution() {
    std::string n = "";
    std::cin >> n;
    std::array<short, 10> hashmap = {};
    for (char &digit : n) {
        ++hashmap[digit - '0'];
    }
    std::string output = "";
    for (int i = 9; i >= 0; --i) {
        for (int digit = 0; digit < 10; ++digit) {
            if (digit < i || !hashmap[digit]) continue;
            --hashmap[digit];
            output.push_back(digit + '0');
            break;
        }
    }
    std::cout << output << "\n";

}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(log10(10) + 10*10) O(10) HashMap Greedy
import sys


def solution() -> None:
    n: str = sys.stdin.readline().rstrip()
    hashmap: list[int] = [0] * 10
    for digit in n: hashmap[int(digit)] += 1
    output: list[str] = []
    for bound in range(9, -1, -1):
        for digit in range(10):
            if digit < bound or not hashmap[digit]: continue
            hashmap[digit] -= 1
            output.append(str(digit))
            break
    sys.stdout.write('{}\n'.format(''.join(output)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()