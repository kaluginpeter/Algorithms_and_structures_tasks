# Modify the kebabize function so that it converts a camel case string into a kebab case.
#
# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"
# Notes:
#
# the returned string should only contain lowercase letters
# FUNDAMENTALSSTRINGSREGULAR EXPRESSIONS
# Solution
import re
def kebabize(string):
    return '-'.join(re.split('(?<=.)(?=[A-Z])', re.sub(r'[0-9]+', '', string))).lower()