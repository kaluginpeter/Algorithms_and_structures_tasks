# I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.
#
# Example:
#
# n = 5;
#
# st = "This is an example string";
#
# Return value:
# Thisi
# sanex
# ample
# strin
# g
#
# Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'
# STRINGSFUNDAMENTALS
# Solution
def string_breakers(n, st):
    st = st.replace(' ', '')
    l = []
    s = len(st)//n if len(st) % n == 0 else len(st)// n + 1
    for i in range(s):
        l.append(st[:n])
        st = st[n:]
    return '\n'.join(l)