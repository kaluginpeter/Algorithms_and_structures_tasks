/*
You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

Return an array answer, where answer[i] is the result for queries[i].

Note

For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
The queries are independent of each other.


Example 1:

Input: s = "01", queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:

Query [0, 3] → Substring "0100" → Augmented to "101001"
Choose "0100", convert "0100" → "0000" → "1111".
The final string without augmentation is "1111". The maximum number of active sections is 4.

Query [0, 2] → Substring "010" → Augmented to "10101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "1110". The maximum number of active sections is 3.

Query [1, 3] → Substring "100" → Augmented to "11001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Query [2, 3] → Substring "00" → Augmented to "1001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 3:

Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

Output: [6,7,2]

Explanation:

Query [1, 5] → Substring "00010" → Augmented to "1000101"
Choose "00010", convert "00010" → "00000" → "11111".
The final string without augmentation is "1111110". The maximum number of active sections is 6.

Query [0, 6] → Substring "1000100" → Augmented to "110001001"
Choose "000100", convert "000100" → "000000" → "111111".
The final string without augmentation is "1111111". The maximum number of active sections is 7.

Query [0, 4] → Substring "10001" → Augmented to "1100011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

Example 4:

Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

Output: [4,4,2]

Explanation:

Query [0, 3] → Substring "0101" → Augmented to "101011"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "11110". The maximum number of active sections is 4.

Query [1, 4] → Substring "1010" → Augmented to "110101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "01111". The maximum number of active sections is 4.

Query [1, 3] → Substring "101" → Augmented to "11011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.



Constraints:

1 <= n == s.length <= 105
1 <= queries.length <= 105
s[i] is either '0' or '1'.
queries[i] = [li, ri]
0 <= li <= ri < n
*/
// Solution
// C++ O(N + QlogN) O(N) SegmentTree
class SegmentTree {
public:
    int n;
    vector<int> arr,segment;
    SegmentTree(vector<int> &nums) {
        n = nums.size();
        arr = nums;
        segment.assign(std::max(1, n) << 2, 0);
        if (n) build(1, 0, n - 1);
    }
    void build(int node, int left, int right) {
        if (left == right){
            segment[node] = arr[left];
            return;
        }
        if (left > right) return;
        int mid = left + ((right - left) >> 1);
        build(node << 1, left, mid);
        build((node << 1) + 1, mid + 1, right);
        segment[node] = std::max(segment[node << 1], segment[(node << 1) + 1]);
    }
    int internalQuery(int node, int st, int en, int left, int right) {
        if (left <= st && en <= right) return segment[node];
        if (st == en) return segment[node];
        if (right < st || en < left) return 0;
        int mid = st + ((en - st) >> 1);
        int res = 0;
        if (mid >= left) res = std::max(res, internalQuery(node << 1, st, mid, left, right));
        if (right > mid) res = std::max(res, internalQuery((node << 1) + 1, mid + 1, en, left, right));
        return res;
    }
    int query(int l, int r) {
        if (l > r || n == 0) return 0;
        return internalQuery(1, 0, n - 1, l, r);
    }
};
class Solution {
public:
    int segmentz = 0;
    int lowerBound(std::vector<int>& v, int x) {
        int l = 0, r = segmentz;
        while (l < r) {
            int m = l + ((r - l) >> 1);
            if (v[m] >= x) r = m;
            else l = m + 1;
        }
        return l;
    }
    int upperBound(vector<int> &v, int x) {
        int l = 0, r = segmentz;
        while (l < r){
            int m = l + ((r - l) >> 1);
            if (v[m] <= x) l = m + 1;
            else r = m;
        }
        return l;
    }
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>> &q) {
        int n = s.size(), cnt1 = 0;
        for (char& c: s) {
            if (c == '1') ++cnt1;
        }
        std::vector<int> zeroBlocks, zeroLeft, zeroRight;
        int idx = 0;
        while (idx < n) {
            int r = idx;
            while (r < n && s[idx] == s[r]) ++r;
            int len = r - idx;
            if (s[idx] == '0') {
                zeroBlocks.push_back(len);
                zeroLeft.push_back(idx);
                zeroRight.push_back(r - 1);
            }
            idx = r;
        }
        int m = zeroBlocks.size();
        segmentz = m;
        std::vector<int> ans;
        if (m <= 1) {
            for (int i = 0; i < q.size(); ++i) ans.push_back(cnt1);
            return ans;
        }
        std::vector<int> nums(m - 1);
        for (int i = 0; i < m - 1; ++i) nums[i] = zeroBlocks[i] + zeroBlocks[i + 1];
        SegmentTree st(nums);
        for (int i = 0; i < q.size(); ++i) {
            int l = q[i][0], r = q[i][1];
            int lidx = lowerBound(zeroRight, l);
            int ridx = upperBound(zeroLeft, r) - 1;
            if (lidx > m - 1 || ridx < 0 || lidx >= ridx) {
                ans.push_back(cnt1);
                continue;
            }
            int leftLen = zeroRight[lidx] - std::max(zeroLeft[lidx], l) + 1;
            int rightLen = std::min(r, zeroRight[ridx]) - zeroLeft[ridx] + 1;
            if (lidx + 1 == ridx) {
                ans.push_back(cnt1 + leftLen + rightLen);
                continue;
            }
            int leftContri = leftLen + zeroBlocks[lidx + 1];
            int rightContri = rightLen + zeroBlocks[ridx - 1];
            int middleContri = st.query(lidx + 1, ridx - 2);
            ans.push_back(cnt1 + std::max(leftContri, std::max(rightContri, middleContri)));
        }
        return ans;
    }
};