/*
You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

Constraints:

1 <= intevals.length <= 5 * 104
intervals[i].length == 3
intervals[i] = [li, ri, weighti]
1 <= li <= ri <= 109
1 <= weighti <= 109
 
*/
// Solution
// C++ O(NlogN + NM^2) O(NM^2) DynamicProgramming BinarySearch
class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<tuple<int, int, int, int>> arr;
        for (int i = 0; i < n; i++) {
            int l = intervals[i][0], r = intervals[i][1],
                weight = intervals[i][2];
            arr.emplace_back(l, r, weight, i);
        }
        sort(arr.begin(), arr.end(),
             [](auto&& a, auto&& b) { return get<1>(a) < get<1>(b); });
        vector<vector<long long>> dp(n + 1, vector<long long>(5));
        vector<vector<vector<int>>> indices(n + 1, vector<vector<int>>(5));
        for (int i = 0; i < n; i++) {
            auto [l, r, weight, idx] = arr[i];
            int k = lower_bound(arr.begin(), arr.begin() + i, l,
                                [](const tuple<int, int, int, int>& t,
                                   int val) { return get<1>(t) < val; }) -
                    arr.begin();

            for (int j = 1; j < 5; j++) {
                long long s1 = dp[i][j];
                long long s2 = dp[k][j - 1] + weight;
                if (s1 > s2) {
                    dp[i + 1][j] = dp[i][j];
                    indices[i + 1][j] = indices[i][j];
                    continue;
                }
                vector<int> newIndex = indices[k][j - 1];
                newIndex.push_back(idx);
                sort(newIndex.begin(), newIndex.end());
                if (s1 == s2 && indices[i][j] < newIndex) {
                    newIndex = indices[i][j];
                }
                dp[i + 1][j] = s2;
                indices[i + 1][j] = newIndex;
            }
        }
        return indices[n][4];
    }
};