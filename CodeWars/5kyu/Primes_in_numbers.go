/*
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
Mathematics
*/
// Solution
package kata

import (
	"fmt"
	"strings"
)

func PrimeFactors(n int) string {
	var sb strings.Builder

	for p := 2; p*p <= n; p++ {
		count := 0
		for n%p == 0 {
			n /= p
			count++
		}
		if count > 0 {
			writeFactor(&sb, p, count)
		}
	}
	if n > 1 {
		writeFactor(&sb, n, 1)
	}
	return sb.String()
}

func writeFactor(sb *strings.Builder, p, count int) {
	if count == 1 {
		fmt.Fprintf(sb, "(%d)", p)
	} else {
		fmt.Fprintf(sb, "(%d**%d)", p, count)
	}
}