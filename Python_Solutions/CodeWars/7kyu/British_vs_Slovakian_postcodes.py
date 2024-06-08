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
# Solution
from string import digits, ascii_lowercase, ascii_uppercase
STRING = ascii_lowercase + ascii_uppercase
def check_british_postcode(postcode):
    if postcode.count(' ') != 1: return False
    first, second = postcode.split()
    letters = dgts = ''
    while first and first[0] in STRING:
        letters += first[0]
        first = first[1:]
    while first and first[0] in digits:
        dgts += first[0]
        first = first[1:]
    if first: return False
    if any(len(i) not in {1, 2} for i in [letters, dgts]): return False
    if len(second) != 3: return False
    if second[0] not in digits: return False
    if not all(i in STRING for i in second[1:]): return False
    return True

def check_slovakian_postcode(postcode):
    if len(postcode) != 6: return False
    if postcode.count(' ') != 1: return False
    first, second = postcode.split()
    if len(first) != 3: return False
    return all(i in digits for i in first + second)

def which_postcode(postcode):
    postcode = postcode.strip()
    if check_british_postcode(postcode): return 'GB'
    elif check_slovakian_postcode(postcode): return 'SK'
    return 'Not valid'