# You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered to your store today.
#
# Your task is to write a function that returns the updated list of your current inventory in alphabetical order.
#
# Example
# cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
# new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]
#
# update_inventory(cur_stock, new_stock)  ==>
# [(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]
# Kata inspired by the FreeCodeCamp's 'Inventory Update' algorithm.
#
# ALGORITHMSDATA STRUCTURESARRAYS
# Solution
def update_inventory(cur_stock, new_stock):
    ht: dict = dict()
    for i in cur_stock:
        ht[i[1]] = ht.get(i[1], 0) + i[0]
    for i in new_stock:
        ht[i[1]] = ht.get(i[1], 0) + i[0]
    ans: list = [(v, k)  for k, v in ht.items()]
    ans.sort(key=lambda x: x[1])
    return ans