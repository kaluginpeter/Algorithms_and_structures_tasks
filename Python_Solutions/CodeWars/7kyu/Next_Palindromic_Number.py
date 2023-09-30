# There were and still are many problem in CW about palindrome numbers and palindrome strings. We suposse that you know which kind of numbers they are. If not, you may search about them using your favourite search engine.
#
# In this kata you will be given a positive integer, val and you have to create the function next_pal()(nextPal Javascript) that will output the smallest palindrome number higher than val.
#
# Let's see:
#
# For Python
# next_pal(11) == 22
#
# next_pal(188) == 191
#
# next_pal(191) == 202
#
# next_pal(2541) == 2552
# You will be receiving values higher than 10, all valid.
#
# Enjoy it!!
#
# FUNDAMENTALSDATA STRUCTURESALGORITHMSMATHEMATICSLOGICSTRINGS
# Solution
def next_pal(val):
    val += 1
    while str(val) != str(val)[::-1]:
        val += 1
    return val