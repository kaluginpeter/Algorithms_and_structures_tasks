# Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.
#
# If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"
#
# If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"
#
# If the total of both even and odd numbers are identical return: "Even and Odd are the same"
#
# FUNDAMENTALS
# Solution
def even_or_odd(s):
    a = sum(int(i) for i in s if int(i)%2 != 0)
    b = sum(int(i) for i in s if int(i)%2 == 0)
    return 'Even is greater than Odd' if b > a else 'Odd is greater than Even' if a>b else 'Even and Odd are the same'