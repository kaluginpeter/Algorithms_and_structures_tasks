# Happy Holidays fellow Code Warriors!
# It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa! Wait... when exactly do we need to do that?
#
# Time for Milk and Cookies
# Complete the function function that accepts a Date object, and returns true if it's Christmas Eve (December 24th), false otherwise.
#
# Examples
# time_for_milk_and_cookies(date(2013, 12, 24))  # True
# time_for_milk_and_cookies(date(2013, 1, 23))   # False
# time_for_milk_and_cookies(date(3000, 12, 24))  # True
# DATE TIMEFUNDAMENTALS
# Solution
def time_for_milk_and_cookies(dt):
    return str(dt)[-5:-3] == '12' and str(dt)[-2:] == '24'