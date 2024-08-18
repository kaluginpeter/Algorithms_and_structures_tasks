# Write a code that orders collection of Uris based on it's domain next way that it will returns fisrt Uris
# with domain "com", "gov", "org" (in alphabetical order of their domains) and then all other Uris ordered
# in alphabetical order of their domains In addition to that
#
# content of Uri should not be changed,
# other part of Uri doesn't affect sorting. (uris "c.com","b.com","a.com" can be placed
# in any order inside their group, so both "c.com","b.com","a.com" and "a.com","c.com","b.com" are correct,
# till they are stand before *.org)
# e.g.
#
# "http://www.google.en/?x=jsdfkj"
# "http://www.google.de/?x=jsdfkj"
# "http://www.google.com/?x=jsdfkj"
# "http://www.google.com/?x=jsdfkj"
# "http://www.google.org/?x=jsdfkj"
# "http://www.google.gov/?x=jsdfkj"
# should be sorted into
#
# "http://www.google.com/?x=jsdfkj"
# "http://www.google.com/?x=jsdfkj"
# "http://www.google.gov/?x=jsdfkj"
# "http://www.google.org/?x=jsdfkj"
# "http://www.google.de/?x=jsdfkj"
# "http://www.google.en/?x=jsdfkj"
# In the final tests consecutive addresses with the same domain will be grouped and sorted before comparison, i.e.:
#
# Given your solution returns ["b.com", "a.com", "c.gov"], the tests will do this:
#
# Split the addresses into groups: [["b.com", "a.com"], ["c.gov"]]
# Sort each group: [["a.com", "b.com"], ["c.gov"]]
# Flatten them: ["a.com", "b.com", "c.gov"]
# FUNDAMENTALSALGORITHMSSORTING
# Solution
def sorting(address):
    d = {"org": "aac", "gov": "aab", "com": "aaa"}
    d1 = address.split('/?')[0].split('.')[-1]
    return d1 if d1 not in d else d[d1]
def order_by_domain(addresses):
    return sorted(addresses, key=sorting)