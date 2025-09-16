# You are given a 0-indexed integer array nums of length n.
#
# A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.
#
# For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
# Return the smallest index i at which the array can be split validly or -1 if there is no such split.
#
# Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.
#
#
#
# Example 1:
#
#
# Input: nums = [4,7,8,15,3,5]
# Output: 2
# Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
# The only valid split is at index 2.
# Example 2:
#
#
# Input: nums = [4,7,15,8,3,5]
# Output: -1
# Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
# There is no valid split.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 104
# 1 <= nums[i] <= 106
# Solution
# NumberTheory
# Numbers aren't co-prime if they share common prime in their prime factorization
# Python O(Nsqrt(max(nums))) O(D) HashMap Math NumberTheory
class Solution:
    def factorize_prime(self, x: int) -> list[int]:
        output: list[int] = []
        while not (x & 1):
            output.append(2)
            x >>= 1
        bound: int = int(x**.5) + 1
        for d in range(3, bound, 2):
            while x % d == 0:
                output.append(d)
                x //= d
        if x > 1: output.append(x)
        return output

    def add_primes(self, primes: list[int], chunk: dict[int, int]) -> None:
        for prime in primes:
            chunk[prime] += 1

    def subtract_primes(self, primes: list[int], chunk: dict[int, int]) -> None:
        for prime in primes:
            chunk[prime] -= 1
            if not chunk[prime]: del chunk[prime]

    def is_co_prime(self, x: dict[int, int], y: dict[int, int]) -> bool:
        return all(prime not in y for prime in x.keys())

    def findValidSplit(self, nums: List[int]) -> int:
        factorization: dict[int, list[int]] = dict()
        prefix: dict[int, int] = defaultdict(int)
        suffix: dict[int, int] = defaultdict(int)
        n: int = len(nums)
        for i in range(n):
            if nums[i] not in factorization:
                primes: list[int] = self.factorize_prime(nums[i])
                factorization[nums[i]] = primes
            self.add_primes(factorization[nums[i]], suffix)
        for i in range(n - 1):
            self.add_primes(factorization[nums[i]], prefix)
            self.subtract_primes(factorization[nums[i]], suffix)
            if self.is_co_prime(prefix, suffix): return i
        return -1

# C++ O(Nsqrt(max(nums))) O(D) HashMap Math NumberTheory
class Solution {
private:
    std::vector<int> factorizePrime(int x) {
        std::vector<int> output = {};
        while (!(x & 1)) {
            output.push_back(2);
            x >>= 1;
        }
        int bound = std::sqrt(x) + 1;
        for (int d = 3; d < bound; d += 2) {
            while (x % d == 0) {
                output.push_back(d);
                x /= d;
            }
        }
        if (x > 1) output.push_back(x);
        return output;
    };
    void addFactors(std::vector<int>& primes, std::unordered_map<int, int>& chunk) {
        for (const int& prime : primes) ++chunk[prime];
    };
    void subtractFactors(std::vector<int>& primes, std::unordered_map<int, int>& chunk) {
        for (const int& prime : primes) {
            --chunk[prime];
            if (!chunk[prime]) chunk.erase(prime);
        }
    };
    bool isCoPrime(std::unordered_map<int, int>& x, std::unordered_map<int, int>& y) {
        for (const auto& p : x) {
            if (y.count(p.first)) return false;
        }
        return true;
    };
public:
    int findValidSplit(vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> factorization;
        std::unordered_map<int, int> prefix, suffix;
        size_t n = nums.size();
        for (size_t i = 0; i < n; ++i) {
            if (!factorization.count(nums[i])) factorization[nums[i]] = factorizePrime(nums[i]);
            addFactors(factorization[nums[i]], suffix);
        }
        for (size_t i = 0; i < n - 1; ++i) {
            addFactors(factorization[nums[i]], prefix);
            subtractFactors(factorization[nums[i]], suffix);
            if (isCoPrime(prefix, suffix)) return static_cast<int>(i);
        }
        return -1;
    }
};