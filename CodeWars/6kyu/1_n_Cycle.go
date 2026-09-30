/*
Let n be an integer coprime with 10, e.g. 7.

1/7 = 0.142857 142857 142857 ....

We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:

1/11 = 0.09 09 09 .... Cycle length is 2.

Task
Given an integer n (n > 1), write a function that returns the length of the cycle if there is one, otherwise (if n and 10 not coprimes) return -1.

Examples
n = 5  --> Should return -1
n = 13 --> Should return 6 -> 0.076923 076923 076923 ...
n = 21 --> Should return 6 -> 0.047619 047619 047619 ...
n = 27 --> Should return 3 -> 0.037 037 037 037 037 037 ...
n = 33 --> Should return 2 -> 0.03 03 03 03 03 03 03 03 ...
n = 37 --> Should return 3 -> 0.027 027 027 027 027 027 ...
n = 94 --> Should return -1 
Notes
n = 22 --> Should return -1 since 1/22 ~ 0.0 45 45 45 45 ...
Please ask before translating..
FundamentalsMathematics
*/
// Solution
package kata

import "sort"

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func totient(n int) int {
	result := n
	p := 2
	for p*p <= n {
		if n%p == 0 {
			for n%p == 0 {
				n /= p
			}
			result -= result / p
		}
		p++
	}
	if n > 1 {
		result -= result / n
	}
	return result
}

func modPow(base, exponent, modulus int) int {
	result := 1
	base %= modulus
	for exponent > 0 {
		if exponent%2 == 1 {
			result = (result * base) % modulus
		}
		base = (base * base) % modulus
		exponent /= 2
	}
	return result
}

func divisors(n int) []int {
	var divs []int
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			divs = append(divs, i)
			if i != n/i {
				divs = append(divs, n/i)
			}
		}
	}
	sort.Ints(divs)
	return divs
}

func Cycle(n int) int {
	if gcd(n, 10) != 1 {
		return -1
	}

	phiN := totient(n)
	for _, k := range divisors(phiN) {
		if modPow(10, k, n) == 1 {
			return k
		}
	}
	return 0
}