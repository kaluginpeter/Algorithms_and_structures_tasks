# You are given two 2D integer arrays nums1 and nums2.
#
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
#
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
#
# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.
#
#
#
# Example 1:
#
# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.
# Example 2:
#
# Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
# Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
# Explanation: There are no common ids, so we just include each id with its value in the resulting list.
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 200
# nums1[i].length == nums2[j].length == 2
# 1 <= idi, vali <= 1000
# Both arrays contain unique ids.
# Both arrays are in strictly ascending order by id.
# Solution
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res, right, left = [], 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left][0] == nums2[right][0]:
                res.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left, right = left + 1, right + 1
            else:
                if nums1[left][0] < nums2[right][0]:
                    res.append([nums1[left][0], nums1[left][1]])
                    left += 1
                else:
                    res.append([nums2[right][0], nums2[right][1]])
                    right += 1
        while left < len(nums1):
            res.append(nums1[left])
            left += 1
        while right < len(nums2):
            res.append(nums2[right])
            right += 1
        return res

# Python O(N + M) O(N + M) Two Pointers
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output: list[list[int]] = []
        n: int = len(nums1)
        m: int = len(nums2)
        left: int = 0
        right: int = 0
        while left < n and right < m:
            if nums1[left][0] < nums2[right][0]:
                output.append(nums1[left])
                left += 1
            elif nums2[right][0] < nums1[left][0]:
                output.append(nums2[right])
                right += 1
            else:
                output.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left += 1
                right += 1
        while left < n:
            output.append(nums1[left])
            left += 1
        while right < m:
            output.append(nums2[right])
            right += 1
        return output

# C++ O(N + M) O(N + M) Two Pointers
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        vector<vector<int>> output;
        int n = nums1.size();
        int m = nums2.size();
        int left = 0;
        int right = 0;
        while (left < n && right < m) {
            if (nums1[left][0] < nums2[right][0]) {
                output.push_back(nums1[left]);
                ++left;
            } else if (nums2[right][0] < nums1[left][0]) {
                output.push_back(nums2[right]);
                ++right;
            } else {
                output.push_back({nums1[left][0], nums1[left][1] + nums2[right][1]});
                ++left;
                ++right;
            }
        }
        while (left < n) {
            output.push_back(nums1[left]);
            ++left;
        }
        while (right < m) {
            output.push_back(nums2[right]);
            ++right;
        }
        return output;
    }
};