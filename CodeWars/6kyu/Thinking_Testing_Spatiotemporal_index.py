# No Story
#
# No Description
#
# Only by Thinking and Testing
#
# Look at the results of the testcases, and guess the code!
#
# Series:
# A and B?
# Incomplete string
# True or False
# Something capitalized
# Uniq or not Uniq
# Spatiotemporal index
# Math of Primary School
# Math of Middle school
# From nothingness To nothingness
# Not perfect? Throw away!
# Welcome to take the bus
# A happy day will come
# Sum of 15(Hetu Luosliu)
# Nebula or Vortex
# Sport Star
# Falsetto Rap Concert
# Wind whispers
# Mobile phone simulator
# Join but not join
# I hate big and small
# I want to become diabetic ;-)
# How many blocks?
# Operator hidden in a string
# Substring Magic
# Report about something
# Retention and discard I
# Retention and discard II
# How many "word"?
# Hail and Waterfall
# Love Forever
# Digital swimming pool
# Archery contest
# The repair of parchment
# Who are you?
# Safe position
# Special recommendation
# Another series, innovative and interesting, medium difficulty. People who like challenges, can try these kata:
#
# Play Tetris : Shape anastomosis
# Play FlappyBird : Advance Bravely
# PUZZLESARRAYS
# Solution
distance: dict[str, int] = {'mm': 1, 'cm': 10, 'dm': 100, 'm': 1_000, 'km': 1_000_000}
time: dict[str, int] = {'ms': 1, 's': 1_000, 'm': 60_000, 'h': 3_600_000 , 'd': 86_400_000}

def check(sentence: list[str]) -> tuple[bool, str]:
    units: list[str] = list()
    for i in sentence:
        units.append(i[get_metric(i):])
    if all(i in distance for i in units): return True, 'distance'
    elif all(i in time for i in units): return True, 'time'
    return False, None

def get_metric(unit):
    idx: int = 0
    while unit[idx] in '0123456789':
        idx += 1
    return idx

def testit(a):
    metrics: bool = check(a)
    if metrics[0] is False: return metrics[1]
    elif metrics[1] == 'distance':
        a.sort(key=lambda x: int(x[:get_metric(x)]) * distance.get(x[get_metric(x):]))
        return a
    else:
        a.sort(key=lambda x: int(x[:get_metric(x)]) * time.get(x[get_metric(x):]))
        return a