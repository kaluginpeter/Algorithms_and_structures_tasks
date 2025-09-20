# Problem Description
#                           ,▄▀▀▀▀▀▀▀▄
#                        ▄P▀     ⁿ '  ▀▄ ,,,
#                     ,Æ▀          ▌]▄▀▀    ╙▀▄
#                   ,▀'         ' ▄▀▌  ▌    ═,▐▀N▄,
#                 ▄▀"           ²  '        ▌¬ ▄╘ `▀▄
#             ▄Æ▀└¬ ▐ ²                              ▀▄
#           ▄▀    *  ⌐             ╒  ┌ ," ²   ┌       ▀▄
#         ▄▀  ┐           ` ',▄▄▄▄,". /  ,ⁿ, ,▄▄mm▄,     ▀N▄
#       ,█¬⌐   ═       ,"▄Æ▀'      `▀▄╓⌐  ▐▄▀-   MÆ;▀▄ ▌▄   ▀▄
#      Æ└ ═ ^   ∞  `  ▄Æ▀─∞           ▀▀▄▀         ═  ▀N,▄  ▄▀
#     ▌╙⌐ + '   ∞  ▄Æ▀',,▄ .           ⌐`▀▄ ∞           `▀▄▀
#     ▀▄ ¬ *└⌐ ▄P▀¬ ╓      ╓`,         `╓  ▀▄╛ ∞*          "█
#  ▄▀▌▀▀▀█▀N▄P▀ `        ,           ╒w      ▀█ " +"╓ª┌      █
# █▄ * ▄A▀▄▀r"⌐ "⌐    "           ,            ▀▄═ ▄═▐,▄,▄▄▄▀└
#   ª-, ▄▀═ ^;" ;  ▌   "         ,*▄`           ╙█▄▄█▄▄▄    "
#        └▀▀▄', ∞ `   ⌐¬  ,  ,   └  ²       ═ ,▄Æ▀ ▀▄▄▄▌▄█
#            ▀▀▄▓▄▓▄▄▄▄▄  '      "⌐ ⌐ ,▄mM▀▀▀█▀▀▀▄▄▄
#          ▐██▌  +  -   ▐▀▀▀═MM∞∞∞MP▀▀ , "╒▀'`╤]▄▄▄A▀
# This Kata is the second in the Do a Smart Guess collection series. If you haven't solved the first Kata, check it out: Find Out the Number of Gold Coins!.
#
# After dealing with the guardian in the last Kata, you and your friends continue the RPG campaign, and now you encounter a mysterious wizard.
#
# The wizard promises to give you a legendary magic item, but for that you must guess the number of grains of magic sand that are in the wizard's bag. For this, he gives the following tips:
#
# 1
# 1. If the number of grains were divided between
# m
# 1
# m
# 1
# ​
#   people,
# a
# 1
# a
# 1
# ​
#   grains would be left.
#
# 2
# 2. If the number of grains were divided between
# m
# 2
# m
# 2
# ​
#   people,
# a
# 2
# a
# 2
# ​
#   grains would be left.
#
# 3
# 3. If the number of grains were divided between
# m
# 3
# m
# 3
# ​
#   people,
# a
# 3
# a
# 3
# ​
#   grains would be left.
#
# ⋮
# N
# N. If the number of grains were divided between
# m
# N
# m
# N
# ​
#   people,
# a
# N
# a
# N
# ​
#   grains would be left.
#
# Of course
# m
# i
# m
# i
# ​
#   is always a positive integer and
# 0
# ≤
# a
# i
# <
# m
# i
# 0≤a
# i
# ​
#  <m
# i
# ​
#  .
#
# The wizard doesn't seem very trustworthy, so he might be trying to trick you, and there aren't any number of grains of sand that satisfy the conditions he gives.
#
# Your Task
# Given the wizard information, write the function number_of_grains that returns the minimum number of grains of magic sand in the wizard's bag.
#
# This function receives information in the form of a list of tuples:
#
# [(a1, m1), (a2, m2), ... , (aN, mN)]
# If the wizard is trying to trick you, and there is no number of grains of sand that satisfies the given information, your function should return None.
#
# Example
#
# Suppose that the tips from the wizard are:
#
# 1
# 1. If the number of grains were divided between
# 4
# 4 people,
# 3
# 3 grains would be left.
#
# 2
# 2. If the number of grains were divided between
# 6
# 6 people,
# 1
# 1 grain would be left.
#
# So, the minimum number of grains of sand is 7, because 7 is the smallest number that when divided by 4 has remainder 3 and when divided by 6 has remainder 1. Thus:
#
# number_of_grains([(3, 4), (1, 6)]) = 7
# Suppose the wizard gave one more tip:
#
# 3
# 3. If the number of grains were divided between
# 2
# 2 people, no grain would be left.
# In this case, the problem has no solution, because there is no number that divided by 2 has a remainder of 0 (that is, an even number) that when divided by 4 has a remainder of 3. Thus:
#
# number_of_grains([(3, 4), (1, 6), (0, 2)]) = None
# Performance Requirements
# Consider that the maximum input length will be 15 (that is, the wizard will give at most 15 tips,
# 1
# ≤
# N
# ≤
# 15
# 1≤N≤15).
#
# The
# m
# i
# m
# i
# ​
#   values will be always less than
# 1
# 0
# 20
# 10
# 20
#  , so the minimum number of grains of sand can be quite large. However, that shouldn't be a problem for your algorithm.
#
# Have fun coding and please don't forget to vote and rank this kata! :-)
#
# MathematicsNumber Theory
# Solution
from math import gcd

def merge(a1, m1, a2, m2):
    g = gcd(m1, m2)
    if (a2 - a1) % g != 0: return None, None
    from math import lcm
    l = m1 // g * m2
    def egcd(a, b):
        if b == 0: return (1, 0, a)
        x1, y1, g = egcd(b, a % b)
        return (y1, x1 - (a // b) * y1, g)
    x1, y1, g2 = egcd(m1, m2)
    k = ((a2 - a1) // g * x1) % (m2 // g)
    a = (a1 + m1 * k) % l
    return a, l

def number_of_grains(info):
    a, m = info[0]
    for ai, mi in info[1:]:
        a, m = merge(a, m, ai, mi)
        if a is None: return None
    return a