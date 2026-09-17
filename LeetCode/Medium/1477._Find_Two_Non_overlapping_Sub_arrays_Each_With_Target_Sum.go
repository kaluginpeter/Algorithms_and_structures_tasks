/*
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 1000
1 <= target <= 108
*/
// Solution
// Go O(NlogN) O(N) BinarySearch Prefix HashMap
func minSumOfLengths(arr []int, target int) int {
    var hashmap map[int]int = map[int]int{}
    hashmap[0] = -1
    var prefix [][2]int = [][2]int{}
    var n int = len(arr)
    var acc, output int = 0, n + 1
    for i := 0; i < n; i++ {
        acc += arr[i]
        // Find the smallest valid subarray from the left
        start, was := hashmap[acc - target]; if was {
            var left, right int = 0, len(prefix) - 1
            for left <= right {
                var middle int = left + ((right - left) >> 1)
                if prefix[middle][0] > start {
                    right = middle - 1
                } else { left = middle + 1 }
            }
            if right >= 0 {
                output = min(output, (i - start) + prefix[right][1])
            }
            // Compress the previous subarrays
            var minSubArrayLength int = i - start
            if len(prefix) == 0 || prefix[len(prefix) - 1][1] > minSubArrayLength {
                prefix = append(prefix, [2]int{i, minSubArrayLength})
            }
        }
        hashmap[acc] = i
    }
    if output == n + 1 { return -1 }
    return output
}

// C++ O(NlogN) O(N) Prefix HashMap BinarySearch
class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        std::unordered_map<int, int> hashmap;
        hashmap[0] = -1;
        std::vector<std::pair<int, int>> prefix;
        size_t n = arr.size();
        int acc = 0, output = n + 1;
        for (int i = 0; i < n; ++i) {
            acc += arr[i];
            if (hashmap.count(acc - target)) {
                // Find the smallest valid subarray from the left
                int start = hashmap[acc - target];
                int left = 0, right = (int)prefix.size() - 1;
                while (left <= right) {
                    int middle = left + ((right - left) >> 1);
                    if (prefix[middle].first > start) right = middle - 1;
                    else left = middle + 1;
                }
                if (right >= 0) output = std::min(output, (i - start) + prefix[right].second);
                // Compress the previous subarray
                if (prefix.empty() || prefix.back().second > (i - start)) {
                    prefix.push_back({i, i - start});
                }
            }
            hashmap[acc] = i;
        }
        return (output == n + 1 ? -1 : output);
    }
};