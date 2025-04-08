# Implement String#whitespace?(str) (Ruby), String.prototype.whitespace(str) (JavaScript), String::whitespace(str) (CoffeeScript), or whitespace(str) (Python), which should return true/True if given object consists exclusively of zero or more whitespace characters, false/False otherwise.
#
# Regular ExpressionsFundamentals
# Solution
def whitespace(string):
    idx: int = 0
    while idx < len(string):
        if string[idx:].startswith(' '): idx += 1
        elif string[idx:].startswith('\n'): idx += 1
        elif string[idx:].startswith('\r'): idx += 1
        elif string[idx:].startswith('\t'): idx += 1
        else: return False
    return True