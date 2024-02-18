# You just got done writing a function that calculates the player's final score for your new game, "Flight of the cockatoo".
#
# Now all you need is a high score table that can be updated with the player's final scores. With such a feature, the player will be motivated to try to beat his previous scores, and hopefully, never stop playing your game.
#
# The high score table will start out empty. A limit to the size of the table will be specified upon creation of the table.
#
# Here's an example of the expected behavior of the high score table :
#
# highScoreTable = HighScoreTable(3)
# highScoreTable.scores == [] # evaluates to True
# highScoreTable.update(10)
# highScoreTable.scores == [10]
# highScoreTable.update(8)
# highScoreTable.update(12)
# highScoreTable.update(5)
# highScoreTable.update(10)
# highScoreTable.scores == [12, 10, 10]
# highScoreTable.reset()
# highScoreTable.scores == []
# # And so on...
# ALGORITHMSSORTINGSEARCHINGARRAYSOBJECT-ORIENTED PROGRAMMING
# Solution
class HighScoreTable:

    def __init__(self, capacity):
        self.scores: list = list()
        self.capacity: int = capacity
        self.size: int = 0

    def update(self, val):
        if self.size > 0 and self.size == self.capacity:
            if min(self.scores) < val:
                self.scores.remove(min(self.scores))
                self.scores.append(val)
        if self.size < self.capacity:
            self.scores.append(val)
            self.size += 1
        self.scores.sort(reverse=True)

    def reset(self):
        self.scores.clear()
        self.size = 0