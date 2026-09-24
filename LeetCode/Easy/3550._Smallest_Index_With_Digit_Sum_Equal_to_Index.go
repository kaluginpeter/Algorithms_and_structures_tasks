/*
You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.
Example 2:

Input: nums = [1,10,11]

Output: 1

Explanation:

For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
Since index 1 is the smallest, the output is 1.
Example 3:

Input: nums = [1,2,3]

Output: -1

Explanation:

Since no index satisfies the condition, the output is -1.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
*/
// Solution
// Go O(Nlog10(max(N))) O(1) Math
func smallestIndex(nums []int) int {
    for i, num := range nums {
        var acc int = 0
        for num > 0 {
            acc += num % 10;
            num /= 10
        }
        if i == acc { return i }
    }
    return -1
}
// C++ O(Nlog10(max(N))) O(1) Math
class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (size_t i = 0; i < nums.size(); ++i) {
            size_t acc = 0;
            while (nums[i]) {
                acc += nums[i] % 10;
                nums[i] /= 10;
            }
            if (i == acc) return i;
        }
        return -1;
    }
};