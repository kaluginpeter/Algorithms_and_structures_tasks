# In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.
#
# You must write a function that changes to a given case. It must be able to handle all three case types:
#
# py> change_case("snakeCase", "snake")
# "snake_case"
# py> change_case("some-lisp-name", "camel")
# "someLispName"
# py> change_case("map_to_all", "kebab")
# "map-to-all"
# py> change_case("doHTMLRequest", "kebab")
# "do-h-t-m-l-request"
# py> change_case("invalid-inPut_bad", "kebab")
# None
# py> change_case("valid-input", "huh???")
# None
# py> change_case("", "camel")
# ""
# Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase.
#
# (Any translations would be greatly appreciated!)
#
# STRINGSREGULAR EXPRESSIONSALGORITHMS
# Solution
def change_case(id, target):
    if target not in {'kebab', 'camel', 'snake'}:
        return None
    if not id:
        return ''
    x = 0
    for i in id:
        if i.isupper():
            x += 1
    y, z = id.count('_'), id.count('-')
    if (x > 0 and (y > 0 or z > 0)) or (y > 0 and (x > 0 or z > 0)) or (z > 0 and (x > 0 or y > 0)):
        return None
    word: str = ''
    flag: bool = False
    for i in id:
        if not i.isupper() and i not in {'-', '_'}:
            if flag:
                word += i.upper()
                flag = not flag
            else:
                word += i
        elif i.isupper():
            if target == 'camel': word += i
            elif target == 'kebab': word += '-' + i.lower()
            elif target == 'snake': word += '_' + i.lower()
        elif i == '-':
            if target == 'snake': word += '_'
            elif target == 'kebab': word += i
            elif target == 'camel': flag = True
        elif i == '_':
            if target == 'kebab': word += '-'
            elif target == 'snake': word += i
            elif target == 'camel': flag = True
    return word