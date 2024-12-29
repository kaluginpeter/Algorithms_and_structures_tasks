# Check that a number is a valid number that has been given to 2 decimal places. The number passed to the function will be given as a string. If the number satisfies the criteria below, the function should return true, else it should return false.

# Please check the criteria for a valid number:

# optional + or - symbol in front

# optional digits before a decimal point (digits are characters ranging from '0' to '9')

# a decimal point

# exactly two digits after the point

# nothing else

# Examples of valid and non-valid numbers

# List of valid numbers: [ "0.00" "3.90" "1000.00" ".00" "-2.55" "+2.10" "-.55"]

# List of non-valid numbers: ["hellow 11.99" "11.9" "11" "11." ".9"]

# Regular ExpressionsFundamentals
# Solution
def valid_number(n):
    idx: int = 0
    while idx < len(n) and n[idx] != '.':
        if not n[idx].isdigit() and (n[idx] not in '+-' or idx):
            return False
        idx += 1
    idx += 1
    if idx >= len(n):
        return False
    return len(n) - idx == 2 and all(digit.isdigit() for digit in n[idx:])