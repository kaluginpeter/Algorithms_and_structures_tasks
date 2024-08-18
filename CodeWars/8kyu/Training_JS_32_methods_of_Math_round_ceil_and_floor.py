# From this lesson, we learn about JS static object: Math. It mainly helps us to carry out mathematical calculations. It has a lot of properties and methods. Some of the properties and methods we rarely used. So we only learn some common methods.
#
# The properties of the Math object are some constants, such as PI, on behalf of the approximate value of pi. The usage is Math.PI. I will no longer introduce one by one, please refer to the manual:
#
# Math Object
# In this lesson we learn three methods to turn a number into an integer: round(), ceil() and floor().
#
# Their definitions and detailed information:
#
# Math.round()
# Math.ceil()
# Math.floor()
# First of all, we have to understand the first thing, all the methods of the Math object are static methods. It means that you need to use the Math method like this: Math.round(1.23). Not like this: (1.23).round().
#
# Here we use some examples to understand their usage:
#
# console.log(Math.round(1.45)); //output:1
# console.log(Math.ceil(1.45));  //output:2
# console.log(Math.floor(1.45)); //output:1
# console.log(Math.round(1.55)); //output:2
# console.log(Math.ceil(1.55));  //output:2
# console.log(Math.floor(1.55)); //output:1
# We can see, ceil() always rounding up to get a large integer; floor() always rounding down to get a small integer; round() according to the fractional part and round it to integer.
#
# When the parameter is negative, they still works:
#
# console.log(Math.round(-1.45)); //output:-1
# console.log(Math.ceil(-1.45));  //output:-1
# console.log(Math.floor(-1.45)); //output:-2
# console.log(Math.round(-1.55)); //output:-2
# console.log(Math.ceil(-1.55));  //output:-1
# console.log(Math.floor(-1.55)); //output:-2
# It should be noted that they are not working on the fractional part. If you want to keep two decimal places or otherwise, you should use Methods of Number object--toFixed(), toExponential() and toPrecision(), or use the following techniques:
#
# var n=1.23456
# var a=Math.round(n*100)/100
# var b=Math.ceil(n*100)/100
# var c=Math.floor(n*100)/100
# console.log(a,b,c);  //output: 1.23 1.24 1.23
# In the example above, we first multiply the number by 100, and then round it. the final result is to retain two decimal places.
#
# Ok, lesson is over. let's us do some task.
#
# Task
# Coding in function roundIt. function accept 1 parameter n. It's a number with a decimal point. Please use different methods based on the location of the decimal point, turn the number into an integer.
#
# If the decimal point is on the left side of the number (that is, the count of digits on the left of the decimal point is less than that on the right), Using ceil() method.
#
# roundIt(3.45) should return 4
# If the decimal point is on the right side of the number (that is, the count of digits on the left of the decimal point is more than that on the right), Using floor() method.
#
# roundIt(34.5) should return 34
# If the decimal point is on the middle of the number (that is, the count of digits on the left of the decimal point is equals that on the right), Using round() method.
#
# roundIt(34.56) should return 35
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
import math
def round_it(n):
    value = str(n)
    find_decimal_position = value.find('.')
    decimal_values = value[(find_decimal_position+1):]
    if(len(decimal_values)>len(value[0:find_decimal_position])):
        return math.ceil(n)
    elif(len(decimal_values)<len(value[0:find_decimal_position])):
        return math.floor(n)
    elif(len(decimal_values)==len(value[0:find_decimal_position])):
        return round(n,0)