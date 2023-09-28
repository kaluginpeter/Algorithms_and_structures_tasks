# Description:
# Remove all exclamation marks from sentence except at the end.
#
# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!!!"
# "!Hi"     ---> "Hi"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi"
# FUNDAMENTALS
# Solution
def remove(s):
    count = 0
    j = s
    while j.endswith('!'):
        count += 1
        j = j[:-1]
    r = (len(s)-len(j))
    return j.replace('!', '') + '!' * r