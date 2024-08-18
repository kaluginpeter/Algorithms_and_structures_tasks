# DNA is a biomolecule that carries genetic information. It is composed of four different building blocks, called nucleotides: adenine (A), thymine (T), cytosine (C) and guanine (G). Two DNA strands join to form a double helix, whereby the nucleotides of one strand bond to the nucleotides of the other strand at the corresponding positions. The bonding is only possible if the nucleotides are complementary: A always pairs with T, and C always pairs with G.
#
# Due to the asymmetry of the DNA, every DNA strand has a direction associated with it. The two strands of the double helix run in opposite directions to each other, which we refer to as the 'up-down' and the 'down-up' directions.
#
# Write a function checkDNA that takes in two DNA sequences as strings, and checks if they are fit to form a fully complementary DNA double helix. The function should return a Boolean true if they are complementary, and false if there is a sequence mismatch (Example 1 below).
#
# Note:
#
# All sequences will be of non-zero length, and consisting only of A, T, C and G characters.
# All sequences will be given in the up-down direction.
# The two sequences to be compared can be of different length. If this is the case and one strand is entirely bonded by the other, and there is no sequence mismatch between the two (Example 2 below), your function should still return true.
# If both strands are only partially bonded (Example 3 below), the function should return false.
# Example 1:
#
# seq1 = 'GTCTTAGTGTAGCTATGCATGC';  // NB up-down
# seq2 = 'GCATGCATAGCTACACTACGAC';  // NB up-down
#
# checkDNA (seq1, seq2);
# // --> false
#
# // Because there is a sequence mismatch at position 4:
# // (seq1)    up-GTCTTAGTGTAGCTATGCATGC-down
# //              ||| ||||||||||||||||||
# // (seq2)  down-CAGCATCACATCGATACGTACG-up
# Example 2:
#
# seq1 = 'GCGCTGCTAGCTGATCGA';             // NB up-down
# seq2 = 'ACGTACGATCGATCAGCTAGCAGCGCTAC';  // NB up-down
#
# checkDNA (seq1, seq2);
# // --> true
#
# // Because one strand is entirely bonded by the other:
# // (seq1)       up-GCGCTGCTAGCTGATCGA-down
# //                 ||||||||||||||||||
# // (seq2)  down-CATCGCGACGATCGACTAGCTAGCATGCA-up
# Example 3:
#
# seq1 = 'CGATACGAACCCATAATCG';  // NB up-down
# seq2 = 'CTACACCGGCCGATTATGG';  // NB up-down
#
# checkDNA (seq1, seq2);
# // --> false
#
# // Because both strands are only partially bonded:
# // (seq1)  up-CGATACGAACCCATAATCG-down
# //                      |||||||||
# // (seq2)          down-GGTATTAGCCGGCCACATC-up
# If you enjoyed this kata, check out also my other DNA kata: Longest Repeated DNA Motif
# FUNDAMENTALSSTRINGS
# Solution
def checking(first: str, second: str) -> bool:
    return first.translate(str.maketrans('ATGC', 'TACG')) in second
def check_DNA(seq1, seq2):
    seq2 = seq2[::-1]
    if len(seq1) <= len(seq2):
        return checking(seq1, seq2)
    return checking(seq2, seq1)