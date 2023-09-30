# In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:
#
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors
# Task:
# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".
#
# Inputs
# Values will be given as one of "rock", "paper", "scissors", "lizard", "spock".
#
#
#
# FUNDAMENTALSLOGIC
# Solution
def rpsls(p1, p2):
    var = "rock lizard spock scissors paper spock rock scissors lizard paper rock"
    return ("Player 1 Won!" if f"{p1} {p2}" in var else "Player 2 Won!" if f"{p2} {p1}" in var else "Draw!")