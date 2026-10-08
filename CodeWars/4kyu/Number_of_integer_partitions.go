/*
An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
Write a function which returns the number of integer partitions of n. The function should be able to find the number of integer partitions of n for n at least as large as 100.

MathematicsAlgorithmsDiscrete Mathematics
*/
// Solution
package kata

func Partitions(n int) int {
	dp := make([]int, n + 1)
  dp[0] = 1
  for k := 1; k <= n; k++ {
      for s := k; s <= n; s++ {
          dp[s] += dp[s - k]
      }
  }
  return dp[n]
}