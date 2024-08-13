# Some but not all
# Description
# Your task is to create a function that given a sequence and a predicate, returns True if only some (but not all) the elements in the sequence are True after applying the predicate
#
# Examples
# some_but_not_all('abcdefg&%$', str.isalpha)
# >>> True
#
# some_but_not_all('&%$=', str.isalpha)
# >>> False
#
# some_but_not_all('abcdefg', str.isalpha)
# >>> False
#
# some_but_not_all([4, 1], lambda x: x>3)
# >>> True
#
# some_but_not_all([1, 1], lambda x: x>3)
# >>> False
#
# some_but_not_all([4, 4], lambda x: x>3)
# >>> False
# LISTSSTRINGSFUNDAMENTALS