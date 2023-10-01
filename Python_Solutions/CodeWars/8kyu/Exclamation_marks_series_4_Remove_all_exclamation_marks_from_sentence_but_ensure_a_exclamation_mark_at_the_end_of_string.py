# Description:
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.
#
# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!"
# "!Hi"     ---> "Hi!"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi!"
# FUNDAMENTALS
# Solution
def remove(s):
    return s.replace('!', '') + '!'