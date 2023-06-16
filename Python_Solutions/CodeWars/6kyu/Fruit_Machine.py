# Introduction
# Slot machine (American English), informally fruit machine (British English), puggy (Scottish English slang),
# the slots (Canadian and American English), poker machine (or pokies in slang)
# (Australian English and New Zealand English) or simply slot (American English),
# is a casino gambling machine with three or more reels which spin when a button is pushed.
# Slot machines are also known as one-armed bandits because they were originally operated by
# one lever on the side of the machine as distinct from a button on the front panel, and because
# of their ability to leave the player in debt and impoverished. Many modern machines are still
# equipped with a legacy lever in addition to the button. (Source Wikipedia)
#
# Task
# You will be given three reels of different images and told at which index the reels stop.
# From this information your job is to return the score of the resulted reels.
# Rules
# 1. There are always exactly three reels
#
# 2. Each reel has 10 different items.
#
# 3. The three reel inputs may be different.
#
# 4. The spin array represents the index of where the reels finish.
#
# 5. The three spin inputs may be different
#
# 6. Three of the same is worth more than two of the same
#
# 7. Two of the same plus one "Wild" is double the score.
#
# 8. No matching items returns 0.
# Scoring
# Item
# Three of the same
# Two of the same
# Two of the same plus one Wild
# Wild
# 100
# 10
# N/A
# Star
# 90
# 9
# 18
# Bell
# 80
# 8
# 16
# Shell
# 70
# 7
# 14
# Seven
# 60
# 6
# 12
# Cherry
# 50
# 5
# 10
# Bar
# 40
# 4
# 8
# King
# 30
# 3
# 6
# Queen
# 20
# 2
# 4
# Jack
# 10
# 1
# 2
#
#
# Returns
# Return an integer of the score.
# Example
# Initialise
# reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
# reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
# reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
# spin = [5,5,5]
# result = fruit([reel1,reel2,reel3],spin)
# Scoring
# reel1[5] == "Cherry"
# reel2[5] == "Cherry"
# reel3[5] == "Cherry"
#
# Cherry + Cherry + Cherry == 50
# Return
# result == 50
# Good luck and enjoy!
#
# Kata Series
# If you enjoyed this, then please try one of my other Katas. Any feedback,
# translations and grading of beta Katas are greatly appreciated. Thank you.
#
# Rank
# Maze Runner
#
# Rank
# Scooby Doo Puzzle
#
# Rank
# Driving License
#
# Rank
# Connect 4
#
# Rank
# Vending Machine
#
# Rank
# Snakes and Ladders
#
# Rank
# Mastermind
#
# Rank
# Guess Who?
#
# Rank
# Am I safe to drive?
#
# Rank
# Mexican Wave
#
# Rank
# Pigs in a Pen
#
# Rank
# Hungry Hippos
#
# Rank
# Plenty of Fish in the Pond
#
# Rank
# Fruit Machine
#
# Rank
# Car Park Escape
#
# ARRAYSGAMESFUNDAMENTALS