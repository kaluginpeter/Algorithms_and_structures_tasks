# Write a program that, given a word, computes the scrabble score for that word.
#
# Letter Values
# You'll need these:
#
# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10
# There will be a preloaded dictionary dict_scores with all these values: dict_scores["E"] == 1
#
# Examples
# "cabbage" --> 14
# "cabbage" should be scored as worth 14 points:
#
# 3 points for C
# 1 point for A, twice
# 3 points for B, twice
# 2 points for G
# 1 point for E
# And to total:
#
# 3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 14
#
# Empty string should return 0. The string can contain spaces and letters (upper and lower case), you should calculate the scrabble score only of the letters in that string.
#
# ""           --> 0
# "STREET"    --> 6
# "st re et"    --> 6
# "ca bba g  e" --> 14
# FUNDAMENTALSSTRINGS
# Solution
def scrabble_score(st):
    w1 = 'A,E,I,O,U,L,N,R,S,T'
    w2 = 'D,G'
    w3 = 'B,C,M,P'
    w4 = 'F,H,V,W,Y'
    w5 = 'K'
    w6 = 'JX'
    w7 = 'QZ'
    count = 0
    st.replace(' ', '')
    for i in st.upper():
        if i in w1:
            count +=1
        elif i in w2:
            count += 2
        elif i in w3:
            count += 3
        elif i in w4:
            count += 4
        elif i in w5:
            count += 5
        elif i in w6:
            count += 8
        elif i in w7:
            count += 10
    return count