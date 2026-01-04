/*
A. Yes or Yes
time limit per test1 second
memory limit per test256 megabytes

Last Christmas, your friend Fernando gifted you a string s
 consisting only of the characters Y
 and N
, representing "Yes" and "No", respectively.

You can repeatedly apply the following operation on s
:

Choose any two adjacent characters and replace them with their logical OR.
Formally, in each operation, you can choose an index i
 (1≤i≤|s|−1
), remove the characters si
 and si+1
, then insert:

A single Y
 if at least one of si
 or si+1
 is Y
;
A single N
 if both si
 and si+1
 are N
.
Note that after each operation, the length of s
 decreases by 1
.

Unfortunately, Fernando does not want you to combine "Yes OR Yes", as he has experienced trauma relating to a certain song.

Determine whether it is possible to reduce s
 to a single character by repeatedly applying the operation above, without ever combining two Y
's.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The only line of each test case contains the string s
 (2≤|s|≤100
). It is guaranteed that si=Y
 or N
.

Output
For each test case, print "YES" if the string can be reduced to a single character by repeatedly applying the described operation, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
InputCopy
7
YY
NN
NNY
YYYNY
NNNNN
YYYYYY
YNNNNN
OutputCopy
NO
YES
YES
NO
YES
NO
YES
Note
In the first test case, you cannot combine s1
 and s2
 since they are both Y
. Thus, the answer is NO.

In the third test case, the following is a valid sequence of operations: NN–––Y→NY–––→Y
. Thus, the answer is YES.

In the fourth test case, there are two possibilities for the first operation: YYYN–––Y→YYYY
 or YYYNY–––→YYYY
. However, in either case, it is not possible to perform any more operations without combining two Y
's. Thus, the answer is NO.

In the fifth test case, the following is a valid sequence of operations: NNN–––NN→NN–––NN→NNN–––→NN–––→N
. Thus, the answer is YES.
*/