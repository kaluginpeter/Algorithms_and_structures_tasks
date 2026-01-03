/*
C. Blackslex and Number Theory
time limit per test2 seconds
memory limit per test256 megabytes
Blackslex worked too hard and started dreaming about numbers. Solve the following task from his dreams.

You are given an array a1,a2,…,an
.

In one operation you choose an index i
 (1≤i≤n
) and an integer x
 which is at least k
 and set
ai:=aimodx,
where umodv
 denotes the remainder of dividing u
 by v
.

Your goal is to make all elements of the array identical. Among all positive integers k
, determine the maximum k
 for which there exists a finite sequence of the above operations that makes all array elements equal.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains a single integer n
 (2≤n≤2⋅105
).

The second line contains n
 integers a1,a2,…,an
 (1≤ai≤109
, all values of a
 are distinct).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print a single integer — the maximum positive integer k
 such that it is possible to make all elements of the array identical using any number of operations with moduli x
 restricted to k≤x
.

Example
InputCopy
3
3
5 7 9
2
2 3
7
11 74 5 22 52 97 82
OutputCopy
5
2
6
*/