# In this kata you must take an input string, reverse the order of the words, and reverse the order of the letters within the words.
#
# But, as a bonus, every test input will end with a punctuation mark (! ? .) and the output should be returned with the mark at the end.
#
# A few examples should help clarify:
#
# esrever("hello world.") == "dlrow olleh."
#
# esrever("Much l33t?") == "t33l hcuM?"
#
# esrever("tacocat!") == "tacocat!"
# Quick Note: A string will always be passed in (though it may be empty) so no need for error-checking other types.
#
# FundamentalsStrings
# Solution
def esrever(st: str) -> str:
    if not st: return st
    mock: str = ''
    if st[-1] in '?!.':
        mock = st[-1]
        st = st[:-1]
    return ' '.join(''.join(reversed(word)) for word in reversed(st.split())) + mock