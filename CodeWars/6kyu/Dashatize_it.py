# Given a variable n,
#
# If n is an integer, Return a string with dash'-'marks before and after each odd integer,
# but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.
#
# If n is not an integer, return the string "None".
#
# Ex:
#
# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'
# STRINGSARRAYSREGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')