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
# Solution
import time

def instrument(fn):
    class Instrumented:
        def __init__(self, func):
            self.func = func
            self.global_stats = Stats()

        def __call__(self, *args, **kwargs):
            return self._call(self.global_stats, None, *args, **kwargs)

        def __get__(self, instance, owner):
            if instance is None: return self
            if not hasattr(instance, "__instrument_stats__"):
                instance.__instrument_stats__ = {}
            if self.func not in instance.__instrument_stats__:
                instance.__instrument_stats__[self.func] = Stats()
            stats = instance.__instrument_stats__[self.func]
            def bound(*args, **kwargs):
                return self._call(stats, instance, *args, **kwargs)
            bound.last_invocation_time = stats.last_invocation_time
            bound.invocation_count = stats.invocation_count
            bound.avg_delay = stats.avg_delay
            bound.reset_stats = stats.reset_stats
            return bound

        def _call(self, stats, instance, *args, **kwargs):
            now = time.time()
            stats.record(now)
            if instance is None: return self.func(*args, **kwargs)
            else: return self.func(instance, *args, **kwargs)
        def last_invocation_time(self):
            return self.global_stats.last_invocation_time()
        def invocation_count(self):
            return self.global_stats.invocation_count()
        def avg_delay(self):
            return self.global_stats.avg_delay()
        def reset_stats(self):
            self.global_stats.reset_stats()

    class Stats:
        def __init__(self):
            self.count = 0
            self.last_time = None
            self.total_delay = 0

        def record(self, now):
            if self.last_time is not None:
                self.total_delay += (now - self.last_time)
            self.last_time = now
            self.count += 1

        def last_invocation_time(self):
            return self.last_time

        def invocation_count(self):
            return self.count

        def avg_delay(self):
            if self.count <= 1:
                return None
            return self.total_delay / (self.count - 1)

        def reset_stats(self):
            self.count = 0
            self.last_time = None
            self.total_delay = 0

    return Instrumented(fn)