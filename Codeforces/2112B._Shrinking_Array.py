# B. Shrinking Array
# time limit per test2 seconds
# memory limit per test256 megabytes
# Let's call an array b
#  beautiful if it consists of at least two elements and there exists a position i
#  such that |bi−bi+1|≤1
#  (where |x|
#  is the absolute value of x
# ).
#
# You are given an array a
# , and as long as it consists of at least two elements, you can perform the following operation:
#
# Choose two adjacent positions i
#  and i+1
#  in the array a
# .
# Choose an integer x
#  such that min(ai,ai+1)≤x≤max(ai,ai+1)
# .
# Remove the numbers ai
#  and ai+1
#  from the array, and insert the number x
#  in their place. Obviously, the size of the array will decrease by 1
# .
# Calculate the minimum number of operations required to make the array beautiful, or report that it is impossible.
#
# Input
# The first line contains one integer t
#  (1≤t≤200
# ) — the number of test cases.
#
# The first line of each test case contains one integer n
#  (2≤n≤1000
# ) — the size of the array a
# .
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤106
# ) — the array a
#  itself.
#
# Output
# For each test case, output one integer — the minimum number of operations needed to make the array a
#  beautiful, or −1
#  if it is impossible to make it beautiful.
#
# Example
# InputCopy
# 4
# 4
# 1 3 3 7
# 2
# 6 9
# 4
# 3 1 3 7
# 4
# 1 3 5 2
# OutputCopy
# 0
# -1
# 1
# 1
# Note
# In the first test case, the given array is already beautiful, as |a2−a3|=|3−3|=0
# .
#
# In the second test case, it is impossible to make the array beautiful, as applying the operation would reduce its size to less than two.
#
# In the third test case, you can, for example, choose a1
#  and a2
#  and replace them with the number 2
# . The resulting array [2,3,7]
#  is beautiful.
#
# In the fourth test case, you can, for example, choose a2
#  and a3
#  and replace them with the number 3
# . The resulting array [1,3,2]
#  is beautiful.
# Solution
# C++ O(N^2) O(1) Greedy
#include <iostream>
#include <vector>
#include <algorithm>

const int INF = 1e9;

void solution() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) std::cin >> a[i];
    for (int i = 0; i < n - 1; ++i) {
        if (std::abs(a[i] - a[i + 1]) <= 1) {
            std::cout << "0\n";
            return;
        }
    }

    int min_ops = INF;
    for (int i = 0; i < n; ++i) {
        if (i > 0) {
            int current_min = a[i - 1];
            int current_max = a[i - 1];
            for (int j = i - 1; j >= 0; --j) {
                current_min = std::min(current_min, a[j]);
                current_max = std::max(current_max, a[j]);
                if (std::max(current_min, a[i] - 1) <= std::min(current_max, a[i] + 1)) {
                    min_ops = std::min(min_ops, (i - 1) - j);
                }
            }
        }
        if (i < n - 1) {
            int current_min = a[i + 1];
            int current_max = a[i + 1];
            for (int j = i + 1; j < n; ++j) {
                current_min = std::min(current_min, a[j]);
                current_max = std::max(current_max, a[j]);
                if (std::max(current_min, a[i] - 1) <= std::min(current_max, a[i] + 1)) {
                    min_ops = std::min(min_ops, j - (i + 1));
                }
            }
        }
    }

    if (min_ops == INF) {
        std::cout << "-1\n";
    } else {
        std::cout << min_ops << "\n";
    }
}

int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
    return 0;
}

# Python O(N^2) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            sys.stdout.write('0\n')
            return
    output: int = float('inf')
    for i in range(n):
        if i:
            current_min: int = a[i - 1]
            current_max: int = a[i - 1]
            for j in range(i - 1, -1, -1):
                current_min = min(current_min, a[j])
                current_max = max(current_max, a[j])
                if max(current_min, a[i] - 1) <= min(current_max, a[i] + 1):
                    output = min(output, (i - 1) - j)
                    break
        if i + 1 == n: continue
        current_min = a[i + 1]
        current_max = a[i + 1]
        for j in range(i + 1, n):
            current_min = min(current_min, a[j])
            current_max = max(current_max, a[j])
            if max(current_min, a[i] - 1) <= min(current_max, a[i] + 1):
                output = min(output, j - (i + 1))
                break
    sys.stdout.write('{}\n'.format([output, -1][output == float('inf')]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()