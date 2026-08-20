/*
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
AlgebraFundamentals
*/
// Solution
package kata

import "math"

func FindNextSquare(sq int64) int64 {
	root := int64(math.Sqrt(float64(sq)))
	for root*root > sq {
		root--
	}
	for (root+1)*(root+1) <= sq {
		root++
	}
	if root*root != sq {
		return -1
	}
	return (root + 1) * (root + 1)
}