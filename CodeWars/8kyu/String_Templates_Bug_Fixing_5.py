# Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!
#
# ◄PREVIOUS KATANEXT KATA►
# STRINGSDEBUGGING
# Solution
def build_string(*args):
    return "I like {}!".format(", ".join(i for i in args))