# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
#
# FUNDAMENTALSSTRINGS
# Solution
def remove_exclamation_marks(s):
    return ''.join( word for word in s if word not in '!')