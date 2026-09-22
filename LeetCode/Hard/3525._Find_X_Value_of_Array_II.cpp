/*
You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Output: [2,2,2]

Explanation:

For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 4, 5]. nums becomes [1, 2].
Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
Remove the empty suffix. nums becomes [3, 5].
Remove the suffix [5]. nums becomes [3].
For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 2, 3, 5]. nums becomes [1].
Remove the suffix [3, 5]. nums becomes [1, 2, 2].
Example 2:

Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

Output: [1,0]

Explanation:

For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
Remove the suffix [2, 4, 8, 16, 32].
For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.
Example 3:

Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

Output: [5]

 

Constraints:

1 <= nums[i] <= 109
1 <= nums.length <= 105
1 <= k <= 5
1 <= queries.length <= 2 * 104
queries[i] == [indexi, valuei, starti, xi]
0 <= indexi <= nums.length - 1
1 <= valuei <= 109
0 <= starti <= nums.length - 1
0 <= xi <= k - 1
*/
// Solution
// C++ O((N + M)KlogN) O(NK) SegmentTree
class SegmentTree {
private:
    static const int MAXK = 6;
    int k;
    int n;
    vector<array<int, MAXK>> tree;
    void makeLeaf(int o, int value) {
        tree[o].fill(0);
        int r = value % k;
        tree[o][r] = 1;
        tree[o][k] = r;
    }

    void mergePre(const array<int, MAXK>& left, const array<int, MAXK>& right, array<int, MAXK>& result) {
        result.fill(0);
        int mulL = left[k];
        int mulR = right[k];
        result[k] = (mulL * mulR) % k;
        for (int x = 0; x < k; ++x) result[x] = left[x];
        for (int x = 0; x < k; ++x) result[(mulL * x) % k] += right[x];
    }

    void maintain(int o) { mergePre(tree[o * 2], tree[o * 2 + 1], tree[o]); }

    void build(const vector<int>& nums, int o, int l, int r) {
        if (l == r) {
            makeLeaf(o, nums[l]);
            return;
        }
        int m = (l + r) / 2;
        build(nums, o * 2, l, m);
        build(nums, o * 2 + 1, m + 1, r);
        maintain(o);
    }

public:
    SegmentTree(const vector<int>& nums, int k) : k(k), n(nums.size()) {
        int size = 2 << (int)ceil(log2(n));
        tree.resize(size);
        build(nums, 1, 0, n - 1);
    }

    void update(int o, int l, int r, int index, int value) {
        if (l == r) {
            makeLeaf(o, value);
            return;
        }
        int m = (l + r) / 2;
        if (index <= m) update(o * 2, l, m, index, value);
        else update(o * 2 + 1, m + 1, r, index, value);
        maintain(o);
    }

    array<int, MAXK> query(int o, int l, int r, int L, int R) {
        if (L <= l && r <= R) return tree[o];
        int m = (l + r) / 2;
        if (R <= m) return query(o * 2, l, m, L, R);
        if (L > m) return query(o * 2 + 1, m + 1, r, L, R);
        array<int, MAXK> left = query(o * 2, l, m, L, R);
        array<int, MAXK> right = query(o * 2 + 1, m + 1, r, L, R);
        array<int, MAXK> result;
        mergePre(left, right, result);
        return result;
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        SegmentTree seg(nums, k);
        vector<int> ans;
        for (auto& q : queries) {
            int index = q[0], value = q[1], start = q[2], x = q[3];
            seg.update(1, 0, n - 1, index, value);
            auto pre = seg.query(1, 0, n - 1, start, n - 1);
            ans.push_back(pre[x]);
        }
        return ans;
    }
};