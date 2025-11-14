/*
A. Alice and Bob
time limit per test2 seconds
memory limit per test512 megabytes
Alice and Bob have a bag with n
 marbles, with the integer vi
 written on the i
-th marble. They play the following game: first, each player chooses an integer (let's denote the integer chosen by Alice as a
, and the integer chosen by Bob as b
). After that, they start drawing marbles from the bag in any order until the bag is empty. For each ball, the point goes to the one whose chosen integer is closer to the integer on the marble; in case of a tie, Alice gets the point.

For example, if a=10
, b=30
, then

for marbles with integers 10,1,7,18,20
, and many others, Alice gets the points (note that she will get a point for the marble 20
);
for marble with integer 59,25,30,21
, and many others, Bob gets the points.
Bob has managed to find out in advance which integer Alice will choose. Help him to choose his integer in such a way as to maximize the number of points he receives.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

Each test case consists of two lines:

The first line contains two integers n
 and a
 (1≤n≤3⋅105
; 1≤a≤109
) — the number of marbles in the bag and the number chosen by Alice, respectively.
The second line contains n
 integers v1,v2,…,vn
 (1≤v1≤v2≤⋯≤vn≤109
).
Additional constraint on the input: the sum of n
 across all test cases does not exceed 3⋅105
.

Output
For each test case, output a single integer b
 (0≤b≤2⋅109
) that Bob should choose to maximize the number of points he receives. If there are multiple such numbers, you may output any of them.

Example
InputCopy
3
7 21
10 20 30 40 50 60 70
6 500
200 200 300 500 600 600
2 7
7 7
OutputCopy
35
333
1337
Note
In the first test case, if Bob chooses 35
, he gets 5
 points for marbles 30,40,50,60,70
.

In the third test case, no matter which integer Bob chooses, he gets 0
 points.
*/