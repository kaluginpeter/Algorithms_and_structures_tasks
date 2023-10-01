# Story
# Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.
#
# Task
# Your mission:
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
#
# A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
#
# Examples:
# checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
# DATE TIMESTRINGSFUNDAMENTALS
# Solution
from datetime import date
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    month = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
            'November': 11, 'December': 12}
    if entered_code is correct_code:
        current_date = current_date.replace(',', '')
        expiration_date = expiration_date.replace(',', '')
        formatted_current = [month.get(i) if i in month.keys() else int(i) for i in current_date.split()]
        formatted_expiration = [month.get(i) if i in month.keys() else int(i) for i in expiration_date.split()]
        to_date_current = date(formatted_current[2], formatted_current[0], formatted_current[1])
        to_date_formatted_expiration = date(formatted_expiration[2], formatted_expiration[0], formatted_expiration[1])
        if to_date_current <= to_date_formatted_expiration:
            return True
        return False
    return False