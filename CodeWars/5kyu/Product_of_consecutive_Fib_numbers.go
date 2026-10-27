/*
The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that:

F
(
0
)
=
0
F
(
1
)
=
1
F
(
n
)
=
F
(
n
−
1
)
+
F
(
n
−
2
)
F(0)=0
F(1)=1
F(n)=F(n−1)+F(n−2)
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:

F
(
n
)
∗
F
(
n
+
1
)
=
p
r
o
d
F(n)∗F(n+1)=prod
Your function takes an integer (prod) and returns an array/tuple (check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:
(F(n), F(n+1), true)
If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:
(F(n), F(n+1), false)
where F(n) is the smallest one such as F(n) * F(n+1) > prod.
Examples:
714 ---> (21, 34, true)
--> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

800 --->  (34, 55, false)
--> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
AlgorithmsMathematics
*/
// Solution
package kata

var f[]uint64 = []uint64{0, 1}

func ProductFib(prod uint64) [3]uint64 {
  for f[len(f) - 2] * f[len(f) - 1] < prod {
    f = append(f, f[len(f) - 2] + f[len(f) - 1])
  }
  var left, right int = 0, len(f) - 2
  for left <= right {
    var middle int = left + ((right - left) >> 1)
    if f[middle] * f[middle + 1] == prod {
      return [3]uint64{f[middle], f[middle + 1], 1}
    } else if f[middle] * f[middle + 1] > prod {
      right = middle - 1
    } else { left = middle + 1}
  }
  return [3]uint64{f[left], f[left + 1], 0}
}