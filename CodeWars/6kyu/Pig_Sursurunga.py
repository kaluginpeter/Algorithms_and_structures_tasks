# Once upon a time, a CodeWarrior, after reading a discussion on what can be the plural, took a look at this page and discovered that more than 1 "kind of plural" may exist.
#
# For example Sursurunga Language distinguishes 5 types of numbers: singular (1 thing), dual (2 things), 'trial' or 'lesser paucal' (3 or 4), 'greater paucal' (more than 4) and plural (many).
#
# In this kata, you'll have to handle only four types of numbers:
#
# singular: 0 or 1 thing
# dual: 2 things
# paucal: 3 to 9 things
# plural: more than 9 things
# To add some flavor the number-marker will not be added in same places:
#
# singular, no marker : 1 cat
# dual, prefixed "bu" : 2 cats -> 2 bucat
# paucal, suffixed "zo" : 4 cats -> 4 catzo
# plural, "circumfixed ga" : 100 cats -> 100 gacatga
# As you all ("hawk eyes") have seen, the final s of english plural disappears.
#
# ( btw these markers, of course, have absolutely nothing to do with true sursurunga language, we're just talking about "pig-sursurunga" with pig as pig in "pig latin" )
#
# Your Job . . .
# . . . if you accept it, will be to write a function which get a string as argument and returns this string with words in it eventually converted to their "pig-sursurunga number type".
#
# If a number ( ie 1 or more digit ) + a space + a word ( letters ) are found then the word should be converted.
#
# Each group of number+space+word found in the string should be evaluated.
#
# Examples :
# "1 tiger" --> "1 tiger" (singular, nothing to change)
#
# "2 tigers" --> "2 butiger" (dual)
# "3 tigers" --> "3 tigerzo" (paucal)
# "13 tigers" --> "13 gatigerga" (plural)
#
# "5 lions and 15 zebras" --> "5 lionzo and 15 gazebraga" (paucal and plural)
# You may assume at least 1 number+space+word group will be provided.
#
# Beware s of english plural should be removed, not ending s of some singular words ( eg "kiss" )
#
# "7 kisses" --> "7 kissezo"
# "1 kiss" --> "1 kiss"
# Good luck!
#
# StringsRegular ExpressionsFundamentals
# Solution
def sursurungal(txt):
    words: list[str] = []
    cur_sep: str = ''
    prev_i: int = 0
    i: int = 0
    while i < len(txt):
        if txt[i] == ' ':
            if i - prev_i: words.append(txt[prev_i:i])
            cur_sep += txt[i]
            i += 1
            prev_i = i
        elif txt[i] == '\n':
            if i - prev_i: words.append(txt[prev_i:i])
            i += 1
            prev_i = i
            cur_sep += '\n'
        else:
            if cur_sep: words.append(cur_sep)
            cur_sep = ''
            i += 1
    if cur_sep:
        words.append(cur_sep)
    if prev_i != len(txt):
        words.append(txt[prev_i:len(txt)])

    for i in range(len(words)):
        if not words[i].isdigit(): continue
        number: int = int(words[i])
        if number <= 1: continue
        word: str = words[i + 2]
        if number == 2:
            if word.endswith('s'):
                words[i + 2] = "bu" + word[:-1]
            else:
                words[i + 2] = "bu" + word
        elif number <= 9:
            if word.endswith('s'):
                words[i + 2] = word[:-1] + "zo"
            else:
                words[i + 2] = word + "zo"
        else:
            if word.endswith('s'):
                words[i + 2] = "ga" + word[:-1] + "ga"
            else:
                words[i + 2] = "ga" + word + "ga"

    return ''.join(words)