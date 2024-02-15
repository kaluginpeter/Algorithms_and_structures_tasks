# You need to play around with the provided string (s).
#
# Move consonants forward 9 places through the alphabet. If they pass 'z', start again at 'a'.
#
# Move vowels back 5 places through the alphabet. If they pass 'a', start again at 'z'. For our Polish friends this kata does not count 'y' as a vowel.
#
# Exceptions:
#
# If the character is 'c' or 'o', move it back 1 place. For 'd' move it back 3, and for 'e', move it back 4.
#
# If a moved letter becomes 'c', 'o', 'd' or 'e', revert it back to it's original value.
#
# Provided string will always be lower case, won't be empty and will have no special characters.
#
# FUNDAMENTALSSTRINGSARRAYSALGORITHMS
# Solution
def vowel_back(st):
    eng_al: str = 'abcdefghijklmnopqrstuvwxyz'
    ans: str = ''
    for i in st:
        prev_x: str = i
        x: str = i
        if i in 'aeoiu':
            if x == 'e':
                idx: int = eng_al.index(x) - 4
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
            elif x == 'o':
                idx: int = eng_al.index(x) - 1
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
            else:
                idx: int = eng_al.index(x) - 5
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
        else:
            if x == 'c':
                idx: int = eng_al.index(x) - 1
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
            elif x == 'd':
                idx: int = eng_al.index(x) - 3
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
            else:
                idx: int = eng_al.index(x) + 9
                if idx > 25:
                    idx %= 26
                x = eng_al[idx]
                if x in 'code':
                    ans += prev_x
                else:
                    ans += x
    return ans