# Suppose we have a class:
#
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
#
# Note:
#
# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
# Example 2:
#
# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
#
#
# Constraints:
#
# nums is a permutation of [1, 2, 3].
# Solution 1 - slow solution by while loop
class Foo(object):
    def __init__(self):
        self.flag1 = False
        self.flag2 = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag1 = True

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.flag1:
            continue
        self.flag1 = True
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag2 = True

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.flag2:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
# Solution 2 - by events
import threading


class Foo(object):
    def __init__(self):
        self.flag1 = threading.Event()
        self.flag2 = threading.Event()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag1.set()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.flag1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag2.set()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.flag2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()