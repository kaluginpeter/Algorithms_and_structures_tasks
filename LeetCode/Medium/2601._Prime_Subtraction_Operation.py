# You are given a 0-indexed integer array nums of length n.
#
# You can perform the following operation as many times as you want:
#
# Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
#
# A strictly increasing array is an array whose each element is strictly greater than its preceding element.
#
#
#
# Example 1:
#
# Input: nums = [4,9,6,10]
# Output: true
# Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
# In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
# After the second operation, nums is sorted in strictly increasing order, so the answer is true.
# Example 2:
#
# Input: nums = [6,8,11,12]
# Output: true
# Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
# Example 3:
#
# Input: nums = [5,8,3]
# Output: false
# Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# nums.length == n
# Solution
# Python O(NlogM) O(N) Math Binary Search
class Solution:
    def get_primes(self, nums: list[int]) -> list[int]:
        max_el: int = max(nums)
        sieve: list[int] = [1] * (max_el + 1)
        sieve[1] = 0
        for num in range(2, int(sqrt(max_el + 1)) + 1):
            if sieve[num]:
                for mod in range(num * num, max_el + 1, num):
                    sieve[mod] = 0
        primes: list[int] = []
        for prime in range(2, max_el + 1):
            if sieve[prime]:
                primes.append(prime)
        return primes

    def binary_search(self, primes: list[int], diff: int, upper_bound: int) -> int:
        left: int = 0
        right: int = len(primes) - 1
        while left <= right:
            middle: int = left + (right - left) // 2
            if primes[middle] >= diff or primes[middle] >= upper_bound:
                right = middle - 1
            else:
                left = middle + 1
        if right + 1 == len(primes) or primes[right + 1] >= upper_bound:
            return -1
        return primes[right + 1]

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes: list[int] = self.get_primes(nums)
        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx] <= nums[idx - 1]:
                diff: int = nums[idx - 1] - nums[idx] + 1
                prime: int = self.binary_search(primes, diff, nums[idx - 1])
                if prime < diff:
                    return False
                nums[idx - 1] -= prime
        return True

# C++ O(NlogM) O(N) Math BinarySearch
class Solution {
public:
    std::vector<int> getPrimes(std::vector<int>& nums) {
        int maxElement = *max_element(nums.begin(), nums.end());
        vector<int> sieve(maxElement + 1, 1);
        sieve[1] = 0;
        for (int i = 2; i <= sqrt(maxElement + 1); i++) {
            if (sieve[i] == 1) {
                for (int j = i * i; j <= maxElement; j += i) {
                    sieve[j] = 0;
                }
            }
        }
        std::vector<int> primes;
        for (int prime = 0; prime < maxElement + 1; ++prime) {
            if (sieve[prime]) {
                primes.push_back(prime);
            }
        }
        return primes;
    }

    int binarySearch(std::vector<int> primes, int diff, int upperBound) {
        int left = 0;
        int right = primes.size() - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (primes[middle] >= diff || primes[middle] >= upperBound) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        if (right + 1 == primes.size() || primes[right + 1] >= upperBound) {
            return -1;
        }
        return primes[right + 1];
    }

    bool primeSubOperation(vector<int>& nums) {
        std::vector<int> primes = getPrimes(nums);
        for (int index = nums.size() - 1; index >= 1; --index) {
            if (nums[index] <= nums[index - 1]) {
                int diff = nums[index - 1] - nums[index] + 1;
                int prime = binarySearch(primes, diff, nums[index - 1]);
                if (prime < diff) {
                    return false;
                }
                nums[index - 1] -= prime;
            }
        }
        return true;
    }
};