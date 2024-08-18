# Create a function that takes two arguments:
#
# An array of objects which feature the season, the team and the country of the Champions League winner.
#
# Country (as a string, for example, 'Portugal')
#
# You function should then return the number which represents the number of times a team from a given country has won. Return 0 if there have been no wins.
#
# For example if the input array is as follows:
#
#
# countWins(winnerList1, 'Spain') => should return 2
# countWins(winnerList1, 'Portugal') => should return 1
# countWins(winnerList1, 'Sportland') => should return 0
#
# STRINGSARRAYSDATA STRUCTURESALGORITHMS
# Solution
def countWins(winnerList, country):
    return sum(i.get('country') == country for i in winnerList)