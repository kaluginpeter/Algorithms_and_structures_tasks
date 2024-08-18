# Similar but fairly harder version : Linked
# Create a function that takes a integer number n and returns the formula for
# formula(0)  --> "1"
# formula(1)  --> "a+b"
# formula(2)  --> "a^2+2ab+b^2"
# formula(-2) --> "1/(a^2+2ab+b^2)"
# formula(3)  --> "a^3+3a^2b+3ab^2+b^3"
# formula(5)  --> "a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5"
# The formula for n=5 is like so :
# So the answer would look like so : a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5
#
# Important notes :
# Your string may not have spaces so you can't do this : a^5 + 5a^4 b + 10a^3 b^2...
# You will show raised to power of by ^ and not using **.
# You need not put * between each multiplication
# There is no need to show a^1 or b^1 since that is basically a and b
# a^0 and/or b^0 also don't need be shown instead be a normal person and use 1 since that is what they equate to.
# You will need to handle both positive and negative numbers + 0
# Note :
# You will not be tested for float (only negative integers and whole numbers)
# input n goes from -200 to 200.
# You will need to use BigInt since otherewise it will not work for both JS and Java
# MATHEMATICSALGEBRASTRINGS
# Solution
from math import comb as c
def formula(n):
    return f'1/({formula(-n)})' if n<0 else '+'.join(f"{[str(c(n,i)),''][c(n,i)==1]}{['','a',f'a^{n-i}'][(n-i>0)+(n-i>1)]}{['','b',f'b^{i}'][(i>0)+(i>1)]}" for i in range(n+1)) or '1'