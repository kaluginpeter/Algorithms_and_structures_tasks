/*
A. Operations with Inversions
time limit per test1 second
memory limit per test256 megabytes
Given an array a1,a2,…,an
. In one operation, you can choose a pair of indices i,j
 such that 1≤i<j≤n
, ai>aj
, and remove the element at index j
 from the array. After that, the size of the array will decrease by 1
, and the relative order of the elements will not change.

Determine the maximum number of operations that can be performed on the array if they are applied optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤50
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤100
) — the size of the initial array.

The second line of each test case contains n
 natural numbers a1,a2,…,an
 (1≤ai≤n
).

Output
For each test case, output the maximum number of operations that you can perform on the given array.

Example
InputCopy
5
3
3 2 1
3
1 2 3
3
3 3 3
5
3 1 4 5 2
1
1
OutputCopy
2
0
0
2
0
Note
In the first example, we can first choose the pair i=2
, j=3
 with values a2=2
, a3=1
 and remove a3
. The resulting array will be a=[3,2]
. After that, we can remove the second element by choosing the pair i=1
, j=2
. The total number of operations is 2
.

In the second, third, and fifth examples, no operations can be performed since there are no suitable pairs.

In the fourth example, we can remove the second and fifth elements. It can be shown that this is the optimal answer and there is no solution that removes more elements.
*/