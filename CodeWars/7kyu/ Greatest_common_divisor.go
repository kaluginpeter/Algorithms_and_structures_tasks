/*
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.

AlgorithmsFundamentalsRecursion
*/
// Solution
package kata

func Gcd(x, y uint32) uint32 {
  if y == 0 { return x }
  return Gcd(y, x % y)
}