# #Task: Write a function get_member_since which accepts a username from someone at Codewars and returns an string containing the month and year separated by a space that they joined CodeWars.
#
# ###If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though because the server may time out.
#
# #Example:
#
# >>> get_member_since('dpleshkov')
# Jul 2016
# >>> get_member_since('jhoffner')
# Oct 2012
# #Libraries/Recommendations:
#
# ##Python:
#
# urllib.request.urlopen: Opens up a webpage.
# re: The RegEx library for Python.
# bs4(BeautifulSoup): A tool for scraping HTML and XML.
# Python 2 is not working for this kata. :(
# #Notes:
#
# Time out / server errors often happen with the test cases depending on the status of the codewars website. Try submitting your code a few times or at different hours of the day if needed.
# Feel free to voice your comments and concerns in the discourse area.
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALS
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_member_since(username):
    username = username.encode('ascii', 'ignore').decode('ascii')
    username = username.replace(' ', '%20')
    url = f'https://www.codewars.com/users/{username}'
    response = urlopen(url)
    soup = BeautifulSoup(response.read(), 'html.parser')
    stats = soup.select('div#app > div#shell > main#shell_content > div > section.user-profile > div.w-full > div > div.flex-box > div.stat-box > div.stat')
    for stat in stats:
        if 'Member Since' in stat.b.text:
            return stat.b.next.next