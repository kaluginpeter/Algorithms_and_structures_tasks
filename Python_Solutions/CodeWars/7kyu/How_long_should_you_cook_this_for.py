# You've purchased a ready-meal from the supermarket.
#
# The packaging says that you should microwave it for 4 minutes and 20 seconds, based on a 600W microwave.
#
# Oh no, your microwave is 800W! How long should you cook this for?!
#
# Input
# You'll be given 4 arguments:
#
# 1. needed power
# The power of the needed microwave.
# Example: "600W"
#
# 2. minutes
# The number of minutes shown on the package.
# Example: 4
#
# 3. seconds
# The number of seconds shown on the package.
# Example: 20
#
# 4. power
# The power of your microwave.
# Example: "800W"
#
# Output
# The amount of time you should cook the meal for formatted as a string.
# Example: "3 minutes 15 seconds"
#
# Note: the result should be rounded up.
#
# 59.2 sec  -->  60 sec  -->  return "1 minutes 0 seconds"
# All comments/feedback/translations appreciated.
# FUNDAMENTALS
# Solution
def cooking_time(needed_power, minutes, seconds, power):
    x, x_sec = int(needed_power[:-1]), minutes * 60 + seconds
    y = int(power[:-1])
    y_sec = x * x_sec / y
    y_sec = int(y_sec) + 1 if int(y_sec) < y_sec else int(y_sec)
    return f'{y_sec // 60} minutes {y_sec % 60} seconds'