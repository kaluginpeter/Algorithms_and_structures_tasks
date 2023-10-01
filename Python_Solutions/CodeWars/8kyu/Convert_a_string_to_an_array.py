# Write a function to split a string and convert it into an array of words.
#
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
# ARRAYSSTRINGSFUNDAMENTALS
# Solution
def string_to_array(s):
    return s.split() if s != '' else ['']