# Write a function that accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.
#
# (5, 4)   ---> "5 is greater than 4"
# (-4, -7) ---> "-4 is greater than -7"
# (2, 2)   ---> "2 is equal to 2"
# There is only one problem...
#
# You cannot use if statements, and you cannot use the ternary operator ? :.
#
# In fact the word if and the character ? are not allowed in your code.
#
# You are always welcome to check out some of my other katas:
# Very Easy (Kyu 8)
#
# Add Numbers
#
# Easy (Kyu 7-6)
#
# Convert Color image to greyscale
# Array Transformations
# Basic Compression
# Find Primes in Range
# No Ifs No Buts
#
# Medium (Kyu 5-4)
#
# Identify Frames In An Image
# Photoshop Like - Magic Wand
# Scientific Notation
# Vending Machine - FSA
# Find Matching Parenthesis
#
# Hard (Kyu 3-2)
#
# Ascii Art Generator
#
# RESTRICTEDFUNDAMENTALS
# Solution
def no_ifs_no_buts(a, b):
    dictionary = {a < b:'smaller than', a == b:'equal to', a > b: 'greater than'}
    return f'{a} is {dictionary[True]} {b}'