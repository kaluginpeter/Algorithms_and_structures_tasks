# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
#
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"
# REGULAR EXPRESSIONSSTRINGSFUNDAMENTALS
# Solution
def remove_url_anchor(url):
    if url.count('#'):
        index = url.index('#')
        return url[:index]
    return url