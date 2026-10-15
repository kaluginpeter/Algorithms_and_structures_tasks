/*
The number six has this interesting property, and is the smallest number in having it (after the integer 1 that obviously fulfills this condition): Its cube, is divisible by the sum of its divisors. Let's see it:

6 ^ 3 = 216
divisors of 6: 1, 2, 3, 6
sum of its divisors= 1 + 2 + 3 + 6 = 12
And 216 / 12 = 18 (integer) and 18.12 = 216
The first terms of this sequence are:

n    a(n)
1       6 
2      28
3      30
4      84
5     102
Your challenge is to create a function that receives an ordinal number n of the term of the sequence as an argument, and returns the nth term of that sequece of integers.

Let's see some cases (input ------> output):

4 ------> 84
/// divisors of 84 : 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84
    sum of divisors = 1 + 2 + 3 + 4 + 6 + 7 + 12 + 14 + 21 + 28 + 42 + 84 = 224
    cube of 84 = 84^3 = 592704
    592704 is a multiple of 224///

5 ------> 102
Your code should use memoization in order to have higher speed for testing. Does your code reach up to the 120-th term? We can get this upper limit in the tests.

Enjoy it and happy coding!!

AlgorithmsMathematicsMemoizationDynamic Programming
*/
// Solution
package kata

var seq []int 
var limit = 1
func grow() {
	newLimit := limit * 2
	if newLimit < 1024 {
		newLimit = 1024
	}
	sigma := make([]int, newLimit+1)
	for d := 1; d <= newLimit; d++ {
		for m := d; m <= newLimit; m += d {
			sigma[m] += d
		}
	}
	for x := limit + 1; x <= newLimit; x++ {
		if x == 1 {
			continue
		}
		s := sigma[x]
		r := x % s
		if r*r%s*r%s == 0 {
			seq = append(seq, x)
		}
	}
	limit = newLimit
}

func IntCubeSumDiv(n int) int {
	for len(seq) < n {
		grow()
	}
	return seq[n-1]
}