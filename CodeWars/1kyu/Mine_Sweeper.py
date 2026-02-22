# Have you ever played Minesweeper? It's a WINDOWS own game that mainly tests the player's ability to think logically.
#
# Here are the rules of the game, maybe helpful to someone who hasn't played Minesweeper:
#
# "The goal of the game is to uncover all the squares that do not contain mines without being "blown up" by clicking on a square with a mine underneath. The location of the mines is discovered by a process of logic. Clicking on the game board will reveal what is hidden underneath the chosen square or squares (a large number of blank squares may be revealed in one go if they are adjacent to each other). Some squares are blank but some contain numbers (1 to 8), each number being the number of mines adjacent to the uncovered square. To help avoid hitting a mine, the location of a suspected mine can be marked by flagging it with the right mouse button. The game is won once all blank squares have been uncovered without hitting a mine, any remaining mines not identified by flags being automatically flagged by the computer. However, in the event that a game is lost and the player mistakenly flags a safe square, that square will either appear with a red X covering the mine (denoting it as safe), or just a red X (also denoting it as safe)."
#
# Task
# In this kata, I'll give you a string map as a game map, and a number n indicating the total number of mines. Like this:
#
# map =
# ? ? ? ? ? ?
# ? ? ? ? ? ?
# ? ? ? 0 ? ?
# ? ? ? ? ? ?
# ? ? ? ? ? ?
# 0 0 0 ? ? ?
#
# n = 6
# Yes, you always get a matrix with some question marks, except for some 0s (because I think you need a place to start your logical reasoning).
#
# Digit 0 means that there's 0 mines around here, so you can safely open the grid cells around 0. How to open the grid cell? I've preloaded a method open, usage is open(row,column) (for Java and Rust users: Game.open(row, column)). It will return a number that indicates how many mines are around this grid cell. If there is an error in your logical reasoning, when you use the open method to open a grid cell, but there is a mine hidden in this grid cell, then the test will fail. Please note, method open only returns a number, but does not modify the map—you should modify the map by yourself.
#
# You open more and more grid cells until all safe grid cells are opened and all mine grid cells are marked by 'x'. Then return the result like this:
#
# 1 x 1 1 x 1
# 2 2 2 1 2 2
# 2 x 2 0 1 x
# 2 x 2 1 2 2
# 1 1 1 1 x 1
# 0 0 0 1 1 1
# If the game cannot get a valid result, return "?" (None in Rust). See following:
#
# map =
# 0 ? ?
# 0 ? ?
# n = 1
#
# First you open two middle grid cells (using `open(0,1)` and `open(1,1)`), then you get:
#
# map =
# 0 1 ?
# 0 1 ?
#
# Now, there is only one mine left, but there are two `?` left.
# The mine can be hidden in either of them. So, you should return "?" / None as the result there.
# PuzzlesGame Solvers
# Solution
#!/usr/bin/env python3
import sys
import itertools
from datetime import datetime
#!/usr/bin/env python3
mf = []
r = []
# 0
mf.append("""
? ? ? 0 ? ? ? 0 ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? 0 0
? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0
0 0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ?
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? 0 0 0 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? 0 0
0 ? ? ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? 0 ? ? ? 0 0 0 0 0
? ? 0 ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? ? 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ?
0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 0 0 0
0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
""".strip())
r.append("""
1 x 1 0 1 1 1 0 1 x 2 x 1 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 0 0
1 1 1 0 1 x 2 2 3 2 2 1 1 0 0 0 1 1 2 1 1 0 0 0 0 1 x 1 0 0
0 0 0 1 2 2 2 x x 2 1 1 0 0 0 0 0 0 1 x 1 0 0 0 0 1 2 2 1 0
1 1 1 1 x 1 1 2 2 2 x 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0 2 x 2 0
2 x 1 1 1 1 1 1 1 1 1 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 2 x 2 0
x 2 1 0 0 0 1 x 1 0 0 0 2 3 x 1 0 0 0 1 x 1 0 0 0 0 1 1 1 0
1 1 0 0 0 0 2 2 2 0 0 0 1 x 2 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0
0 0 0 0 0 0 1 x 1 0 0 0 2 2 2 0 1 1 1 0 0 0 1 1 1 1 x 1 0 0
0 0 0 0 1 1 2 1 1 0 0 0 1 x 1 0 1 x 1 1 1 2 2 x 1 1 1 1 0 0
0 0 0 0 1 x 1 0 0 0 0 0 1 1 1 0 2 2 2 2 x 3 x 2 1 0 0 0 1 1
0 0 0 0 1 1 1 0 0 0 0 1 1 1 0 0 1 x 1 2 x 4 2 2 0 1 1 1 1 x
0 1 1 1 0 0 0 0 0 0 0 1 x 1 0 0 1 2 2 2 1 2 x 1 0 1 x 1 1 1
0 1 x 2 1 2 1 1 0 0 0 1 1 1 0 0 0 1 x 1 0 1 2 2 1 1 1 1 0 0
0 1 1 2 x 2 x 3 2 1 0 1 2 2 1 0 0 1 2 2 1 0 1 x 1 0 0 0 0 0
1 1 0 1 1 2 2 x x 1 0 1 x x 1 0 0 0 1 x 1 0 1 2 2 1 0 0 0 0
x 1 0 0 0 0 2 3 3 1 0 1 2 2 1 0 0 0 1 1 1 0 0 2 x 2 0 0 0 0
1 1 0 0 0 0 1 x 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 2 x 3 1 0 0 0
0 0 0 0 0 0 1 1 1 0 0 0 0 1 x 1 0 0 0 1 1 1 0 1 2 x 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 2 x 2 0 1 2 2 1 0 0 0
1 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 2 0 1 x 1 0 1 1 1
1 x x 1 1 1 1 0 1 1 1 0 0 1 1 2 1 1 0 1 1 1 1 2 2 1 0 1 x 1
1 2 3 2 2 x 1 0 1 x 2 1 0 1 x 3 x 2 0 0 0 0 1 x 1 0 0 1 1 1
0 0 1 x 3 2 2 0 1 2 x 1 1 2 2 3 x 3 1 0 0 0 1 1 1 0 0 0 0 0
0 0 1 1 2 x 1 0 0 1 1 2 2 x 2 2 2 x 2 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 1 x 4 x 1 1 1 2 x 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 2 2 x 2 1 0 0 1 1 1 1 x 2 1 1 0 0 0 0
0 0 0 0 0 1 1 2 1 2 x 1 1 1 1 0 0 1 2 2 1 1 1 2 x 2 1 1 1 1
0 0 0 0 0 1 x 4 x 4 2 1 0 0 0 0 0 2 x x 2 2 2 2 3 x 2 1 x 1
0 0 0 0 0 1 2 x x x 1 0 0 0 0 0 0 2 x 3 2 x x 1 2 x 2 1 1 1
""".strip())

