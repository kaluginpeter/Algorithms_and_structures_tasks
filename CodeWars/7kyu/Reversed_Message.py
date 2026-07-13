# Reverse a message so that the words and letters passed into it are made lower case and reversed. In addition, capitalise the first letter of the newly reversed words. If a number or symbol(!#,>) is now in the first position of the word, no capitalisation needs to occur.
#
# Example:
#
# reverseMessage('This is an example of a Reversed Message!')
# Returns: '!egassem Desrever A Fo Elpmaxe Na Si Siht'
#
# FundamentalsStrings
# Solution
def reverse_message(text):
    output: list[str] = []
    for word in text.lower().split():
        word = word[::-1]
        if word[0] in '!#,>0123456789': output.append(word)
        else: output.append(word[0].upper() + word[1:])
    return ' '.join(reversed(output))