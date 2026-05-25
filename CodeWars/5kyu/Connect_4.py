# Introduction
# We all love to play games especially as children. I have fond memories playing Connect 4 with my brother so decided to create this Kata based on the classic game. Connect 4 is known as several names such as “Four in a Row” and “Captain’s Mistress" but was made popular by Hasbro MB Games
# Connect 4
# Task
# The game consists of a grid (7 columns and 6 rows) and two players that take turns to drop their discs. The pieces fall straight down, occupying the next available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.
#
# Your task is to create a Class called Connect4 that has a method called play which takes one argument for the column where the player is going to place their disc.
# Rules
# If a player successfully has 4 discs horizontally, vertically or diagonally then you should return "Player n wins!” where n is the current player either 1 or 2.
#
# If a player attempts to place a disc in a column that is full then you should return ”Column full!” and the next move must be taken by the same player.
#
# If the game has been won by a player, any following moves should return ”Game has finished!”.
#
# Any other move should return ”Player n has a turn” where n is the current player either 1 or 2.
#
# Player 1 starts the game every time and alternates with player 2.
#
# The columns are numbered 0-6 left to right.
# Good luck and enjoy!
#
# Kata Series
# If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.
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
# ArraysFundamentals
# Solution
class Connect4:
    def __init__(s):
        s.b = [[0] * 7 for _ in range(6)]
        s.p = 1
        s.w = 0

    def play(s, c):
        if s.w: return 'Game has finished!'

        for r in range(5, -1, -1):
            if not s.b[r][c]:
                s.b[r][c] = p = s.p
                break
        else:
            return 'Column full!'

        for dr, dc in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            n = 1
            for d in -1, 1:
                rr, cc = r, c
                while 1:
                    rr += dr * d;
                    cc += dc * d
                    if 0 <= rr < 6 and 0 <= cc < 7 and s.b[rr][cc] == p:
                        n += 1
                    else:
                        break
            if n > 3:
                s.w = 1
                return f'Player {p} wins!'

        s.p = 3 - p
        return f'Player {p} has a turn'