/*
This is the SUPER performance version of This kata.

You task is exactly the same as that kata. But this time, you should output result % 998244353, or otherwise the result would be too large.

Data range
sometimes
  n <= 80000
  m <= 100000
while sometimes
  n <= 3000
  m <= 2^200
There are 150 random tests. You will need more than just a naive linear algorithm for this task :D

PerformanceAlgorithmsMathematics
*/
// Solution
package kata

import "math/big"

const MOD int64 = 998244353

func normalizeMod(x int64) int64 {
	x %= MOD
	if x < 0 { x += MOD }
	return x
}

func Height(n, m *big.Int) int64 {
	nInt := int(n.Int64())
	mReduced := new(big.Int).Mod(m, big.NewInt(MOD))
	mVal := mReduced.Int64()
	inv := make([]int64, nInt+1)
	var prev, output int64 = 1, 0
	for i := 1; i <= nInt; i++ {
		ii := int64(i)
		if i > 1 {
			inv[i] = normalizeMod(-(MOD/ii)*inv[MOD%ii])
		} else { inv[i] = 1 }
		term := normalizeMod(mVal - ii + 1)
		prev = normalizeMod(prev * term)
		prev = normalizeMod(prev * inv[i])
		output = normalizeMod(output + prev)
	}
	return output
}