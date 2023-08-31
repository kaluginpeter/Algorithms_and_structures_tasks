# Given the string representations of two integers, return the string representation of the sum of those integers.
#
# For example:
#
# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
#
# I have removed the use of BigInteger and BigDecimal in java
#
# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
#
# STRINGSBIG INTEGERSALGORITHMS
# Solution
def sum_strings(x, y):
    if len(x)> len(y):
        temp = x
        x = y
        y = temp
    str3, n1, n2 = "", len(x), len(y)
    diff, carry = n2 - n1, 0
    for i in range(n1-1, -1, -1):
        sum = ((ord(x[i]) - ord('0')) + int((ord(y[i + diff]) - ord('0'))) + carry)
        str3 = str3 + str(sum%10)
        carry = sum//10
    for i in range(n2-n1-1, -1, -1):
        sum = ((ord(y[i]) - ord('0')) + carry)
        str3 = str3 + str(sum%10 )
        carry = sum//10
    if carry:
        print(carry, str3)
        str3 += str(carry)
    str3 = str3[::-1]
    if not str3:
        return '0'
    if str3[0] == '0':
        str3 = str3[1:]
    return str3 if str3 else '0'