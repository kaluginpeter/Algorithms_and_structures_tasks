# Description:
# Remove all exclamation marks from the end of sentence.
#
# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"
# FUNDAMENTALS
# Solution
def remove(s):
    while s.endswith('!'):
        s = s[:-1]
    return s