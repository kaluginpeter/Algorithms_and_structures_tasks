/*
You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

Partition nums into consecutive subarrays of length k.
Cyclically rotate each subarray independently any number of times to the left or to the right.
Return an integer denoting the sum of all possible sortable integers k.

 

Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:​​​​​​​

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
Only k = 3 is sortable. Hence, the answer is 3.
Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
No k is sortable. Hence, the answer is 0.
Example 3:

Input: nums = [5,8]

Output: 3

Explanation:​​​​​​​

For n = 2, possible divisors are 1 and 2.
Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 105
 

*/
// Solution
// Go O(Nsqrt(N)) O(1) Math
import "math"

func check(nums []int, target int) bool {
    var leftMx int = 0
    var start int = 0
    for start < len(nums) {
        var rightMx, rightMn int = 0, 1e5
        var inValid int = 0
        for i := start; i < start + target; i++ {
            rightMx = max(rightMx, nums[i])
            rightMn = min(rightMn, nums[i])
            if (i - 1 >= start) && (nums[i - 1] > nums[i]) {
                inValid++
                if inValid > 1 { return false }
                for j := i; j < i + target - 1; j++ {
                    if nums[start + (j % target)] > nums[start + ((j + 1) % target)] {
                        return false
                    }
                }
            }
        }
        if leftMx > rightMn { return false }
        leftMx = rightMx
        start += target
    }
    return true
}

func sortableIntegers(nums []int) int {
    var n, output int = len(nums), 0
    var bound int = int(math.Sqrt(float64(n)) + 1)
    for i := 1; i < bound; i++ {
        if n % i != 0 { continue }
        if check(nums, i) { output += i }
        if n / i != i && check(nums, n / i) { output += n / i }
    }
    return output
}