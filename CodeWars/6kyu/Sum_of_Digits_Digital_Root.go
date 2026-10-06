/*
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
MathematicsAlgorithms
*/
// Solution
package kata

func f(n int) bool {
  var steps int = 0
  for n > 0 {
    n /= 10
    steps++
  }
  return steps > 1
}

func decompose(n int) int {
  var acc int = 0
  for n > 0 {
    acc += n % 10
    n /= 10
  }
  return acc
}

func DigitalRoot(n int) int {
  for f(n) {
    n = decompose(n)
  }
  return n
}