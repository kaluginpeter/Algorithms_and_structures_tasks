/*
You are given an array nums of n integers and an integer k.

For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.

An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

 

Example 1:

Input: nums = [6,3,1,2,4,4], k = 7

Output: 17

Explanation:

Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

Example 2:

Input: nums = [6,3,1,3,6], k = 4

Output: 12

Explanation:

The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
*/
// Solution
// C++ O(NlogN) O(N) PriorityQueue SlidingWindow
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        long long operations = 0;
        // Maintain the window maximum with a priority queue
        priority_queue<pair<int, int>> q;
        // Record the set of elements covered by this index
        vector<vector<int>> cnt(n);
        // Index of the first greater-or-equal element to the right
        vector<int> pos(n, n);
        // Decreasing monotonic stack
        stack<int> st;

        for (int left = 0, right = 0; right < n; right++) {
            while (!st.empty() && nums[right] >= nums[st.top()]) {
                pos[st.top()] = right;
                st.pop();
            }
            if (!st.empty()) {
                cnt[st.top()].push_back(right);
            }
            st.push(right);
            q.emplace(nums[right], right);
            operations += max(0, q.top().first - nums[right]);
            while (operations > k) {
                for (int i : cnt[left]) {
                    operations -=
                        (long long)(nums[left] - nums[i]) *
                        (min(pos[i], right + 1) - i);
                }
                left++;
            }
            while (!q.empty() && q.top().second < left) {
                q.pop();
            }
            ans += right - left + 1;
        }

        return ans;
    }
};