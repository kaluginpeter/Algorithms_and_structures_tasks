# A. Vus the Cossack and a Contest
# time limit per test1 second
# memory limit per test256 megabytes
# Vus the Cossack holds a programming competition, in which n
#  people participate. He decided to award them all with pens and notebooks. It is known that Vus has exactly m
#  pens and k
#  notebooks.
#
# Determine whether the Cossack can reward all participants, giving each of them at least one pen and at least one notebook.
#
# Input
# The first line contains three integers n
# , m
# , and k
#  (1≤n,m,k≤100
# ) — the number of participants, the number of pens, and the number of notebooks respectively.
#
# Output
# Print "Yes" if it possible to reward all the participants. Otherwise, print "No".
#
# You can print each letter in any case (upper or lower).
#
# Examples
# InputCopy
# 5 8 6
# OutputCopy
# Yes
# InputCopy
# 3 9 3
# OutputCopy
# Yes
# InputCopy
# 8 5 20
# OutputCopy
# No
# Note
# In the first example, there are 5
#  participants. The Cossack has 8
#  pens and 6
#  notebooks. Therefore, he has enough pens and notebooks.
#
# In the second example, there are 3
#  participants. The Cossack has 9
#  pens and 3
#  notebooks. He has more than enough pens but only the minimum needed number of notebooks.
#
# In the third example, there are 8
#  participants but only 5
#  pens. Since the Cossack does not have enough pens, the answer is "No".