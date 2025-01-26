# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
#
# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
#
# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.
#
#
#
# Example 1:
#
#
# Input: favorite = [2,2,1,2]
# Output: 3
# Explanation:
# The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
# All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
# Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
# The maximum number of employees that can be invited to the meeting is 3.
# Example 2:
#
# Input: favorite = [1,2,0]
# Output: 3
# Explanation:
# Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
# The seating arrangement will be the same as that in the figure given in example 1:
# - Employee 0 will sit between employees 2 and 1.
# - Employee 1 will sit between employees 0 and 2.
# - Employee 2 will sit between employees 1 and 0.
# The maximum number of employees that can be invited to the meeting is 3.
# Example 3:
#
#
# Input: favorite = [3,0,1,4,1]
# Output: 4
# Explanation:
# The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
# Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
# So the company leaves them out of the meeting.
# The maximum number of employees that can be invited to the meeting is 4.
#
#
# Constraints:
#
# n == favorite.length
# 2 <= n <= 105
# 0 <= favorite[i] <= n - 1
# favorite[i] != i
# Solution
# We should solve Need For Speed Most Wanted: Black Edition by 2005
#
# Intro
# Hi, I'm Josie Maran, I play Mia in Need for Speed: Most Wanted
# In the game you can drive without any rules
# But-oh... in life, be careful on the road
#
# Complexity
# Since you black list contains only 15 racers, you anyways should won them all. So time complexity will be linear
#
# Time complexity: O(N)
# Also when you won a black list player yor take his car. So you need a garage to contain all 15 black list players cars. So memory complexity also will be linear
#
# Space complexity: O(N)
# Code
# Python O(N) O(N)
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        black_list_players: int = len(favorite)
        black_list: list[int] = [0] * black_list_players
        for rider in range(black_list_players):
            opponent: int = favorite[rider]
            black_list[opponent] += 1
        cur_riders: list[int] = []
        next_riders: list[int] = []
        for rider in range(black_list_players):
            if not black_list[rider]: cur_riders.append(rider)
        wins: list[int] = [1] * black_list_players
        while cur_riders:
            for cur_rider in cur_riders:
                opponent: int = favorite[cur_rider]
                wins[opponent] = max(wins[opponent], wins[cur_rider] + 1)
                black_list[opponent] -= 1
                if not black_list[opponent]: next_riders.append(opponent)
            cur_riders = next_riders
            next_riders = []
        won_races_in_row: int = 0
        black_list_battles: int = 0
        for black_list_rider in range(black_list_players):
            if not black_list[black_list_rider]: continue
            races_won: int = 0
            cur_rider: int = black_list_rider
            while black_list[cur_rider]:
                races_won += 1
                black_list[cur_rider] = 0
                opponent: int = favorite[cur_rider]
                cur_rider = opponent
            if races_won == 2:
                opponent: int = favorite[black_list_rider]
                black_list_battles += wins[black_list_rider] + wins[opponent]
            else:
                won_races_in_row = max(won_races_in_row, races_won)
        most_wanted: int = max(won_races_in_row, black_list_battles)
        return most_wanted

# C++ O(N) O(N)
cclass Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        int blackListPlayers = favorite.size();
        std::vector<int> blackList (blackListPlayers, 0);
        for (int rider = 0; rider < blackListPlayers; ++rider) {
            int opponent = favorite[rider];
            ++blackList[opponent];
        }
        std::vector<int> curRiders;
        std::vector<int> nextRiders;
        for (int rider = 0; rider < blackListPlayers; ++rider) {
            if (!blackList[rider]) curRiders.push_back(rider);
        }
        std::vector<int> wins (blackListPlayers, 1);
        while (!curRiders.empty()) {
            for (int& curRider : curRiders) {
                int opponent = favorite[curRider];
                wins[opponent] = std::max(wins[opponent], wins[curRider] + 1);
                --blackList[opponent];
                if (!blackList[opponent]) nextRiders.push_back(opponent);
            }
            curRiders = nextRiders;
            nextRiders = {};
        }
        int wonRacesInRow = 0;
        int blackListBattles = 0;
        for (int rider = 0; rider < blackListPlayers; ++rider) {
            if (!blackList[rider]) continue;
            int racesWon = 0;
            int curRider = rider;
            while (blackList[curRider]) {
                ++racesWon;
                blackList[curRider] = 0;
                int opponent = favorite[curRider];
                curRider = opponent;
            }
            if (racesWon == 2) {
                int opponent = favorite[rider];
                blackListBattles += wins[rider] + wins[opponent];
            } else wonRacesInRow = std::max(wonRacesInRow, racesWon);
        }
        int mostWanted = std::max(wonRacesInRow, blackListBattles);
        return mostWanted;
    }
};