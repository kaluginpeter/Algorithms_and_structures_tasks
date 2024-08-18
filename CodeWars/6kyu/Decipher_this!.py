# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#
# For each word:
#
# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces
#
# Examples
#
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'
# STRINGSARRAYSCIPHERSFUNDAMENTALS
# Solution
def decipher_this(string):
    l = string.split(' ')
    first = []
    second = []
    num, alpha, final = "", "", ""
    for word in l:
        for letter in word:
            if letter.isdigit():
                first.append(letter)
            if letter.isalpha():
                second.append(letter)
        num = chr(int("".join(first)))
        if second is not False:
            if len(second) > 1:
                temp = second[0]
                second[0] = second[-1]
                second[-1] = temp
            alpha = "".join(second)
        final = final + num + alpha + ' '
        alpha = ''
        del first[:]
        del second[:]
    return final[0:len(final)-1]