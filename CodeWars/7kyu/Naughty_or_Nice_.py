# In this kata, you will write a function that receives an array of string and returns a string that is either 'naughty' or 'nice'. Strings that start with the letters b, f, or k are naughty. Strings that start with the letters g, s, or n are nice. Other strings are neither naughty nor nice.
#
# If there is an equal amount of bad and good actions, return 'naughty'
#
# Examples:
#
# bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
# whatListAmIOn(bad_actions)
# #-> 'naughty'
# good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
# what_list_am_i_on(good_actions)
# #-> 'nice'
# actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
# what_list_am_i_on(actions)
# #-> 'naughty'
# MathematicsFundamentals
# Solution
def what_list_am_i_on(actions):
    x: int = 0
    y: int = 0
    for string in actions:
        if string[0] in 'bfk': x += 1
        elif string[0] in 'gsn': y += 1
    return 'nice' if y > x else 'naughty'