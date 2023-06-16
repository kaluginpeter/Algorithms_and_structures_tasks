# Vowel harmony is a phenomenon in some languages. It means that "A vowel or vowels in
# a word are changed to sound the same (thus "in harmony.")" (wikipedia). This kata is
# based on vowel harmony in Hungarian.
#
# Task:
# Your goal is to create a function instrumental() which returns the valid form of a
# valid Hungarian word w in instrumental case i. e. append the correct suffix -vel or -val
# to the word w based on vowel harmony rules.
#
# Vowel Harmony Rules (simplified)
# Front vowels: e, é, i, í, ö, ő, ü, ű
#
# Back vowels: a, á, o, ó, u, ú
#
# Vowel pairs (short -> long): a -> á, e -> é, i -> í, o -> ó, u -> ú, ö -> ő, ü -> ű
#
# Digraphs: sz, zs, cs
#
# Word ends with a vowel
# Change the ending vowel from short to long form.
# Append the suffix:
# vel if the ending vowel is a front vowel
# val if the ending vowel is a back vowel
# Word ends with a consonant
# Step one
# Default case: Double the ending consonant and continue with step two.
# Special case: If the word ends with a digraph then double the first letter (e. g. sz -> ssz)
# Step two
# Append the suffix:
#
# el if the last vowel is a front vowel
# al if the last vowel is a back vowel
# Examples:
# instrumental("fa") == "fával"
# instrumental("teve") == "tevével"
# instrumental("betű") == "betűvel"
# instrumental("ablak") == "ablakkal"
# instrumental("szék") == "székkel"
# instrumental("otthon") == "otthonnal"
# instrumental("kar") == "karral"
# instrumental("rács") == "ráccsal"
# instrumental("kosz") == "kosszal"
# Preconditions:
# All strings are unicode strings.
# The tests don't contain:
# exceptional cases like kávé -> kávéval
# words ending with doubled consonants (e. g. tett)
# words ending with y
# words ending with u, i
# STRINGSFUNDAMENTALS
# Solution
def instrumental(word):
    d = {"e": u"é", "i": u"í", u"ö": u"ő", u"ü": u"ű", "a": u"á", "o": u"ó", "u": u"ú"}
    for i in word[::-1]:
        if i in u"aáoóuú":
            suf = "val"
            break
        elif i in u"eéiíöőüű":
            suf = "vel"
            break
    if i == word[-1]: return word[:-1] + d.get(i, word[-1]) + suf
    if word[-2:] in ("sz", "zs", "cs"): word = word[:-1] + word[-2:]
    else: word += word[-1]
    return word + suf[1:]