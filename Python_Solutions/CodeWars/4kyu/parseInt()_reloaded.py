# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#
# Examples:
#
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
#
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them
# PARSINGSTRINGSALGORITHMS
# Solution
def parse_int(string):
    digits: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    teens: dict[str, int] = {
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19
    }
    tens: dict[str, int] = {
        'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
    }
    ordinal: dict[str, int] = {
        'hundred': 100, 'thousand': 1000, 'million': 1_000_000
    }
    string = string.replace('-', ' ')
    number: int = 0
    string = string.split()
    if string[0] in teens: return teens.get(string[0])
    n: int = len(string)
    idx: int = 0
    inner_num: int = 0
    while idx < n:
        char: str = string[idx]
        if char in teens:
            number += inner_num + teens.get(char)
            inner_num = 0
        elif char in digits:
            x: int = digits.get(char)
            inner_num += x
            if idx + 1 < n and string[idx + 1] != 'and' and not ordinal.get(string[idx + 1]):
                output += inner_num
                inner_num = 0
        elif char in tens:
            x: int = tens.get(char)
            inner_num += x
            print(inner_num)
            if (idx + 1 < n and string[idx + 1] != 'and' and not ordinal.get(string[idx + 1]) and not digits.get(string[idx + 1])):
                number += inner_num
                inner_num = 0
        elif char in ordinal:
            while idx < n and ordinal.get(string[idx]):
                inner_num *= ordinal.get(string[idx])
                idx += 1
            if idx < n and string[idx] != 'and':
                if digits.get(string[idx]) and (idx + 2 == n and string[-1] == 'thousand'):
                    inner_num += digits.get(string[idx])
                    idx += 1
                elif tens.get(string[idx]) and (idx + 1 < n and not ordinal.get(string[idx + 1])):
                    inner_num += tens.get(string[idx])
                    idx += 1
                else:
                    number += inner_num
                    inner_num = 0
            continue
        idx += 1
    number += inner_num
    return number