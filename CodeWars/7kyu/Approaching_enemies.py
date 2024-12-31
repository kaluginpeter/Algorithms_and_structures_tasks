# You are in a military mission in the middle of the jungle where your enemies are really hard to spot because of their camouflage. Luckily you have a device that shows the position of your enemies!
#
# Your device is a radar that computes the x and y coordinates of an enemy in meters every 5 seconds. You are always at the point (0, 0) and your enemies are always heading towards you.
#
# Your task
# The radar will give you two consecutive points P1(x, y) and P2(x, y) of an enemy and you should write a function that will return the estimated time in seconds that the enemy will take to reach you, so you can defend! Python results should be rounded to 3 decimal places.
#
# Hints
# Distance between two points. Remember that you are working with only 2 dimensions!
#
# Tests will have a precision of 3 decimal points. Good luck!
#
# PuzzlesGames
# Solution
def calculate_time(p1, p2):
    speed: float = ( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )**.5 / 5
    return round( ( p2[0]**2 + p2[1]**2 )**.5 / speed, 3)