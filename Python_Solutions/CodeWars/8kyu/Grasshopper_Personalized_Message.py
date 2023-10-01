# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
#
# Use conditionals to return the proper message:
#
# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'
# FUNDAMENTALSSTRINGS
# Solution
def greet(name, owner):
    # Add code here
    if name == owner:
        return ('Hello boss')

    else:
        return ('Hello guest')