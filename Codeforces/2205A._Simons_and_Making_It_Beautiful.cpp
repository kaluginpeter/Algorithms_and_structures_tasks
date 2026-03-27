/*
A. Simons and Making It Beautiful
time limit per test1 second
memory limit per test256 megabytes

Those cling-on troubles that ride my stride — cough up the fee, or step aside.
— SHUN, TAKE IT AWAY
For a permutation∗
 r
 of length m
, we call an index i
 (1≤i≤m
) ugly if and only if i=max({r1,r2,…,ri})
.

Simons has a permutation p
 of length n
, and he can perform the following operation on p
 at most once:

Choose two indices i
 and j
 (1≤i≠j≤n
), then swap pi
 and pj
.
Find a permutation q
 that can be obtained from p
 by performing the above operation at most once, such that the number of ugly indices in q
 is minimized.

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

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The first line contains an integer n
 (1≤n≤500
) — the length of p
.

The second line contains n
 integers p1,p2,…,pn
 (1≤pi≤n
, all pi
-s are distinct) — the elements of p
.

Output
For each test case, print n
 integers q1,q2,…,qn
 — the permutation you found.

If there are multiple possible permutations, you may output any.

Example
InputCopy
5
2
1 2
4
2 3 1 4
5
3 2 4 5 1
1
1
8
4 1 3 2 6 7 8 5
OutputCopy
2 1
2 4 1 3
3 2 4 5 1
1
4 1 3 8 6 7 2 5
Note
In the first test case, Simons can obtain only two possible permutations: [1,2]
 and [2,1]
.

For permutation [1,2]
, we can see 1=max({1})
 and 2=max({1,2})
. So there are two ugly indices.
For permutation [2,1]
, we can see 1≠max({2})
 and 2=max({2,1})
. So there is only one ugly index.
Thus, permutation [2,1]
 has the minimum count of ugly indices.

In the second test case, Simons can obtain permutation [2,4,1,3]
 by choosing indices 2
 and 4
 to swap. There is only one ugly index in the permutation:

1≠max({2})
, so index 1
 is not ugly;
2≠max({2,4})
, so index 2
 is not ugly;
3≠max({2,4,1})
, so index 3
 is not ugly;
4=max({2,4,1,3})
, so index 4
 is ugly.
In the third test case, note that Simons does not perform the operation.
*/