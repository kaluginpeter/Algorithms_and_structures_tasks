# This clicker game is destroying my thumbs!
# I'm way too lazy to play this...
#
# That's it: from now on, I refuse to click the screen any more than strictly necessary.
#
# Rules
# Your starting balance is 0 cash. Your starting cpc is up.
# A single click gains you cpc cash.
# You may spend cpc^3 cash to upgrade. This increases your cpc by up and can be done any number of times.
# Upgrading requires a click!
# Task
# Function parameters are non-negative integers up and goal.
# Return the minimum number of clicks required to reach the cash goal, as an integer. If this is impossible, return -1.
# Spent cash does not compound to the goal: the goal is reached when your current balance is at least as much as the goal.
# Examples
# clicker_solver(up = 2, goal = 6) --> 3
# Click 3 times, gaining 6 cash.
# clicker_solver(up = 2, goal = 24) --> 11
# Click 4 times, gaining 8 cash.
# Buy upgrade (this entails a click): cpc increases to 4, no cash left.
# Click 6 times, gaining 24 cash.
# clicker_solver(up = 5, goal = 3030) --> 329
# Click 25 times, gaining 125 cash.
# Buy upgrade (this entails a click): cpc increases to 10, no cash left.
# Click 100 times, gaining 1000 cash.
# Buy upgrade (this entails a click): cpc increases to 15, no cash left.
# Click 202 times, gaining 3030 cash.
# Alternative solution: instead of buying the second upgrade, click 203 more times.
#
# Performance
# Approx. 600 cases from the test suite also evaluate performance: up ranges from 2 to 40 and goal goes up to 10^10!
# The reference solution executes with O(log n) taking less than 1s.
# Game SolversGamesMathematicsNumPyPerformancePuzzlesSimulation
# Solution
from math import ceil


def clicker_solver(up: int, goal: int) -> int:
    if not up:
        return 0 if not goal else -1
    cpc: int = up
    prev: int = ceil(goal / up)
    money: int = 0
    cur: int = 0
    while True:
        next_upgrade: int = cpc ** 3
        additional_steps: int = max(0, ceil((next_upgrade - money) / cpc))
        cur += additional_steps + 1
        money = money + additional_steps * cpc - next_upgrade
        cpc += up
        if cur + ceil(max(0, goal - money) / cpc) <= prev:
            prev = cur + ceil(max(0, goal - money) / cpc)
        else:
            break

    return prev