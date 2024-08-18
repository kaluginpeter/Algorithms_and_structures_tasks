# Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.
#
# To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.
#
# the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.
#
# Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.
#
# Given a seat number, your task is to return the seat location in the following format:
#
# '2B' would return 'Front-Left'.
#
# If the number is over 60, or the letter is not valid, return 'No Seat!!'.
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def plane_seat(a):
    al: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if int(a[:-1]) > 60 or a[-1] in {'I', 'J'} or al.index(a[-1]) > 10:
        return 'No Seat!!'
    x, y = '', ''
    n = al.index(a[-1])
    if 0 <= n <= al.index('C'):
        y = 'Left'
    elif al.index('C') < n <= al.index('F'):
        y = 'Middle'
    else:
        y = 'Right'
    n = int(a[:-1])
    if 1 <= n <= 20:
        x = 'Front'
    elif 21 <= n <= 40:
        x = 'Middle'
    else:
        x = 'Back'
    return f'{x}-{y}'