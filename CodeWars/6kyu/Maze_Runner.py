# Introduction
# Welcome Adventurer. Your aim is to navigate the maze and reach the
# finish point without touching any walls. Doing so will kill you instantly!
# Task
# You will be given a 2D array of the maze and an array of directions.
# Your task is to follow the directions given. If you reach the end point
# before all your moves have gone, you should return Finish. If you hit any
# walls or go outside the maze border, you should return Dead. If you find
# yourself still in the maze after using all the moves, you should return Lost.
# The Maze array will look like
#
# maze = [[1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,3],
#         [1,0,1,0,1,0,1],
#         [0,0,1,0,0,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,2,1,0,1,0,1]]
# ..with the following key
#
#       0 = Safe place to walk
#       1 = Wall
#       2 = Start Point
#       3 = Finish Point
#   direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
# Rules
# 1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
#
# 2. The start and finish positions will change for the final tests.
#
# 3. The directions array will always be in upper case and will be
# in the format of N = North, E = East, W = West and S = South.
#
# 4. If you reach the end point before all your moves have gone, you should return Finish.
#
# 5. If you hit any walls or go outside the maze border, you should return Dead.
#
# 6. If you find yourself still in the maze after using all the moves, you should return Lost.
# Good luck, and stay safe!
#
# Kata Series
# If you enjoyed this, then please try one of my other Katas.
# Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.
#
# Rank
# Maze Runner
#
# Rank
# Scooby Doo Puzzle
#
# Rank
# Driving License
#
# Rank
# Connect 4
#
# Rank
# Vending Machine
#
# Rank
# Snakes and Ladders
#
# Rank
# Mastermind
#
# Rank
# Guess Who?
#
# Rank
# Am I safe to drive?
#
# Rank
# Mexican Wave
#
# Rank
# Pigs in a Pen
#
# Rank
# Hungry Hippos
#
# Rank
# Plenty of Fish in the Pond
#
# Rank
# Fruit Machine
#
# Rank
# Car Park Escape
#
# ARRAYSFUNDAMENTALS
# Solution
def maze_runner(maze, directions):
    startX = 0 ; startY = 0
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[x][y] == 2:
                startX = y
                startY = x
    for dire in directions:
        if dire == "N": startY = startY - 1
        if dire == "E": startX = startX + 1
        if dire == "S": startY = startY + 1
        if dire == "W": startX = startX -1
        if startY < 0 or startY > len(maze)-1 or startX < 0 or startX > len(maze)-1 or maze[startY][startX] == 1: return "Dead"
        if maze[startY][startX] == 3: return "Finish"
    return "Lost"