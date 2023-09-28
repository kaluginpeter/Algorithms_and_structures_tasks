# Create a function that returns a villain name based on the user's birthday. The birthday will be passed to the function as a valid Date object, so for simplicity, there's no need to worry about converting strings to dates.
#
# The first name will come from the month, and the last name will come from the last digit of the date:
#
# Month -> first name
#
# January -> "The Evil"
# February -> "The Vile"
# March -> "The Cruel"
# April -> "The Trashy"
# May -> "The Despicable"
# June -> "The Embarrassing"
# July -> "The Disreputable"
# August -> "The Atrocious"
# September -> "The Twirling"
# October -> "The Orange"
# November -> "The Terrifying"
# December -> "The Awkward"
# Last digit of date -> last name
#
# 0 -> "Mustache"
# 1 -> "Pickle"
# 2 -> "Hood Ornament"
# 3 -> "Raisin"
# 4 -> "Recycling Bin"
# 5 -> "Potato"
# 6 -> "Tomato"
# 7 -> "House Cat"
# 8 -> "Teaspoon"
# 9 -> "Laundry Basket"
# The returned value should be a string in the form of "First Name Last Name".
#
# For example, a birthday of November 18 would return "The Terrifying Teaspoon"
#
# ARRAYSDATE TIMEFUNDAMENTALS
# Solution
def get_villain_name(birthdate):
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    return first[birthdate.month - 1] + ' ' + last[int(str(birthdate.day)[-1])]