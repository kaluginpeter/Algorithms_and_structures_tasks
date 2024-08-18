# Description
# You've been working with a lot of different file types recently as your interests have broadened.
#
# But what file types are you using the most? With this question in mind we look at the following problem.
#
# Given a List/Array of Filenames (strings) files return a List/Array of string(s) containing the most common extension(s). If there is a tie, return a sorted list of all extensions.
#
# Important Info:
# Don't forget, you've been working with a lot of different file types, so expect some interesting extensions/file names/lengths in the random tests.
# Filenames and extensions will only contain letters (case sensitive), and numbers.
# If a file has multiple extensions (ie: mysong.mp3.als) only count the last extension (.als in this case)
# Examples
# files = ['Lakey - Better days.mp3',
#          'Wheathan - Superlove.wav',
#          'groovy jam.als',
#          '#4 final mixdown.als',
#          'album cover.ps',
#          'good nights.mp3']
# would return: ['.als', '.mp3'], as both of the extensions appear two times in files.
#
# files = ['Lakey - Better days.mp3',
#          'Fisher - Stop it.mp3',
#          'Fisher - Losing it.mp3',
#          '#4 final mixdown.als',
#          'album cover.ps',
#          'good nights.mp3']
# would return ['.mp3'], because it appears more times then any other extension, and no other extension has an equal amount of appearences.
#
# FUNDAMENTALSALGORITHMSSTRINGSARRAYS
# Solution HashTable O(N) O(N)
def solve(files):
    ht: dict = dict()
    for i in files:
        indx: int = -1
        while i[indx] != '.':
            indx -= 1
        x: str = i[indx:]
        ht[x] = ht.get(x, 0) + 1
    mx = None
    for i in ht:
        if not mx:
            mx = i
        elif ht[i] > ht[mx]:
            mx = i
    ans: list = list()
    for i in ht:
        if ht[i] == ht[mx]:
            ans.append(i)
    ans.sort()
    return ans