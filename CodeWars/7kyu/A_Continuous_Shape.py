# Have you ever seen those "Can you draw this shape without lifting up your pen?" tasks online? In this kata, you're going to be doing just that.
#
# To get the feeling of the kata, I would like you to get a sheet of paper and a pen. Now, try to draw these 2 shapes, without lifting your pen up:
#
#
#
# The first one is not that hard after some tries, however, if you try to draw the second, relatively smaller shape, every path seems impossible. But why?
#
# The task
# Your task is to, given a graph representation of a shape, determine whether or not the given shape is possible to draw continuously.
#
# Input
# Shapes will be given to you as connected undirected graphs; you don't need to worry about detecting separate islands or other forms of input validation.
#
# The graphs are encoded as dictionaries, with each vertex mapped to a list of vertices it is connected to. Vertices themselves will be encoded as strings.
#
# As an example, the representation for the two shapes given above is:
#
# shape1 = {
#     "A": ["B", "C"],
#     "B": ["A", "C", "D", "F"],
#     "C": ["A", "B", "E", "F"],
#     "D": ["B", "E", "F"],
#     "E": ["C", "D", "F"],
#     "F": ["B", "C", "D", "E"]
# }
#
# #           A
# #         /   \
# #       /       \
# #     /           \
# #   /               \
# # B - - - - - - - - - C
# # | \               / |
# # |   \           /   |
# # |     \       /     |
# # |       \   /       |
# # |         F         |
# # |       /   \       |
# # |     /       \     |
# # |   /           \   |
# # | /               \ |
# # D - - - - - - - - - E
#
# shape2 = {
#     "A": ["B", "C", "E"],
#     "B": ["A", "D", "E"],
#     "C": ["A", "D", "E"],
#     "D": ["B", "C", "E"],
#     "E": ["A", "B", "C", "D"]
# }
#
# # A - - - - - - - - - B
# # | \               / |
# # |   \           /   |
# # |     \       /     |
# # |       \   /       |
# # |         E         |
# # |       /   \       |
# # |     /       \     |
# # |   /           \   |
# # | /               \ |
# # C - - - - - - - - - D
#
# can_draw(shape1) # True
# can_draw(shape2) # False
# There will be 200 random tests, each with between 3 and 50 vertices per shape.
#
# Graph Theory