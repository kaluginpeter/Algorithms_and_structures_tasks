# Hey You !
# Sort these integers for me ...
#
# By name ...
#
# Do it now !
#
# Input
# Range is 0-999
#
# There may be duplicates
#
# The array may be empty
#
# Example
# Input: 1, 2, 3, 4
# Equivalent names: "one", "two", "three", "four"
# Sorted by name: "four", "one", "three", "two"
# Output: 4, 1, 3, 2
# Notes
# Don't pack words together:
# e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
# e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
# Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
# e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
# e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"
# SORTINGSTRINGSALGORITHMS
# Solution
def convertation(dgt: int) -> str:
    digits: list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ten: list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    double: list = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    ans: list = list()
    while True:
        if dgt < 10:
            ans.append(digits[dgt])
            break
        elif dgt < 20:
            ans.append(ten[int(str(dgt)[1])])
            break
        elif dgt < 100:
            x, y = str(dgt)[:]
            if y == '0':
                ans.append(double[int(x) - 1])
                break
            else:
                ans.append(double[int(x) - 1] + ' ' + digits[int(y)])
                break
        else:
            if dgt % 100 == 0:
                ans.append(digits[int(str(dgt)[0])] + ' hundred')
                break
            ans.append(digits[int(str(dgt)[0])] + ' hundred')
            dgt %= 100
    return ' '.join(ans)


def sort_by_name(arr):
    ht: dict = {i:convertation(i) for i in arr}
    arr.sort(key=lambda x: ht[x])
    return arr