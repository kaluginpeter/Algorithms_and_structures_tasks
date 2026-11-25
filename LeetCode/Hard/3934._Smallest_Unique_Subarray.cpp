/*
You are given an integer array nums.

Find the minimum length of a subarray that is not identical to any other subarray in nums.

Return an integer denoting the minimum possible length of such a subarray.

Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.

 

Example 1:

Input: nums = [3,3,3]

Output: 3

Explanation:

Subarrays of length 1: [3] → appears 3 times
Subarrays of length 2: [3, 3] → appears 2 times
Subarrays of length 3: [3, 3, 3] → appears once
The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

Example 2:

Input: nums = [2,1,2,3,3]

Output: 1

Explanation:

Subarrays of length 1:

[2] → appears 2 times
[1] → appears once
[3] → appears 2 times
The subarray [1] is unique, so the smallest unique subarray length is 1.
Example 3:

Input: nums = [1,1,2,2,1]

Output: 2

Explanation:

Subarrays of length 1:

[1] → appears 3 times
[2] → appears 2 times
Subarrays of length 2:

[1, 1] → appears once
[1, 2] → appears once
[2, 2] → appears once
[2, 1] → appears once
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
*/
// Solution
// C++ O(NlogN) O(N) BinarySearch RollingHash Math
class Solution {
public:
    static constexpr long long MOD = 1'000'000'007;
    static constexpr long long BASE = 100'003;   // > max value (1e5)
    long long pw = 1;                             // BASE^(k-1) % MOD for the current k

    void buildHash(int left, int right, std::vector<int>& nums, int& hash) {
        if (left != -1) {
            // remove left part out of hash
            hash = (hash - nums[left] * pw % MOD + MOD) % MOD;
        }
        // insert the right part of hash
        hash = (1LL * hash * BASE + nums[right]) % MOD;
    }

    bool check(size_t& k, size_t& n, std::vector<int>& nums) {
        pw = 1;
        for (size_t i = 0; i + 1 < k; ++i) pw = pw * BASE % MOD;
        std::unordered_map<int, int> subarrays;
        int hash = 0;
        for (size_t i = 0; i < k - 1; ++i) {
            buildHash(-1, i, nums, hash);
        }
        for (int i = k - 1; i < n; ++i) {
            buildHash(i - k, i, nums, hash);
            ++subarrays[hash];
        }
        for (auto& [_, freq] : subarrays) {
            if (freq == 1) return true;
        }
        return false;
    }

    int smallestUniqueSubarray(vector<int>& nums) {
        size_t n = nums.size();
        size_t left = 1, right = n;
        while (left <= right) {
            size_t middle = left + ((right - left) >> 1);
            if (check(middle, n, nums)) right = middle - 1;
            else left = middle + 1;
        }
        return left;
    }
};

// Let's look at the constraints
// Since the inpute array is 10^5 we need to find a solution
// that <= O(NlogN) complexity
// Also look at the numbers itself 1 <= i <= 10^5(only positive ones)

// And we cannot try all possible subarrays cause it will lead to O(N^2) complexity

// We can observe the some facts about "not identical" subarray
// Let's say that we have "not identical" subarray of size x.
// Then we definitely know that there exist another "not identical" subarrays
// of size x + 1, x + 2, ..., (x + y = n).
// That property means that the comparison of subarrays by their size is
// monotonic here.
// Using that property we can use a "binary search on answer" technique
// Let's use left = 1, right = n bounds and search for a any valid
// "non-identical" subarray of size k = left + ((right - left) >> 1) amongs
// all possible n - k + 1 possible subarrays

// But the next problem is "how to quickly check that there isn't any other subarray"?
// Cause basically scanning will take square time
// Can we use hashing here?
// We need to be able to build a "dynamic hash" here
// These will leads us to a "rolling hash" technique

// Let's say that when we define our window size(k)
// We scan the entire n - k + 1 subarray and build their
// respectively hashes into hashmap
// Then scan again and for each current subarray, just check wether their hash are
// located into the hashmap or not. And if any of the subarray is "non-identical"
// we return "true" and shrink our pointers to lower sizes(since we need to find a smallest one)

// Another question: "how to build a rolling hash?" we need to create a hashmap in
// determinitive way and consider the requirement about "corresponding positions" and not 
// just "equal elements". We can use "polynomial hashing" here.

// The overall complexity is O(Nlog(N))
// And memory complexity is O(N)