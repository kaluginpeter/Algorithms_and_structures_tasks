# Story:
# Alex is a great fan of Snooker and he likes recording the results of his favorite players by recording the balls that fall into the pockets of the table. He asks you to help him with a program that calculates the points a player scored in a given set using his notes.
# Unfortunatly his notes are quiet a mess ...
#
# Task:
# Given his short hand notation as string, calculate the points a player scored in a set.
# He codes the ball colors with letters:
#
# R = red (1 point)
# Y = yellow (2 points)
# G = green (3 points)
# Bn = brown (4 points)
# Be = blue (5 points)
# P = pink (6 points)
# Bk = black (7 points)
# W = white (no points because it's a foul)
# The color may be followed by a number 'R12' would stand for 12 red balls pocketed. If there is no number given, the ball was pocketed once.
# "R15P3G1Bk4Y1Bn1Be3" or "R13Bk14YRGBnBkRBePBk1"
#
# Sometimes Alex forgets that he already wrote down a color and records it multiple times.
#
# For your convenience the points for each color are provided as hash / dictionary with the name 'blz'.
#
# If the string include white ball("W"-symbol) - return 'Foul'
# for example: "G9G11P9Bn2Bn1Be10G7WBn10G3"
# If the total score is more than 147 - 'invalid data'
# for example: "Bn14Bn14Bn8P9"
#
# StringsArrays
# Solution
def frame(balls):
    if 'W' in balls: return 'Foul'
    score: int = 0
    i: int = 0
    while i < len(balls):
        for key, point in blz.items():
            if balls[i:].startswith(key):
                i += len(key)
                x: int = 0
                while i < len(balls) and balls[i].isdigit():
                    x = x * 10 + int(balls[i])
                    i += 1
                score += point * max(x, 1)
        if score > 147: return 'invalid data'
    return score