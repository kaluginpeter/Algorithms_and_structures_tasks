/*
A. Blocked
time limit per test1 second
memory limit per test256 megabytes
Given an array a
 of integers of size n
, we say that a position 1≤i≤n
 is blocked if ai
 can be expressed as the sum of a subset of a1,a2,…,ai−1
 (i.e. there exist 1≤j1<j2<…<jk≤i−1
 such that aj1+aj2+…+ajk=ai
). Reorder a
 so that no position is blocked or report that it is impossible.

For example, reordering the array [3,2,5
] to [2,3,5
] makes position 3
 blocked, since we can express 5=2+3
, but if we reorder it to [3,5,2
], no position is blocked.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤400
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤200
).

The second line contains n
 integers, denoting the array a
 (1≤ai≤100
).

Output
For each test case, print any order of a
 such that no position is blocked if it exists, otherwise print −1
.

Example
InputCopy
4
3
1 5 9
4
1 3 3 2
3
1 2 3
1
1
OutputCopy
5 9 1
-1
3 1 2
1
Note
In the third test case, the array [3,1,2
] has no position blocked:

Position 1
 is not blocked since 3
 can't be expressed as the sum of a subset of [].

Position 2
 is not blocked since 1
 can't be expressed as the sum of a subset of [3
].

Position 3
 is not blocked since 2
 can't be expressed as the sum of a subset of [3,1
].
*/
// Solution
// C++ O(NlogN) O(1) Greedy Sorting
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end(), std::greater<int>());
    bool isValid = true;
    for (size_t i = 1; i < n; ++i) {
        if (nums[i] == nums[i - 1]) {
            isValid = false;
            break;
        }
    }
    if (!isValid) {
        std::cout << "-1\n";
        return;
    }
    for (int& num : nums) std::cout << num << " ";
    std::cout << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}