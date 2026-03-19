/*
In front of you, there are
n
n piles of
$
1
$1 bills.

Your assistant will perform the following operations until one of the piles is empty:

Calculate the greatest common divisor of the amounts of money in the piles.
Take out that amount of bills from each pile and give them to you.
You want to know: When one of the piles is emptied, how much money have you received in total?

Write a function calc which will return the total money you have received at the end of all operations.

You will be given an array of size
n
n, the number of
$
1
$1 bills in each pile.

Examples
calc([1, 2, 3, 4, 5]) = 5
calc([3, 4]) = 6
C
o
n
s
t
r
a
i
n
t
s
Constraints

1
≤
n
≤
1
0
6
1≤n≤10
6

let
x
x denote the biggest number in the array,
x
≤
1
0
9
x≤10
9

all of the numbers in the array are postive integers
Fundamentals
*/