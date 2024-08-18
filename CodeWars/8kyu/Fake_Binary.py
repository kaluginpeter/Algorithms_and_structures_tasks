# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def fake_bin(x):
    word = []
    for elem in x:
        if elem in '56789':
            word.append('1')
            continue
        word.append('0')
    return ''.join(word)