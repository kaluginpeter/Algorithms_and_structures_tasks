# Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.
#
# # Please do not use anything from the following list:
# ['encode','decode','join','zfill','codecs','chr','bytes','ascii', 'substitute','template','bin', 'os','sys','re', '"', "'", 'str','repr', '%s', 'format', 'type', '__', '.keys','eval','exec','subprocess']
#
# RECURSIONFUNDAMENTALS
# Solution
def reverse(n, count=0):
	return reverse(n // 10, count * 10 + n % 10) if n else count