
/*
Your task is to create a new implementation of modpow so that it computes (x^y)%n for large y. The problem with the current implementation is that the output of Math.pow is so large on our inputs that it won't fit in a 64-bit float.

You're also going to need to be efficient, because we'll be testing some pretty big numbers.

Random tests
MathematicsAlgorithmsPerformance
*/
// Solution

package kata

func ModPow(base, exponent, modulo uint64) uint64 {
	if modulo == 1 {
		return 0
	}
	base %= modulo
	result := uint64(1)
	for exponent > 0 {
		if exponent&1 == 1 {
			result = (result * base) % modulo
		}
		base = (base * base) % modulo
		exponent >>= 1
	}
	return result
}