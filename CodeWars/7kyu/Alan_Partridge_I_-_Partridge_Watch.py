# Backstory
#
# To celebrate today's launch of my Hero's new book: Alan Partridge: Nomad, We have a new series of kata arranged around the great man himself.
#
# Task
# Given an array of terms, if any of those terms relate to Alan Partridge, return Mine's a Pint!
#
# The number of exclamation mark (!) after the t should be determined by the number of Alan related terms you find in the given array (x). The related terms are as follows:
#
# Partridge
# PearTree
# Chat
# Dan
# Toblerone
# Lynn
# AlphaPapa
# Nomad
# If you don't find any related terms, return Lynn, I've pierced my foot on a spike!!
#
# Other katas in this series:
# Alan Partridge II - Apple Turnover
# Alan Partridge III - London
#
# FUNDAMENTALSARRAYSSTRINGS
# Solution
def part(arr):
    l = ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    s = sum(1 for i in arr if i in l)
    return f"Mine's a Pint{'!'*s}" if any(i in l for i in arr) else "Lynn, I've pierced my foot on a spike!!"