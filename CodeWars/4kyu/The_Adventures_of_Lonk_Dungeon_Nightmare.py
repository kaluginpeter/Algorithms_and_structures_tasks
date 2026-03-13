# The Adventures of Lonk - Dungeon Analyzer
# In many classic dungeon-crawling games, such as The Legend of Zelda, dungeons are carefully designed so that players can never permanently trap themselves by using keys in the wrong order.
#
# Unfortunately, this is not one of those games.
#
# Welcome to The Legend of Zorlda, set in the proud kingdom of Hyrole, where architectural oversight is more of a “guideline” than a rule. You have recently been hired by the Royal Dungeon-Vetting Division after a series of alarming reports from the kingdom’s most courageous (and mildly confused) adventurer, Lonk.
#
# According to Lonk, some dungeons are:
#
# Completely impossible to finish.
# Technically possible, but only if you don't accidentally open the wrong door.
# "Probably fine?" (Lonk's words)
# This situation is clearly unacceptable. Princess Zorlda herself has tasked you with auditing the kingdom’s dungeons so that proper warning signs can be posted outside each entrance:
#
# "May Be Impossible"
# "May Cause Existential Regret."
# "Probably Fine."
# Your task is to analyze a dungeon and determine:
#
# Is the dungeon solvable? -- Does there exist at least one sequence of actions that reaches the goal?
#
# Is the dungeon softlock-proof? -- From every reachable game state, is it still possible to eventually reach the goal?
#
# In other words... Can Lonk save the day? And can he do so without accidentally ruining everything?
#
# Click to expand the sections below for details
#
# Dungeon Model
# Input Format
# Expected Output
# Examples
# AlgorithmsGraph Theory