/*
In this kata, you will implement cipher functions using utf-8 strings.

The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key). The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" ("the unbreakable cipher")

The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. The key advances for every character in the message, regardless of whether that character belongs to the alphabet. Characters not in the alphabet are not encrypted, but they still consume one character of the key. This is different than some other implementations of the Vigenère Cipher.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation:

"abcdefghijklmnopqrstuvwxyz"       // alphabet
"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key

// The space between "my" and "secret" consumes the 
// first "s" of the key, even though the space character 
// is not in the alphabet and will not be encrypted.
Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

Examples
alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "password"

"codewars" --> encode -->  "rovwsoiv"
"laxxhsj"  --> decode -->  "waffles"
Note: any character not in the alphabet must be left alone. For example in the above case:

"CODEWARS"  --> encode -->  "CODEWARS"
AlgorithmsCiphersSecurityObject-oriented ProgrammingStrings
*/