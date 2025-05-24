# The Midnight Escape
# Story (Lore)
# As the campfire's last embers fade, a group of friends realizes they've lost track of time. The forest's darkness envelops them, and they must return to civilization before dawn. However, a rickety-old bridge stands between them and safety. With only one flashlight and limited time, they face a critical challenge. Can you help them devise the most efficient strategy to cross the treacherous bridge and make it home safely?
#
# Problem Description
# You are tasked with creating an algorithm to help a group of people cross a narrow bridge in the shortest possible time. The bridge can only support two people at once, and a flashlight must be carried on every crossing. There is only one flashlight available.
#
# Input
# An unordered array of tuples, where each tuple contains:
# A string representing a person's name (unique)
# An integer representing the time (in minutes) it takes that person to cross the bridge (not unique)
# Output
# An array of arrays, where each inner array represents a crossing:
# Even-indexed arrays contain the name(s) of person(s) crossing to the destination side
# Odd-indexed arrays contain the name(s) of person(s) returning to the starting side
# Rules
# Only 1 or 2 people can cross the bridge at a time.
# A flashlight must be carried on every crossing, and there is only 1 flashlight.
# When two people cross together, they move at the pace of the slower person.
# All people must reach the destination side of the bridge; no one can be left behind.
# Names within a crossing can be in any order.
# If multiple solutions with the fastest time exist, any one is acceptable.
# Constraints
# Performance constraints: O(n log n) expected.
# The number of people will be between 1 and 10,000.
# Each person's crossing time will be between 1 and 45 minutes.
# Example
# Note: depending on your programming language, a tuple can be an array or other equivalent data structure instead.
#
# Input:
#
# [("Alice", 1), ("Bob", 4), ("Charlie", 5), ("David", 8)]
# Output:
#
# [
#   [ 'Alice', 'David' ],
#   [ 'Alice' ],
#   [ 'Alice', 'Charlie' ],
#   [ 'Alice' ],
#   [ 'Alice', 'Bob' ]
# ]
# Solution breakdown:
#
# Alice and David cross (8 minutes)
# Alice returns (1 minute)
# Alice and Charlie cross (5 minutes)
# Alice returns (1 minute)
# Alice and Bob cross (4 minutes)
# Total time: 8 + 1 + 5 + 1 + 4 = 19 minutes
#
# Remember that these people need to get home before dawn. Get them across the bridge fast!
#
# Good luck, have fun!
#
# AlgorithmsRiddlesPerformance
# Solution
def solve(people):
    if len(people) == 1:
        return [[people[0][0]]]
    people.sort(key=lambda x: x[1])
    names = [p[0] for p in people]
    times = [p[1] for p in people]
    i = j = len(people) - 1

    result = []
    n = len(people)

    while n > 3:
        option1 = times[0] + times[i] + times[0] + times[i - 1]
        option2 = times[0] + times[1] + times[i] + times[1]

        if option1 < option2:
            result.append([names[0], names[i]])
            result.append([names[0]])
            result.append([names[0], names[i - 1]])
            result.append([names[0]])
        else:
            result.append([names[0], names[1]])
            result.append([names[0]])
            result.append([names[i - 1], names[i]])
            result.append([names[1]])
        n -= 2
        i -= 2

    if n == 3:
        result.append([names[0], names[2]])
        result.append([names[0]])
        result.append([names[0], names[1]])
    elif n == 2: result.append([names[0], names[1]])
    else: result.append([names[0]])

    return result