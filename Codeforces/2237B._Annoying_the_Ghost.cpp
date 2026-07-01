/*
B. Annoying the Ghost
time limit per test1.5 seconds
memory limit per test256 megabytes

Ja the Ghost is playing with rubber ducks. He has n
 piles of rubber ducks arranged in a row, where the i
-th pile contains ai
 ducks. Quack the Duck gives Ja a strictly increasing sequence b1,b2,…,bn
 and commands him to make the piles a1,a2,…,an
 become exactly this sequence.

Ja performs the process in the following two stages:

Ja may add any number of ducks to each pile.
Formally, for each pile i
, he chooses a non-negative integer xi
 and replaces ai
 with ai+xi
.

Ja may repeatedly swap two adjacent piles.
Formally, he may perform the following operation any number of times, possibly zero: choose an index i
 such that 1≤i≤n−1
, and swap the values of ai
 and ai+1
.

A process is called valid if, after both stages end, the sequence of pile sizes is exactly b1,b2,…,bn
.

Find the minimum possible number of operations performed in the second stage among all valid processes. If there is no valid process, output −1
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤2000
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤2000
) — the number of piles of rubber ducks.

The second line contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the initial number of rubber ducks in each pile.

The third line contains n
 integers b1,b2,…,bn
 (1≤b1<b2<⋯<bn≤109
) — the final number of rubber ducks in each pile.

It is guaranteed that the sum of n
 over all test cases does not exceed 2000
.

Output
For each test case, output a single integer — the minimum possible number of operations performed in the second stage among all valid processes. If there is no valid process, output −1
.

Example
InputCopy
10
3
1 2 2
1 3 5
3
2 2 1
1 2 3
2
5 1
2 4
6
6 5 4 3 2 1
1 2 3 4 5 6
7
4 7 1 6 2 5 3
1 2 3 4 5 6 7
2
2 1
2 3
4
3 2 2 1
1 2 3 4
4
4 3 2 1
1 3 4 5
5
1 5 4 3 2
2 3 4 5 6
5
10 3 8 6 9
3 6 8 9 10
OutputCopy
0
2
-1
15
12
0
4
4
3
5
Note
In the first test case, Ja only needs the first stage. He can set x1=0,x2=1,x3=3
, so the piles become 1,3,5
. No swaps are needed, so the answer is 0
.

In the second test case, Ja needs both stages. He can set x1=0,x2=1,x3=0
, so the piles become 2,3,1
. Then he can perform two swaps:
[2,3,1]→[2,1,3]→[1,2,3].
The pile with 1
 duck must move from the third position to the first position, so at least two swaps are necessary. Therefore the answer is 2
.

In the third test case, it is impossible. The first pile initially contains 5
 ducks, but every number in the target sequence is at most 4
. Since Ja can only add ducks and cannot remove them, this pile cannot become equal to any number in the target sequence. Therefore the answer is −1
.

In the fourth test case, no ducks need to be added. Ja only needs to reorder the piles into increasing order. The minimum number of adjacent swaps is 15
.

In the fifth test case, no ducks need to be added. Again, Ja only needs to reorder the piles into increasing order. The minimum number of adjacent swaps is 12
.
*/