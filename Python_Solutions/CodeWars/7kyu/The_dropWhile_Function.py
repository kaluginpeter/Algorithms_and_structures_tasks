# Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to remove the longest prefix of elements such that the predicate is true for each element. We'll call this the dropWhile function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence.
#
# def isEven(num):
#   return num % 2 == 0
#
# arr = [2,4,6,8,1,2,5,4,3,2]
#
# dropWhile(arr, isEven) == [1,2,5,4,3,2] # True
# Your task is to implement the dropWhile function. If you've got a span function lying around, this is a one-liner! Alternatively, if you have a takeWhile function on your hands, then combined with the dropWhile function, you can implement the span function in one line. This is the beauty of functional programming: there are a whole host of useful functions, many of which can be implemented in terms of each other.
#
# FUNCTIONAL PROGRAMMINGARRAYSALGORITHMS
# Solution
def drop_while(arr, pred):
    for k,v in enumerate(arr):
        if not pred(v):
            return arr[k:]
    return []