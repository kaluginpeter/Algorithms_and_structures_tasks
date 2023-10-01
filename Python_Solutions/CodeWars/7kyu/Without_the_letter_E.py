# Is it possible to write a book without the letter 'e' ?
#
# Task
# Given String str, return:
#
# How many "e" does it contain (case-insensitive) in string format.
# If given String doesn't contain any "e", return: "There is no "e"."
# If given String is empty, return empty String.
# If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`
# REGULAR EXPRESSIONSSTRINGSFUNDAMENTALS
# Solution
def find_e(s):
    try:
        c = str(s.lower().count('e'))
        return c if s != '' and int(c) > 0 else 'There is no "e".' if int(c) == 0 and s!='' else '' if s == '' else None
    except:
        return None