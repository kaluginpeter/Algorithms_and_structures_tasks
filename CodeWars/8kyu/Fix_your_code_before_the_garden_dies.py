# You have an award-winning garden and every day the plants need exactly 40mm of water. You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. Your jealous neighbour hacked your computer and filled your code with bugs.
#
# Your task is to debug the code before your plants die!
#
# FUNDAMENTALSDEBUGGING
# Solution
def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    return  f"You need to give your plant {abs(mm - 40)}mm of water"