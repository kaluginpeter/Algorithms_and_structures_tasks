# You are given an array of integers nums. Perform the following steps:
#
# Find any two adjacent numbers in nums that are non-coprime.
# If no such numbers are found, stop the process.
# Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
# Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.
#
# The test cases are generated such that the values in the final array are less than or equal to 108.
#
# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
#
#
#
# Example 1:
#
# Input: nums = [6,4,3,2,7,6,2]
# Output: [12,7,6]
# Explanation:
# - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
# - (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
# - (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
# - (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [12,7,6].
# Note that there are other ways to obtain the same resultant array.
# Example 2:
#
# Input: nums = [2,2,1,1,3,3,3]
# Output: [2,1,1,3]
# Explanation:
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
# - (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [2,1,1,3].
# Note that there are other ways to obtain the same resultant array.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# The test cases are generated such that the values in the final array are less than or equal to 108.
# Solution
# Python O(NlogN) O(N) Math Stack
class Solution:
    def gcd(self, x: int, y: int) -> int:
        if not x: return y
        return self.gcd(y % x, x)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        output: list[int] = []
        for num in nums:
            output.append(num)
            while len(output) > 1 and (gcd_ := self.gcd(output[-2], output[-1])) > 1:
                output.append(output.pop() * output.pop() // gcd_)
        return output

# C++ O(NlogN) O(N) Math Stack
class Solution {
public:
    int gcd(int x, int y) {
        if (!x) return y;
        return gcd(y % x, x);
    }
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        std::vector<int> output;
        for (const int& num : nums) {
            output.push_back(num);
            while (output.size() > 1 && gcd(output.back(), output[output.size() - 2]) > 1) {
                int lcm = static_cast<long long>(output.back()) * output[output.size() - 2] / gcd(output.back(), output[output.size() - 2]);
                output.pop_back();
                output.pop_back();
                output.push_back(lcm);
            }
        }
        return output;
    }
};