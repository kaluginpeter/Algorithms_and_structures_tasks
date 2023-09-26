# Batman & Robin have gotten into quite a pickle this time. The Joker has mixed up their iconic quotes and also replaced one of the characters in their names, with a number. They need help getting things back in order.
#
# Implement the getQuote method which takes in an array of quotes, and a string comprised of letters and a single number (e.g. "Rob1n") where the number corresponds to their quote indexed in the passed in array.
#
# Return the quote along with the character who said it:
#
# BatmanQuotes.getQuote(["I am vengeance. I am the night. I am Batman!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"], "Rob1n") should output =>  "Robin: Holy haberdashery, Batman!
# Hint: You are guaranteed that the number in the passed in string is placed somewhere after the first character of the string. The quotes either belong to "Batman", "Robin", or "Joker".
#
# ARRAYSFUNDAMENTALS
# Solution
class BatmanQuotes(object):
    l = ['Batman', 'Robin', 'Joker']
    @staticmethod
    def get_quote(quotes, hero):
        i = next((int(x) for x in hero if x.isdigit()))
        return BatmanQuotes.l[i] + ": " + quotes[i]