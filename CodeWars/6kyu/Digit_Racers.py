# Many of the digits, zero through nine showed up for a race one day.
#
# The digit with the most occurences in the input string got 1st place.
#
# The digit that had the second most occurences got 2nd place, and so on it went, possibly all the way to 10th place.
#
# When there were ties, the digit with the largest index in the input string was listed first, 2nd largest index listed next, and so on.
#
# Digits that didnt make it to the race were listed at the bottom in ascending order like this as example "Absent digits: 3, 7".
#
# If none of the digits were absent from the race, the bottom of the winners list would display "All digits present".
#
# The end of each line has a break except for the last.
#
# example:
#
# Input:
# "00009393936611528"
#
# Output:
# "1st place: 0
#  2nd place: 3, 9
#  3rd place: 1, 6
#  4th place: 8, 2, 5
#  Absent digits: 4, 7"
# Notice in the above example, the tied digits are listed in order of larger indexes first.
# For more examples check out the Example Test Cases.
#
# Input and Output:
#
# input : a string of one or more digits.
#
# output : a string formatted as in the above example.
#
# StringsSortingFundamentals
# Solution
def digit_racers(s):
    hashmap: dict[str, int] = dict()
    absent: list[bool] = [False] * 10
    for digit in s:
        absent[int(digit)] = True
        hashmap[digit] = hashmap.get(digit, 0) + 1
    racers: list[tuple[str, int]] = sorted(
        hashmap.items(),
        key=lambda racer: (racer[1], -s[::-1].index(racer[0])),
        reverse=True
    )
    output: list[str] = []
    left: int = 0
    right: int = 0
    n: int = len(racers)
    for place in range(len(racers)):
        winners: list[str] = []
        while right < n and racers[left][1] == racers[right][1]:
            winners.append(racers[right])
            right += 1
        left = right
        if place + 1 == 1:
            output.append('1st place: {}'.format(', '.join(winner[0] for winner in winners)))
        elif place + 1 == 2:
            output.append('2nd place: {}'.format(', '.join(winner[0] for winner in winners)))
        elif place + 1 == 3:
            output.append('3rd place: {}'.format(', '.join(winner[0] for winner in winners)))
        else: output.append('{}th place: {}'.format(str(place + 1), ', '.join(winner[0] for winner in winners)))
        if left == n: break
    absent_digits: list[str] = [str(digit) for digit in range(10) if not absent[digit]]
    if not absent_digits: output.append('All digits present')
    else: output.append('Absent digits: {}'.format(', '.join(absent_digits)))
    return '\n'.join(output)