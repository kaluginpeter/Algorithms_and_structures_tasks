# Remember the spongebob meme that is meant to make fun of people by repeating what they say in a mocking way?
#
# "Dont use that weird spongebob mocking meme" Me: DonT uSe thAt WeIrd SpoNgEboB MoCkinG MEme
#
# You need to create a function that converts the input into this format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.
#
# Example:
#
# input:  "stop Making spongebob Memes!"
# output: "StOp mAkInG SpOnGeBoB MeMeS!"
# FUNDAMENTALSSTRINGS
# Solution
def sponge_meme( s ):
    bob = ''
    i = 0
    while i < len(s):
        if i % 2 != 0:
            bob += s[i].lower()
        else:
            bob += s[i].upper()
        i += 1
    return bob