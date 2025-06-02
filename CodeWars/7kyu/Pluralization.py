# Your code should take an English noun with a regular plural form and return its plural.
#
# Rules for pluralization in English:
#
# If a singular noun ends in '-s', '-x', '-z', '-ch' or '-sh', add '-es'
#
# If a singular noun ends with a consonant and '-y', change '-y' to '-ies'.
#
# All other words just add '-s'
#
# None of the tests end in '-f' or '-o' and none are irregular nouns (e.g. child, mouse etc.)
#
# Examples
#
# table -> tables,
# window -> windows,
# church -> churches,
# watch -> watches,
# bus -> buses,
# box -> boxes,
# buzz -> buzzes,
# fly -> flies
#
# Algorithms
# Solution
def pluralize(word):
    if word[-1] in {'s', 'x', 'z'}: return word + 'es'
    elif word[-2:] in {'ch', 'sh'}: return word + 'es'
    elif len(word) > 1 and word[-2] not in 'aeoiu' and word[-1] == 'y': return word[:-1] + 'ies'
    return word + 's'