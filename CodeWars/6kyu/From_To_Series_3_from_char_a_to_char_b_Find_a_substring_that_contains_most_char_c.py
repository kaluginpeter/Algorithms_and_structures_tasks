# Description:
# Give you a string s, find a substring that starting with character a and ending with character b and contains most numbers of character c.
#
# Please note:
#
# The characters in the string can be: letters(a-z,A-Z), numbers(0-9), some punctuation marks(,.()[]{}) and space;
#
# a,b and c are three diffrent characters;
#
# Characters a and b can not appear in the middle of the substring;
#
# You should count the numbers of character c in the substring, instead of the length of the substring;
#
# A valid substring is only can from a to b, the substring from b to a is invalid;
#
# If more than one substring found, returns the first result(from left to right).
#
# If string s doesn't contains such a substring(from a to b and contains c), return "".
#
# Examples
# s="abacbaccb", a = "a", b = "b", c = "c"
# findSub(s,a,b,c) === "accb"
#
# s="abacbaccbbccca", a = "a", b = "b", c = "c"
# findSub(s,a,b,c) === "accb"
#
# s="x.z.z.yxzzzy", a = "x", b = "y", c = "z"
# findSub(s,a,b,c) === "xzzzy"
#
# s="x.z.z.z.yxzzzy", a = "x", b = "y", c = "z"
# findSub(s,a,b,c) === "x.z.z.z.y"
#
# s="xyx.yx..y", a = "x", b = "y", c = "z"
# findSub(s,a,b,c) === ""
#
# s="((( )))((  ))", a = "(", b = ")", c = " "
# findSub(s,a,b,c) === "(  )"
# FUNDAMENTALS
# Solution
def find_sub(s, a, b, c):
    output: str = ''
    count_output: int = 0
    a_idx: int = 0
    c_count: int = 0
    is_valid: bool = False
    for b_idx in range(len(s)):
        if s[b_idx] == a:
            if is_valid:
                c_count = 0
                a_idx = b_idx
            else:
                a_idx = b_idx
                is_valid = True
        if s[b_idx] == b:
            if not is_valid: continue
            if c_count > count_output:
                count_output = c_count
                output = s[a_idx:b_idx + 1]
            c_count = 0
            is_valid = False
        elif s[b_idx] == c and is_valid: c_count += 1
    return output