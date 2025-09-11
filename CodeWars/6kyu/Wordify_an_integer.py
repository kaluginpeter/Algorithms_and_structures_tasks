# Turn a given number (an integer > 0, < 1000) into the equivalent English words. For the purposes of this kata, no hyphen is needed in numbers 21-99.
#
# Examples:
#
# 1   --> "one"
# 12  --> "twelve"
# 17  --> "seventeen"
# 56  --> "fifty six"
# 90  --> "ninety"
# 326 --> "three hundred twenty six"
# Based on "Speech module" mission from Checkio.
#
# Algorithms
# Solution
def wordify(n):
    ones = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n >= 100:
        if n % 100: return "{0} hundred {1}".format(wordify(n // 100), wordify(n % 100))
        else: return "{0} hundred".format(wordify(n // 100))
    if n < 20: return ones[n]
    return "{0}{1}".format(tens[n // 10], " {0}".format(wordify(n % 10)) if n % 10 else "")