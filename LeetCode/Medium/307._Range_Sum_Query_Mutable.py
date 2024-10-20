# Given an integer array nums, handle multiple queries of the following types:
#
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
#
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 104 calls will be made to update and sumRange.
# Solution
# Python O(NlogN) O(N) Segment Tree
class SegmentTree:
    def __init__(self, sum_: int, left_bound: int, right_bound: int) -> None:
        self.total_sum: int = sum_
        self.left_index: int = left_bound
        self.right_index: int = right_bound
        self.left_child: SegmentTree = None
        self.right_child: SegmentTree = None

    @staticmethod
    def build(nums: list[int], left: int, right: int) -> 'SegmentTree':
        if left == right:
            return SegmentTree(nums[left], left, right)
        root: SegmentTree = SegmentTree(0, left, right)
        middle: int = (left + right) // 2
        root.left_child = SegmentTree.build(nums, left, middle)
        root.right_child = SegmentTree.build(nums, middle + 1, right)
        root.total_sum = root.left_child.total_sum + root.right_child.total_sum
        return root

    def update(self, index: int, value: int) -> None:
        if self.left_index == self.right_index:
            self.total_sum = value
            return
        middle: int = (self.left_index + self.right_index) // 2
        if index > middle:
            self.right_child.update(index, value)
        else:
            self.left_child.update(index, value)
        self.total_sum = self.left_child.total_sum + self.right_child.total_sum

    def sum_range(self, left: int, right: int) -> int:
        if self.left_index == left and self.right_index == right:
            return self.total_sum
        middle: int = (self.left_index + self.right_index) // 2
        if left > middle:
            return self.right_child.sum_range(left, right)
        elif right <= middle:
            return self.left_child.sum_range(left, right)
        else:
            return (
                    self.left_child.sum_range(left, middle)
                    + self.right_child.sum_range(middle + 1, right)
            )


class NumArray:

    def __init__(self, nums: List[int]):
        self.ST: SegmentTree = SegmentTree.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.ST.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.ST.sum_range(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# C++ O(NlogN) O(N) Segment Tree
class SegmentTree {
public:
    int totalSum, leftIndex, rightIndex;
    SegmentTree* leftChild;
    SegmentTree* rightChild;

    SegmentTree (int sum, int leftBound, int rightBound) {
        totalSum = sum;
        leftIndex = leftBound;
        rightIndex = rightBound;
        leftChild = nullptr;
        rightChild = nullptr;
    };

    static SegmentTree* build(std::vector<int>& nums, int L, int R) {
        if (L == R) {
            return new SegmentTree(nums[L], L, R);
        }
        int M = (L + R) / 2;
        SegmentTree* root = new SegmentTree(0, L, R);
        root->leftChild = SegmentTree::build(nums, L, M);
        root->rightChild = SegmentTree::build(nums, M + 1, R);
        root->totalSum = root->leftChild->totalSum + root->rightChild->totalSum;
        return root;
    }

    void update(int index, int val) {
        if (leftIndex == rightIndex) {
            totalSum = val;
            return;
        }
        int M = (leftIndex + rightIndex) / 2;
        if (index > M) {
            rightChild->update(index, val);
        } else {
            leftChild->update(index, val);
        }
        totalSum = leftChild->totalSum + rightChild->totalSum;
    }

    int sumRange(int left, int right) {
        if (leftIndex == left && rightIndex == right) {
            return totalSum;
        }
        int M = (leftIndex + rightIndex) / 2;
        if (left > M) {
            return rightChild->sumRange(left, right);
        } else if (right <= M) {
            return leftChild->sumRange(left, right);
        } else {
            return leftChild->sumRange(left, M) + rightChild->sumRange(M + 1, right);
        }
    }
};

class NumArray {
public:
    std::vector<int> numbers;
    SegmentTree* ST;
    NumArray(vector<int>& nums) {
        numbers = nums;
        ST = SegmentTree::build(nums, 0, static_cast<int>(nums.size()) - 1);
    }

    void update(int index, int val) {
        ST->update(index, val);
    }

    int sumRange(int left, int right) {
        return ST->sumRange(left, right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */