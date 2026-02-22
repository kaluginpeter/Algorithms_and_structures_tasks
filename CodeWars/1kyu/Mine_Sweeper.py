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