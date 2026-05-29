# Failure on the factory floor!! One box of 'deluxe' ball-bearings has been mixed in with all the boxes of 'normal' ball-bearings! We need your help to identify the right box!
#
# Information
# What you know about the bearings:
#
# 'deluxe' ball-bearings weigh exactly 11 grams
# 'normal' ball-bearings weigh exactly 10 grams
# Besides weight, both kinds of ball-bearings are identical
# There are (effectively) infinite bearings in each box
# Each box contains exclusively one type of bearing (either regular, or 'deluxe')
# To help you identify the right box, you also have access to a Super Scale™ which will tell you the exact weight of anything you give it. Unfortunately, getting it ready for each measurement takes a long time, so you only have time to use it once!
#
# Task
# Write a function which accepts two arguments:
#
# bearings: A list of the bearing types contained in each 'box'. (length between 1 and 200 inclusive)
# weigh: a function which accepts any number of arguments, returning the total weight of all. Can only be used once!
# Your function should identify and return the single 'deluxe' bearing sample from bearings.
#
# Example
# def identify_bb(bearings, weigh):
#     a, b, c = bearings
#     if weigh(a, b) == 20:
#         # bearings 'a' and 'b' must both be 10, so 'c' must be deluxe
#         return c
#     if weigh(a) == 10: # Error: weigh has already been used!
#         return b
#     return a
# Note: modules sys and inspect have been disabled.
#
# Try some other riddle kata:
# Hat Game
# Extreme Hat Game
# Hat Game 2
# Riddles
# Solution
def identify_bb(bearings, weigh):
    samples = []
    for i, bearing in enumerate(bearings):
        samples.extend([bearing] * (i + 1))
    actual = weigh(*samples)
    expected = 10 * (len(bearings) * (len(bearings) + 1) // 2)
    deluxe_index = actual - expected - 1
    return bearings[deluxe_index]