# In this Kata, your goal is to write a financial function with memory!
#
# Given a numeric input, register_transaction should format it as a string rounded to two decimals of precision, with a comma as the thousands separator, a period as the decimal separator, and a dollar sign in front. (Use the "round half to even" rounding method, which is the default behavior of round in Python and Javascript.) For example, 1000.557 should be rendered as "$1,000.56". If the input is less than one, use a leading zero for the dollars place. That is, render 0.2 as "$0.20".
#
# But that's not all! Like a predatory bookie at the racetrack, register_transaction should keep a running tally of every transaction registered with it. After formatting the input, the function should output an ordered list (or array) of all transactions ever registered with the function—with the new transaction at the end of the list.
#
# You may assume that all function inputs will be valid integers or floats.
#
# Example:
#
# register_transaction(15) -> ["$15.00"]
# register_transaction(10) -> ["$15.00", "$10.00"]
# StringsLanguage Features