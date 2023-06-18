# Write a method that takes a number and returns a string of that number in English.
#
# Your method should be able to handle any number between 0 and 99999. If the given number is outside of that range or not an integer, the method should return an empty string.
#
# Examples
# 0      -->  "zero"
# 27     -->  "twenty seven"
# 100    -->  "one hundred"
# 7012   -->  "seven thousand twelve"
# 99205  -->  "ninety nine thousand two hundred five"
# STRINGSPARSINGALGORITHMS
# Solution
def number_to_english(n):
    d={0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30:'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 1000: 'one thousand'}
    if n<0 or n>99999 or type(n)==float: return ''
    elif n<=20 or n in (20,30,40,50,60,70,80,90,100,1000): return d[n]
    elif 20<=n<100:
        a = int(str(n)[0])
        return f'{number_to_english(a*10)} {number_to_english(n%10)}'
    elif 100<n<1000:
        if n%100==0:
            return f'{number_to_english(n//100)} hundred'
        return f'{number_to_english(n//100)} hundred {number_to_english(n%100)}'
    elif 1000<n<=99999:
        if n%1000==0:
            return f'{number_to_english(n//1000)} thousand'
        return f'{number_to_english(n//1000)} thousand {number_to_english(n%1000)}'