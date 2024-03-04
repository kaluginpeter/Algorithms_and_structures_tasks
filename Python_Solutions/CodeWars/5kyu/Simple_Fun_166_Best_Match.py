# Task
# "AL-AHLY" and "Zamalek" are the best teams in Egypt, but "AL-AHLY" always wins the matches between them. "Zamalek" managers want to know what is the best match they've played so far.
#
# The best match is the match they lost with the minimum goal difference. If there is more than one match with the same difference, choose the one "Zamalek" scored more goals in.
#
# Given the information about all matches they played, return the index of the best match (0-based). If more than one valid result, return the smallest index.
#
# Example
# For ALAHLYGoals = [6,4] and zamalekGoals = [1,2], the output should be 1 (2 in COBOL).
#
# Because 4 - 2 is less than 6 - 1
#
# For ALAHLYGoals = [1,2,3,4,5] and zamalekGoals = [0,1,2,3,4], the output should be 4.
#
# The goal difference of all matches are 1, but at 4th match "Zamalek" scored more goals in. So the result is 4 (5 in COBOL).
#
# Input/Output
# [input] integer array ALAHLYGoals
# The number of goals "AL-AHLY" scored in each match.
#
# [input] integer array zamalekGoals
# The number of goals "Zamalek" scored in each match. It is guaranteed that zamalekGoals[i] < ALAHLYGoals[i] for each element.
#
# [output] an integer
# Index of the best match.
#
# FUNDAMENTALS
# Solution OnePass O(N) O(1)
def best_match(goals1, goals2):
    idx, val, gol = 0, goals1[0] - goals2[0], goals2[0]
    for i in range(1, len(goals1)):
        if goals1[i] - goals2[i] < val:
            idx, val, gol = i, goals1[i] - goals2[i], goals2[i]
        elif goals1[i] - goals2[i] == val:
            if gol >= goals2[i]:
                continue
            idx, val, gol = i, goals1[i] - goals2[i], goals2[i]
    return idx