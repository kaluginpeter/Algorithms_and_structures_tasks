# OK, my warriors! Now that you beat the big BOSS, you can unlock three new skills. (Does it sound like we're playing an RPG? ;-)
#
# The Arrow Function (JS only)
# The first skill is the arrow function. Let's look at some examples to see how it works:
#
# #ignore this part, it is just for JS
# As you can see, its syntax is:
#
# #ignore this part, it is just for JS
# If only one parameter exists on the left side of the arrow, the bracket can be omitted. If only one expression exists on the right side of the arrow, the curly braces can also be omitted. The example below shows a function with the () and {} omitted.
#
# #ignore this part, it is just for JS
# If the right side of the arrow is a complex statement, you must use curly braces:
#
# #ignore this part, it is just for JS
# So far, our examples have used function assignment. However, an arrow function can also be used as a parameter to a function call, as well. When used as a parameter, the arrow function does not require a name. Let's rewrite the string.replace() example we saw from a previous training using our new skill:
#
# #ignore this part, it is just for JS
# String.replace takes a regular expression and a function. The function is invoked on each substring matching the regex, and return the string replacement of that match. In this case, the arrow function takes the matched string as the parameter x, and returns the upper cased value of x.
#
# In the soon to learn the arrayObject and its methods, there are many applications on the arrow function, which is the reason we first learn the arrow function. The arrow function has more complex usage and usage restrictions, but we don't need to learn to be so deep, so we only learn the contents of the above.
#
# The Spread Operator
# The second skill is the spread operator. The spread operator allows an expression to be expanded in places where multiple arguments (for function calls) or multiple elements (for array literals) are expected.
#
# It looks like this: ...obj. It can be used in three places:
#
# 1. In function calls:
#
# def plus(a,b,c,d,e): return a+b+c+d+e
#
# arg1=[1,2,3,4,5]
# arg2=[2,3]
# print(plus(*arg1)) #output is 15
# print(plus(*arg2)) #output is 5
# ...arg1 spreads all the elements in arg1 into individual parameters to plus(). In Javascript, it's also possible to use the spread operator in the middle of a parameter list, as was done with ...arg2.
#
# 2. Creating array literals (JS and Ruby):
#
# #ignore this part, it is just for JS and Ruby
# ...a spreads out the array's elements, making them individual elements in b.
#
# 3. Used for deconstruction. destructuring is also a new member of ES6. It is the third skill we learn in this training.
#
# First, let's look at a simple example of destructuring:
#
# a,b=[1,2] #or [a,b]=[1,2]
# print a #output is 1
# print b #output is 2
# Destructuring allows us to assign variables in a sentence-like form. Here's a slightly more complicated example:
#
# a,b=[1,2] #or [a,b]=[1,2]
# #old way to swap them:
# #c=a; a=b; c=b
# b,a=[a,b] #or [b,a]=[a,b]
# print a #output is 2
# print b #output is 1
# With destructuring, we don't need a temporary variable to help us exchange the two values.
#
# You can use the spread operator for destructuring like this:
#
# #ignore this part, it is just for JS
# Please note: the spread operator must be the last variable: [...a,b]=[1,2,3,4,5] does not work.
#
# a was assigned to the first element of the array, andbwas initialized with the remaining elements in the array.
#
# Javascript note: If you see an ellipse ... in the argument list in a function declaration, it is not a spread operator, it is a structure called rest parameters. The rest parameter syntax allows us to represent an indefinite number of arguments as an array, like this:
#
# def plus(*num):
#   rs=0
#   for x in num: rs+=x
#   return rs
# print plus(1,2) #output is 3
# print plus(3,4,5) #output is 12
# The rest paramater must be the last argument in the function definition argument list.
#
# In the next example, we use a rest parameter to collect all the values passed to mul() after the first into an array. We then multiply each of them by the first parameter and return that array:
#
# def mul(a,*b):
#   b=list(b) #default type would be tuple
#   for i in xrange(len(b)): b[i]*=a
#   return b
# print mul(2,1,1,1) #output is [2,2,2]
# print mul(2,1,2,3,4) #output is [2,4,6,8]
# Ok, the lesson is over. Did you get it all? Let's do a task, now.
#
# Task
# Create a function shuffleIt. The function accepts two or more parameters. The first parameter arr is an array of numbers, followed by an arbitrary number of numeric arrays. Each numeric array contains two numbers, which are indices for elements in arr (the numbers will always be within bounds). For every such array, swap the elements. Try to use all your new skills: arrow functions, the spread operator, destructuring, and rest parameters.
#
# Example:
#
# shuffleIt([1,2,3,4,5],[1,2]) should return [1,3,2,4,5]
# shuffleIt([1,2,3,4,5],[1,2],[3,4]) should return [1,3,2,5,4]
# shuffleIt([1,2,3,4,5],[1,2],[3,4],[2,3]) should return [1,3,5,2,4]
# Next training (#23 Array Methods) >>
#
# Series
# ( ↑↑↑ Click the link above can get my newest kata list, Please add it to your favorites)
#
# #1: create your first JS function helloWorld
# #2: Basic data types--Number
# #3: Basic data types--String
# #4: Basic data types--Array
# #5: Basic data types--Object
# #6: Basic data types--Boolean and conditional statements if..else
# #7: if..else and ternary operator
# #8: Conditional statement--switch
# #9: loop statement --while and do..while
# #10: loop statement --for
# #11: loop statement --break,continue
# #12: loop statement --for..in and for..of
# #13: Number object and its properties
# #14: Methods of Number object--toString() and toLocaleString()
# #15: Methods of Number object--toFixed(), toExponential() and toPrecision()
# #16: Methods of String object--slice(), substring() and substr()
# #17: Methods of String object--indexOf(), lastIndexOf() and search()
# #18: Methods of String object--concat() split() and its good friend join()
# #19: Methods of String object--toUpperCase() toLowerCase() and replace()
# #20: Methods of String object--charAt() charCodeAt() and fromCharCode()
# #21: Methods of String object--trim() and the string template
# #22: Unlock new skills--Arrow function,spread operator and deconstruction
# #23: methods of arrayObject---push(), pop(), shift() and unshift()
# #24: methods of arrayObject---splice() and slice()
# #25: methods of arrayObject---reverse() and sort()
# #26: methods of arrayObject---map()
# #27: methods of arrayObject---filter()
# #28: methods of arrayObject---every() and some()
# #29: methods of arrayObject---concat() and join()
# #30: methods of arrayObject---reduce() and reduceRight()
# #31: methods of arrayObject---isArray() indexOf() and toString()
# #32: methods of Math---round() ceil() and floor()
# #33: methods of Math---max() min() and abs()
# #34: methods of Math---pow() sqrt() and cbrt()
# #35: methods of Math---log() and its family
# #36: methods of Math---kata author's lover:random()
# #37: Unlock new weapon---RegExp Object
# #38: Regular Expression--"^","$", "." and test()
# #39: Regular Expression--"?", "*", "+" and "{}"
# #40: Regular Expression--"|", "[]" and "()"
# #41: Regular Expression--""
# #42: Regular Expression--(?:), (?=) and (?!)
# FUNDAMENTALSTUTORIALS
# Solution
def shuffle_it(arr, *args):
    for k,v in args:
        arr[k], arr[v] = arr[v], arr[k]
    return arr