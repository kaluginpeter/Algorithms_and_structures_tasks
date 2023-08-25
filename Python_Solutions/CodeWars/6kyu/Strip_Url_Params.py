# Complete the method so that it does the following:
# Removes any duplicate query string parameters from the url (the first occurence should be kept)
# Removes any query string parameters specified within the 2nd argument (optional array)
# Examples:
# strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
# strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
# strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
# STRINGSALGORITHMS