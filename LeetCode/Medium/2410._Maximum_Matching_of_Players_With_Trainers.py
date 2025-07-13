# You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.
#
# The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.
#
# Return the maximum number of matchings between players and trainers that satisfy these conditions.
#
#
#
# Example 1:
#
# Input: players = [4,7,9], trainers = [8,2,5,8]
# Output: 2
# Explanation:
# One of the ways we can form two matchings is as follows:
# - players[0] can be matched with trainers[0] since 4 <= 8.
# - players[1] can be matched with trainers[3] since 7 <= 8.
# It can be proven that 2 is the maximum number of matchings that can be formed.
# Example 2:
#
# Input: players = [1,1,1], trainers = [10]
# Output: 1
# Explanation:
# The trainer can be matched with any of the 3 players.
# Each player can only be matched with one trainer, so the maximum answer is 1.
#
#
# Constraints:
#
# 1 <= players.length, trainers.length <= 105
# 1 <= players[i], trainers[j] <= 109
#
#
# Note: This question is the same as 445: Assign Cookies.
# Solution
# Python O(NlogN) O(1) Two Pointers Sorting Greedy
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left: int = 0
        right: int = 0
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                left += 1
            right += 1
        return left

# C++ O(NlogN) O(1) Two Pointers Sorting Greedy
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        size_t left = 0;
        size_t right = 0;
        int content = 0;
        std::sort(players.begin(), players.end());
        std::sort(trainers.begin(), trainers.end());
        while (left < players.size() && right < trainers.size()) {
            if (players[left] <= trainers[right]) {
                content++;
                left++;
            }
            right++;
        }
        return content;
    }
};


# Python O(NlogN + MlogM + min(N, M)) O(1) TwoPointers Sorting Greedy
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i: int = 0
        j: int = 0
        n: int = len(players)
        m: int = len(trainers)
        output: int = 0
        while i < n and j < m:
            while j < m and trainers[j] < players[i]: j += 1
            if j < m:
                output += 1
                j += 1
                i += 1
        return output

# C++ O(NlogN + MlogM + min(N, M)) O(1) TwoPointers Sorting Greedy
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        std::sort(players.begin(), players.end());
        std::sort(trainers.begin(), trainers.end());
        int i = 0, j = 0, n = players.size(), m = trainers.size(), output = 0;
        while (i < n && j < m) {
            while (j < m && trainers[j] < players[i]) ++j;
            if (j < m) {
                ++output;
                ++j;
                ++i;
            }
        }
        return output;
    }
};