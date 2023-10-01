# Write a regex to validate a 24 hours time string. See examples to figure out what you should check for:
#
# Accepted: 01:00 - 1:00
#
# Not accepted:
#
# 24:00
#
# You should check for correct length and no spaces.
#
# REGULAR EXPRESSIONSDATE TIMEFUNDAMENTALS
# Solution
import re
def validate_time(timestamp):
    return bool(re.match(r'(2[0-3]|[01]?\d):[0-5]\d$', timestamp))