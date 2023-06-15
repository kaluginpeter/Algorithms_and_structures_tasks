# After yet another dispute on their game the Bingo Association decides to change course and automate the game.
#
# Can you help the association by writing a method to create a random Bingo card?
#
# Bingo Cards
# A Bingo card contains 24 unique and random numbers according to this scheme:
#
# 5 numbers from the B column in the range 1 to 15
# 5 numbers from the I column in the range 16 to 30
# 4 numbers from the N column in the range 31 to 45
# 5 numbers from the G column in the range 46 to 60
# 5 numbers from the O column in the range 61 to 75
# Task
# Write the function get_card()/getCard(). The card must be returned as an array of Bingo style numbers:
#
# [ 'B14', 'B12', 'B5', 'B6', 'B3', 'I28', 'I27', ... ]
# The numbers must be in the order of their column:
# B, I, N, G, O. Within the columns the order of the numbers is random.
#
# a bingo card
#
# GAMESALGORITHMS
# Solution
from random import randint
def get_bingo_card():
    CHARS = ['B', 'I', 'N', 'G', 'O']
    INTERVALS = [(1, 15), (16, 30), (31, 45), (46, 60), (61,75)]
    ITERATIONS = [5, 5, 4, 5, 5]
    l, top = [0] * 24, 0
    for i in range(5):
        start, end, char = INTERVALS[i][0], INTERVALS[i][1], CHARS[i]
        for j in range(ITERATIONS[i]):
            flag = False
            while not flag:
                el = str(randint(start, end))
                if char + el not in l:
                    flag = True
                    l[top] = char + el
            top += 1
    return l