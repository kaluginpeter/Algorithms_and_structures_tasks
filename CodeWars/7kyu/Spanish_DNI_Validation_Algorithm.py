# Spanish DNI Validation Algorithm
# In this kata, you are tasked with validating Spanish National Identity Numbers (DNI). A valid Spanish DNI consists of 8 digits followed by a letter. The letter is determined based on the 8-digit number using a specific algorithm.
#
# Problem Statement
# You need to implement a function that validates a given Spanish DNI number. The function should return true/True if the DNI is valid and false/False otherwise.
#
# DNI Format
# A valid Spanish DNI follows this structure:
#
# 8 digits followed by 1 letter.
# Example: 12345678A.
# The letter is calculated based on the 8-digit number. The algorithm is as follows:
#
# Divide the 8-digit number by 23.
# The remainder of the division will correspond to a specific letter.
# The correspondence between the remainder and the letter is fixed and follows a specific order.
# Letter Mapping
# The letter corresponding to the remainder of the division is chosen from a predefined list of letters. The mapping between the number and the letter is as follows:
#
# Remainder (mod 23)	Letter
# 0	T
# 1	R
# 2	W
# 3	A
# 4	G
# 5	M
# 6	Y
# 7	F
# 8	P
# 9	D
# 10	X
# 11	B
# 12	N
# 13	J
# 14	Z
# 15	S
# 16	Q
# 17	V
# 18	H
# 19	L
# 20	C
# 21	K
# 22	E
# Validation Rules
# The input string should strictly follow the format:
# 8 digits followed by 1 uppercase letter.
# If the letter does not correspond to the number (as per the division and remainder mapping), the function should return false/False.
# If the input contains whitespace, you should return false/False.
# Example
# Valid DNI Example:
#
# 12345678Z: This is a valid DNI because:
# 12345678 % 23 = 14, which corresponds to the letter Z in the table.
# Invalid DNI Example:
#
# 12345678A: This is an invalid DNI because:
# 12345678 % 23 = 14, the letter at that position should be Z, not A.
# Requirements
# Implement a method called isValid(String document) that accepts a String representing the Spanish DNI number.
# The method should return:
# true/True if the DNI is valid.
# false/False if the DNI is invalid.