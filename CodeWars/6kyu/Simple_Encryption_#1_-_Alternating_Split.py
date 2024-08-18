# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.
#
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.
#
# This kata is part of the Simple Encryption Series:
#
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
# Have fun coding it and please don't forget to vote and rank this kata! :-)
#
# CRYPTOGRAPHYALGORITHMSSTRINGSARRAYSFUNDAMENTALS
# Solution
def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def decrypt_one_rep(encrypted_text):
    word1 = ""
    word2 = ""
    lenght = int(len(encrypted_text) / 2)
    word1 += encrypted_text[0:lenght]
    word2 += encrypted_text[lenght:]
    final_word = ""
    for i in range(0, lenght):
        final_word += word2[i] + word1[i]

    if len(encrypted_text) % 2 != 0:
        final_word += word2[lenght]
    return final_word


def decrypt(encrypted_text, n):
    if n < 0:
        return encrypted_text
    list = [encrypted_text]
    for i in range(1, n + 1):
        list.append(decrypt_one_rep(list[i - 1]))
    return list[n]