/*
You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]​​​​​​​
nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
Return true if it is possible to construct such an array, otherwise return false.

 

Example 1:

Input: nums1 = [1,4,7]

Output: true

Explanation:​​​​​​​​​​​​​​

Set nums2[0] = nums1[0] = 1.
Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
Set nums2[2] = nums1[2] = 7.
nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.
Example 2:

Input: nums1 = [2,3]

Output: false

Explanation:

It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

Example 3:

Input: nums1 = [4,6]

Output: true

Explanation:

Set nums2[0] = nums1[0] = 4.
Set nums2[1] = nums1[1] = 6.
nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

Constraints:

1 <= n == nums1.length <= 105
1 <= nums1[i] <= 109
nums1 consists of distinct integers.
*/
// Solution
// Go O(NlogN) O(1) Sorting TwoPointers
func uniformArray(nums1 []int) bool {
    slices.Sort(nums1)
    var odd, left, n int = 0, 0, len(nums1)
    var isEven, isOdd bool = nums1[0] & 1 == 0, nums1[0] & 1 == 1
    for i := 1; i < n; i++ {
        for nums1[i] - nums1[left] >= 1 {
            if (nums1[left] & 1 == 1) {
                odd++
            }
            left++
        }
        if (nums1[i] & 1 == 1) {
            isEven = isEven && odd > 0
        } else {
            isOdd = isOdd && odd > 0
        }
    }
    return isEven || isOdd
}

// C++ O(NlogN) O(1) Sorting TwoPointers
class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        std::sort(nums1.begin(), nums1.end());
        size_t odd = 0, left = 0, n = nums1.size();
        bool isOdd = nums1[0] & 1, isEven = nums1[0] % 2 == 0;
        for (size_t i = 1; i < n; ++i) {
            while (nums1[i] - nums1[left] >= 1) {
                if (nums1[left] & 1) ++odd;
                ++left;
            }
            if (nums1[i] & 1) { // cur number is odd
                isEven &= odd > 0;
            } else { // cur number is even
                isOdd &= odd > 0;
            }
        }
        return isOdd || isEven;
    }
};