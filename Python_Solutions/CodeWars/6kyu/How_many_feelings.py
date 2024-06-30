# You have two arguments: string - a string of random letters(only lowercase) and array - an array of strings(feelings). Your task is to return how many specific feelings are in the array.
#
# For example:
#
# string -> 'yliausoenvjw'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '3 feelings.' // 'awe', 'joy', 'love'
#
#
# string -> 'griefgriefgrief'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '1 feeling.' // 'grief'
#
#
# string -> 'abcdkasdfvkadf'
# array -> ['desire', 'joy', 'shame', 'longing', 'fear']
# output -> '0 feelings.'
# If the feeling can be formed once - plus one to the answer.
#
# If the feeling can be formed several times from different letters - plus one to the answer.
#
# Eeach letter in string participates in the formation of all feelings. 'angerw' -> 2 feelings: 'anger' and 'awe'.
#
# FUNDAMENTALSSTRINGS
# Solution
def count_feelings(st, arr):
    arr = [''.join(sorted(word)) for word in arr]
    st = ''.join(sorted(st))
    count: int = 0
    for feel in arr:
        equal: bool = True
        idx: int = 0
        for char in feel:
            while idx < len(st) and st[idx] != char:
                idx += 1
            if idx >= len(st):
                equal = False
                break
            idx += 1
        count += equal
    return f"{count} feeling{'s' if count != 1 else ''}."