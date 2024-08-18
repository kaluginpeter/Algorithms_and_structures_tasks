# All Unix user know the command line history. This one comes with a set of useful commands know as the bang command.
#
# For more information about the history command line you can take a look at:
#
# The man page -> simply type man history in your terminal.
# The online man page here.
# And for more information about the bang command you can read this article
# For this second kata we will explore the !n command, according to the man page this one refer to command line n.
#
# In this kata you should complete a function that take in an integer that correspond to n, and an history with the following format:
#
#   1  cd /pub
#   2  more beer
#   3  lost
#   4  ls
#   5  touch me
#   6  chmod 000 me
#   7  more me
#   8  history
# and that should return the nth executed command line, for example with n=4 and the above history it should return ls. If user ask for a n without any know entry for example n=12 here, the function should return !12: event not found. Note: For this kata we will assume that n >= 1.
#
# Note: Lot of the command line comes form some geeky t-shirt and form this excellent page.
#
# STRINGSPARSINGREGULAR EXPRESSIONSALGORITHMS
# Solution
def bang_n(n, history):
    history = [i.lstrip().rstrip() for i in history.split('\n ')]
    if n - 1 >= len(history): return f'!{n}: event not found'
    return ' '.join(history[n - 1].split()[1:])