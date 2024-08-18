# Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"
#
# STRINGSFUNDAMENTALS
# Solution
def nerdify(txt):
    d = {'a': 4, 'e': 3, 'l': 1, 'A': 4, 'E': 3}
    return ''.join(str(d[i]) if i in d else i for i in txt)