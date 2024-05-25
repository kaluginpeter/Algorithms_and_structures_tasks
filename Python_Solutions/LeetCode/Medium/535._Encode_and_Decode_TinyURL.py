# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Implement the Solution class:
#
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
#
#
# Example 1:
#
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
#
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.
#
#
# Constraints:
#
# 1 <= url.length <= 104
# url is guranteed to be a valid URL.
# Solution HashTable O(1) O(N)
class Codec:
    def __init__(self):
        self.storage_encoded: dict[str, str] = dict()
        self.storage_decoded: dict[str, str] = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.storage_encoded:
            return self.storage_encoded.get(longURL)
        decoded_url: str = 'https://' + str(abs(hash(longUrl)))
        while decoded_url in self.storage_decoded:
            decoded_url = 'https://' + str(abs(hash(longUrl)))
        self.storage_encoded[longUrl] = decoded_url
        self.storage_decoded[decoded_url] = longUrl
        return decoded_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.storage_decoded.get(shortUrl)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))