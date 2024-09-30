# Description
# In AD 2050, human beings finally found a planet in the distant XY constellation, which is very suitable for human survival. Many spacecraft from the earth to the distant planet, the star immigrants began...
#
# Nearly 10 years later, Human civilization is built up in the new planet, they put the planet named "paradise" and they call themselves "new human beings".
#
# They created their own language on the basis of the English alphabet and binary. That is to say, their text is expressed in binary, but only limited to letters, they still use punctuation and spaces in English.
#
# They use some special rules:
#
# Their binary is the opposite of the "old human beings". That is to say, their 1 is equals to our 0 and their 0 is equals to our 1.
#
# They re-encode the English alphabet in the opposite order: "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA", using binary 1 to 52. For example, z is 10, y is 01, x is 00, and so on.. Each letter ends with 2. See examples below:
#
# old human beings: Hello world!
# new human beings: 0100102(H)010012(e)00002(l)00002(l)00112(o)
#                   0112(w)00112(o)01102(r)00002(l)010002(d)!
#
# old human beings: I am new human beings.
# new human beings: 0100112(I) 001012(a)00012(m) 00102(n)010012(e)0112(w)
#                   011002(h)0012(u)00012(m)001012(a)00102(n)
#                   001102(b)010012(e)011012(i)00102(n)010112(g)01112(s).
# Task
# Complete two function encode and decode that can tranlate the words between "new human beings" and "old human beings".
#
# Examples
# encode("Hello world!") should return:
# "0100102010012000020000200112 0112001120110200002010002!"
#
# decode("0100102010012000020000200112 0112001120110200002010002!")
# should return: "Hello world!"
#
# decode(encode("Hello world!")) should return "Hello world!"
# PUZZLESGAMES