# Task
# When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a note with a strange, coded message.
#
# Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.
#
# The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.
#
# Example
# For note = "you'll n4v4r 6u4ss 8t: cdja",
#
# the output should be "you'll never guess it: 2390".
#
# Input/Output
# [input] string note
#
# A string consisting of lowercase English letters, digits, punctuation marks and whitespace characters (' ').
#
# Constraints: 0 ≤ note.length ≤ 500.
#
# [output] a string
#
# The deciphered note.
#
# Puzzles
# Solution
def stolen_lunch(note):
    return ''.join(ch if ((not ch.isalpha() and not ch.isdigit()) or (not ch.isdigit() and ch > 'j')) else chr(int(ch) + 97) if ch.isdigit() else str(ord(ch) - 97) for ch in note)