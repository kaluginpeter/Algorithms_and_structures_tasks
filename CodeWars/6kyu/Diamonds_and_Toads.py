# Base on the fairy tale Diamonds and Toads from Charles Perrault. In this kata you will have to complete a function that take 2 arguments:
#
# A string, that correspond to what the daugther says.
# A string, that tell you wich fairy the girl have met, this one can be good or evil.
# The function should return the following count as a hash:
#
# If the girl have met the good fairy:
# count 1 ruby everytime you see a r and 2 everytime you see a R
# count 1 crystal everytime you see a c and 2 everytime you see a C
# If the girl have met the evil fairy:
# count 1 python everytime you see a p and 2 everytime uou see a P
# count 1 squirrel everytime you see a s and 2 everytime you see a S
# Note: For this kata I decided to remplace the normal Diamonds and Toads by some programming languages. And just discover that Squirrel is a programming language.
#
# FUNDAMENTALSSTRINGS
# Solution
def diamonds_and_toads(sentence, fairy):
    flag: bool = fairy == 'good'
    ht: dict = {}
    if flag:
        ht['ruby'] = 0
        ht['crystal'] = 0
    else:
        ht['python'] = 0
        ht['squirrel'] = 0
    for i in sentence:
        if flag:
            if i in 'rR':
                ht['ruby'] += (1 if i.islower() else 2)
            if i in 'cC':
                ht['crystal'] += (1 if i.islower() else 2)
        else:
            if i in 'pP':
                ht['python'] += (1 if i.islower() else 2)
            if i in 'sS':
                ht['squirrel'] += (1 if i.islower() else 2)
    return ht