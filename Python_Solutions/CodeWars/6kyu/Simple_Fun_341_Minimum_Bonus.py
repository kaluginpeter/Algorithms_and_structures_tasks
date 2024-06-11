# Task
# International hackers group organized a programming competition, in which n teams participated.
#
# They were assigned to separate rooms for competitions, and the rooms were lined up in a straight line.
#
# The game was over and each team scored points. It's time to pay bonuses. The rule is:
#
# - The bonus unit is 1K($1000), and each team gets at least 1k.
# - The bonus payment process is not public.
# - A team can know the bonus amount of its adjacent team, if the
#   score of the adjacent team is lower than itself.
# - If a team finds that its bonus is no higher than the adjacent team whose
#   score is lower than itself, the team will not be satisfied
# Given an integer array scores represents the score of all teams. Your task is to calculate how much bonuses international hackers group need to pay to keep all teams satisfied.
#
# Note, the unit of bonus is 1K. All teams are in a straight line, and their order is the same as that of the array elements.
#
# Example
# For scores = [10,20,30], the output should be 6.
#
# team1's score = 10
# team2's score = 20
# team3's score = 30
#
# team1 can get 1K, The team was satisfied
# because it knew nothing about the other teams.
#
# team2 can know team1's bonus amount,
# So team2 at least get 2K to be satisfied
#
# team3 can know team2's bonus amount,
# So team3 at least get 3K to be satisfied
#
# 1 + 2 + 3 = 6
# For scores = [10,20,20,30], the output should be 6.
#
# The possible bonus amount of each team can be:[1,2,1,2]
#
# For scores = [20,30,10,30,40,10,20,30,40,30], the output should be 20.
#
# The possible bonus amount of each team can be:[1,2,1,2,3,1,2,3,4,1]
#
# ALGORITHMS
# Solution
from collections import defaultdict
def minimum_bonus(scores):
    ht: dict[int, int] = defaultdict(int)
    for team in range(len(scores)):
        ht[team] += 1
    while True:
        swaped: bool = False
        for team in range(len(scores)):
            if team + 1 < len(scores) and scores[team] > scores[team + 1] and ht[team] <= ht[team + 1]:
                ht[team] = ht[team + 1] + 1
                swaped = True
            if team - 1 >= 0 and scores[team] > scores[team - 1] and ht[team] <= ht[team - 1]:
                ht[team] = ht[team - 1] + 1
                swaped = True
        if not swaped:
            return sum(ht.values())