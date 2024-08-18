# Write a function that removes every lone 9 that is inbetween 7s.
#
# "79712312" --> "7712312"
# "79797"    --> "777"
# LOGICSTRINGSFUNDAMENTALS
# Solution
def seven_ate9(str_):
    strung_out = str_
    for i in range(len(strung_out)):
        if strung_out[i:i+3] == '797':
            strung_out = strung_out.replace('797','77')
            continue
    return strung_out