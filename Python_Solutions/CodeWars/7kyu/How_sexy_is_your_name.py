# How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.
#
# There is a preloaded dictionary of letter scores called SCORES(Python & JavaScript) / $SCORES (Ruby). Add up the letters (case-insensitive) in your name to get your sexy score. Ignore other characters.
#
#     SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
#               'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
#               'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
#               'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}
# The program must return how sexy one's name is according to the "Sexy score ranking" chart.
#
#        score <= 60:   'NOT TOO SEXY'
#  61 <= score <= 300:  'PRETTY SEXY'
# 301 <= score <= 599:  'VERY SEXY'
#        score >= 600:  'THE ULTIMATE SEXIEST'
# FUNDAMENTALS
# Solution
def sexy_name(name):
    s = sum(SCORES[i.upper()] for i in name.replace(' ', ''))
    return 'THE ULTIMATE SEXIEST' if s >=600 else 'VERY SEXY' if 301 <= s <= 599 else 'PRETTY SEXY' if 61 <= s <= 300 else 'NOT TOO SEXY'