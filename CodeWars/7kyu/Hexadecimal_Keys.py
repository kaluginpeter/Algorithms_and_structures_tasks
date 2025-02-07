# Hector the hacker has stolen some information, but it is encrypted. In order to decrypt it, he needs to write a function that will generate a decryption key from the encryption key which he stole (it is in hexadecimal). To do this, he has to determine the two prime factors P and Q of the encyption key, and return the product (P-1) * (Q-1).
#
# Note: the primes used are < 105
#
# Examples
# For example if the encryption key is "47b", it is 1147 in decimal. This factors to 31*37, so the key Hector needs is 1080 (= 30*36).
#
# More examples:
#
# input: "2533", result: 9328 (primes: 89, 107)
# input: "1ba9", result: 6912 (primes: 73, 97)
# Algorithms
# Solution
def is_prime(n: int) -> bool:
    for d in range(2, int(n**.5) + 1):
        if n % d == 0: return 0
    return 1
primes: set[int] = set(num for num in range(1, 10**5 + 1) if is_prime(num))
def find_key(encryption_key):
    t: int = int(encryption_key, 16)
    for p in primes:
        if t // p in primes and t % p == 0: return (p - 1) * (t // p - 1)