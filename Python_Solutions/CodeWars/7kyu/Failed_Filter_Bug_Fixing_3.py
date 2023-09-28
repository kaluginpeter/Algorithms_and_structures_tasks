# Failed Filter - Bug Fixing #3
# Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the FilterNumber function to remove all the numbers from the string.
# STRINGSDEBUGGING
# Solution
def filter_numbers(string):
    return "".join(x for x in string if not x.isdigit())