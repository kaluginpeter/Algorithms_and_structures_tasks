# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.
#
# Write a function that computes the nth smallest Hamming number.
#
# Specifically:
#
# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in the Example test fixture.
#
# Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) Hamming numbers without timing out.
#
# NUMBER THEORYALGORITHMS
# Solution
def hamming(n):
    l = [1]
    n2, n3, n5 = 0, 0, 0
    for i in range(1, n):
        mn = min(l[n2] * 2, l[n3] * 3, l[n5] * 5)
        if 2 * l[n2] == mn:
            n2 += 1
        if 3 * l[n3] == mn:
            n3 += 1
        if 5 * l[n5] == mn:
            n5 += 1
        l.append(mn)
    return l[-1]