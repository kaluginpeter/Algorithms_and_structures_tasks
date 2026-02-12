# Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.
#
# Examples
# number2words(0)  ==>  "zero"
# number2words(1)  ==>  "one"
# number2words(9)  ==>  "nine"
# number2words(10)  ==>  "ten"
# number2words(17)  ==>  "seventeen"
# number2words(20)  ==>  "twenty"
# number2words(21)  ==>  "twenty-one"
# number2words(45)  ==>  "forty-five"
# number2words(80)  ==>  "eighty"
# number2words(99)  ==>  "ninety-nine"
# number2words(100)  ==>  "one hundred"
# number2words(301)  ==>  "three hundred one"
# number2words(799)  ==>  "seven hundred ninety-nine"
# number2words(800)  ==>  "eight hundred"
# number2words(950)  ==>  "nine hundred fifty"
# number2words(1000)  ==>  "one thousand"
# number2words(1002)  ==>  "one thousand two"
# number2words(3051)  ==>  "three thousand fifty-one"
# number2words(7200)  ==>  "seven thousand two hundred"
# number2words(7219)  ==>  "seven thousand two hundred nineteen"
# number2words(8330)  ==>  "eight thousand three hundred thirty"
# number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
# number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"
# Fundamentals
# Solution
def number2words(n):
    if n == 0: return "zero"

    ones = [
        "", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]

    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def below_thousand(num):
        result = []
        if num >= 100:
            result.append(ones[num // 100])
            result.append("hundred")
            num %= 100
        if 10 <= num <= 19:
            result.append(teens[num - 10])
        else:
            if num >= 20:
                ten_part = tens[num // 10]
                if num % 10: ten_part += "-" + ones[num % 10]
                result.append(ten_part)
            elif num > 0:
                result.append(ones[num])
        return " ".join(result)

    parts = []
    if n >= 1000:
        parts.append(below_thousand(n // 1000))
        parts.append("thousand")
        n %= 1000
    if n > 0: parts.append(below_thousand(n))
    return " ".join(parts)