# ##Task: You have to write a function add which takes two binary numbers as strings and returns their sum as a string.
#
# ##Note:
#
# You are not allowed to convert binary to decimal & vice versa.
# The sum should contain No leading zeroes.
# ##Examples:
#
# add('111','10'); => '1001'
# add('1101','101'); => '10010'
# add('1101','10111') => '100100'
# BinaryBitsFundamentals
# Solution
def add(bin1, bin2):
    result = []
    carry = 0
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    for i in range(max_len - 1, -1, -1):
        bit1 = 1 if bin1[i] == '1' else 0
        bit2 = 1 if bin2[i] == '1' else 0
        total = bit1 + bit2 + carry
        if total >= 2:
            result.append('0' if total % 2 == 0 else '1')
            carry = 1
        else:
            result.append('0' if total == 0 else '1')
            carry = 0
    if carry:
        result.append('1')
    while len(result) > 1 and result[-1] == '0':
        result.pop()
    result.reverse()
    return ''.join(result)