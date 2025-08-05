# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
#
# From left to right, place the fruits according to these rules:
#
# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.
#
#
#
# Example 1:
#
# Input: fruits = [4,2,5], baskets = [3,5,4]
#
# Output: 1
#
# Explanation:
#
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.
#
# Example 2:
#
# Input: fruits = [3,6,1], baskets = [6,4,7]
#
# Output: 0
#
# Explanation:
#
# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.
#
#
#
# Constraints:
#
# n == fruits.length == baskets.length
# 1 <= n <= 105
# 1 <= fruits[i], baskets[i] <= 109
# Solution
# Python O(NlogN) O(4N) SegmentTree
class SegmentTree:
    def __init__(self, n: int, baskets: list[int]) -> None:
        self.seg_tree: list[int] = [0] * (4 * 100 + 1)
        self.build(1, 0, n, baskets)

    def build(self, parent: int, left: int, right: int, baskets: list[int]) -> None:
        if left == right:
            self.seg_tree[parent] = baskets[left]
            return
        middle: int = left + ((right - left) >> 1)
        self.build(parent << 1, left, middle, baskets)
        self.build(parent << 1 | 1, middle + 1, right, baskets)
        self.seg_tree[parent] = max(self.seg_tree[parent << 1], self.seg_tree[parent << 1 | 1])

    def query(self, parent: int, left: int, right: int, target: int) -> int:
        if self.seg_tree[parent] < target:
            return -1
        elif left == right:
            return left
        middle: int = left + ((right - left) >> 1)
        if self.seg_tree[parent << 1] >= target: return self.query(parent << 1, left, middle, target)
        return self.query(parent << 1 | 1, middle + 1, right, target)

    def update(self, parent: int, left: int, right: int, pos: int, val: int) -> None:
        if left == right:
            self.seg_tree[parent] = val
            return
        middle: int = left + ((right - left) >> 1)
        if pos <= middle:
            self.update(parent << 1, left, middle, pos, val)
        else:
            self.update(parent << 1 | 1, middle + 1, right, pos, val)
        self.seg_tree[parent] = max(self.seg_tree[parent << 1], self.seg_tree[parent << 1 | 1])


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n: int = len(fruits)
        st: SegmentTree = SegmentTree(n - 1, baskets)
        output: int = 0
        for fruit in fruits:
            pos: int = st.query(1, 0, n - 1, fruit)
            if pos == -1:
                output += 1
            else:
                st.update(1, 0, n - 1, pos, -1)
        return output

# C++ O(NlogN) O(4N) SegmentTree
class SegmentTree {
public:
    int segTree[401];
    SegmentTree(int parent, int left, int right, std::vector<int> baskets) {
        build(parent, left, right,  baskets);
    };

    void build(int p, int l, int r, const std::vector<int> &baskets) {
        if (l == r) {
            segTree[p] = baskets[l];
            return;
        }
        int mid = l + ((r - l) >> 1);
        build(p << 1, l, mid, baskets);
        build(p << 1 | 1, mid + 1, r, baskets);
        segTree[p] = max(segTree[p << 1], segTree[p << 1 | 1]);
    }

    int query(int p, int l, int r, int target) {
        if (segTree[p] < target) return -1;
        if (l == r) return l;
        int mid = l + ((r - l) >> 1), pos = -1;
        if (segTree[p << 1] >= target) pos = query(p << 1, l, mid, target);
        else pos = query(p << 1 | 1, mid + 1, r, target);
        return pos;
    }

    void update(int p, int l, int r, int pos, int val) {
        if (l == r) {
            segTree[p] = val;
            return;
        }
        int mid = l + ((r - l ) >> 1);
        if (pos <= mid) update(p << 1, l, mid, pos, val);
        else update(p << 1 | 1, mid + 1, r, pos, val);
        segTree[p] = max(segTree[p << 1], segTree[p << 1 | 1]);
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int m = baskets.size();
        if (m == 0) return fruits.size();
        int output = 0;
        SegmentTree st = SegmentTree(1, 0, m - 1, baskets);
        for (int i = 0; i < m; i++) {
            int pos = st.query(1, 0, m - 1, fruits[i]);
            if (pos == -1) ++output;
            else st.update(1, 0, m - 1, pos, -1);
        }
        return output;
    }
};