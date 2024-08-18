# Implement String#ipv4_address?, which should return true if given object is an IPv4 address
# - four numbers (0-255) separated by dots.
#
# It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
#
# REGULAR EXPRESSIONSFUNDAMENTALS
# Solution
import re
def ipv4_address(address):
    regex = re.compile(r'''
    #      200-249   | 250-255 | 100-109| 0-99 110-199
    \b([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\b    
    ''', re.VERBOSE)
    mo = regex.match(address)
    if mo is None:
        return False
    elif  mo.group() == address:
        return (bool(mo))
    else:
        return False