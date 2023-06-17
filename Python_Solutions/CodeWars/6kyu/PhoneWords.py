# Given a string of numbers, you must perform a method in which you
# will translate this string into text, based on the below image:
#
#
# For example if you get "22" return "b", if you get "222" you will return "c". If you get "2222" return "ca".
#
# Further details:
#
# 0 is a space in the string.
# 1 is used to separate letters with the same number.
# always transform the number to the letter with the maximum value, as
# long as it does not have a 1 in the middle. So, "777777" -->  "sq" and "7717777" --> "qs".
# you cannot return digits.
# Given a empty string, return empty string.
# Return a lowercase string.
# Examples:
# "443355555566604466690277733099966688"  -->  "hello how are you"
# "55282"                 -->  "kata"
# "22266631339277717777"  -->  "codewars"
# "66885551555"           -->  "null"
# "833998"                -->  "text"
# "000"                   -->  "   "
# STRINGSFUNDAMENTALS
# Solution
def phone_words(text):
    d = {
        222: 'c',
        22: 'b',
        2: 'a',
        333: 'f',
        33: 'e',
        3: 'd',
        444: 'i',
        44: 'h',
        4: 'g',
        555: 'l',
        55: 'k',
        5: 'j',
        666: 'o',
        66: 'n',
        6: 'm',
        7777: 's',
        777: 'r',
        77: 'q',
        7: 'p',
        888: 'v',
        88: 'u',
        8: 't',
        9999: 'z',
        999: 'y',
        99: 'x',
        9: 'w',
        0: ' ',
        1: ''
    }
    while (text.isdigit()):
        for i in d:
            text = text.replace(str(i), d[i])
    return text