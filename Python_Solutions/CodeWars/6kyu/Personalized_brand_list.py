# Assume you are creating a webshop and you would like to help the user in the search. You have products with brands, prices and name. You have the history of opened products (the most recently opened being the first item).
#
# Your task is to create a list of brands ordered by popularity, if two brands have the same popularity level then choose the one which was opened last from the two and second the other one.
#
# Product popularity is calculated from the history. If a product is more times in the history than it is more popular.
#
# Your function will have one parameter which will be always an array/list of object.
#
# example product: { name: "Phone", price: 25, brand: "Fake brand" }
#
# ALGORITHMS
# Solution
from collections import Counter
def sorted_brands(history):
    storage = Counter([i['brand'] for i in history])
    store = list(storage.keys())
    store.sort(key=lambda x: storage[x], reverse=True)
    return store