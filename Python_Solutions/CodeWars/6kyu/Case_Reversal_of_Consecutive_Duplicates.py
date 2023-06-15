# The aim of this Kata is to write a function which will reverse the case of
# all consecutive duplicate letters in a string. That is, any letters that occur one after the other and are identical.
#
# If the duplicate letters are lowercase then they must be set to uppercase,
# and if they are uppercase then they need to be changed to lowercase.
#
# Examples:
#
# reverse_case("puzzles")    Expected Result: "puZZles"
# reverse_case("massive")    Expected Result: "maSSive"
# reverse_case("LITTLE")     Expected Result: "LIttLE"
# reverse_case("shhh")       Expected Result: "sHHH"
# Arguments passed will include only alphabetical letters A–Z or a–z.
#
# FUNDAMENTALS
# Solution
import re
def reverse(s):
    return re.sub(r'(.)\1+', lambda x: x.group().swapcase(), s)