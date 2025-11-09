# 100th Kata
# You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see, complete with the mirror frame. Example:
#
# 'Hello World'
#
# would give:
#
#
# Words in your solution should be left-aligned.
#
# FundamentalsStringsArrays
# Solution
def mirror(text):
    words: list[str] = [word[::-1] for word in text.split()]
    bound: int = max(len(word) for word in words)
    output: list[str] = ['*' * (bound + 4)]
    for word in words:
        part: str = '* ' + word + ' ' * (bound - len(word)) + ' *'
        output.append(part)
    output.append('*' * (bound + 4))
    return '\n'.join(output)