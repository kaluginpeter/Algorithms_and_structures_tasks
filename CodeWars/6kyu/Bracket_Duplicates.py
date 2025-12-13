# Create a program that will take in a string as input and, if there are duplicates of more than two alphabetical characters in the string, returns the string with all the extra characters in a bracket.
#
# For example, the input "aaaabbcdefffffffg" should return "aa[aa]bbcdeff[fffff]g"
#
# Please also ensure that the input is a string, and return "Please enter a valid string" if it is not.
#
# StringsRegular ExpressionsAlgorithms
# Solution
def string_parse(strng):
    if not isinstance(strng, str): return "Please enter a valid string"
    output: list[str] = []
    for word in strng.split():
        cur: list[str] = []
        left: int = 0
        right: int = 0
        n: int = len(word)
        while right < n:
            while right < n and word[left] == word[right]: right += 1
            if right - left > 2:
                cur.append(word[left:left + 2] + f"[{word[left + 2:right]}]")
            else: cur.append(word[left:right])
            left = right
        output.append("".join(cur))
    return " ".join(output)