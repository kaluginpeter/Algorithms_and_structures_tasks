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