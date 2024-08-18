# No Story
#
# No Description
#
# Only by Thinking and Testing
#
# Look at result of testcase, guess the code!
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
# PUZZLESGAMES
# Solution
def testit(act, s):
    return ''.join('x' if (s[i] == '_' and act[i] != 'run') else '/' if (s[i] == '|' and act[i] != 'jump') else s[i] for i in range(len(s)))