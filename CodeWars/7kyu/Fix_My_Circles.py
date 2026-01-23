# Story
# You are a geometricist, a humble member of an ancient, secret order dedicated to creating geometric shapes for use in people's daily lives around the world. One day, you arrive at work to find that a wild Ouroboros has eaten into your circle supply, corrupting many of them! Without these circles, trigonometric functions will cease to exist. People will be unable to study AC power systems. And worst of all, the world will no longer be able to produce LOLLIPOPS! 🍭
#
# You must fix the corrupted circles as soon as possible - before the world turns square!
#
# Task
# Write a function circle_mender that takes as an input a string representing a circle with some holes and returns the same string with the holes filled.
#
# The input has the following characteristics:
#
# It is a string representing an ASCII-art circle;
# It consists of exactly 20 lines, each with 40 characters followed by a newline character;
# The circle is drawn using the pound sign (#), and any holes within it are represented by spaces ( );
# The edges of the circle are never missing.
# Below are some examples to better represent what it is that is expected:
#
# Example 1:
# -------
# Input:
#
#
#
#                          #####
#                    #################
#                  #####           #####
#                 ####               ####
#                ######            #######
#                 #######     ###########
#                  #####################
#                    #################
#                          #####
#
#
#
#
#
#
#
#
# -------
# Output:
#
#
#
#                          #####
#                    #################
#                  #####################
#                 #######################
#                #########################
#                 #######################
#                  #####################
#                    #################
#                          #####
#
#
#
#
#
#
#
#
# Example 2:
# -------
# Input:
#
#
#           #####
#     #################
#   #######     #########
#  ######         ########
# #######           #######
#  ####               ####
#   #####           #####
#     #################
#           #####
#
#
#
#
#
#
#
#
#
# -------
# Output:
#
#
#           #####
#     #################
#   #####################
#  #######################
# #########################
#  #######################
#   #####################
#     #################
#           #####
#
#
#
#
#
#
#
#
#
# Example 3:
# -------
# Input:
#
#
#
#
#
#
#
#                  #####
#          #####################
#       ###########################
#     ########     ##################
#   ########         ##################
#   ##########     ####     ###########
#  ##############             ##########
#   ###########             ###########
#   #############             #########
#     #################     #########
#       ###########################
#          #####################
#                  #####
# -------
# Output:
#
#
#
#
#
#
#
#                  #####
#          #####################
#       ###########################
#     ###############################
#   ###################################
#   ###################################
#  #####################################
#   ###################################
#   ###################################
#     ###############################
#       ###########################
#          #####################
#                  #####
# AlgorithmsASCII ArtStrings
# Solution
from collections import deque

def circle_mender(content: str) -> str:
    rows = content.splitlines()
    h, w = 20, 40
    grid = [list(row) for row in rows]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    for r in range(h):
        for c in (0, w - 1):
            if grid[r][c] == ' ' and not visited[r][c]:
                q.append((r, c))
                visited[r][c] = True
    for c in range(w):
        for r in (0, h - 1):
            if grid[r][c] == ' ' and not visited[r][c]:
                q.append((r, c))
                visited[r][c] = True
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if grid[nr][nc] == ' ' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    for r in range(h):
        for c in range(w):
            if grid[r][c] == ' ' and not visited[r][c]:
                grid[r][c] = '#'
    return "\n".join("".join(row) for row in grid) + "\n"