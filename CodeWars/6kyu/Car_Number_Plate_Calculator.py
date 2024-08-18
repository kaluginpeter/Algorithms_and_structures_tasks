# Introduction
# Let’s assume that when you register a car you are assigned two numbers:
#
# Customer ID – number between 0 and 17558423 inclusively. It is assigned to car buyers in the following order:
# the first customer receives an ID of 0, the second customer receives an ID of 1, the third - 2, and so on;
#
# A Number Plate – 6-character combination composed of the series - three Latin lowercase letters
# from a to z; and the serial number - three digits from 0 to 9. Example: aaa001, xyz123, tok469;
#
# Each Number Plate is related to the given Customer ID. For example:
#
# Customer ID of 0: aaa001
#
# Customer ID of 21: aaa022
#
# Customer ID of 169: aaa170
#
# Your Task
# Write a function
# find_the_number_plate
#
# which takes the Customer ID as an argument, calculates the Number Plate corresponding to this ID and returns
# it as a string;
#
# Rules
# The serial number changes first. For each 3-letter series it goes through 001 to 999, such as: aaa001, aaa002,
# aaa003, ......, aaa998, aaa999
#
# The leftmost letter in the series switches alphabetically each time after the serial number has moved through
# 001 to 999 inclusively;
#
# aaa001...aaa999
# at this point the leftmost letter will switch alphabetically, while the serial number repeats the same cycle again;
#
# baa001...baa999,
# ...... ,
# zaa001...zaa999
# The middle letter switches alphabetically each time after the leftmost letter has moved through a to z
# and the z** series has moved through 001 to 999.
#
# zaa001...zaa999
# at this point the middle letter will switch alphabetically, while the leftmost letter and the serial
# number repeat the same cycle again;
#
# aba001...aba999,
# bba001...bba999,
# ......,
# zza001...zza999
# The rightmost letter switches alphabetically each time after the middle letter has moved through
# a to z and the zz* series has moved through 001 to 999.
#
# zza001...zza999
# at this point the rightmost letter will switch alphabetically, while the middle letter,
# the leftmost letter, and the serial number repeat the same cycle again;
#
# aab001...aab999,
# bab001...bab999,
# ......,
# zab001...zab999,
# abb001...abb999,
# bbb001...bbb999,
# ......,
# zbb001...zbb999,
# acb001...acb999,
# ......,
# zzz001...zzz999
# Note
# If the serial number has less than 3 digits, the missing places should be adjusted with zeroes.
# i.e: 12 should equal 012; 4 should equal 004.
#
# Once again, the customer ID starts with 0.
#
# Good luck!
# ALGORITHMSLOGICMATHEMATICSFUNDAMENTALS
# Solution
def find_the_number_plate(i):
    return f'{97+i//999%26:c}{97+i//999//26%26:c}{97+i//999//26//26:c}{1+i%999:03}'