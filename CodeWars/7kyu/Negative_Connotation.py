# You will be given a string with sets of characters, (i.e. words), seperated by between one and four spaces (inclusive).
#
# Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").
#
# Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.
#
# "A big brown fox caught a bad rabbit" => True/true
# "Xylophones can obtain Xenon." => False/false
# FUNDAMENTALS
# Solution
def connotation(strng):
    en_al_l = 'abcdefghijklmnopqrstuvwxyz'
    n = [1 if en_al_l.index(i[0].lower()) <= en_al_l.index('m') else 0 for i in strng.split()]
    return n.count(1) >= n.count(0)