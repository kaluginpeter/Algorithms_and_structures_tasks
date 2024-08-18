# Paul is an excellent coder and sits high on the CW leaderboard. He solves kata like a banshee but would also like to lead a normal life, with other activities. But he just can't stop solving all the kata!!
#
# Given an array (x) you need to calculate the Paul Misery Score. The values are worth the following points:
#
# kata = 5
# Petes kata = 10
# life = 0
# eating = 1
# The Misery Score is the total points gained from the array. Once you have the total, return as follows:
#
# < 40 = 'Super happy!'
# < 70 >= 40 = 'Happy!'
# < 100 >= 70 = 'Sad!'
# > 100 = 'Miserable!'
# FUNDAMENTALSARRAYS
# Solution
def paul(x):
    d = {'kata':5, 'Petes kata':10, 'life':0, 'eating':1}
    count = sum(d[i] for i in x)
    return 'Super happy!' if count < 40 else 'Happy!' if 40 <= count < 70 else 'Sad!' if 70 <= count < 100 else 'Miserable!'