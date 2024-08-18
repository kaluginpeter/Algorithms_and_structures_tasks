# Open/Closed Principle
# The open/closed principle states that code should be closed for modification, yet open for extension. That means you should be able to add new functionality to an object or method without altering it.
#
# One way to achieve this is by using a lambda, which by nature is lazily bound to the lexical context. Until you call a lambda, it is just a piece of data you can pass around.
#
# Task at hand
# Implement 3 lambdas that alter a message based on emotion:
#
# spoken    = lambda greeting: ... # "hello WORLD" --> "Hello world."
# shouted   = lambda greeting: ... # "Hello world" --> "HELLO WORLD!"
# whispered = lambda greeting: ... # "HELLO WORLD" --> "hello world."
# Then create a fourth lambda, this one will take one of the above lambdas and a message, and the last lambda will delegate the emotion and the message up the chain.
#
# greet = lambda style, msg: ...
# Input
# Input message contains only ASCII alphabets and spaces.
#
# While here we only test for spoken, shouted, and whispered emotions, the open/closed principle allows us to add functionality to the greet function using other emotions/lambdas as well. For example, feeling like L33tsp34k1ng or sPoNgEbOb MeMe-ing today? No need to change the original greet function (closed for modification), you can just extend the greet function (open for extension) by passing a new lambda and message to the greet function. So, embrace the power of open/closed principle now and make your code more flexible and easier to extend!
#
# FUNDAMENTALS
# Solution
spoken    = lambda greeting: greeting.title() + '.'
shouted   = lambda greeting: greeting.upper() + '!'
whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)