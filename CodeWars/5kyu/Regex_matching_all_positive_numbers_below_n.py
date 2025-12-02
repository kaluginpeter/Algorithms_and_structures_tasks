# You are given a positive natural number n (which is n > 0) and you should create a regular expression pattern which only matches the decimal representation of all positive natural numbers strictly less than n without leading zeros. The empty string, numbers with leading zeros, negative numbers and non-numbers should not match the regular expression compiled from your returned pattern.
#
# Input
# n > 0 natural number, n can be from the full possible positive range
# Output
# regular expression pattern as string which will be used to compile a regular expression to do the matches
# Tests
# The compiled regular expression will be tested against decimal representations of random numbers with and without leading zeros, strings including letters and the empty string and should only match for decimal representations of numbers k with 0 < k < n.
#
# Tests use re.match() to do the matches.
#
# Regular Expressions