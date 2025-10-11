# A magician has various spells.
#
# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
#
# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
#
# Each spell can be cast only once.
#
# Return the maximum possible total damage that a magician can cast.
#
#
#
# Example 1:
#
# Input: power = [1,1,3,4]
#
# Output: 6
#
# Explanation:
#
# The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
#
# Example 2:
#
# Input: power = [7,1,6,6]
#
# Output: 13
#
# Explanation:
#
# The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
#
#
#
# Constraints:
#
# 1 <= power.length <= 105
# 1 <= power[i] <= 109
# Solution Dynamic Programming O(N**2) O(N)
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ht = dict()
        for num in power:
            ht[num] = ht.get(num, 0) + 1
        spells = sorted(ht.keys())
        k = len(spells)
        dp = [0] * k
        for spell_index in range(k):
            if spell_index == 0:
                dp[spell_index] = spells[spell_index] * ht[spells[spell_index]]
            else:
                dp[spell_index] = dp[spell_index - 1]
            current_damage = spells[spell_index] * ht[spells[spell_index]]
            previous_damage_index = spell_index - 1
            while previous_damage_index >= 0 and spells[previous_damage_index] >= spells[spell_index] - 2:
                previous_damage_index -= 1
            if previous_damage_index >= 0:
                dp[spell_index] = max(dp[spell_index], current_damage + dp[previous_damage_index])
            else:
                dp[spell_index] = max(dp[spell_index], current_damage)
        return max(dp)


# Python O(N) O(N) DynamicProgramming
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        nums: list[int] = []
        for num in power:
            if num not in hashmap:
                hashmap[num] = 0
                nums.append(num)
            hashmap[num] += 1
        nums.sort()
        dp: list[int] = [0] * len(nums)
        dp[0] = hashmap[nums[0]] * nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(
                dp[i - 1],
                hashmap[nums[i]] * nums[i] + max(
                    dp[i - 1] if nums[i - 1] + 2 < nums[i] else 0,
                    dp[i - 2] if i >= 2 and nums[i - 2] + 2 < nums[i] else 0,
                    dp[i - 3] if i >= 3 and nums[i - 3] + 2 < nums[i] else 0,
                )
            )
        return dp[len(dp) - 1]

# C++ O(N) O(N) DynamicProgramming
class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        std::unordered_map<int, int> hashmap;
        std::vector<int> nums;
        for (int& num : power) {
            if (!hashmap.count(num)) nums.push_back(num);
            ++hashmap[num];
        }
        std::sort(nums.begin(), nums.end());
        std::vector<long long> dp(nums.size(), 0);
        dp[0] = static_cast<long long>(hashmap[nums[0]]) * nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            dp[i] = std::max(
                dp[i - 1],
                static_cast<long long>(hashmap[nums[i]]) * nums[i] + (
                    std::max({
                        (i && nums[i - 1] + 2 < nums[i] ? dp[i - 1] : 0LL),
                        (i >= 2 && nums[i - 2] + 2 < nums[i] ? dp[i - 2] : 0LL),
                        (i >= 3 ? dp[i - 3] : 0LL),
                        (i >= 4 ? dp[i - 4] : 0LL)
                    })
                )
            );
        }
        return dp[nums.size() - 1];
    }
};