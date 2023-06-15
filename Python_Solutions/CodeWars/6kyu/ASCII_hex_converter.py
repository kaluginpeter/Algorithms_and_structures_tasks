# Write a module Converter that can take ASCII text and convert it to hexadecimal.
# The class should also be able to take hexadecimal and convert it to ASCII text.
# To make the conversion well defined, each ASCII character is represented by exactly two hex digits,
# left-padding with a 0 if needed. The conversion from ascii
# to hex should produce lowercase strings (i.e. f6 instead of F6).
#
# Example
# Converter.to_hex("Look mom, no hands")
# => "4c6f6f6b206d6f6d2c206e6f2068616e6473"
#
# Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
# => "Look mom, no hands"
# FUNDAMENTALSBITSSTRINGS
# Solution
class Converter():
    @staticmethod
    def to_ascii(h):
        return bytes.fromhex(h).decode()
    @staticmethod
    def to_hex(s):
        return ''.join(hex(ord(i))[2:] for i in s)