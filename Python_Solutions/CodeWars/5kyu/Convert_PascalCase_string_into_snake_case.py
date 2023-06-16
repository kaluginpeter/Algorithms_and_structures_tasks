# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
# Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
#
# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"
# STRINGSALGORITHMS
# Solution
def to_underscore(string):
    if type(string) == int:
        return str(string)
    l, word, flag = [], '', False
    for i in string:
        if i.isupper():
            if not flag:
                flag = True
                word += i
                continue
            l.append(word)
            flag, word = True, i
            continue
        word += i
    l.append(word)
    return '_'.join(i.lower() for i in l)