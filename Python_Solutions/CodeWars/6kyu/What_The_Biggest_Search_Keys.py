# You're a programmer in a SEO company. The SEO specialist of your company gets the list of all project keywords everyday, then he looks for the longest keys to analyze them.
#
# You will get the list with keywords and must write a simple function that returns the biggest search keywords and sorts them in lexicographical order.
#
# For instance you might get:
#
# 'key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1'
# And your function should return:
#
# "'bigkey1', 'bigkey2'"
# Don't forget to rate this kata! Thanks :)
#
# FUNDAMENTALSARRAYS
# Solution
def the_biggest_search_keys(*args):
    ans: list = list()
    ln: int = -1
    for i in args:
        if len(i) > ln:
            ans.clear()
            ans.append(i)
            ln = len(i)
        elif len(i) == ln:
            ans.append(i)
    ans.sort()
    if not ans:
        return "''"
    return ', '.join(f"'{i}'" for i in ans)