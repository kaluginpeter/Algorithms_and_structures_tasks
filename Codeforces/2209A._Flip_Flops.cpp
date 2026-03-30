/*
A. Flip Flops
time limit per test1 second
memory limit per test256 megabytes
OtterZ set up a battle with n
 monsters in order to increase his combat power. Each monster has a combat power ai
 and OtterZ has a combat power of c
. He has k
 flip flops and can perform the following operations:

Kill an alive monster i
 if ai≤c
; then c
 becomes c+ai
.
Throw a flip flop at an alive monster i
; the flip-flop will be broken and the monster will become angrier, then ai
 becomes ai+1
.
Help OtterZ obtain the maximum possible c
 after the battle.
Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains three integers n
, c
 and k
 (1≤n≤100
, 0≤c,k≤109
).

The second line contains n
 integers a1,a2,…,an
 (0≤ai≤109
).

Output
For each test case, output an integer — the maximum possible combat power.

Example
InputCopy
10
1 12 23
21
1 8 4
5
1 3 4
16
3 6 3
14 9 11
5 9 2
20 16 18 16 11
5 18 30
1 2 93 84 2
7 29 13
2 9 38 4 7 1 6
10 9 2
8 1 8 11 17 3 14 16 20 10
10 192 109
1 9 20 9 829 3 87 1 283 7
10 1000000000 1000000000
19 1000000000 1 9 2 3 8 1 2 3
OutputCopy
12
16
3
6
9
53
109
119
721
3000000048
Note
In the first test,OtterZ found a strong monster and ran away, with combat power 12
.

In the sixth test, OtterZ participated in the battle:

Throw 10
 flip flops to monster 2
, the combat power of monster 2
 turns to 12
.
Throw 10
 flip flops to monster 1
, the combat power of monster 1
 turns to 11
.
Kill monster 1
, OtterZ's combat power turns to 29
.
Throw 10
 flip flops to monster 5
, the combat power of monster 5
 turns to 12
.
Kill monster 2
, OtterZ's combat power turns to 41
.
Kill monster 5
, OtterZ's combat power turns to 53
.
OtterZ runs away with combat power 53
.
*/