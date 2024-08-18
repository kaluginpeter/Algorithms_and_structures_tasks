# Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).
#
# Each 8 bits on the binary string represent 1 character on the ASCII table.
#
# The input string will always be a valid binary string.
#
# Characters can be in the range from "00000000" to "11111111" (inclusive)
#
# Note: In the case of an empty binary string your function should return an empty string.
#
# BINARYSTRINGSFUNDAMENTALS
# Solution
import binascii
def binary_to_string(binary):
    try:
        input_string=int(binary, 2)
        Total_bytes= (input_string.bit_length() +7) // 8
        input_array = input_string.to_bytes(Total_bytes, "big")
        ASCII_value=input_array.decode()
        return ASCII_value
    except:
        return '' if binary == '' else None