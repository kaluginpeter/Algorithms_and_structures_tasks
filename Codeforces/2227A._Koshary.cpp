/*
A. Koshary
time limit per test1 second
memory limit per test256 megabytes
Yousef is at the coordinates (0,0)
 and wants to reach a plate of Koshary at (x,y)
.

To get there, Yousef takes long steps. From any point (a,b)
, a long step moves him to:

(a+2,b)
 or (a,b+2)
However, Yousef is allowed to take at most one short step during his entire journey. A short step moves him to:

(a+1,b)
 or (a,b+1)
Can Yousef reach the exact coordinates (x,y)
 of the Koshary plate?

Input
The first line contains an integer t
 (1≤t≤100
) — the number of test cases.

Each test case contains two integers x
 and y
 (1≤x,y≤10
) — the coordinates of the Koshary plate.

Output
For each test case, output "YES" if Yousef can reach the Koshary plate and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
InputCopy
6
1 1
1 2
4 6
5 9
7 2
10 10
OutputCopy
NO
YES
YES
NO
YES
YES
Note
In the first test case, it is impossible to reach (1,1)
 using the mentioned steps.

In the second test case, an optimal sequence of steps would be:
(0,0)−→−long(0,2)−→−−short(1,2)

In the third test case, an optimal sequence of steps would be:
(0,0)−→−long(0,2)−→−long(2,2)−→−long(2,4)−→−long(4,4)−→−long(4,6)
*/