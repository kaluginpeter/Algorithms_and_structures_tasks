# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
#
# The chemistry of a team is equal to the product of the skills of the players on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
#
#
#
# Example 1:
#
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
# Example 2:
#
# Input: skill = [3,4]
# Output: 12
# Explanation:
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.
# Example 3:
#
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation:
# There is no way to divide the players into teams such that the total skill of each team is equal.
#
#
# Constraints:
#
# 2 <= skill.length <= 105
# skill.length is even.
# 1 <= skill[i] <= 1000
# Solution
# Python O(NlogN) O(1) Two Pointers Sorting
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        median_skill: int = skill[0] + skill[-1]
        chemistry_sum: int = 0
        left: int = 0
        right: int = len(skill) - 1
        while left < right:
            cur_skill_sum: int = skill[left] + skill[right]
            if cur_skill_sum != median_skill: return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        return chemistry_sum

# C++ O(NlogN) O(1) Two Pointers Sorting
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        std::sort(skill.begin(), skill.end());
        long long median_skill = skill[0] + skill[skill.size() - 1];
        long long chemistry_sum = 0;
        size_t left = 0;
        size_t right = skill.size() - 1;
        while (left < right){
            long long cur_skill_sum = skill[left] + skill[right];
            if (cur_skill_sum != median_skill) {
                return -1;
            }
            chemistry_sum += skill[left] * skill[right];
            left += 1;
            right -= 1;
        }
        return chemistry_sum;
    }
};

# Python O(N) O(N) Two Pointers Sorting Counting Sort
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_skill: list[int] = [0] * (max(skill) + 1)
        for num in skill:
            sorted_skill[num] += 1
        left: int = 0
        right: int = len(sorted_skill) - 1
        while left < right and not sorted_skill[left]:
            left += 1
        while left < right and not sorted_skill[right]:
            right -= 1
        median_skill: int = left + right
        chemistry_sum: int = 0
        while left <= right and sorted_skill[left] > 0 and sorted_skill[right] > 0:
            cur_skill_sum: int = left + right
            if cur_skill_sum != median_skill: return -1
            chemistry_sum += left * right
            sorted_skill[left] -= 1
            sorted_skill[right] -= 1
            if sorted_skill[left] == 0: left += 1
            if sorted_skill[right] == 0: right -= 1
            while left <= right and not sorted_skill[left]:
                left += 1
            while left <= right and not sorted_skill[right]:
                right -= 1
        return chemistry_sum

# C++ O(N) O(N) Two Pointers Sorting Counting Sort
#include <vector>
#include <algorithm>

class Solution {
public:
    long long dividePlayers(std::vector<int>& skill) {
        std::vector<int> sorted_skill(*std::max_element(skill.begin(), skill.end()) + 1, 0);
        for (int num : skill) {
            sorted_skill[num]++;
        }
        int left = 0;
        int right = sorted_skill.size() - 1;
        while (left < right && sorted_skill[left] == 0) {
            left++;
        }
        while (left < right && sorted_skill[right] == 0) {
            right--;
        }
        long long median_skill = left + right;
        long long chemistry_sum = 0;
        while (left <= right && sorted_skill[left] > 0 && sorted_skill[right] > 0) {
            long long cur_skill_sum = left + right;
            if (cur_skill_sum != median_skill) {
                return -1;
            }
            chemistry_sum += static_cast<long long>(left) * right;
            sorted_skill[left]--;
            sorted_skill[right]--;
            if (sorted_skill[left] == 0) {
                left++;
            }
            if (sorted_skill[right] == 0) {
                right--;
            }
            while (left <= right && sorted_skill[left] == 0) {
                left++;
            }
            while (left <= right && sorted_skill[right] == 0) {
                right--;
            }
        }
        return chemistry_sum;
    }
};