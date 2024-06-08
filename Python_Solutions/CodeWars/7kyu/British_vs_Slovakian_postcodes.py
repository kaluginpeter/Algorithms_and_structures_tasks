# Task
# Write a function called which_postcode/whichPostcode that takes a string, and determines whether it represents a British or Slovakian postcode. If the string is a valid British postcode, return "GB". If it's a valid Slovakian postcode, return "SK". If the input is neither a valid British nor a valid Slovakian postcode, return "Not valid".
#
# Leading and trailing spaces should be ignored, but if there are spaces in wrong place in the middle of the postcode, then it is invalid.
#
# The input will always be a valid British postcode, a valid Slovakian postcode or an invalid postcode.
#
# British Postcodes
# To be considered valid, a British postcode must follow the rules below:
#
# Consists a mix of letters and numbers, seperated to two segments by a single space.
# First segment must start with either 1 or 2 letters, followed by 1 or 2 numbers. Example: G4, G40, DN4 or DN11
# Second segment must start with a digit, followed by 2 letters. Example: 1AB
# British postcodes are not case-sensitive, so Se21 7aA is a valid postcode.
#
# Slovakian Postcodes
# Consists of 5 numbers, where the first 3 are seperated by a space from the last 2 numbers. Example: 123 45.
# Examples
# Valid British postcodes:
#   G4 7AH
# G12 8NU
# Dn1 1aA
# SE21 7AA
# Valid Slovakian postcodes:
#  040 01
# 810 08
# 984 59
# Invalid postcodes:
# 0765 820 - Should only have 3 numbers in the first segment, 2 numbers in the second segment
# SE 21 7AA - Should only contain 2 segments
# 070  08 - Should have single space separating the two segments, not double space
# REGULAR EXPRESSIONSSTRINGS