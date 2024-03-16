# Task
# Pac-Man got lucky today! Due to minor performance issue all his enemies have frozen. Too bad Pac-Man is not brave enough to face them right now, so he doesn't want any enemy to see him.
#
# Given a gamefield of size N x N, Pac-Man's position(PM) and his enemies' positions(enemies), your task is to count the number of coins he can collect without being seen.
#
# An enemy can see a Pac-Man if they are standing on the same row or column.
#
# It is guaranteed that no enemy can see Pac-Man on the starting position. There is a coin on each empty square (i.e. where there is no Pac-Man or enemy).
#
# Example
# For N = 4, PM = [3, 0], enemies = [[1, 2]], the result should be 3.
#
# Let O represent coins, P - Pac-Man and E - enemy.
# OOOO
# OOEO
# OOOO
# POOO
# Pac-Man cannot cross row 1 and column 2.
#
# He can only collect coins from points (2, 0), (2, 1) and (3, 1), like this:
#
# x is the points that Pac-Man can collect the coins.
# OOOO
# OOEO
# xxOO
# PxOO
# Input/Output
# [input] integer N
# The field size.
#
# [input] integer array PM
# Pac-Man's position (pair of integers)
#
# [input] 2D integer array enemies
# Enemies' positions (array of pairs)
#
# [output] an integer
# Number of coins Pac-Man can collect.
#
# More PacMan Katas
# Play PacMan: Devour all
#
# Play PacMan 2: The way home
#
# ALGORITHMSPUZZLES
# Solution
def pac_man(n, pm, enemies):
    mtrx: list = [[True] * n for i in range(n)]
    ans: int = 0
    for i in enemies:
        for j in range(n):
            mtrx[i[0]][j] = False
            mtrx[j][i[1]] = False
            if pm[1] < i[1]:
                for rows in range(i[1], n):
                    print(j, rows)
                    mtrx[j][rows] = False
            else:
                for rows in range(i[1] + 1):
                    mtrx[j][rows] = False
    for i in enemies:
        if pm[0] > i[0]:
            for r in range(i[0] + 1):
                for c in range(n):
                    mtrx[r][c] = False
        else:
            for r in range(i[0], n):
                for c in range(n):
                    mtrx[r][c] = False
    for i in range(n):
        for j in range(n):
            ans += mtrx[i][j]
    return ans - 1