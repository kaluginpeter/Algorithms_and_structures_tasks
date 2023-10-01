# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
#
# Your task is to change the letters with diacritics:
#
# ą -> a,
# ć -> c,
# ę -> e,
# ł -> l,
# ń -> n,
# ó -> o,
# ś -> s,
# ź -> z,
# ż -> z
# and print out the string without the use of the Polish letters.
#
# For example:
#
# "Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
# STRINGSFUNDAMENTALS
# Solution
def correct_polish_letters(st):
    dict = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}
    return ''.join(dict[i] if i in dict else i for i in st)