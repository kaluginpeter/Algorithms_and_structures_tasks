/*
B. New Year Cake
time limit per test2 seconds
memory limit per test512 megabytes
Monocarp is going to bake a New Year cake.

The cake must consist of at least one layer. The size of the top layer of the cake must be 1
; the size of the layer below it must be 2
; the layer below that must be 4
, and so on (each layer, except for the top one, is twice the size of the layer above it).

Additionally, each layer must be covered with either white or dark chocolate. To cover a layer of size k
, Monocarp will need k
 kilograms of chocolate. Each layer must be covered with exactly one type of chocolate, and these types must alternate (if some layer is covered with dark chocolate, both the layer directly below it and the layer directly above it must be covered with white chocolate, and vice versa).

Monocarp has a
 kilograms of white chocolate and b
 kilograms of dark chocolate. He wants to calculate the maximum number of layers that the cake can consist of, ensuring that he has enough chocolate of both types.

Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases.

Each test case consists of one line containing two integers a
 and b
 (1≤a,b≤106
).

Output
For each test case, output one integer — the maximum possible number of layers in the cake.

Example
InputCopy
7
1 1
1 2
3 1
4 3
5 2
1000000 1000000
1000000 1
OutputCopy
1
2
2
2
3
20
2
Note
In the first example, Monocarp can bake a cake with one layer of size 1
 and cover it with any type of chocolate.

In the second example, Monocarp can bake a cake with two layers: the top layer of size 1
 with white chocolate, and below it a layer of size 2
 with dark chocolate.

In the third example, Monocarp can bake a cake with two layers: the top layer of size 1
 with dark chocolate, and below it a layer of size 2
 with white chocolate.

In the fourth example, Monocarp can bake a cake with two layers: the top layer of size 1
 with dark chocolate, and below it a layer of size 2
 with white chocolate. Note that a cake with three layers, where the top layer of size 1
 and the layer below it of size 2
 are both dark chocolate, and the bottom layer of size 4
 is white chocolate, is not valid, as the types of layers must alternate.
*/