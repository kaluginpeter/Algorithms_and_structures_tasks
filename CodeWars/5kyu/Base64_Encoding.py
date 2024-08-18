# Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.
#
# Example (input -> output):
# 'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
# You can learn more about Base64 encoding and decoding here.
#
# Note: This kata uses the non-padding version ("=" is not added to the end).
#
# BINARYSTRINGSALGORITHMS
# Solution
from base64 import b64encode, b64decode


def to_base_64(string):
    return b64encode(string.encode('ascii')).decode('ascii').replace('=', '')


def from_base_64(string):
    try:
        return b64decode((string + '=').encode('ascii'), '-_').decode('ascii')
    except:
        return b64decode((string + '==').encode('ascii'), '-_').decode('ascii')