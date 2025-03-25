# Your task is to get Zodiac Sign using input day and month.
#
# For example:
#
# get_zodiac_sign(1,5) => 'Taurus'
# get_zodiac_sign(10,10) => 'Libra'
# Correct answers are (preloaded):
#
# SIGNS = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
# P.S. Each argument is correct integer number.
#
# WESTERN ASTROLOGY STAR SIGN DATES
#
# Aries (March 21-April 19)
# Taurus (April 20-May 20)
# Gemini (May 21-June 20)
# Cancer (June 21-July 22)
# Leo (July 23-August 22)
# Virgo (August 23-September 22)
# Libra (September 23-October 22)
# Scorpio (October 23-November 21)
# Sagittarius (November 22-December 21)
# Capricorn (December 22-January 19)
# Aquarius (January 20 to February 18)
# Pisces (February 19 to March 20)
# Fundamentals
# Solution spaghetti code
def get_zodiac_sign(day, month):
    if (month >= 12 and day >= 22) or (month == 1 and day <= 19): return SIGNS[0]
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18): return SIGNS[1]
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): return SIGNS[2]
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): return SIGNS[3]
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return SIGNS[4]
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return SIGNS[5]
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return SIGNS[6]
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return SIGNS[7]
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return SIGNS[8]
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return SIGNS[9]
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return SIGNS[10]
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return SIGNS[11]