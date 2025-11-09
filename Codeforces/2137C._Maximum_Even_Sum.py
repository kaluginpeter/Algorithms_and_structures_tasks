# C. Maximum Even Sum
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two integers a
#  and b
# . You are to perform the following procedure:
#
# First, you choose an integer k
#  such that b
#  is divisible by k
# . Then, you simultaneously multiply a
#  by k
#  and divide b
#  by k
# .
#
# Find the greatest possible even value of a+b
# . If it is impossible to make a+b
#  even, output −1
#  instead.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers a
#  and b
#  (1≤a,b≤a⋅b≤1018)
# .
#
# Output
# For each test case, output the maximum even value of a+b
#  on a new line.
#
# Example
# InputCopy
# 7
# 8 1
# 1 8
# 7 7
# 2 6
# 9 16
# 1 6
# 4 6
# OutputCopy
# -1
# 6
# 50
# 8
# 74
# -1
# 14
# Note
# In the first test case, it can be shown it is impossible for a+b
#  to be even.
#
# In the second test case, the optimal k
#  is 2
# . The sum is 2+4=6
# .
# Solution
# C++ O(1) O(1) NumberTheory
#include <iostream>


void solution() {
    unsigned long long a, b;
    std::cin >> a >> b;
    bool isFirst = !(a & 1), isSecond = !(b & 1);
    if (isFirst && isSecond) {
        unsigned long long output = a + b;
        if (!((b / 2 * a + 2) & 1)) {
            output = std::max(output, b / 2 * a + 2);
        }
        if (!(a * 2 + b / 2 & 1)) output = std::max(output, a * 2 + b / 2);
        std::cout << output << "\n";
    } else if (isFirst) {
        std::cout << "-1\n";
        return;
    } else if (isSecond) {
        // a is odd and b is even
        // odd * even = even
        bool was = false;
        unsigned long long output = 0;
        if (!((b / 2) & 1)) {
            was = true;
            output = a * (b / 2) + 2;
        }
        if (!((a * 2 + b / 2) & 1)) {
            was = true;
            output = std::max(output, a * 2 + b / 2);
        }
        if (was) std::cout << output << "\n";
        else std::cout << "-1\n";
    } else {
        unsigned long long output = a * b + 1;
        std::cout << output << "\n";
    }
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}