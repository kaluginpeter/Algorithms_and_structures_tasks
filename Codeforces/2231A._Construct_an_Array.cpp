/*
A. Construct an Array
time limit per test1 second
memory limit per test256 megabytes
You are given an integer n
. You need to construct an array of integers a1,a2,…,an
 such that the following conditions are satisfied:

1≤ai≤2⋅n
 for all i
 from 1
 to n
.
All elements of the array and the sums of adjacent elements are pairwise distinct. In other words, among the numbers {a1,a2,…,an,a1+a2,a2+a3,…,an−1+an}
, there should not be two equal numbers.
Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The only line of each test case contains one integer n
 (1≤n≤500
).

Output
For each test case, output an array of length n
 that satisfies the condition of the problem. It can be shown that such an array always exists under the given constraints.

Example
InputCopy
3
1
3
6
OutputCopy
1
6 2 3
8 1 11 2 3 4
Note
In the second example, all elements and adjacent sums form the set 6,2,3,8,5
, all of whose elements are distinct.

In the third example, all elements and adjacent sums form the set 8,1,11,2,3,4,9,12,13,5,7
, whose elements are also distinct.
*/