# Given an array of integers arr, return the number of subarrays with an odd sum.
#
# Since the answer can be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
# Example 2:
#
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
# Example 3:
#
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
#
#
# Constraints:
#
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 100
# Solution
# Python O(N) O(1) Math DynamicProgramming
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD: int = 1000000007
        output: int = 0
        prefix_sum: int = 0
        odd_subs: int = 0
        even_subs: int = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum & 1:
                output = (output % MOD + (even_subs + 1) % MOD) % MOD
                odd_subs += 1
            else:
                output = (output % MOD + odd_subs % MOD) % MOD
                even_subs += 1
        return output

# C++ O(N) O(1) Math DynamicProgramming
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int MOD = 1000000007;
        int prefixSum = 0;
        int evenSubs = 0;
        int oddSubs = 0;
        int output = 0;
        for (int i = 0; i < arr.size(); ++i) {
            prefixSum += arr[i];
            if (prefixSum % 2 != 0) {
                output = (output % MOD + (evenSubs + 1) % MOD) % MOD;
                ++oddSubs;
            } else {
                output = (output % MOD + oddSubs % MOD) % MOD;
                ++evenSubs;
            }

        }
        return output;
    }
};


# Go O(N) O(1) DynamicProgramming Math
func numOfSubarrays(arr []int) int {
    var dp [2]int = [2]int{0, 0}
    var output, mod int = 0, 1000000007
    for _, num := range arr {
        if num & 1 == 1 { // current number is odd
            output = (output + dp[0] + 1) % mod
            var newDp0 int = dp[1] % mod
            dp[1] = (dp[0] + 1) % mod
            dp[0] = newDp0
        } else { // current number is even
            output = (output + dp[1]) % mod
            dp[0] = (dp[0] + 1) % mod
        }
    }
    return output
}


// The length of the array is the 10^5
// So we need to find a soluton less than or equal to O(NlogN)

// Let's notice that the numbers by itself is in range from 1 to 100
// How that fact can help us?

// Generally, we don't care about the exact subarray sum,
// but more about parity of that sum

// Since we need to return answer by module, it means
// that the overall number of subarrays will be greater than 10^9
// which means that we cannot just to count all the subarrays
// This leads us to some kind of combinatorial approach

// The combinatorial approach can be resolved through dynamic programming
// So what is the state of dp?

// Since we don't care about the exact sum, let's consider
// all previous subarray subs my module 2, just as '0' and '1'

// So then i'th element will be the "end" of current window
// Then we use some module arithmetic
// And the answer will be the sum of all 0 <= i < n computations

// Time complexity is O(N)
// Memory complexity is O(1)