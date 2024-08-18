# Given an array of words and a target compound word, your objective is to find the two words which combine into the target word, returning both words in the order they appear in the array, and their respective indices in the order they combine to form the target word. Words in the array you are given may repeat, but there will only be one unique pair that makes the target compound word. If there is no match found, return null/nil/None.
#
# Note: Some arrays will be very long and may include duplicates, so keep an eye on efficiency.
#
# Examples:
#
# fn(['super','bow','bowl','tar','get','book','let'], "superbowl")      =>   ['super','bowl',   [0,2]]
# fn(['bow','crystal','organic','ally','rain','line'], "crystalline")   =>   ['crystal','line', [1,5]]
# fn(['bow','crystal','organic','ally','rain','line'], "rainbow")       =>   ['bow','rain',     [4,0]]
# fn(['bow','crystal','organic','ally','rain','line'], "organically")   =>   ['organic','ally', [2,3]]
# fn(['top','main','tree','ally','fin','line'], "mainline")             =>   ['main','line',    [1,5]]
# fn(['top','main','tree','ally','fin','line'], "treetop")              =>   ['top','tree',     [2,0]]
# Have fun, and if you enjoyed it don't forget to rank & upvote! :)
#
# ARRAYSPERFORMANCEALGORITHMS
# Solution
def compound_match(words, target):
    ht: dict = dict()
    for i in range(len(words)):
        if words[i] not in ht:
            ht[words[i]] = i
    for i in ht:
        if target.startswith(i):
            for j in ht:
                if i + j == target:
                    x, y = ht[i], ht[j]
                    return [i if x < y else j, i if x > y else j, [ht[i], ht[j]]]
    return