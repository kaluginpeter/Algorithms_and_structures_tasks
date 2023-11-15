# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
#
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"
# STRINGSALGORITHMSDATE TIME
# Solution
def what_century(year):
    x = (int(year) - 1) // 100 + 1
    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= x % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(x % 10, 'th')
    return str(x) + suffix