# RSA is a widely used public-key cryptosystem. Like other public-key encryption systems, RSA takes in data and encrypts it using a publicly available key. The private key is then used to decrypt the data. It is useful for sending data to servers because anyone can encrypt their own data, but only the server containing the private key can decrypt it. The driving force behind the difficulty in breaking an RSA encryption is the complexity of prime factorization of very large numbers. In this kata, you will implement an RSA object that can encrypt and decrypt data. For the sake of simplity, we will just use numbers instead of string/text data.
#
# Here is the basic outline of how RSA works (see this link for more details):
#
# Pick 2 prime numbers called p and q
# Compute the modulus n = p * q
# Compute the totient of n, which can be found by the formula phi(n) = (p - 1) * (q - 1)
# Pick a positive integer e that is coprime to the totient (see here for an explanation of coprimes) - this will be the exponent used in the public key
# Compute the modular multiplicative inverse of 'e (mod phi(n))' - this will be the exponent d used in the private key - (for details on modular multiplicative inverses, click here)
# To encrypt a number m into a ciphered number c, use the following formula: c = m**e (mod n)
# To decrypt a number c back into the original number m, use the following formula: m = c**d (mod n)
# Note: Since e is generally a much smaller number than d, encryption is much quicker than decryption. In real practice (and in this kata), you will need to implement an optimized decryption method, as the formula given above will probably take too long for some of the more difficult test cases.
#
# Your task is to create a class that when initialized with some p, q, and e, will be able to encrypt and decrypt numbers using the RSA algorithm. You may assume that the test cases will only test valid inputs.
#
# CRYPTOGRAPHYALGORITHMSNUMBER THEORY
# Solution
class RSA:
    import math
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)

    def encrypt(self, m):
        return m ** self.e % self.n

    def decrypt(self, c):
        d = pow(self.e, -1, self.phi_n)
        return pow(c, d, self.n)