# 1
mf.append("""
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip())
r.append("""
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
""".strip())

# 2
mf.append("""
0 ? ?
0 ? ?
""".strip())
r.append("""
0 1 1
0 1 x
""".strip())

# 3
mf.append("""
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip())
r.append("""
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
""".strip())

# 4
mf.append("""
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 0 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0 0
""".strip())
r.append("""
0 0 0 0 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 0 0 0 2 x 2 1 x 1 0
1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 1 2 x 1 0 0 0 0 2 x 2 1 1 1 0
1 x 1 1 1 1 0 1 x 2 1 1 0 0 1 x 2 1 1 0 0 0 0 1 1 1 0 0 0 0
1 2 2 3 x 2 0 1 1 2 x 1 0 0 1 2 2 1 0 0 0 0 0 1 1 1 0 0 1 1
0 1 x 3 x 2 0 0 0 1 1 1 0 1 2 3 x 1 0 0 0 0 0 1 x 1 0 0 1 x
0 1 1 3 3 3 2 1 1 1 1 2 1 2 x x 2 2 1 1 0 0 0 1 1 1 1 1 2 1
0 0 0 1 x x 2 x 1 1 x 2 x 2 3 3 3 2 x 1 0 1 1 1 0 0 2 x 2 0
0 1 1 2 2 2 3 2 2 1 1 2 1 1 1 x 2 x 2 1 0 1 x 1 0 0 2 x 2 0
1 2 x 1 0 1 2 x 1 0 0 0 1 1 2 2 3 2 1 0 0 1 1 1 0 0 1 1 1 0
1 x 2 1 0 1 x 3 2 1 0 0 1 x 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 0
1 1 2 1 2 2 2 2 x 1 0 0 1 1 1 1 2 x 1 0 0 0 1 x 2 1 0 0 0 0
1 1 2 x 2 x 1 1 1 1 0 0 0 0 1 1 2 1 1 0 0 0 1 2 x 1 0 0 0 0
1 x 3 2 2 1 1 0 0 1 1 1 0 0 1 x 1 0 0 0 0 0 1 2 2 1 0 0 0 0
1 2 x 1 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 x 1 0 0 0 0 0
""".strip())

