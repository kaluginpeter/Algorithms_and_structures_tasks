# We define a special score for a word (ssw) as follows. We multiply the corresponding 10 - base ascii code for each letter of the word by its respective frequency of this letter in the word, we collect these addens and we sum them up.
#
# For example for the word, investigation we have the respective ascci codes and frequencies for each letter:
#
# Letter    Ascii decimal code        Letter Frequency (in "investigation")
#  i             105                            3
#  n             110                            2
#  t             116                            2
#  a              97                            1
#  e             101                            1
#  g             103                            1
#  o             111                            1
#  s             115                            1
#  v             118                            1
# So the ssw for this word will be:
#
# ssw = 3 * 105 + 2 * 110 + 2 * 116 + 97 * 1 + 101 * 1 + 103 * 1 + 111 * 1 + 115 * 1 + 118 * 1 = 1412
# We need a function find_word() (Javascript: findWord()) that receives two arguments, number of letters, num_let (Javascript: numLet) and a maximum special scoremax_ssw (Javascript: maxSsw) for the word. The function will output a word from a data base of 2000 words that have the highest possible ssw of the given number of letters but smaller or equal than the given max_ssw. If we have more than one word with the same number of letters, num_let, and the same special score, ssw, it will be chosen the last word of the list of words sorted. You were provided with a list of 2000 words of the Oxford Dictionary Of English (U.K. English), named WORD_LIST for python, $word_list for ruby, wordList for javascript.
#
# Let's see some cases:
# num_let = 8
# max_ssw = 888
# find_word(num_let, max_ssw) == 'southern'
# /// There are three words with 8 letters and with ssw == 888
# 'question', 'security' and 'southern'
# The list of these words sorted withe its respespective ssw is [(888, 'question'),
# (888, 'security'), (888, 'southern')], 'southern' should be chosen
#
# num_let = 9
# max_ssw = 500
# find_word(num_let, max_ssw) == None # in Ruby nil, in Javascript null
# /// the word of 9 letters with minimum ssw is 'candidate' with ssw = 925
# There are no word of 9 letters less than 500
# We may have the case when the all the words of certain number of letters are bellow max_ssw
#
# num_let = 7
# max_ssw = 1412
# find_word(num_let, max_ssw) == 'support'
# ///'support' is the word of 7 letters with highest ssw (797)
# Enjoy it!
#
# FUNDAMENTALSDATA STRUCTURESALGORITHMSMEMOIZATION