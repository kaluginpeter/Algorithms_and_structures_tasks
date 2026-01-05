/*
B. Impost or Sus
time limit per test1 second
memory limit per test256 megabytes

A string w
 consisting of lowercase Latin letters is called suspicious if and only if all of the following conditions hold:

The letter s
 appears at least twice, and
For every occurrence of the letter u
, the two nearest occurrences of s
 are the same number of characters away from the u
.
After watching you finish a string task, your friend Aka has gifted you a string r
 consisting only of letters s
 and u
. You can perform the following operation on r
:

Choose an index i
 (1≤i≤|r|
), and set ri
 to s
.
Determine the minimum number of operations needed to make r
 suspicious. It can be shown that, under the given constraints, it is always possible to transform r
 into a suspicious string.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The only line of each test case contains the string r
 (3≤|r|≤2⋅105
). It is guaranteed that ri=s
 or u
.

It is guaranteed that the sum of |r|
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the minimum number of operations needed to make r
 suspicious.

Example
InputCopy
9
sus
uuuu
sssss
uusuuu
suuuuuu
usssssss
sssuuusss
susuusuuus
uuuuuuuuuuu
OutputCopy
0
3
0
3
3
1
1
2
6
Note
In the first test case, the string sus
 is already suspicious because s
 appears twice in the string and the two nearest s
 to the only u
 are both 1
 character away: su––s
.

In the second test case, it is optimal to perform the operation on indices 1
, 3
, and 4
. After that, the string s
 becomes suss
. The string suss
 is suspicious because s
 appears 3
 times in the string and the two nearest s
 to the only u
 are both 1
 character away: su––ss
.

In the third test case, the condition on u
 is vacuously true because there is no u
 in the string sssss
. Thus, the given string is already suspicious.

In the sixth test case, the initial string usssssss
 is not suspicious because the two nearest s
 to the only u
 are one and two characters away, respectively: u––sssssss
.
*/