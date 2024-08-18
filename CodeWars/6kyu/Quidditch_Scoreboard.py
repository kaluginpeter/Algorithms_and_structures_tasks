# Your wizard cousin works at a Quidditch stadium and wants you to write a function that calculates
# the points for the Quidditch scoreboard!
#
# Story
# Quidditch is a sport with two teams. The teams score goals by throwing the Quaffle through a hoop,
# each goal is worth 10 points.
#
# The referee also deducts 30 points (- 30 points) from the team who are guilty of carrying out any
# of these fouls: Blatching, Blurting, Bumphing, Haverstacking, Quaffle-pocking, Stooging
#
# The match is concluded when the Snitch is caught, and catching the Snitch is worth 150 points.
# Let's say a Quaffle goes through the hoop just seconds after the Snitch is caught, in that case
# the points of that goal should not end up on the scoreboard seeing as the match is already concluded.
#
# You don't need any prior knowledge of how Quidditch works in order to complete this kata,
# but if you want to read up on what it is, here's a link: https://en.wikipedia.org/wiki/Quidditch
#
# Task
# You will be given a string with two arguments, the first argument will
# tell you which teams are playing and the second argument tells you what's
# happened in the match. Calculate the points and return a string containing
# the teams final scores, with the team names sorted in the same order as in the first argument.
#
# Examples:
# Given an input of:
# quidditchScoreboard("Ilkley vs Yorkshire", "Ilkley: Quaffle goal,
# Yorkshire: Haverstacking foul, Yorkshire: Caught Snitch")
# The expected output would be:
# "Ilkley: 10, Yorkshire: 120"
# Separate the team names from their respective points with a colon and separate the two teams with a comma.
#
# Good luck!
#
# FUNDAMENTALSSTRINGSALGORITHMS
# Solution
def quidditch_scoreboard(teams, actions):
    d = {t: 0 for t in teams.split(' vs ')}
    for t, a in map(lambda x: x.split(': '), actions.split(', ')):
        if 'goal' in a: d[t] += 10
        elif 'foul' in a: d[t] -= 30
        elif 'Caught Snitch' in a: d[t] += 150; break
    return ', '.join('{}: {}'.format(k, v) for k,v in d.items())