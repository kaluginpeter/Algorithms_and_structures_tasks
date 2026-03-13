# The Adventures of Lonk - Dungeon Analyzer
# In many classic dungeon-crawling games, such as The Legend of Zelda, dungeons are carefully designed so that players can never permanently trap themselves by using keys in the wrong order.
#
# Unfortunately, this is not one of those games.
#
# Welcome to The Legend of Zorlda, set in the proud kingdom of Hyrole, where architectural oversight is more of a “guideline” than a rule. You have recently been hired by the Royal Dungeon-Vetting Division after a series of alarming reports from the kingdom’s most courageous (and mildly confused) adventurer, Lonk.
#
# According to Lonk, some dungeons are:
#
# Completely impossible to finish.
# Technically possible, but only if you don't accidentally open the wrong door.
# "Probably fine?" (Lonk's words)
# This situation is clearly unacceptable. Princess Zorlda herself has tasked you with auditing the kingdom’s dungeons so that proper warning signs can be posted outside each entrance:
#
# "May Be Impossible"
# "May Cause Existential Regret."
# "Probably Fine."
# Your task is to analyze a dungeon and determine:
#
# Is the dungeon solvable? -- Does there exist at least one sequence of actions that reaches the goal?
#
# Is the dungeon softlock-proof? -- From every reachable game state, is it still possible to eventually reach the goal?
#
# In other words... Can Lonk save the day? And can he do so without accidentally ruining everything?
#
# Click to expand the sections below for details
#
# Dungeon Model
# Input Format
# Expected Output
# Examples
# AlgorithmsGraph Theory
# Solution
from collections import deque, defaultdict

def analyze_dungeon(dungeon):
    start = dungeon["start"]
    goal = dungeon["goal"]
    rooms = dungeon["rooms"]
    start_keys = rooms[start]["keys"]
    start_state = (start, start_keys, frozenset(), frozenset([start]))
    q = deque([start_state])
    visited = set([start_state])
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    goal_states = set()
    while q:
        room, keys, opened, collected = q.popleft()
        if room == goal: goal_states.add((room, keys, opened, collected))

        for e in rooms[room]["exits"]:
            to = e["to"]
            door = e["door"]
            new_keys = keys
            new_opened = set(opened)

            if door is not None and door not in opened:
                if new_keys == 0: continue
                new_keys -= 1
                new_opened.add(door)

            new_collected = set(collected)

            if to not in new_collected:
                new_keys += rooms[to]["keys"]
                new_collected.add(to)

            new_state = (
                to,
                new_keys,
                frozenset(new_opened),
                frozenset(new_collected),
            )

            graph[(room, keys, opened, collected)].append(new_state)
            reverse_graph[new_state].append((room, keys, opened, collected))

            if new_state not in visited:
                visited.add(new_state)
                q.append(new_state)

    solvable = any(s[0] == goal for s in visited)
    if not solvable: return (False, False)

    reachable_to_goal = set()
    q = deque(goal_states)

    while q:
        s = q.popleft()
        if s in reachable_to_goal: continue
        reachable_to_goal.add(s)
        for prev in reverse_graph[s]: q.append(prev)
    softlock_proof = all(s in reachable_to_goal for s in visited)
    return (solvable, softlock_proof)