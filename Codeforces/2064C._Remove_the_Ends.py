# C. Remove the Ends
# time limit per test3 seconds
# memory limit per test256 megabytes
# You have an array a
#  of length n
#  consisting of non-zero integers. Initially, you have 0
#  coins, and you will do the following until a
#  is empty:
#
# Let m
#  be the current size of a
# . Select an integer i
#  where 1≤i≤m
# , gain |ai|
# ∗
#  coins, and then:
# if ai<0
# , then replace a
#  with [a1,a2,…,ai−1]
#  (that is, delete the suffix beginning with ai
# );
# otherwise, replace a
#  with [ai+1,ai+2,…,am]
#  (that is, delete the prefix ending with ai
# ).
# Find the maximum number of coins you can have at the end of the process.
#
# ∗
# Here |ai|
#  represents the absolute value of ai
# : it equals ai
#  when ai>0
#  and −ai
#  when ai<0
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of testcases.
#
# The first line of each testcase contains an integer n
#  (1≤n≤2⋅105
# ) — the length of a
# .
#
# The second line of each testcase contains n
#  integers a1,a2,…,an
#  (−109≤ai≤109
# , ai≠0
# ).
#
# The sum of n
#  across all testcases does not exceed 2⋅105
# .
#
# Output
# For each test case, output the maximum number of coins you can have at the end of the process.
#
# Example
# InputCopy
# 3
# 6
# 3 1 4 -1 -5 -9
# 6
# -10 -3 -17 1 19 20
# 1
# 1
# OutputCopy
# 23
# 40
# 1
# Note
# An example of how to get 23
#  coins in the first testcase is as follows:
#
# a=[3,1,4,−1,−5,−9]−→−i=6a=[3,1,4,−1,−5]
# , and get 9
#  coins.
# a=[3,1,4,−1,−5]−→−i=1a=[1,4,−1,−5]
# , and get 3
#  coins.
# a=[1,4,−1,−5]−→−i=1a=[4,−1,−5]
# , and get 1
#  coin.
# a=[4,−1,−5]−→−i=3a=[4,−1]
# , and get 5
#  coins.
# a=[4,−1]−→−i=2a=[4]
# , and get 1
#  coin.
# a=[4]−→−i=1a=[]
# , and get 4
#  coins.
# After all the operations, you have 23
#  coins.
# An example of how to get 40
#  coins in the second testcase is as follows:
#
# a=[−10,−3,−17,1,19,20]−→−i=4a=[19,20]
# , and get 1
#  coin.
# a=[19,20]−→−i=1a=[20]
# , and get 19
#  coins.
# a=[20]−→−i=1a=[]
# , and get 20
#  coins.
# After all the operations, you have 40
#  coins.
# Solution
# C++ O(N) O(N) Prefix Suffix Greedy
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
	std::vector<long long>a(n + 1);
	for(int i = 1; i <= n; i++) std::cin >> a[i];
	std::vector<long long>b(n + 1), c(n + 2);
	b[0] = 0;
	c[n + 1] = 0;
	for(int i = 1; i <= n; i++) {
		b[i] = b[i - 1];
		if(a[i] > 0) b[i] = b[i - 1] + a[i];
	}
	for(int i = n; i >= 1; i--) {
		c[i] = c[i + 1];
		if(a[i] < 0) c[i] = c[i + 1] + std::abs(a[i]);
	}
	long long output = 0;
	for(int i = 1; i <= n; i++) output = std::max(output, b[i] + c[i]);
	std::cout << output << std::endl;
}


int main() {
	int t;
	std::cin >> t;
	while(t--) solution();
}

# Python O(N) O(N) Prefix Suffix Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    prefix: list[int] = [0] * (n + 1)
    suffix: list[int] = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (nums[i] if nums[i] > 0 else 0)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] - (nums[i] if nums[i] < 0 else 0)
    output: int = 0
    for i in range(n + 1):
        output = max(output, prefix[i] + suffix[i])
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()