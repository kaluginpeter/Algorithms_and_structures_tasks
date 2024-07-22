# Been a while, but here's part 2!
#
# You are given a string of lowercase letters and spaces that you need to type out. In the string there is a special function: [shift]. Once you encounter a [shift] , you capitalise the character right after it, as if you're actually holding the key. Return the final string .
#
#
#
# e.g. [shift]john [shift]green return John Green (capitalise the j and g)
#
# Walkthrough:
#
# [shift]
# J capitalise the j
# Jo
# Joh
# John
# John[space]
# John G capitalise the g
# John Gr
# John Gre
# John Gree
# John Green
#
# John Green
#
#
#
# e.g. [shift]n[shift]o[shift]o[shift]o return NOOO (capitalise all the letters)
#
# Walkthrough:
#
# [shift]
# N capitalise the n
# NO capitalise the O
# NOO capitalise the O
# NOOO capitalise the O
#
# NOOO
#
# Notice if we want to capitalise a long string of letters, it will look very confusing viually. So, let's add two new functions, holdshift and unshift. It's self-explanatory.
#
#
#
# Some examples:
#
# [holdshift]uppercase[unshift] return UPPERCASE (holdshift all letters)
#
# Walkthrough:
#
# [holdshift]
# U
# UP
# UPP
# ...
#
# UPPERCASE
# [unshift]
#
# UPPERCASE
#
#
#
# unshift can also apply to normal shift, but since normal shift only affects the character right after, unshift would have to be directly after normal shift for it to affect it.
#
# Example: [shift][unshift]dont [shift][unshift]shift returns dont shift
#
# Walkthrough:
#
# [shift][unshift] cancels
# dont[space]
# [shift][unshift] cancels
# dont shift
#
# dont shift
#
#
#
# Whew! That was lengthy!
#
# Ok, to summerise:
#
# [shift] capitalises the character right after it ([shift]a -> A)
# [holdshift] capitalises all the characters after it until it reaches unshift ([holdshift]one[unshift]two -> ONEtwo)
# [unshift] releases shift (either [shift] or [holdshift])
# [shift][unshift]d returns d
# Other necessary things you might want to know:
#
# Shifting a space is a space
# After a [holdshift], there is always an unshift, without any functions in between
# After unshifting, the next function called will not be an unshift (you can't release something if you're not pressing it)
# Things like [shift][holdshift] or [shift][shift] or [holdshift][shift]can't occur, but [shift][unshift] can
# The string will never start with [unshift] for obvious reasons
# Good luck! More examples in the example tests (The description took me way too long lol)
#
# Please give this a good rating, I spent a really long time coding this.
#
# Thank you!