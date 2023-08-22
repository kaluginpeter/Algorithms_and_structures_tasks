# In this Kata, you have to design a simple routing class for a web framework.
#
# The router should accept bindings for a given url, http method and an action.
#
# Then, when a request with a bound url and method comes in, it should return the result of the action.
#
# Example usage:
#
# router = Router()
# router.bind('/hello', 'GET', lambda: 'hello world')
#
# router.runRequest('/hello', 'GET') // returns 'hello world'
# When asked for a route that doesn't exist, router should return:
#
# 'Error 404: Not Found'
# The router should also handle modifying existing routes. See the example tests for more details.
#
# OBJECT-ORIENTED PROGRAMMINGARRAYSFUNDAMENTALS
# Solution
class Router:
    def __init__(self):
        self._routes = {}
    def bind(self, url, method, a):
        self._routes[(url, method)] = a
    def runRequest(self, url, method):
        return self._routes.get((url, method), lambda: "Error 404: Not Found")()