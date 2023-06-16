# Each exclamation mark's weight is 2; each question mark's weight is 3.
# Putting two strings left and right on the balance - are they balanced?
#
# If the left side is more heavy, return "Left"; if the right side is more heavy,
# return "Right"; if they are balanced, return "Balance".
#
# Examples
# "!!", "??"     -->  "Right"
# "!??", "?!!"   -->  "Left"
# "!?!!", "?!?"  -->  "Left"
# "!!???!????", "??!!?!!!!!!!"  -->  "Balance"
# FUNDAMENTALS
# Solution
def balance(left, right):
    count_l = 0
    count_r = 0
    d = {'!':2, '?':3}
    for i in left:
        count_l += d[i]
    for i in right:
        count_r += d[i]
    return 'Balance' if count_l == count_r else 'Left' if count_l > count_r else 'Right'