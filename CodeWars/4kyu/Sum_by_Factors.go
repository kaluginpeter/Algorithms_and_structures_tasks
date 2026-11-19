/*
Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = (/12, 15/); // result = "(2 12)(3 27)(5 15)"
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
ArraysAlgorithmsMathematics
*/
// Solution
package kata

import (
	"fmt"
	"sort"
	"strings"
)

func SumOfDivided(lst []int) string {
	sums := make(map[int]int)

	for _, num := range lst {
		x := num
		if x < 0 {
			x = -x
		}
		for p := 2; p*p <= x; p++ {
			if x%p == 0 {
				sums[p] += num
				for x%p == 0 {
					x /= p
				}
			}
		}
		if x > 1 {
			sums[x] += num
		}
	}

	primes := make([]int, 0, len(sums))
	for p := range sums {
		primes = append(primes, p)
	}
	sort.Ints(primes)

	var sb strings.Builder
	for _, p := range primes {
		fmt.Fprintf(&sb, "(%d %d)", p, sums[p])
	}
	return sb.String()
}