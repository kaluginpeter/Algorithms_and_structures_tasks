# You are given an array nums of n positive integers and an integer k.
#
# Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:
#
# Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
# Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
# Multiply your score by x.
# Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.
#
# The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.
#
# Return the maximum possible score after applying at most k operations.
#
# Since the answer may be large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: nums = [8,3,9,3,8], k = 2
# Output: 81
# Explanation: To get a score of 81, we can apply the following operations:
# - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
# - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
# It can be proven that 81 is the highest score one can obtain.
# Example 2:
#
# Input: nums = [19,12,14,6,10,18], k = 3
# Output: 4788
# Explanation: To get a score of 4788, we can apply the following operations:
# - Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
# - Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
# - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
# It can be proven that 4788 is the highest score one can obtain.
#
#
# Constraints:
#
# 1 <= nums.length == n <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= min(n * (n + 1) / 2, 109)
# Solution
# Python O(Nsqrt(M) + N + NlogN + NlogK) O(N) Monotonic Stack Greedy Number Theory Math
class Solution:
    MOD: int = 1000000007

    def get_prime_factor(self, x: int) -> int:
        primes: set[int] = set()
        while not (x & 1):
            primes.add(2)
            x //= 2
        bound: int = int(x ** .5) + 1
        for p in range(3, bound, 2):
            while x % p == 0:
                primes.add(p)
                x //= p
        if x > 2: primes.add(x)
        return len(primes)

    def fast_pow(self, base: int, exponent: int, module: int) -> int:
        result: int = 1
        while exponent:
            if exponent & 1:
                result = result * base % module
            base = base * base % module
            exponent //= 2
        return result

    def get_score(self, score: int, number: int, amount: int) -> int:
        exponent_number: int = self.fast_pow(number, amount, self.MOD)
        return score * exponent_number % self.MOD

    def maximumScore(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        prime_factor: list[int] = [0] * n
        for idx in range(n):
            prime_factor[idx] = self.get_prime_factor(nums[idx])
        left: list[int] = [-1] * n
        right: list[int] = [n] * n
        stack: list[int] = []
        for idx in range(n):  # Lestmost that greater
            while stack and prime_factor[stack[-1]] < prime_factor[idx]:
                stack.pop()
            if stack: left[idx] = stack[-1]
            stack.append(idx)
        stack.clear()
        for idx in range(n - 1, -1, -1):  # Rightmost greater
            while stack and prime_factor[stack[-1]] <= prime_factor[idx]:
                stack.pop()
            if stack: right[idx] = stack[-1]
            stack.append(idx)
        comb: list[tuple[int, int]] = []
        for idx in range(n):
            r: int = right[idx] - idx
            comb.append((nums[idx], (idx - left[idx] - 1) * r + r))
        comb.sort()
        score: int = 1
        for idx in range(n - 1, -1, -1):
            diff: int = min(k, comb[idx][1])
            k -= diff
            score = self.get_score(score, comb[idx][0], diff)
            if not k: break
        return score

# C++ O(Nsqrt(M) + N + NlogN + NlogK) O(N) Math NumberTheory MonotonicStack Greedy Sorting
const int MOD = 1000000007;

class Solution {
public:
    int getDistinctPrimeFact(int x) {
        unordered_set<int> fact;
        while (x % 2 == 0) {
            fact.insert(2);
            x /= 2;
        }
        int bound = (int)sqrt((double)x) + 1;
        for (int p = 3; p < bound; p += 2) {
            while (x % p == 0) {
                fact.insert(p);
                x /= p;
            }
        }
        if (x > 2) fact.insert(x);
        return static_cast<int>(fact.size());
    }

    long long fast_pow(long long base, long long exponent, long long mod) {
        long long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exponent /= 2;
        }
        return result;
    }

    long long computeResult(long long start, long long amount, long long number) {
        long long pow_result = fast_pow(number, amount, MOD);
        return (start * pow_result) % MOD;
    }

    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> primeFactor (n, 0);
        for (int idx = 0; idx < n; ++idx) {
            primeFactor[idx] = getDistinctPrimeFact(nums[idx]);
        }

        vector<int> left(n, -1), right(n, n);
        stack<int> st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && primeFactor[st.top()] < primeFactor[i]) {
                st.pop();
            }
            if (!st.empty()) {
                left[i] = st.top();
            }
            st.push(i);
        }
        while (!st.empty()) st.pop();
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && primeFactor[st.top()] <= primeFactor[i]) {
                st.pop();
            }
            if (!st.empty()) {
                right[i] = st.top();
            }
            st.push(i);
        }
        vector<pair<int, long long>> comb;
        for (int i = 0; i < n; ++i) {
            long long r = right[i] - i;
            comb.push_back({nums[i], r + (i - left[i] - 1) * r});
        }
        sort(comb.begin(), comb.end());
        long long score = 1;
        for (int idx = n - 1; idx >= 0; --idx) {
            long long diff = min((long long)k, comb[idx].second);
            k -= diff;
            score = computeResult(score, diff, (long long)comb[idx].first);
            if (!k) break;
        }
        return (int) score;
    }
};