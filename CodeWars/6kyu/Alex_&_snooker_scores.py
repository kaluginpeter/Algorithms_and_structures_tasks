# Alex is a devoted fan of snooker Masters and in particular, he recorded results of all matches. Help Alex to know the score of matches.
#
# Hint:
# A string with a score presented as follows: "24-79(72); 16-101(53); ..."
# "24" - Points scored the first player;
# "79" - the number of points of the second player.
# "(72)" - the maximum score for one approach.
# Also, the player's account may be expressed as 105(53,52):
# "105" - points in the frame, "53" and "52" - two separate numbers(not float) maximum points in the frame.
# Frames are separated by ";" and players score - "-"
# It should count the number of frames won by one and another player, and output the data as a "[10,7]"
#
# Statistics URL:
#
# STATISTICSARRAYSSTRINGSALGORITHMS
# Solution
def frame(score):
    matches: list[str] = score.split('; ')
    first = second = 0
    for game in matches:
        while '(' in game:
            op: idx = game.index('(')
            cl: idx = game.index(')')
            game = game[:op] + game[cl + 1:]
        x, y = map(int, game.split('-'))
        if x > y:
            first += 1
        elif y > x:
            second += 1
    return [first, second]