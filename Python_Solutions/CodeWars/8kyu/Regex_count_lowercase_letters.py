# Your task is simply to count the total number of lowercase letters in a string.
#
# Examples
# "abc" ===> 3
#
# "abcABC123" ===> 3
#
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#
# "" ===> 0;
#
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#
# "abcdefghijklmnopqrstuvwxyz" ===> 26
# FUNDAMENTALSREGULAR EXPRESSIONSALGORITHMS
# Solution
def lowercase_count(strng):
    return len(list(i for i in strng if i.islower()))