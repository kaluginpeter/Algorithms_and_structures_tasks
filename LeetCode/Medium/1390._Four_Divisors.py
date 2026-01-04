# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
#
#
#
# Example 1:
#
# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:
#
# Input: nums = [21,21]
# Output: 64
# Example 3:
#
# Input: nums = [1,2,3,4,5]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105
#
# Solution
# Python O(Nsqrt(M)) O(1) Math
class Solution:
    def check(self, num: int) -> int:
        output: int = 1
        divs: int = 0
        tmp: int = num
        while not (num & 1):
            divs += 1
            output += 2**divs
            num >>= 1
        if 2**divs != tmp:
            divs += 1
            output += tmp
        divs += 1
        bound: int = int(num**.5) + 1
        for d in range(3, bound, 2):
            cnt: int = 0
            while num % d == 0:
                cnt += 1
                if d**cnt == tmp: cnt -= 1
                else: output += d**cnt
                num //= d
            divs += cnt
            if divs > 4: return 0
        if num > 2:
            divs += 1
            output += num
        return 0 if divs != 4 else output

    def sumFourDivisors(self, nums: List[int]) -> int:
        output: int = 0
        for num in nums:
            output += self.check(num)
        return output

# C++ O(Nsqrt(M)) O(1) Math
class Solution {
public:
    int check(int num) {
        int output = 1, divs = 0, tmp = num;
        while (!(num & 1)) {
            ++divs;
            output += std::pow(2, divs);
            num >>= 1;
        }
        if (std::pow(2, divs) != tmp) {
            ++divs;
            output += tmp;
        }
        ++divs; // for ones
        int bound = std::sqrt(num) + 1;
        for (int d = 3; d <= bound; d += 2) {
            int cnt = 0;
            while (num % d == 0) {
                ++cnt;
                if (std::pow(d, cnt) == tmp) --cnt;
                else output += std::pow(d, cnt);
                num /= d;
            }
            divs += cnt;
            if (divs > 4) return 0;
        }
        if (num > 2) {
            ++divs;
            output += num;
        }
        return divs == 4 ? output : 0;
    }
    int sumFourDivisors(vector<int>& nums) {
        int output = 0;
        for (int& num : nums) {
            output += check(num);
        }
        return output;
    }
};