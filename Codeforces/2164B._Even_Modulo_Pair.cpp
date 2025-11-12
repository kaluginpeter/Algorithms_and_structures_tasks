/*
B. Even Modulo Pair
time limit per test1 second
memory limit per test256 megabytes

You are given a strictly increasing sequence of positive integers a1<a2<…<an
. Find two distinct elements x
 and y
 from the sequence such that x<y
 and ymodx
 is even, or determine that no such pair exists.

pmodq
 denotes the remainder from dividing p
 by q
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤2⋅104
). The description of the test cases follows.

The first line of each test case contains one integer n
 (2≤n≤105
) — the length of the sequence.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤a1<…<an≤109
) — the given sequence.

It is guaranteed that the sum of n
 over all test cases does not exceed 105
.

Output
For each test case:

If no such pair exists, output -1.
Otherwise, output two integers x
 and y
 — the elements that satisfy the condition.
If there are multiple valid pairs, you may output any of them.

Example
InputCopy
4
5
1 3 4 5 6
6
2 3 5 7 11 13
4
2 3 13 37
3
17 117 1117
OutputCopy
3 5
3 11
-1
17 1117
Note
Visualizer link

In the first test case, choosing x=3
 and y=5
 yields ymodx=5mod3=2
, which is even.

In the third test case, it is clear that no valid pair exists.
*/