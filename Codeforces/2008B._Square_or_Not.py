# B. Square or Not
# time limit per test2 seconds
# memory limit per test256 megabytes
# A beautiful binary matrix is a matrix that has ones on its edges and zeros inside.
#
# Examples of four beautiful binary matrices.
# Today, Sakurako was playing with a beautiful binary matrix of size r×c
#  and created a binary string s
#  by writing down all the rows of the matrix, starting from the first and ending with the r
# -th. More formally, the element from the matrix in the i
# -th row and j
# -th column corresponds to the ((i−1)∗c+j)
# -th element of the string.
#
# You need to check whether the beautiful matrix from which the string s
#  was obtained could be squared. In other words, you need to check whether the string s
#  could have been build from a square beautiful binary matrix (i.e., one where r=c
# ).
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤2⋅105
# ) — the length of the string.
#
# The second line of each test case contains the string s
#  of length n
# . The string is always the result of writing out the strings of a beautiful matrix.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# Print "Yes", if the original matrix could have been square, and "No" otherwise.
#
# Example
# InputCopy
# 5
# 2
# 11
# 4
# 1111
# 9
# 111101111
# 9
# 111111111
# 12
# 111110011111
# OutputCopy
# No
# Yes
# Yes
# No
# No
# Note
# For the second test case, string 1111 can be obtained from the matrix:
#
# 1
# 1
# 1
# 1
# For the third test case, string 111101111 can be obtained from the matrix:
#
# 1
# 1
# 1
# 1
# 0
# 1
# 1
# 1
# 1
# There is no square matrix in the fourth case, such that the string can be obtained from it.
# Solution
# Python O(N) O(K) String
#include <iostream>
#include <string>


void solution() {
    size_t n;
    std::cin >> n;
    std::string matrix;
    std::cin >> matrix;
    size_t zeros = 0, left = 0;
    for (size_t right = 0; right < n; ++right) {
        if (matrix[right] != '0') left = right + 1;
        zeros = std::max(zeros, right - left + 1);
    }
    std::string pattern = "1";
    for (size_t i = 0; i < zeros; ++i) pattern.push_back('0');
    pattern.push_back('1');
    bool isValid = true;
    size_t chunk = pattern.size();
    for (size_t start = chunk; start < n - chunk; start += chunk) {
        for (size_t i = 0; i < chunk; ++i) {
            if (matrix[start + i] != pattern[i]) {
                isValid = false;
                break;
            }
        }
        if (!isValid) break;
    }
    for (size_t i = 0; i < chunk; ++i) {
        if (matrix[i] != '1' || matrix[n - i - 1] != '1') isValid = false;
    }
    isValid = isValid && (chunk == n / chunk && n % chunk == 0);
    std::cout << (isValid ? "Yes" : "No") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(K) String
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    matrix: str = sys.stdin.readline().rstrip()
    zeros: int = 0
    left: int = 0
    for right in range(n):
        if matrix[right] != '0': left = right + 1
        zeros = max(zeros, right - left + 1)
    pattern: str = '1' + '0' * zeros + '1'
    chunk: int = len(pattern)
    if chunk != n // chunk or n % chunk != 0:
        sys.stdout.write('No\n')
        return
    is_valid: bool = True
    for i in range(chunk, n - chunk, chunk):
        for j in range(chunk):
            if matrix[i + j] != pattern[j]:
                is_valid = False
                break
        if not is_valid: break
    for i in range(chunk):
        if matrix[i] != '1' or matrix[n - i - 1] != '1':
            is_valid = False
            break
    sys.stdout.write('{}\n'.format(['No', 'Yes'][is_valid]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()