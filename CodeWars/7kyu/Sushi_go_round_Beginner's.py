# Sam has opened a new sushi train restaurant - a restaurant where sushi is served on plates that travel around the bar on a conveyor belt and customers take the plate that they like.
#
# Sam is using Glamazon's new visual recognition technology that allows a computer to record the number of plates at a customer's table and the colour of those plates. The number of plates is returned as a string. For example, if a customer has eaten 3 plates of sushi on a red plate the computer will return the string "rrr".
#
# Currently, Sam is only serving sushi on red plates as he's trying to attract customers to his restaurant. There are also small plates on the conveyor belt for condiments such as ginger and wasabi - the computer notes these in the string that is returned as a space; e.g. "rrr r" denotes 4 plates of red sushi and a plate of condiment.
#
# Sam would like your help to write a program for the cashier's machine to read the string and return the total amount a customer has to pay when they ask for the bill. The current price for the dishes are as follows:
#
# Red plates of sushi: $2 each - but every 5th one is free!
# Condiments: free
# Examples
# "rr"           -->  4     # 2 plates
# "rr rrr"       -->  8     # 5 plates, 1 free
# "rrrrr rrrrr"  -->  16    # 10 plates, 2 free
# FUNDAMENTALSSTRINGSLOGIC
# Solution
def total_bill(s):
    return s.count('r') * 2 if s.count('r') < 5 else (s.count('r') - (s.count('r')//5)) * 2