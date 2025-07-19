# Convert hex-encoded (https://en.wikipedia.org/wiki/Hexadecimal) string to base64 (https://en.wikipedia.org/wiki/Base64)
#
# Example:
#
# The string:
#
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# Should produce:
#
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# StringsAlgorithms
# Solution
import codecs
def hex_to_base64(hex: str) -> str:
	return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()[:-1]