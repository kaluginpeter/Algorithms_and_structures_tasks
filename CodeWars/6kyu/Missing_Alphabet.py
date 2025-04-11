# In this Kata you have to create a function,named insertMissingLetters,that takes in a string and outputs the same string processed in a particular way.
#
# The function should insert only after the first occurrence of each character of the input string, all the alphabet letters that:
#
# -are NOT in the original string
# -come after the letter of the string you are processing
#
# Each added letter should be in uppercase, the letters of the original string will always be in lowercase.
#
# Example:
#
# input: "holly"
#
# missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"
#
# output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"
#
# You don't need to validate input, the input string will always contain a certain amount of lowercase letters (min 1 / max 50).
#
# StringsAlgorithmsGames
# Solution
import bisect
def insert_missing_letters(st: str) -> str:
    extra: list[int] = list(range(65, 91))
    for letter in st:
        if ord(letter.upper()) in extra: extra.remove(ord(letter.upper()))
    output: list[str] = []
    seen: set[str] = set()
    for letter in st:
        output.append(letter)
        if letter not in seen:
            seen.add(letter)
            output.append(''.join(chr(code) for code in extra[bisect.bisect_right(extra, ord(letter.upper())):]))
    return ''.join(output)
