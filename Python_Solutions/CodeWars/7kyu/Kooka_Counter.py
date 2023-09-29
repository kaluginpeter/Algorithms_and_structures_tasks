# A family of kookaburras are in my backyard.
#
# I can't see them all, but I can hear them!
#
# How many kookaburras are there?
#
# Hint
# The trick to counting kookaburras is to listen carefully
#
# The males sound like HaHaHa...
#
# The females sound like hahaha...
#
# And they always alternate male/female
#
# Examples
# ha = female => 1
# Ha = male => 1
# Haha = male + female => 2
# haHa = female + male => 2
# hahahahaha = female => 1
# hahahahahaHaHaHa = female + male => 2
# HaHaHahahaHaHa = male + female + male => 3
# ^ Kata Note : No validation is necessary; only valid input will be passed :-)
#
# STRINGSALGORITHMS
# Solution
import re
def kooka_counter(laughing):
    return len(re.findall(r'(ha)+|(Ha)+',laughing))