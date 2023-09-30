# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0.
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def move_ten(st):
    d = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    return ''.join(d[d.index(i)+10] for i in st)