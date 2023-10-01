# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
#
# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹
# FUNDAMENTALSDEBUGGING
# Solution
def multiply(n):
    i =(5**len(str(n)))
    return n * i if n >=0 else n * (5**(len(str(n))-1))