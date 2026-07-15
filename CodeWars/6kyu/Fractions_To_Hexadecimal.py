# Suppose I want to change the improper fraction 41/4 to hexadecimal. The decimal equivalent of 41/4 is 10.25. The integer part is easy: 10 = a (hexadecimal). The fractional part is 0.25 = 1/4 = 4/16. But the first place to the right of the hexadecimal point in base 16 is 16ths place. So 41/4 = 10 4/16 = a.4 in hexadecimal.
#
# Write a function f2hex() that takes a non-negative fraction in string form and converts it to hexadecimal. Carry your answer out to six hexadecimal places but remove trailing zeroes and trailing hexadecimal points.
#
# Examples
# f2hex('1/2') → '0.8'
# f2hex('3/4') → '0.c'
# f2hex('88/1') → '58'
# f2hex('99/98') → '1.029cbc'
# f2hex('7/7') → '1'
# Mathematics
# Solution
def f2hex(fraction):
    num, den = map(int, fraction.split("/"))
    whole = num // den
    rem = num % den
    whole_hex = hex(whole)[2:]
    if not rem: return whole_hex
    digits = []
    for _ in range(6):
        rem *= 16
        digits.append("0123456789abcdef"[rem // den])
        rem %= den
    while digits and digits[-1] == "0": digits.pop()
    if digits: return whole_hex + "." + "".join(digits)
    return whole_hex