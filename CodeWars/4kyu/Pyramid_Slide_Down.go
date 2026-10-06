/*
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem: imagine that you have a pyramid built of numbers, like the ones here:

    3                10
   7 4             10  20
  2 4 6          10  10  20
 8 5 9 3       10  90  10  20
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the largest 'slide downs' are 3 + 7 + 4 + 9 = 23, and 10 + 20 + 10 + 90 = 130.

Your task is to write a function that takes a pyramid representation as an argument and returns its largest 'slide down'. For example:

With the input [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], your function should return 23.
With the input [[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]], your function should return 130.
By the way...
Tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of Problem 18 and/or Problem 67 on ProjectEuler.

AlgorithmsDynamic Programming
*/