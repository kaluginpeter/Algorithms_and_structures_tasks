/*
C. Snowfall
time limit per test2 seconds
memory limit per test256 megabytes
Yousef has given you an array a
 of n
 positive integers.

Let f(a)
 denote the number of subarrays∗
 of a
 whose product is divisible by 6
.

More formally, for every pair of indices l
 and r
 such that 1≤l≤r≤n
, consider the subarray al,al+1,…,ar
. This subarray is counted if the product of its elements is divisible by 6
.

For example, if a=[1,6,2]
, then the subarrays whose products are divisible by 6
 are [6]
, [1,6]
, [6,2]
, and [1,6,2]
, so f(a)=4
.

Your task is to reorder the elements of the array a
 so that f(a)
 is minimized. If there are multiple ways to do this, you may output any of them.

∗
An array b
 is a subarray of an array a
 if b
 can be obtained from a
 by deleting several (possibly zero or all) elements from the beginning and several (possibly zero or all) elements from the end.

Input
The first line of the input contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the size of the array.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the elements of the array.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output the array after reordering it in such a way that f(a)
 is minimized. If there are multiple answers, you may output any of them.

Example
InputCopy
5
6
12 7 9 4 18 5
4
3 6 2 8
7
1 10 15 20 3 6 9
5
11 14 21 2 5
3
6 6 6
OutputCopy
12 18 4 7 5 9
2 8 3 6
6 10 20 1 15 3 9
21 5 11 2 14
6 6 6
Note
In the first test case, an optimal arrangement is a=[12,18,4,7,5,9]
. The subarrays whose products are divisible by 6
 are:

[12]
[18]
[12,18]
[18,4]
[12,18,4]
[18,4,7]
[12,18,4,7]
[18,4,7,5]
[4,7,5,9]
[12,18,4,7,5]
[18,4,7,5,9]
[12,18,4,7,5,9]
Therefore, f(a)=12
. It can be proven that no other arrangement yields a smaller value of f(a)
.
*/