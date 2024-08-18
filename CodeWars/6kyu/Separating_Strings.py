# Create a function that takes a string and separates it into a sequence of letters.
#
# The array will be formatted as so:
#
# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]
# The function should separate each word into individual letters, with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.
#
# Shorter words will have an empty string in the place once the word has already been mapped out. (See the last element in the last part of the array.)
#
# Examples:
#
# sep_str("Just Live Life Man")
# # => [['J','L','L','M'],
# # => ['u','i','i','a'],
# # => ['s','v','f','n'],
# # => ['t','e','e','']]);
#
# sep_str("The Mitochondria is the powerhouse of the cell")
# # => [ [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
# # => [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
# # => [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
# # => [ '', 'o', '', '', 'e', '', '', 'l' ],
# # => [ '', 'c', '', '', 'r', '', '', '' ],
# # => [ '', 'h', '', '', 'h', '', '', '' ],
# # => [ '', 'o', '', '', 'o', '', '', '' ],
# # => [ '', 'n', '', '', 'u', '', '', '' ],
# # => [ '', 'd', '', '', 's', '', '', '' ],
# # => [ '', 'r', '', '', 'e', '', '', '' ],
# # => [ '', 'i', '', '', '', '', '', '' ],
# # => [ '', 'a', '', '', '', '', '', '' ]]
# FUNDAMENTALS
# Solution
def sep_str(st):
    return [[j[i] if len(j) > i else '' for j in st.split()] for i in range(max(map(len, st.split())))] if st else []