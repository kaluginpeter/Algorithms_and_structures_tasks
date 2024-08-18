# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
# is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a
# triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
# Example scoring
#
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function. This is something that
# you should never do. If you mutate the input, you will not be able to pass all the tests.
# Solution
def score(dice):
    cop_l = sorted(dice)
    d = {'111': 1000, '666': 600, '555': 500, '444': 400, '333': 300, '222':200, '1': 100, '5': 50}
    count = 0
    while True:
        if len(cop_l) == 1:
            if str(cop_l[0]) in '15':
                return count + d[str(cop_l[0])]
            return count
        if len(cop_l) == 0:
            return count
        for i in range(len(cop_l)-1):
            if cop_l[i] == cop_l[i+1]:
                if i+2 <= len(cop_l)-1:
                    if cop_l[i] == cop_l[i+2]:
                        count += d[str(cop_l[i])*3]
                        cop_l = cop_l[i+3:]
                        break
                    if str(cop_l[i]) in '15':
                        count += d[str(cop_l[i])] * 2
                        cop_l = cop_l[i+2:]
                        break
                if i+2 > len(cop_l)-1:
                    if str(cop_l[i]) in '15':
                        count += d[str(cop_l[i])] * 2
                        cop_l = cop_l[i+2:]
                        break
                    return count
            if str(cop_l[i]) not in '15':
                cop_l = cop_l[i+1:]
                break
            if str(cop_l[i]) in '15':
                count += d[str(cop_l[i])]
                cop_l = cop_l[i+1:]
                break