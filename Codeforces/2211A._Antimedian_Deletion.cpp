/*
A. Antimedian Deletion
time limit per test1 second
memory limit per test256 megabytes

You are given a permutation∗
 p
 of size n
. You may perform the following operation any number of times:

Choose a subarray†
 of size 3
. Then, delete either the smallest or largest element within it.
For example, for the permutation [2,4,5,3,1]
, you may choose the subarray [2,4,5,3,1]
. Since 5=max(2,4,5)
. you can delete 5
 to obtain the array [2,4,3,1]
. You may also choose to delete 2
 instead as 2=min(2,4,5)
.

For each i
 from 1
 to n
, find the minimum length of an obtainable array that contains the number pi
. Note that this problem is to be solved independently for each i
.

∗
A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (n=3
 but there is 4
 in the array).

†
An array a
 is a subarray of an array b
 if a
 can be obtained from b
 by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤100
) — the length of the array.

The second line of each test case contains n
 integers p1,p2,…,pn
 (1≤pi≤n
). It is guaranteed that each element from 1
 to n
 appears exactly once.

Output
For each test case, output n
 numbers on a new line: the answer for i=1,2,…,n
.

Example
InputCopy
2
1
1
3
2 1 3
OutputCopy
1
2 2 2
Note
In the first example, we cannot perform any operations as the size of the array is only 1<3
.

In the second example, for i=2
, we can choose the subarray [2,1,3]
, and delete the largest number 3
 to obtain the array [2,1]
. It can be shown that 2
 is the minimum length of any reachable array that contains a2=1
.
*/
// Solution
// C++ O(N) O(1) Greedy Math
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    for (size_t i = 0; i < n; ++i) {
        std::cout << (n < 3 ? n : 2);
        std::cout << " " ;
    }
    std::cout << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}