# Description:
# Move all exclamation marks to the end of the sentence
#
# Examples
# "Hi!"          ---> "Hi!"
# "Hi! Hi!"      ---> "Hi Hi!!"
# "Hi! Hi! Hi!"  ---> "Hi Hi Hi!!!"
# "Hi! !Hi Hi!"  ---> "Hi Hi Hi!!!"
# "Hi! Hi!! Hi!" ---> "Hi Hi Hi!!!!"
# FUNDAMENTALS
# Solution
def remove(s):
    count = s.count('!')
    return s.replace('!', '') + '!'*count