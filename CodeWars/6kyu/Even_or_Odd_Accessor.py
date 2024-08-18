# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers. The function should also return "Even" or "Odd" when accessing a value at an integer index.
#
# For example:
#
# evenOrOdd(2); //'Even'
# evenOrOdd[2]; //'Even'
# evenOrOdd(7); //'Odd'
# evenOrOdd[7]; //'Odd'
# MATHEMATICSFUNDAMENTALS
# Solution
class EvenOrOdd:
    def __call__(self, number):
        return "Even" if number % 2 == 0 else "Odd"

    def __getitem__(self, number):
        return self(number)
even_or_odd = EvenOrOdd()