# 5
mf.append("""
? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ?
? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ? ? ?
? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0
""".strip())
r.append("""
1 2 x 1 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 1 x 1
1 x 2 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 1 1 x 1 1 1 1
1 2 2 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 x 2 2 1 1 0 0 0
0 1 x 2 1 2 2 x 2 1 0 0 0 0 0 0 0 0 1 3 x 3 1 1 0 0 0
0 1 1 2 x 2 x 3 x 1 0 0 0 0 0 0 0 0 0 2 x 3 x 1 0 0 0
""".strip())

# 6
mf.append("""
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? 0 ? ? ?
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 ? ? ? ? ? ? 0
? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ?
? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ?
? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ?
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
""".strip())
r.append("""
0 0 0 0 0 0 0 0 1 x x 2 1 0 1 x 1 0 1 2 x
0 0 0 0 0 0 0 0 1 2 3 x 1 0 2 2 2 1 2 x 2
0 0 0 0 0 0 0 0 0 0 2 2 2 0 1 x 1 1 x 2 1
0 0 0 0 0 1 1 1 0 0 1 x 1 0 1 2 2 2 1 1 0
1 1 0 0 0 1 x 1 0 1 2 2 1 0 0 1 x 1 1 1 1
x 1 0 0 0 1 1 1 0 1 x 1 0 0 0 1 1 1 1 x 1
2 2 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1
1 x 1 0 0 0 0 0 0 0 1 2 2 1 0 0 1 1 1 0 0
1 1 1 0 0 0 0 0 0 0 1 x x 1 0 0 1 x 1 0 0
""".strip())

# 7
mf.append("""
1 1 1 1 x 2 1 1 0 0 0 0
2 2 1 1 1 2 x 2 1 1 1 1
? ? ? ? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ? ? ?
""".strip())
r.append("""
1 1 1 1 x 2 1 1 0 0 0 0
2 2 1 1 1 2 x 2 1 1 1 1
x x 2 2 2 2 3 x 2 1 x 1
x 3 2 x x 1 2 x 2 1 1 1
""".strip())

# 8
mf.append("""
0 1 ? ? ? ? ?
0 2 ? ? ? ? ?
0 2 ? ? ? ? ?
0 2 ? ? ? ? ?
0 1 ? ? ? ? ?
""".strip())
r.append("""
0 1 x 1 0 1 x
0 2 2 2 0 2 2
0 2 x 2 0 2 x
0 2 2 2 0 2 2
0 1 x 1 0 1 x
""".strip())

# 9
mf.append("""
0 1 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
0 2 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
0 2 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
0 2 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
0 1 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
""".strip())
r.append("""
0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0
0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0
0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0 2 x 2 0
0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0 2 2 2 0
0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0 1 x 1 0
""".strip())

