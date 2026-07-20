# Once upon a time, more precisely upon BASIC time, there were 2 functions named LEFT$ and RIGHT$ (I wrote them uppercase because it was the custom in those early years).
#
# These functions let you read left(/right)-most characters of a string.
#
# use: LEFT$ (str, i) -> returns i left-most characters of str.
# - eg:
# A$="ABCDEFG":PRINT LEFT$(A$,3) - prints ABC
# and RIGHT$ (str, i ), of course, returns i right-most characters of str.
#
# So, your mission is...
# ...to write 2 functions that will work as the BASIC ones did... except :
#
# if i is an integer:
# i may be a negative integer. In this case the function returns the whole string but i right(/left)-most chars (respectively in left$(/right$) function).
# if i === 0 : returns an empty string;
# if no i is provided consider it should be 1 ( not zero ).
# if i is greater than str length : returns the whole str.
# if i is a string: returns part of str at left(/right) of i.
# returns left of first occurence of i
# returns right of last occurence of i
# If i is not a substring of str, return the empty string.
# Examples:
# text = 'Hello (not so) cruel World!'
#
# ##== with integer as 2nd argument ==
# left(text,5)   # -> 'Hello'
# left(text,-22) # -> 'Hello'
# left(text,1)   # -> 'H'
# left(text)     # -> i defaults to 1
# left(text,0)   # -> ''
# left(text,99)  # -> 'Hello (not so) cruel World!'
#
# right(text,6)  # -> 'World!'
# right(text)    # -> '!' (i defaults to 1)
#
# #== with string as 2nd argument ==
# left(text,'o') # -> 'Hell'
# right(text,'o')# -> 'rld!'
# left(text,' ') # -> 'Hello'
# left(text, 'xyz') # -> '' (substring not found)
# StringsFundamentals
# Solution
def left(s: str, i=1) -> str:
    if isinstance(i, int):
        if i == 0: return ""
        if i < 0: return s[:len(s) + i]
        return s[:i]
    pos = s.find(i)
    return "" if pos == -1 else s[:pos]


def right(s: str, i=1) -> str:
    if isinstance(i, int):
        if i == 0: return ""
        if i < 0: return s[-(len(s) + i):]
        return s[-i:] if i <= len(s) else s
    pos = s.rfind(i)
    return "" if pos == -1 else s[pos + len(i):]