# At the casino you are presented with a wide array of games to play. You are there for fun, but you want to be economical about it by playing the game that maximises your profits (minimises your losses, let's be real).
#
# To do this, you will pick the game with the highest expected value (EV). If you are unfamiliar with the concept, you can read the article on investopedia.
#
# You will get a tuple containing instances of namedtuple Game. Each instance of Game has a field name and outcomes. name is just the name of the game represented as a string. outcomes is a tuple of tuples where each inner tuple represents a single possible outcome.
#
# Example Game instance:
#
# g1 = Game("Breakeven Steven", ((0.5, 20), (0.5, -20)))
# For each outcome (inner tuple), the first value represent the probability of occurrence while the second value represent the reward. In the above example there is a 50% chance of winning 20, and 50% chance of losing 20.
#
# The function which you will construct should return the name of the game with the highest expected value of playing.
#
# Constraints:
#
# 2 <= N <= 20
#
# Notes:
#
# Each input has one clear winner.
# Namedtuple Game has been preloaded.
# Game namedtuple:
#
# Game = namedtuple("Game", ["name", "outcomes"])
# Example with explanation:
#
# g1 = Game("Breakeven Steven", ((0.5, 20), (0.5, -20)))
# g2 = Game("Go big or go home", ((0.99, -10), (0.01, 980)))
#
# find_best_game((g1, g2)) # => "Breakeven Steven"
# Breakeven Steven has a higher EV than Go big or go home (0 vs -0.1) and therefore the function should return that name.
#
# ProbabilityMathematicsFundamentalsData ScienceStatistics