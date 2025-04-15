# You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].
#
# A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.
#
# Return the total number of good triplets.
#
#
#
# Example 1:
#
# Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# Output: 1
# Explanation:
# There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3).
# Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
# Example 2:
#
# Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# Output: 4
# Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
#
#
# Constraints:
#
# n == nums1.length == nums2.length
# 3 <= n <= 105
# 0 <= nums1[i], nums2[i] <= n - 1
# nums1 and nums2 are permutations of [0, 1, ..., n - 1].
# Solution
# Python O(NlogN) O(N) BinaryIndexedTree
class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree: list[int] = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        output: int = 0
        while index:
            output += self.tree[index]
            index -= index & -index
        return output


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n: int = len(nums1)
        pos2: list[int] = [0] * n
        pos1: list[int] = [0] * n
        for i in range(n): pos2[nums2[i]] = i
        for i in range(n): pos1[pos2[nums1[i]]] = i
        tree: FenwickTree = FenwickTree(n)
        inversions: int = 0
        for number in range(n):
            pos: int = pos1[number]
            left: int = tree.query(pos)
            tree.update(pos, 1)
            right: int = (n - 1 - pos) - (number - left)
            inversions += left * right
        return inversions

# C++ O(NlogN) O(N) BinaryIndexedTree
class FenwickTree {
public:
    FenwickTree(int size) : tree(size + 1, 0) {}
    void update(int index, int delta) {
        ++index;
        while (index < tree.size()) {
            tree[index] += delta;
            index += index & -index;
        }
    }
    int query(int index) {
        ++index;
        int res = 0;
        while (index > 0) {
            res += tree[index];
            index -= index & -index;
        }
        return res;
    }
private:
    vector<int> tree;
};

class Solution {
public:
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> pos2(n), pos1(n);
        for (int i = 0; i < n; i++) pos2[nums2[i]] = i;
        for (int i = 0; i < n; i++) pos1[pos2[nums1[i]]] = i;
        FenwickTree tree(n);
        long long inversions = 0;
        for (int number = 0; number < n; number++) {
            int pos = pos1[number];
            int left = tree.query(pos);
            tree.update(pos, 1);
            int right = (n - 1 - pos) - (number - left);
            inversions += static_cast<long long>(left) * right;
        }
        return inversions;
    }
};