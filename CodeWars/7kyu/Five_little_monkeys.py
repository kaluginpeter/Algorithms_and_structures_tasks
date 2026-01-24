# Return the lyrics of the nursery rhyme "Five little monkeys" (see below).
#
# But even monkeys can copy-paste, so you have to be smarter and make it short, because your code can be maximum 450 bytes long! (The original text is 800 bytes)
#
# Hint: use loops and variables for repeated text, or any other way to reduce your code size.
#
# Happy coding!
#
# Five little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!
#
# Four little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!
#
# Three little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!
#
# Two little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!
#
# One little monkey jumping on the bed,
# He fell off and bumped his head.
# Mother called the doctor and the doctor said:
# Put those monkeys right to bed!
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
#
# Translations are welcome!
# (except for Ruby, which is coming shortly)
#
# StringsRestricted
# Solution
def monkeys():
    n=["Five","Four","Three","Two","One"]
    s=" little monkey"
    t=" jumping on the bed,\n"
    c="Mother called the doctor and the doctor said:\n"
    r=[]
    for i,w in enumerate(n):
        r+= [f"{w}{s+(w!='One')*'s'}{t}", f"{('One','He')[w=='One']} fell off and bumped his head.\n", c, ("No more monkeys jumping on the bed!\n\n","Put those monkeys right to bed!")[w=='One']]
    return "".join(r).rstrip()