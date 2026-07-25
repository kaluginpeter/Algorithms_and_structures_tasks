# HI! You have the array of sheeps:
#
# ['sheep', 'sheep', 'sheep', 'sheep'...]
#
# But somebody is "sick":
#
# ['shpee', 'sheep', 'hspee', 'sheep', 'pehes'...]
#
# You can help them:
#
# shpee => sheep
#
# pehes => sheep
#
# Because shpee and pehes have 1 s, 1 h, 2 e, 1 p.
#
# shep !=> sheep
#
# And:
#
# sheeep !=> sheep
#
# return array(list) with "sheep". if you can't help - delete.
#
# Hard register!!!
# A!==a
#
# Example:
# ShEep !=> sheep
#
# EXAMPLE:
#
# ['sheep', 'Shpee', 'pEhEs', 'PPh', 'heep', 'phees']
# return:
#
# ['sheep', 'sheep']
# Good luck!!!
#
# Arrays
# Solution
is_valid = lambda sheep: sorted(sheep) == sorted('sheep')
def reload_sheeps(arr):
    return ['sheep' for sheep in arr if is_valid(sheep)]