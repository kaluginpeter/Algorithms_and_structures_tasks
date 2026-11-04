/*
You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):

Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

 

Example 1:

Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

Output: 8

Explanation:

Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.
Example 2:

Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2

Output: 3

Explanation:

Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.
 

Constraints:

2 <= nums.length <= 105
-106 <= nums[i] <= 106
2 <= x <= nums.length
1 <= k <= 15
2 <= k * x <= nums.length
 


*/
// Solution
// C++ O(NlogX + NK) O(NK + X) DynamicProgramming PriorityQueue
class Solution {
public:
    void insertToStream(int& num, std::multiset<int>& left, long long& leftSum, std::multiset<int>& right, long long& rightSum) {
        right.insert(num);
        rightSum += num;

        // keep order: the smallest of right goes to left
        auto it = right.begin();
        left.insert(*it);
        leftSum += *it;
        rightSum -= *it;
        right.erase(it);

        // keep sizes: left may have at most one extra element
        if (left.size() > right.size() + 1) {
            auto jt = std::prev(left.end());
            right.insert(*jt);
            rightSum += *jt;
            leftSum -= *jt;
            left.erase(jt);
        }
    }

    void eraseFromStream(int num, std::multiset<int>& left, long long& leftSum, std::multiset<int>& right, long long& rightSum) {
        auto it = left.find(num);
        if (it != left.end() && num <= *left.rbegin()) {
            left.erase(it);
            leftSum -= num;
        } else {
            right.erase(right.find(num));
            rightSum -= num;
        }
        // rebalance
        if (left.size() > right.size() + 1) {
            auto jt = std::prev(left.end());
            right.insert(*jt); rightSum += *jt; leftSum -= *jt; left.erase(jt);
        } else if (left.size() < right.size()) {
            auto jt = right.begin();
            left.insert(*jt); leftSum += *jt; rightSum -= *jt; right.erase(jt);
        }
    }

    long long minOperations(vector<int>& nums, int x, int k) {
        long long bound = INT64_MAX;
        size_t n = nums.size();
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(k + 1, bound));
        for (size_t i = 0; i <= n; ++i) dp[i][0] = 0;
        std::multiset<int> left, right;
        long long leftSum = 0LL, rightSum = 0LL;
        for (size_t i = 1; i < x; ++i) insertToStream(
            nums[i - 1],
            left, leftSum,
            right, rightSum
        );

        for (size_t i = x; i <= n; ++i) {
            insertToStream(nums[i - 1], left, leftSum, right, rightSum);

            int median = *left.rbegin();
            long long neededOps = (median * 1LL * left.size() - leftSum) + (rightSum - median * 1LL * right.size());
            
            for (size_t curSegment = 1; curSegment <= k && i >= x; ++curSegment) {
                dp[i][curSegment] = dp[i - 1][curSegment];
                if (dp[i - x][curSegment - 1] == bound) continue; // cannot take previous segment
                dp[i][curSegment] = std::min({
                    dp[i][curSegment],
                    dp[i - x][curSegment - 1] + neededOps
                });
            }

            eraseFromStream(nums[i - x], left, leftSum, right, rightSum);   
        }

        return dp[n][k];
    }
};

// let's imagine dp[n][k],
//   where dp[i] is the end of segment with endpoint i
//      and dp[i][j] j is is represent the j'th segment
//         then previous segment is from dp[i - X][j - 1]
//  So we need to collect minimum and that choose the minimal amongst
// the all dp[i][k] 0 <= i <= n


// So how to fast know the needed operations?
// We can use a "stream technique" for fast median finding
//   and calculating of needed operations for a constant time

// So general approach is to initialize an array dp[n][k]
// then for each i'th element will be represent the current segment
// so iterate through all 1 <= seg <= k and search comparing
// with dp[i - x][seg - 1] + current ops
// Then the answer will be minimum amongs all dp[i][k] where 0 <= i <= n
// Time Complexity O(NlogX + NK) memory is O(NK + X)