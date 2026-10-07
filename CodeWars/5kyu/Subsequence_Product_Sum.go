/*
Given an array of integers and an integer m, return the sum of the product of its subsequences of length m.

Ex1:

a := []int{1, 2, 3}
m := 2
the subsequences (of length 2) are (1,2) (1,3) (2,3), you should multiply the numbers of each subsequence and take their sum

ProductSum = (1*2) + (1*3) + (2*3) //=> 11
Ex2:

a := []int{2,3,4,5}
m := 3
the subsequences (of length 3) are (2,3,4) (2,4,5) (2,3,5) (3,4,5)

ProductSum = (2*3*4) + (2*3*5) + (2*4*5) + (3*4*5) //=> 154
Task:
Write a function `productSum(a, m)`` that does as described above

The sum can be really large, so return the result in modulo 109+7

Constraints
0 <= A[i] < 1000000

1 <= m <= 50
99 random tests |A| = 10^5
1 big test |A| = 10^6
m < |A|

CombinatoricsPerformanceDynamic ProgrammingFundamentals
*/
// Solution
package kata

const mod = 1_000_000_007

func ProductSum(a []int, m int) int {
	dp := make([]int, m+1)
	dp[0] = 1

	for _, x := range a {
		x %= mod
		for j := m; j >= 1; j-- {
			dp[j] = (dp[j] + dp[j-1]*x) % mod
		}
	}
	return dp[m]
}