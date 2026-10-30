/*
This kata is the part two version of the Find X kata, if you haven't solved it you should try solving it, it's pretty easy.

In this version you're given the following function

func FindX(n int) int {
  if n == 0 {
    return 0
  }
  x := 0
  for i:=1; i<=n; i++ {
    x += FindX(i-1) + 3*i
  }
  return x
}
Since this computation is exponential, it gets very slow quickly as n increases, your task is to optimize the function so it works well for large numbers.

FindX(2) //=> 12
FindX(3) //=> 33
FindX(5) //=> 171
The result gets pretty large even for small inputs, so you should return the result % (109+7)

Input Range
1 <= n <= 106

FundamentalsPerformance
*/