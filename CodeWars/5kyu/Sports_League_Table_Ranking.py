# Note: There is a harder version (Sports League Table Ranking (with Head-to-head)) of this.
#
# Description
# You organize a sports league in a round-robin-system. Each team meets all other teams. In your league a win gives a team 2 points, a draw gives both teams 1 point. After some games you have to compute the order of the teams in your league. You use the following criteria to arrange the teams:
#
# Points
# Scoring differential (the difference between goals scored and those conceded)
# Goals scored
# First you sort the teams by their points. If two or more teams reached the same number of points, the second criteria comes into play and so on. Finally, if all criteria are the same, the teams share a place.
#
# Input
# number: Number of teams in your league.
# games: An array of arrays. Each item represents a played game with an array of four elements [TeamA,TeamB,GoalA,GoalB] (TeamA played against TeamB and scored GoalA goals and conceded GoalB goals ).
# Output
# positions: An array of positions. The i-th item should be the position of the i-th team in your league.
# Example
# number = 6
# games = [[0, 5, 2, 2],   // Team 0 - Team 5 => 2:2
#          [1, 4, 0, 2],   // Team 1 - Team 4 => 0:2
#          [2, 3, 1, 2],   // Team 2 - Team 3 => 1:2
#          [1, 5, 2, 2],   // Team 1 - Team 5 => 2:2
#          [2, 0, 1, 1],   // Team 2 - Team 0 => 1:1
#          [3, 4, 1, 1],   // Team 3 - Team 4 => 1:1
#          [2, 5, 0, 2],   // Team 2 - Team 5 => 0:2
#          [3, 1, 1, 1],   // Team 3 - Team 1 => 1:1
#          [4, 0, 2, 0]]   // Team 4 - Team 0 => 2:0
# You may compute the following table:
#
# Rank	Team	For : Against	GD	Points
# 1.	Team 4	5 : 1	+4	5
# 2.	Team 5	6 : 4	+2	4
# 3.	Team 3	4 : 3	+1	4
# 4.	Team 0	3 : 5	-2	2
# 4.	Team 1	3 : 5	-2	2
# 6.	Team 2	2 : 5	-3	1
# Team 5 and Team 3 reached the same number of points. But since Team 5 got a better scoring differential, it ranks better than Team 3. All values of Team 0 and Team 1 are the same, so these teams share the fourth place.
#
# In this example you have to return the array [4, 4, 6, 3, 1, 2].
#
# FUNDAMENTALSALGORITHMSARRAYSSORTING
# Solution
def compute_ranks(number, games):
    storage: dict[int, list[int, int, int]] = dict()
    for team in range(number):
        storage[team] = [0, 0, 0]
    for game in games:
        com1, com2, gol1, gol2 = game
        com1_stats: list[int, int, int] = storage.get(com1, None)
        com1_stats[0] += 2 if gol1 > gol2 else 1 if gol1 == gol2 else 0
        com1_stats[1] += gol1 - gol2
        com1_stats[2] += gol1
        storage[com1] = com1_stats
        com2_stats: list[int, int, int] = storage.get(com2, None)
        com2_stats[0] += 2 if gol2 > gol1 else 1 if gol2 == gol1 else 0
        com2_stats[1] += gol2 - gol1
        com2_stats[2] += gol2
        storage[com2] = com2_stats
    scores: list[tuple[int, int, int]] = list({tuple(com) for com in storage.values()})
    scores.sort(reverse=True)
    output: list[int] = [scores.index(tuple(storage[team])) + 1 for team in storage.keys()]
    addition: int = 0
    move: bool = False
    rank: int = 1
    for _ in range(len(scores)):
        quantity: int = output.count(rank)
        move = quantity > 1
        if move:
            addition = quantity - 1
            rank += 1
            for team in range(number):
                if output[team] >= rank:
                    output[team] += addition
            rank += addition
        else: rank += 1
    return output