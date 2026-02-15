/*
A. DBMB and the Array
time limit per test1 second
memory limit per test256 megabytes
DBMB had a birthday yesterday. He was gifted an array a
 of n
 elements and a number x
. But there is one problem: he only likes arrays where the sum of the elements equals s
. To make the array appealing to him, you can perform the following operation any number of times:

Choose an index i
 (1≤i≤n
) and add x
 to the number ai
.
For example, if he was given the array [1,2,3,5]
 and x=2
, you can choose index 3
 and get the array [1,2,5,5]
. Your task is to determine whether the array can appeal to DBMB after any number of operations.
Input
Each test consists of several test cases. The first line contains a single integer t
 (1≤t≤1000
) — the number of test cases. The following describes the test cases.

The first line of each test case contains three integers n
, s
, x
 (1≤n,x≤10
, 1≤s≤100
).

The second line of each test case contains n
 integers a1,a2,…an
 (1≤ai≤10
) — the elements of the array gifted to DBMB.

Output
For each test case, output "YES" if the array can appeal to DBMB. Otherwise, output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Example
InputCopy
6
3 3 5
1 1 1
3 8 2
1 2 3
4 7 2
1 1 1 1
3 15 1
2 4 10
2 100 5
4 6
5 12 1
1 2 2 3 2
OutputCopy
YES
YES
NO
NO
YES
YES
Note
In the second test case, a=[1,2,3]
, applying the operation on a2
 gives us a=[1,4,3]
. The sum of the array equals s
.
*/