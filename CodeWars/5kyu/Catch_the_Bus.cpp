/*
The book "Guide to Teaching Puzzle-based Learning" includes the following puzzle:

"A boy sometimes misses the bus. The bus is supposed to leave at 8:00, but it arrives at the stop some time between 7:58 and 8:02 and departs immediately once everyone is on board. The boy tries to reach the stop early, but due to various circumstances he arrives some time between 7:55 and 8:01. How often does the boy miss the bus?" (Text edited for brevity.) The book explains how to find the solution, which is 18.75%.

Let's solve this problem in general. Inputs are the bus range first, followed by the boy range. Both ranges are tuples (or lists or arrays, depending on language) of two elements; the second time is guaranteed to be later than the first. The bus and boy are equally likely to arrive at any time in their range. You don't have to take into account the time that the bus waits - assume people board the bus instantly :-). The boy makes the bus only if he arrives before or at the moment it does. Compute how often the boy misses the bus, as a percentage.

Times are given as strings containing hour, minute, and AM/PM. Example: (("7:58 AM", "8:02 AM"), ("7:55 AM", "8:01 AM")) should return 18.75 Answers are accepted if within 0.001 of the solution.

Note: The bus runs between 2am and 11pm. The boy's times will be sufficiently close to the bus times so that calculating across to the previous or next day is not needed.

Also check out Catch the Bus - Continuous Edition

ProbabilityDate TimeGeometry
*/