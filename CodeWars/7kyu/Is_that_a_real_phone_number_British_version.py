# Congratulations! That Special Someone has given you their phone number.
#
# But WAIT, is it a valid number?
#
# Your task is to write a function that verifies whether a given string contains a valid British mobile (cell) phone number or not.
#
# If the string is a valid UK number, return "In with a chance".
#
# If it is invalid, or if you're given an empty string, return "Plenty more fish in the sea".
#
# A number can be valid in the following ways:
#
# Here in the UK, mobile numbers begin with "07" followed by 9 other digits, e.g. "07454876120".
#
# Sometimes the number is preceded by the country code, the prefix "+44", which replaces the "0" in ‘07’, e.g. "+447454876120".
#
# And sometimes you will find numbers with dashes in-between digits or on either side, e.g. "+44--745---487-6120" or "-074-54-87-61-20-". As you can see, dashes may be consecutive.
#
# Good Luck Romeo/Juliette!
#
# Regular ExpressionsStringsAlgorithms
# Solution
def validate_number(st):
    st = st.replace('+44', '0', 1).replace('-', '')
    if not st.startswith('07'):
        return 'Plenty more fish in the sea'
    if len(st[2:]) == 9 and all(ch.isdigit() for ch in st[2:]):
        return 'In with a chance'
    return 'Plenty more fish in the sea'