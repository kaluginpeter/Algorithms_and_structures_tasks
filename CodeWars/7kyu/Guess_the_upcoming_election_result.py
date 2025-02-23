# An local election is happening this year and 3 parties are participating (Party A, B, C). You have done a survey and guessed what will be the vote swing (absolute percentage) for each of the parties this year. You also have the vote share of these parties from last year. Based on last year's result and guessed vote swing, you have to predict the order in which the parties will fare this year.
#
# The task is to write a function 'expected_party_rank' which takes the following input and returns the output
#
# Input -> 4 arguments - voteA, voteB, swingA, swingB where:
#
# voteA and voteB are the vote share (in percentage passed as integer) of last year for Party A and B respectively.
#
# swingA and swingB are the guessed vote swing (in absolute percentage passed as integer) expected this year for party A and B respectively
#
# Note - Vote share and vote swing for party C wont be given explicitly as input. For cases where there is a tie, the output should be sorted in alphabetical order.
#
# Output -> Rank of parties in descending order of expected vote share
#
# An example: expected_party_rank(44, 40, 2, -25) should return [A,C,B]
#
# Fundamentals