#10
mf.append("""
0 0 0 0 0 0 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0
0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 0 0 ? ? ? ? ? ?
0 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? 0 0 0
0 0 0 ? ? ? ? 0 0 0
0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
? ? 0 ? ? ? 0 0 0 0
? ? 0 ? ? ? 0 0 0 0
? ? ? ? ? ? ? ? ? 0
? ? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ?
0 0 ? ? ? 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ?
""".strip())
r.append("""
0 0 0 0 0 0 0 1 1 1
1 1 1 1 1 1 0 2 x 2
1 x 2 2 x 1 0 2 x 2
1 1 2 x 2 1 0 1 1 1
0 0 2 2 2 1 1 1 0 0
0 0 1 x 1 1 x 2 1 1
0 0 1 1 2 2 2 3 x 2
0 0 0 0 1 x 1 2 x 2
0 0 0 0 1 1 1 1 1 1
0 0 0 1 2 2 1 0 0 0
0 0 0 1 x x 1 0 0 0
0 0 0 1 2 2 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 1 0 0 0 0
x 1 0 1 x 1 0 0 0 0
2 3 1 3 2 2 1 1 1 0
x 2 x 2 x 1 1 x 2 1
1 2 1 2 1 1 1 2 x 1
0 0 1 1 1 0 0 1 1 1
0 0 1 x 1 1 1 2 2 2
0 0 1 1 1 1 x 2 x x
0 0 0 0 0 1 1 2 2 2
""".strip())

#11
mf.append("?")
r.append("0")

#12
mf.append("""
? ? ?
? ? ?
? ? ?
""".strip())
r.append("""
x x x
x x x
x x x
""".strip())

#13
mf.append("""
0 0 0 0
0 0 0 0
? ? 0 0
? ? ? ?
? ? ? ?
? ? ? ?
? ? 0 0
0 0 0 0
0 0 0 0
0 0 0 0
""".strip())
r.append("""
0 0 0 0
0 0 0 0
1 1 0 0
x 2 1 1
x 3 1 x
x 2 1 1
1 1 0 0
0 0 0 0
0 0 0 0
0 0 0 0
""".strip())

#14
mf.append("""
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ?
? ? 0 ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ?
0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ?
0 0 0 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ?
0 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
""".strip())
r.append("""
1 1 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0
x 1 0 1 x 1 0 0 2 x 2 0 0 0 0 1 x 2 1
1 1 0 2 3 3 1 1 3 x 2 0 0 0 0 1 2 x 1
0 1 1 2 x x 1 2 x 3 1 0 0 0 0 0 1 1 1
0 1 x 2 2 2 1 3 x 3 0 0 0 0 0 0 0 0 0
0 1 1 1 0 0 0 2 x 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 2 2 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 x x 1 0 0 0 0 0
0 0 1 1 1 0 1 1 1 0 1 2 2 1 0 0 0 0 0
0 0 1 x 2 1 3 x 2 0 0 0 0 0 0 1 1 1 0
0 0 1 1 2 x 3 x 3 1 1 0 0 0 0 1 x 1 0
0 0 0 0 1 2 3 2 2 x 1 0 0 0 0 1 1 1 0
0 0 0 0 0 1 x 1 1 1 1 0 0 0 0 0 1 1 1
0 0 1 1 2 2 2 1 0 0 0 0 0 0 0 0 1 x 1
0 0 1 x 2 x 2 1 1 0 0 0 0 0 0 0 1 1 1
0 0 1 1 2 1 3 x 3 1 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 2 x x 1 0 0 0 1 1 1 0 1 x
0 0 0 1 1 1 1 2 2 1 0 0 0 1 x 1 1 2 2
0 0 0 1 x 3 2 1 0 0 0 1 1 2 1 1 1 x 2
0 0 0 1 2 x x 1 0 0 0 1 x 1 0 1 2 3 x
0 0 0 0 1 2 2 1 1 1 1 1 1 1 0 1 x 3 2
0 0 0 0 1 1 1 1 2 x 1 1 1 1 0 2 3 x 2
0 0 0 0 1 x 1 1 x 2 1 1 x 1 0 1 x 3 x
""".strip())

