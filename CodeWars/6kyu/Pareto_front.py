# Introduction
# Suppose you want to buy a train ticket. You want to minimize both the ticket cost and the travel time. 3 tickets are for sale:
#
# Ticket	Travel Time	Price
# A	2h00	50$
# B	1h20	75$
# C	2h30	100$
# It is difficult to compare tickets A and B, because there is a tradeoff between them: one is cheaper, and the other is faster.
#
# However, it is clear that both of them are better than C, because C is both slower and more expensive than either of them. It is said that C is Pareto-dominated by A and B, while Aand B are Pareto-efficient or Pareto-optimal.
#
# The set of all Pareto-optimums is called the Pareto front.
#
#
# On this graph, the axes f1 and f2 respectively represent the travel time and cost. The red line joins all the points in the Pareto front, which comprises A, B, and the dark blue squares. C and the light blue squares are the Pareto-dominated points.
#
# Task
# Your function takes as input a list of tuples. A tuple represents the characteristics of an object or situation (e.g. train tickets). You want to minimize every one of these characteristics. You have to return the Pareto front of the input, as a set of tuples.
#
# Examples
# [ (120, 50), (80, 75), (150, 100) ] -> { (120, 50), (80, 75) }
# This is the example with the train tickets, with the time expressed in minutes.
# [ (1, 2, 3), (1, 3, 2), (1, 5, 2), (2, 3, 3), (0, 7, 7) ] -> { (1, 2, 3), (1, 3, 2), (0, 7, 7) }
#
# * (1, 5, 2) and (2, 3, 3) are dominated by (1, 3, 2) and (1, 2, 3)
# * (0, 7, 7) is not dominated by any point because it has the smallest x
# * (1, 2, 3) and (1, 3, 2) are in a tradeoff; neither dominates the other
# [ (1), (4), (9), (1) ] -> { (1) }
# In 1D, the Pareto Optimum is the smallest element.
# ALGORITHMSMATHEMATICSMATRIXTUTORIALS