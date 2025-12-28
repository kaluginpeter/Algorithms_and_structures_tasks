/*
B. Ashmal
time limit per test1 second
memory limit per test256 megabytes

You have an array a
 of n
 strings a1,a2,…,an
, each consisting of lowercase English letters, and an empty string s
.

In the i
-th (1≤i≤n
) step, you should do one of the following:

add ai
 to the beginning of s
, or
add ai
 to the end of s
.
For example, if before the i
-th step s=aba
 and ai=bba
, after the i
-th step, s
 will be equal to ababba
 or bbaaba
.

What's the lexicographically smallest string s
 you can reach after n
 steps?

A string a
 is lexicographically smaller than a string b
 of the same length, if and only if the following holds:

in the first position where a
 and b
 differ, the string a
 has a letter that appears earlier in the alphabet than the corresponding letter in b
.
Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤1000
) — size of array a
. The next line contains n
 strings a1,a2,…,an
 (1≤|ai|≤4000
), each consisting of lowercase English letters.

It is guaranteed that the sum of n
 over all test cases does not exceed 1000
, and the total length of all strings in the input (over all test cases) does not exceed 4000
.

Output
For each test case, print the lexicographically minimum string s
 you can reach after n
 steps.

Example
InputCopy
3
4
amir rima amin nima
1
codeforces
3
a ab abc
OutputCopy
aminamirrimanima
codeforces
aababc
Note
In the first test case, one possible way to construct the lexicographically minimum string s
 is as follows:

After the first step, s=amir
 regardless of whether we add it to the beginning or the end, since s
 was initially empty.
In the second step, we add a2=rima
 to the end of s
. Now s=amirrima
.
In the third step, we add a3=amin
 to the beginning of s
. Now s=aminamirrima
.
In the last step, we add a4=nima
 to the end of s
. Therefore, the final value of s
 is aminamirrimanima
.
It can be proven that this resulting string is indeed the lexicographically smallest string obtainable after all steps.
*/