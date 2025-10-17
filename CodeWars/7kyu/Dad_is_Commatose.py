# Your dad doesn't really get punctuation, and he's always putting extra commas in when he posts. You can tolerate the run-on sentences, as he does actually talk like that, but those extra commas have to go!
#
# Write a function that takes a string as an argument and returns a string with the extraneous commas removed. The returned string should not end with a comma or have any trailing whitespace.
#
# FundamentalsStringsRegular Expressions
# Solution
def dad_filter(string):
    string = string.split()
    for i in range(len(string)):
        was_comma: bool = string[i].endswith(',')
        string[i] = string[i].replace(',', '')
        if was_comma and i + 1 != len(string): string[i] += ','
    return ' '.join(string)