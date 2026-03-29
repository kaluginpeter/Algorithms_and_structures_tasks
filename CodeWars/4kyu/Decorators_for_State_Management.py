# Overview
# A while ago, researchers from Carnegie Mellon University studied the way that non-programmers approach typical programming problems in order to compare with the way that programmers do, as part of the "Natural Programming Project".
#
# (PDF Warning) The paper can be found here
#
# One outcome of this research was that non-programmers will often describe events in the past tense, such as "If Pac-Man ate a Power Pellet in the last 10 seconds, he can eat the ghost". Of course, translating this into an imperative programming language isn't direct; we can't easily look back into the past and examine it for Power Pellet consumption.
#
# class PacMan:
#     def eat_power_pellet(self):
#         self.score += 50
#
#     def eat_ghost(self):
#         # If I ate a Power Pellet in the last 10 seconds, I can eat the ghost
#         # But how do I know whether I did that or not?
#         ...
# We instead need to think forward when programming, assigning state ahead of time so when we try to eat a ghost we have the information we need
#
# class PacMan:
#     def eat_power_pellet(self):
#         self.score += 50
#         self.last_power_pellet_consumption_time = now()
#
#     def eat_ghost(self):
#         if now() - self.last_power_pellet_consumption_time <= some_threshold:
#             ...
# ...but what if we leaned into the "natural" way of doing things a little more? Rather than rewriting our code to store certain state explicitly, what if we just had a decorator that did it for us?
#
# The Task
# Implement a decorator function @instrument which allows us to access metadata about a function, such that:
#
# @instrument
# def some_function():
#     ...
# some_function.last_invocation_time() returns the timestamp of the last invocation, or None if it hasn't been called
#
# some_function.invocation_count() returns the number of times the function has been called
#
# some_function.avg_delay() returns the average number of seconds between calls, or None if it hasn't been called more than once
#
# some_function.reset_stats() resets all metadata; as if the function had never been called
#
# Timestamps should be retrieved by calling time() from the time module.
#
# The Tricky Bit
# The @instrument decorator must work on instance methods and on regular functions; that is to say:
#
# p = PacMan()
# p2 = PacMan()
# p.wakka()  # An @instrumented method
# p.wakka.invocation_count() # 1
# p2.wakka.invocation_count() # 0
#
#
# @instrument
# def something():
#     ...
#
#
# something()
# something.invocation_count() # 1
# Static methods etc. are out of scope for this problem.
#
# DecoratorMetaprogramming