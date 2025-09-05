# You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.
#
# Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.
#
# Return the minimum number of magic beans that you have to remove.
#
#
#
# Example 1:
#
# Input: beans = [4,1,6,5]
# Output: 4
# Explanation:
# - We remove 1 bean from the bag with only 1 bean.
#   This results in the remaining bags: [4,0,6,5]
# - Then we remove 2 beans from the bag with 6 beans.
#   This results in the remaining bags: [4,0,4,5]
# - Then we remove 1 bean from the bag with 5 beans.
#   This results in the remaining bags: [4,0,4,4]
# We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
# There are no other solutions that remove 4 beans or fewer.
# Example 2:
#
# Input: beans = [2,10,3,2]
# Output: 7
# Explanation:
# - We remove 2 beans from one of the bags with 2 beans.
#   This results in the remaining bags: [0,10,3,2]
# - Then we remove 2 beans from the other bag with 2 beans.
#   This results in the remaining bags: [0,10,3,0]
# - Then we remove 3 beans from the bag with 3 beans.
#   This results in the remaining bags: [0,10,0,0]
# We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
# There are no other solutions that removes 7 beans or fewer.
#
#
# Constraints:
#
# 1 <= beans.length <= 105
# 1 <= beans[i] <= 105
# Solution
# Python O(NlogN + N) O(1) Greedy Sorting
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total_sum: int = sum(beans)
        n: int = len(beans)
        output: int = total_sum
        for i in range(n):
            output = min(output, total_sum - (n - i) * beans[i])
        return output

# C++ O(NlogN + N) O(1) Greedy Sorting
class Solution {
public:
    long long minimumRemoval(vector<int>& beans) {
        std::sort(beans.begin(), beans.end());
        size_t n = beans.size();
        long long totalSum = std::accumulate(beans.begin(), beans.end(), 0LL), output = totalSum;
        for (size_t i = 0; i < n; ++i) {
            output = std::min(output, static_cast<long long>(totalSum - (n - i) * beans[i]));
        }
        return output;
    }
};
