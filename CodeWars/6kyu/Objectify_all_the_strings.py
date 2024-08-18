# Write
#
# String.prototype.hashify()
# that will turn a string into a hash/object. Every character in the string will be the key for the next character.
# E.g.
#
# '123456'.hashify() == {"1":"2","2":"3","3":"4","4":"5","5":"6","6":"1"} // The last char will be key for 1st
# char
# '11223'.hashify() == {"1":["1","2"],"2":["2","3"],"3":"1"} // when duplicates exist, group them in an array
# // i.e. 1 is key for next char 1, that 1 is key for next char 2, but 1 is already in the hash, so add 2 to key 1
# 'Codewars'.hashify() == {"C":"o","o":"d","d":"e","e":"w","w":"a","a":"r","r":"s","s":"C"}
# Order is not important
# There is a preloaded function equals(x,y) that will check if objects are same regardless of property order.
#
# ALGORITHMS
# Solution
def hashify(string):
    d = dict()
    for f, s in zip(string, string[1:] + string[0]):
        try:
            try: d[f].append(s)
            except: d[f] = [d[f], s]
        except: d[f] = s
    return d