# You are given a small extract of a catalog:
#
# s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>
#
# <prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>
#
# <prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>
#
# <prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>
#
# <prod><name>saw</name><prx>9</prx><qty>10</qty></prod>
#
# ...
# (prx stands for price, qty for quantity) and an article i.e "saw".
#
# The function catalog(s, "saw") returns the line(s) corresponding to the article with $ before the prices:
#
# "table saw > prx: $1099.99 qty: 5\nsaw > prx: $9 qty: 10\n..."
# If the article is not in the catalog return "Nothing".
#
# Notes
# There is a blank line between two lines of the catalog.
#
# The same article may appear more than once. If that happens return all the lines concerned by the article (in the same order as in the catalog; however see below a note for Prolog language).
#
# The line separator of results may depend on the language \nor \r\n. In Pascal \n is replaced by LineEnding.
#
# in Perl use "£" instead of "$" before the prices.
#
# You can see examples in the "Sample tests".
#
# Note for Prolog language
# If the article is not in the catalog then R equals "".
#
# R substrings (separated by "\n") must be in alphabetic order.
#
# FUNDAMENTALSSTRINGS
# Solution
def catalog(s, article):
    s = s.split('\n')
    ans: list = []
    for i in s:
        if article in i:
            x = i.replace('<prod>', '').replace('</prod>', '').replace('<name>', '').replace('</name>', '')
            x = x.replace('<prx>', ' > prx: $').replace('</prx>', '').replace('<qty>', ' qty: ').replace('</qty>', '')
            ans.append(x)
    return '\r\n'.join(ans) if ans else 'Nothing'