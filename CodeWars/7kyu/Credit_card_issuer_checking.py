# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
#
# Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.
#
# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |
# Examples
# get_issuer(4111111111111111) == "VISA"
# get_issuer(4111111111111) == "VISA"
# get_issuer(4012888888881881) == "VISA"
# get_issuer(378282246310005) == "AMEX"
# get_issuer(6011111111111117) == "Discover"
# get_issuer(5105105105105100) == "Mastercard"
# get_issuer(5105105105105106) == "Mastercard"
# get_issuer(9111111111111111) == "Unknown"
# ALGORITHMS
# Solution
def get_issuer(number):
    card = str(number)
    nums = len(card)
    if card[:2] in ("34", "37") and nums == 15:return "AMEX"
    elif card[:4] == "6011" and nums == 16:return "Discover"
    elif 51 <= int(card[:2]) <= 55 and nums == 16:return "Mastercard"
    elif card[0] == "4" and nums in (13, 16):return "VISA"
    return "Unknown"