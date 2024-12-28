# A. Case of the Zeros and Ones
# time limit per test1 second
# memory limit per test256 megabytes
# Andrewid the Android is a galaxy-famous detective. In his free time he likes to think about strings containing zeros and ones.
#
# Once he thought about a string of length n consisting of zeroes and ones. Consider the following operation: we choose any two adjacent positions in the string, and if one them contains 0, and the other contains 1, then we are allowed to remove these two digits from the string, obtaining a string of length n - 2 as a result.
#
# Now Andreid thinks about what is the minimum length of the string that can remain after applying the described operation several times (possibly, zero)? Help him to calculate this number.
#
# Input
# First line of the input contains a single integer n (1 ≤ n ≤ 2·105), the length of the string that Andreid has.
#
# The second line contains the string of length n consisting only from zeros and ones.
#
# Output
# Output the minimum length of the string that may remain after applying the described operations several times.
#
# Examples
# InputCopy
# 4
# 1100
# OutputCopy
# 0
# InputCopy
# 5
# 01010
# OutputCopy
# 1
# InputCopy
# 8
# 11101111
# OutputCopy
# 6
# Note
# In the first sample test it is possible to change the string like the following: .
#
# In the second sample test it is possible to change the string like the following: .
#
# In the third sample test it is possible to change the string like the following: .
# Solution
# C++ O(N) O(N) Stack
#include <iostream>
#include <string>
#include <stack>


void solution() {
    int n;
    std::cin >> n;
    std::string sequence;
    std::cin >> sequence;
    std::stack<char> st;
    for (int i = 0; i < n; ++i) {
        if (st.size() && st.top() != sequence[i]) {
            st.pop();
        } else {
            st.push(sequence[i]);
        }
    }
    std::cout << st.size() << "\n";
}


int main() {
    solution();
}
# Python O(N) O(N) Stack
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    sequence: str = sys.stdin.readline().rstrip()
    stack: list = []
    for i in range(n):
        if stack and stack[-1] != sequence[i]:
            stack.pop()
        else:
            stack.append(sequence[i])
    sys.stdout.write(str(len(stack)) + '\n')


if __name__ == '__main__':
    solution()