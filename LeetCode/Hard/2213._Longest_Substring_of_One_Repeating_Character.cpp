
/*
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.



Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation:
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc".
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
k == queryCharacters.length == queryIndices.length
1 <= k <= 105
queryCharacters consists of lowercase English letters.
0 <= queryIndices[i] < s.length
*/
// Solution
// O((N + K)logN) O(N) SegmentTree
class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters,
                                 vector<int>& queryIndices) {
        int n = s.size();
        vector<int> pre(4 * n), suf(4 * n), maxLen(4 * n);
        vector<char> leftChar(4 * n), rightChar(4 * n);

        auto pushUp = [&](int u, int l, int r) {
            int mid = (l + r) >> 1;
            int leftLen = mid - l + 1, rightLen = r - mid;
            int left = u << 1, right = u << 1 | 1;
            leftChar[u] = leftChar[left];
            rightChar[u] = rightChar[right];
            pre[u] = pre[left];
            if (pre[left] == leftLen && rightChar[left] == leftChar[right]) {
                pre[u] = pre[left] + pre[right];
            }
            suf[u] = suf[right];
            if (suf[right] == rightLen && rightChar[left] == leftChar[right]) {
                suf[u] = suf[right] + suf[left];
            }
            maxLen[u] = max(maxLen[left], maxLen[right]);
            if (rightChar[left] == leftChar[right]) {
                maxLen[u] = max(maxLen[u], suf[left] + pre[right]);
            }
        };

        function<void(int, int, int)> build = [&](int u, int l, int r) {
            if (l == r) {
                pre[u] = 1;
                suf[u] = 1;
                maxLen[u] = 1;
                leftChar[u] = s[l];
                rightChar[u] = s[l];
                return;
            }
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
            pushUp(u, l, r);
        };

        function<void(int, int, int, int, char)> update =
            [&](int u, int l, int r, int pos, char ch) {
                if (l == r) {
                    leftChar[u] = ch;
                    rightChar[u] = ch;
                    return;
                }
                int mid = (l + r) >> 1;
                if (pos <= mid) {
                    update(u << 1, l, mid, pos, ch);
                } else {
                    update(u << 1 | 1, mid + 1, r, pos, ch);
                }
                pushUp(u, l, r);
            };

        build(1, 0, n - 1);
        int k = queryIndices.size();
        vector<int> ans(k);
        for (int i = 0; i < k; i++) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans[i] = maxLen[1];
        }
        return ans;
    }
};