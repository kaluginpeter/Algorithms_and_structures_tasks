# Task
# Mr.Odd is my friend. Some of his common dialogues are “Am I looking odd?” , “It’s looking very odd” etc. Actually “odd” is his favorite word.
#
# In this valentine when he went to meet his girlfriend. But he forgot to take gift. Because of this he told his gf that he did an odd thing. His gf became angry and gave him punishment.
#
# His gf gave him a string str of contain only lowercase letter and told him,
#
# “You have to take 3 index i,j,k such that i<j<k and str[i] =‘o’,str[j]=’d’,str[k]=’d’ and cut them from the string and make a new string “odd”. How many string you can make?”
#
# Mr.Odd wants to impress his gf so he want to make maximum number of “odd”. As he is lazy, he ask you to help him and tell him maximum number of “odd” he an make.
#
# Example
# For str="oudddbo", the result should be 1.
#
# "oudddbo"(cut 1 odd)--> ".u..dbo"(no more odd)
#
# For str="ooudddbd", the result should be 2.
#
# "ooudddbd"(cut 1st odd)--> ".ou..dbd"(cut 2nd odd) --> "..u...b."
#
# Input/Output
# [input] string str
# a non-empty string that contains only lowercase letters.
#
# 0 < str.length <= 10000
#
# [output] an integer
# the maximum number of "odd".
#
# PUZZLES
# Solution
def odd(s):
    s, c, g = ''.join(i for i in s if i in 'od'), 0, 2
    for i,j in enumerate(s):
        if j=='o' and s[i:].count('d')>=g:
            c+=1
            g+=2
        if j=='d': g-=1
        if g<2: g=2
    return c