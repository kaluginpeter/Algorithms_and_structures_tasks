# Mike and Joe are fratboys that love beer and games that involve drinking. They play the following game: Mike chugs one beer, then Joe chugs 2 beers, then Mike chugs 3 beers, then Joe chugs 4 beers, and so on. Once someone can't drink what he is supposed to drink, he loses.
#
# Mike can chug at most A beers in total (otherwise he would pass out), while Joe can chug at most B beers in total. Who will win the game?
#
# Write the function game(A,B) that returns the winner, "Mike" or "Joe" accordingly, for any given integer values of A and B.
#
# Note: If either Mike or Joe cannot drink at least 1 beer, return the string "Non-drinkers can't play".
#
# STRINGSFUNDAMENTALS
# Solution
def game(a, b):
    if a < 1 or b < 1:
        return "Non-drinkers can't play"
    level: int = 1
    players: list[int] = [a, b]
    first: bool = False
    while True:
        if players[first] - level < 0:
            return ['Mike', 'Joe'][not first]
        players[first] -= level
        level += 1
        first = not first