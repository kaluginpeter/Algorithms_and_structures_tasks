# Math geeks and computer nerds love to anthropomorphize numbers and assign emotions and personalities to them.
# Thus there is defined the concept of a "happy" number. A happy number is defined as an integer in which the
# following sequence ends with the number 1.
#
# Start with the number itself.
# Calculate the sum of the square of each individual digit.
# If the sum is equal to 1, then the number is happy. If the sum is not equal to 1, then repeat steps 1 and 2.
# A number is considered unhappy once the same number occurs multiple times in a sequence because this means there
# is a loop and it will never reach 1.
# For example, the number 7 is a "happy" number:
#
# 72 = 49 --> 42 + 92 = 97 --> 92 + 72 = 130 --> 12 + 32 + 02 = 10 --> 12 + 02 = 1
#
# Once the sequence reaches the number 1, it will stay there forever since 12 = 1
#
# On the other hand, the number 6 is not a happy number as the sequence that is generated is
# the following: 6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58, 89
#
# Once the same number occurs twice in the sequence, the sequence is guaranteed to go on
# infinitely, never hitting the number 1, since it repeat this cycle.
#
# Your task is to write a program which will print a list of all happy numbers between 1 and x (both inclusive), where:
#
# 2 <= x <= 5000
# Disclaimer: This Kata is an adaptation of a HW assignment I had for McGill
# University's COMP 208 (Computers in Engineering) class.
#
# If you're up for a challenge, you may want to try a performance version of this kata by FArekkusu.
#
# RECURSIONARRAYSALGORITHMS
# Solution
def happy_numbers(n):
    def is_happy(n):
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
    return [i for i in range(1, n+1) if is_happy(i)]