#15 time to solve: 0:01:47.742415
# Case demonstrates need to solve on a per cluster basis
mf.append("""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0
? ? ? ? ? ? ? 0 0 ? ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
""".strip())
r.append("""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0
1 1 1 1 2 x 1 0 0 1 2 2 1 0 1 2 2 1 0 0 1 x 2 1 1 1 1
1 x 1 2 x 3 2 2 2 2 x x 2 0 2 x x 2 2 2 2 3 x 2 1 x 1
1 1 1 2 x 2 1 x x 2 3 x 2 0 2 x 3 2 x x 1 2 x 2 1 1 1
""".strip())


class MineSweeper():
    """
    Minesweeper solver
    """
    def __init__(self, mine_field, bombs):
        """
        initializes MineSweeper game solver
        """
        if type(mine_field).__name__ == 'str':
            self.mf = mine_field.split('\n')
            for x in range(len(self.mf)):
                self.mf[x] = self.mf[x].split(' ')
        else:
            self.mf = mine_field
        self.bombs = bombs
        self.ROWS, self.COLS = len(self.mf), len(self.mf[0])
        self.borders = {}

    def generate_border_spaces(self, r, c, idx):
        """
        this containes all border spaces if on the board
        """
        self.borders[idx] = [True]
        b = [True]
        if r > 0:                                   b.append([r - 1, c])
        if r > 0 and c < self.COLS - 1:             b.append([r - 1, c + 1])
        if r > 0 and c > 0:                         b.append([r - 1, c - 1])
        if c < self.COLS - 1:                       b.append([r, c + 1])
        if c > 0:                                   b.append([r, c - 1])
        if r < self.ROWS - 1:                       b.append([r + 1, c])
        if r < self.ROWS - 1 and c < self.COLS - 1: b.append([r + 1, c + 1])
        if r < self.ROWS - 1 and c > 0:             b.append([r + 1, c - 1])
        self.borders[idx] = b

    def complete_border_neighbors(self):
        """
        completes generation of border neighbors
        """
        i = 0
        needed = list(
            set(range(0, self.ROWS * self.COLS)) - set(self.borders.keys())
        )
        while i < len(needed):
            idx = needed[i]
            r = idx // self.COLS
            c = idx - (r * self.COLS)
            self.generate_border_spaces(r, c, idx)
            i += 1

    def find_neighbors(self, idx, char, test=False):
        """
        finds neighboring spaces of givin input character
        """
        coords = []
        if char == '?' and self.borders[idx][0] is False: return []
        for space in self.borders[idx][1:]:
            if char == 'int' == type(self.mf[space[0]][space[1]]).__name__:
                coords.append(space)
            elif self.mf[space[0]][space[1]] == char:
                coords.append(space)
        if char == '?' and len(coords) == 0 and test is False:
            self.borders[idx][0] = False
        return sorted(coords)

    def open_list(self, coords):
        """
        CALLS OPEN BASED ON INPUT LIST
        """
        for coord in coords:
            revealed = open(coord[0], coord[1])
            if type(revealed).__name__ == 'str':
                revealed = int(revealed)
            self.mf[coord[0]][coord[1]] = revealed

    def mark_bombs(self, coords):
        """
        Marks Bombs on input field from input coords
        """
        for coord in coords: self.mf[coord[0]][coord[1]] = 'x'

    def initial_board_scan_with_basic_logic(self):
        """
        Reveals Board based on revealed spaces logic
        """
        r = 0
        while r < self.ROWS:
            c = 0
            while c < self.COLS:
                square = self.mf[r][c]
                idx = r * self.COLS + c
                if idx not in self.borders:
                    self.generate_border_spaces(r, c, idx)
                if square == 'x' or square == '?':
                    c += 1
                    continue
                unknown = self.find_neighbors(idx, '?')
                if len(unknown) == 0:
                    c += 1
                    continue
                bombs = self.find_neighbors(idx, 'x')
                if type(square).__name__ == 'str' and square.isdigit():
                    square = int(square)
                    self.mf[r][c] = square
                if self.mf[r][c] == '0' or self.mf[r][c] == 0: self.open_list(unknown)
                elif len(bombs) == square: self.open_list(unknown)
                elif square - len(bombs) == len(unknown):
                    self.mark_bombs(unknown)
                    self.bombs -= len(unknown)
                else:
                    c += 1
                    continue
                nr, nc = unknown[0][0], unknown[0][1]
                if nr * self.COLS + nc < r * self.COLS + c:
                    r, c = nr, nc
                r = 0 if r == 0 else r - 1
            r += 1
        self.complete_border_neighbors()

    def scan_perimeter_pieces_for_bombs(self, perimeter):
        """
        scans for bombs in all perimeter integer pieces around unknown squares
        """
        updates = 0
        for space in perimeter:
            r, c = space[0], space[1]
            square = self.mf[r][c]
            idx = r * self.COLS + c
            unknown = self.find_neighbors(idx, '?')
            bombs = self.find_neighbors(idx, 'x')
            if len(bombs) == square:
                updates += 1
                self.open_list(unknown)
            elif square - len(bombs) == len(unknown):
                updates += 1
                self.mark_bombs(unknown)
                self.bombs -= len(unknown)
        return updates

    def find_integers_next_to_unknown_spaces(self, unknown):
        """
        finds all perimeter integer spaces around the unknown spaces
        """
        perimeter = set()
        for space in unknown:
            idx = space[0] * self.COLS + space[1]
            int_neighbors = self.find_neighbors(idx, 'int')
            for n in int_neighbors:
                idx = n[0] * self.COLS + n[1]
                perimeter.add(idx)
        perimeter = sorted(list(perimeter))
        for i in range(len(perimeter)):
            idx = perimeter[i]
            r = idx // self.COLS
            c = idx - (r * self.COLS)
            perimeter[i] = [r, c]
        return perimeter

    def guess_is_valid_bomb_placement(self, perimeter, unknown):
        """
        DETERMINES IF PERIMETER IS VALID BASED ON BOMB PLACEMENTS
        """
        for space in perimeter:
            r, c = space[0], space[1]
            square = self.mf[r][c]
            idx = r * self.COLS + c
            unknown = self.find_neighbors(idx, '?', test=True)
            bombs = self.find_neighbors(idx, 'x')
            if len(bombs) != square:
                return False
        return True

    def clean_field_of_bomb_guesses(self, unknown, i, end):
        """
        cleans board of guesses, resets to '?'
        """
        numbers = []
        while i < end:
            r, c = unknown[i][0], unknown[i][1]
            if self.mf[r][c] != 'x':
                numbers.append([r, c])
            self.mf[r][c] = '?'
            i += 1
        return numbers

    def brute_force_combo_check(self, unknown, perimeter, bombs):
        """
        checks potential bomb combinations using a brute force algo
        """
        guesses = []
        for combo in itertools.combinations(
            [x for x in range(len(unknown))], bombs
        ):
            guess_combo = []
            for i in combo:
                r, c = unknown[i][0], unknown[i][1]
                self.mf[r][c] = 'x'
                guess_combo.append([r, c])
            if self.guess_is_valid_bomb_placement(perimeter, unknown) is True:
                numbers = self.clean_field_of_bomb_guesses(unknown, 0, len(unknown))
                guesses.append({
                    'bombs': guess_combo,
                    'numbers': numbers
                })
            else:
                self.clean_field_of_bomb_guesses(unknown, 0, len(unknown))
        return guesses

    def find_patterns_in_guesses(self, all_guesses):
        """
        Attempts to find all common bombs and numbers from all potential bomb patterns
        """
        com_n, com_b = {}, {}
        for guess in all_guesses:
            n, b = guess['numbers'], guess['bombs']
            nidx, bidx = [s[0] * self.COLS + s[1] for s in n], [s[0] * self.COLS + s[1] for s in b]
            if com_n == {}:
                com_n, com_b = set(nidx), set(bidx)
                continue
            com_n, com_b = com_n.intersection(set(nidx)), com_b.intersection(set(bidx))
        com_n = [[i // self.COLS, i - (i // self.COLS) * self.COLS] for i in com_n]
        com_b = [[i // self.COLS, i - (i // self.COLS) * self.COLS] for i in com_b]
        if len(com_n) > 0:
            self.open_list(list(com_n))
        if len(com_b) > 0:
            self.mark_bombs(list(com_b))
            self.bombs -= len(com_b)
        return 1 if len(com_n) > 0  or len(com_b) > 0 else 0

    def do_handle_unknown_spaces(self, unknown):
        """
        checks unrevealed spaces using a variety of logical computations
        """
        perimeter = self.find_integers_next_to_unknown_spaces(unknown)
        updates, all_guesses = 0, []
        potential_bombs = len(unknown) if len(unknown) < self.bombs else self.bombs
        total_unknown = self.find_unknown_spaces(total=True)
        start = self.bombs if len(total_unknown) == len(unknown) else 1
        for bombs in range(start, potential_bombs + 1):
            guesses = self.brute_force_combo_check(
                unknown, perimeter, bombs
            )
            for guess in guesses:
                all_guesses.append(guess)
        if len(all_guesses) == 1:
            self.mark_bombs(all_guesses[0]['bombs'])
            self.bombs -= len(all_guesses[0]['bombs'])
            self.open_list(all_guesses[0]['numbers'])
            if self.bombs == 0:
                i = 0
                while i < len(unknown):
                    r, c = unknown[i][0], unknown[i][1]
                    if self.mf[r][c] != '?':
                        del unknown[i]
                    else:
                        i += 1
                self.open_list(unknown)
                updates -= 1
            updates += 1
        else:
            updates += self.find_patterns_in_guesses(all_guesses)
        updates += self.scan_perimeter_pieces_for_bombs(perimeter)
        return None if updates == 0 else True

    def find_unknown_spaces(self, total=False):
        """
        returns a list of all unkown spaces that are not completely
        surrounded by '?' unknown spaces, except if input variable
        total is True, then all unknowns are returned
        """
        unknown = []
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.mf[r][c] == '?':
                    idx = r * self.COLS + c
                    int_neighbors = self.find_neighbors(idx, 'int')
                    bombs = self.find_neighbors(idx, 'x')
                    unknown_neighbors = self.find_neighbors(idx, '?')
                    known_spaces = len(int_neighbors) + len(bombs)
                    if (known_spaces > 0) or total is True:
                        unknown.append([r, c])
        return unknown

    def solve_remaining_unknowns(self):
        """
        recursively handles all remaining unknown sections until
        no changes are made or until the entire board is revealed
        """
        unknown = self.find_unknown_spaces()
        updates = self.do_handle_unknown_spaces(unknown)
        if updates is None or self.bombs == 0: return
        return self.solve_remaining_unknowns()

    def make_return_object(self):
        """
        returns string of current state of the mine field board
        """
        unknown = self.find_unknown_spaces(total=True)
        if self.bombs == 0:
            self.open_list(unknown)
            unknown = self.find_unknown_spaces(total=True)
        if self.bombs == len(unknown):
            self.mark_bombs(unknown)
        obj = '\n'.join([' '.join([str(x) for x in row]) for row in self.mf])
        return '?' if '?' in obj else obj


def solve_mine(mine_field, n):
    """
    solves MineSweeper from input mine sweeper board
    """
    game = MineSweeper(mine_field, n)
    game.initial_board_scan_with_basic_logic()
    game.solve_remaining_unknowns()
    result = game.make_return_object()
    return result

def run_testing_suite():
    """
    runs mine solver on all tests from mine_field.py
    """
    global RESULT
    for i in range(len(mf)):
        mine_field, RESULT = mf[i], r[i]
        N = RESULT.count('x')
        RESULT = RESULT.split('\n')
        for x in range(len(RESULT)):
            RESULT[x] = RESULT[x].split(' ')
        print('beginning to solve new mine field # {}...'.format(i))
        print('UNSOLVED Mine Field:')
        print("{}".format(mine_field))
        starttime = datetime.now()
        answer = solve_mine(mine_field, N)
        endtime = datetime.now()
        print('time to solve... {}'.format(endtime - starttime))
        print('SOLVED Mine Field:')
        print('Mine Field Requires Guesses' if answer == '?' else answer)

if __name__ == "__main__":
    """
    MAIN APP, calls solve_mine
    """
    run_testing_suite()