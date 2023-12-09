# You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:
#
# products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
# amounts: [3, 24, 8]
# prices: [199, 299, 399]
# return the three product names with the highest revenue (amount * price).
#
# Note: if multiple products have the same revenue, order them according to their original positions in the input list.
#
# FUNDAMENTALS
# Solution
def top3(products, amounts, prices):
    d = {products[i]: amounts[i] * prices[i] for i in range(len(products))}
    l = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [i[0] for i in l][:3]