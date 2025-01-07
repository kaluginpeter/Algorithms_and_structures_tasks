# Write
#
# function repeating_fractions(numerator, denominator)
# that given two numbers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part has repeated digits, replace those digits with a single digit in parentheses.
#
# For example:
#
# repeating_fractions(1,1) === '1'
# repeating_fractions(1,3) === '0.(3)'
# repeating_fractions(2,888) === '0.(0)(2)5(2)5(2)5(2)5(2)5(2)'
# StringsFundamentals
def repeating_fractions(numerator: int, denominator: int) -> str:
    pattern: str = str(numerator / denominator)
    n: int = len(pattern)
    output: list[str] = []
    was_point: bool = False
    left: int = 0
    right: int = 0
    while right < n:
        while right < n and pattern[left] == pattern[right]:
            right += 1
        if right - left > 1:
            if not was_point:
                output.append(pattern[left:right])
            else:
                output.append(f'({pattern[left]})')
            left = right
        else:
            output.append(str(pattern[left]))
            if pattern[left] == '.':
                was_point = True
            left += 1
    return ''.join(output)