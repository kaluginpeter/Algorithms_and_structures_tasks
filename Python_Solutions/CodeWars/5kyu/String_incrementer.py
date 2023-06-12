# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.
# Solution
def increment_string(strng):
    stripped = strng.rstrip('1234567890')
    ints = strng[len(stripped):]
    if len(ints) == 0:
        return strng + '1'
    else:
        length_word = len(ints)
        new_ints = int(ints) + 1
        new_ints = str(new_ints).zfill(length_word)
        return stripped + new_ints