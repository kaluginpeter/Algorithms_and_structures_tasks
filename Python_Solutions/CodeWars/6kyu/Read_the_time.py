# Given time in 24-hour format, convert it to words.
#
# For example:
# 13:00 = one o'clock
# 13:09 = nine minutes past one
# 13:15 = quarter past one
# 13:29 = twenty nine minutes past one
# 13:30 = half past one
# 13:31 = twenty nine minutes to two
# 13:45 = quarter to two
# 00:48 = twelve minutes to one
# 00:08 = eight minutes past midnight
# 12:00 = twelve o'clock
# 00:00 = midnight
#
# Note: If minutes == 0, use 'o'clock'. If minutes <= 30, use 'past', and for minutes > 30, use 'to'.
# More examples in test cases. Good luck!
#
# FUNDAMENTALS
# Solution
def solve(time):
    first_part, second_part = map(int, time.split(':'))
    string_representation: dict[int, str] = {
        0: 'midnight',
        1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'
    }
    tens: dict[int, str] = {
        11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 2: 'twenty',
        3: 'thrity', 4: 'fourty', 5: 'fifty'
    }
    if first_part == second_part == 0:
        return string_representation[0]
    more_than_half: bool = second_part > 30
    if more_than_half:
        first_part += 1
    if first_part > 12:
        first_part %= 12
    if second_part == 0:
        return f"{string_representation.get(first_part)} o'clock"
    if second_part % 30 == 0:
        return f"half past {string_representation[first_part]}"
    elif second_part % 15 == 0:
        return f"quarter {'to' if more_than_half else 'past'} {string_representation[first_part]}"
    if more_than_half:
        second_part = 60 - second_part
    if second_part in {1, 59}:
        return f"one minute {'to' if more_than_half else 'past'} {string_representation[first_part]}"
    else:
        if second_part in tens and second_part > 10:
            second_part = tens[second_part]
        elif second_part <= 10:
            second_part = string_representation[second_part]
        else:
            if second_part % 10 == 0:
                second_part = f'{tens[second_part // 10]}'
            else:
                second_part = f'{tens[second_part // 10]} {string_representation[second_part % 10]}'
        return f"{second_part} minutes {'to' if more_than_half else 'past'} {string_representation[first_part]}"