# It happened decades before Snapchat, years before Twitter and even before Facebook. Targeted advertising was a bit of a challenge back then. One day, the marketing professor at my university told us a story that I am yet to confirm using reliable sources. Nevertheless, I retold the story to dozens of my students already, so, sorry BMW if it is all a big lie.
#
# Allegedly, BMW, in an attempt to target the educated, produced billboard posters featuring the English alphabet with three letters missing: B, M and W. Needless to say, many were confused, some to the extent of road accidents.
#
# Your task is to write a function that takes one parameter str that MUST be a string and removes all capital and small letters B, M and W.
# If data of the wrong data type was sent as a parameter the function must throw an error with the following specific message:
#
# TypeError("This program only works for text.")
# For Python here's a good resource you might need for the exception type ;)
#
# FUNDAMENTALSSTRINGSREGULAR EXPRESSIONS
# Solution
def remove_bmw(string):
    try:
        return string.replace('B', '').replace('M', '').replace('W', '').replace('b', '').replace('m', '').replace('w', '')
    except:
        return "This program only works for text."