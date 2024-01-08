# Complete the solution so that it returns the number of times the search_text is found within the full_text.
#
# search_substr( full_text, search_text, allow_overlap = True )
# so that overlapping solutions are (not) counted. If the searchText is empty, it should return 0. Usage examples:
#
# search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
# search_substr('aaabbbcccc', 'bbb') # should return 1
# search_substr( 'aaa', 'aa' ) # should return 2
# search_substr( 'aaa', '' ) # should return 0
# search_substr( 'aaa', 'aa', False ) # should return 1
# STRINGSREGULAR EXPRESSIONSALGORITHMS