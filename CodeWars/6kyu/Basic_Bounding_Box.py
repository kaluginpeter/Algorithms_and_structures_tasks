# You are given an image represented as a binary array. Your task is to predict the bounding box that encloses all the 1s within the image. The bounding box should be a hollow rectangle, where only the edges of the bounding box are 1s, and the interior is filled with 0s returned in an array of the same size as the original input.
#
# You can make the following assumptions:
#
# An image will only ever be comprised of 0s or 1s.
# An image will always have a consistent m x n shape.
# Important things to remember:
#
# If an empty image is passed, then an empty array should also be returned.
# If there are no 1s present then no bounding box should be drawn.
# Example
# Input:
# [[0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,1,1,0,0,0,0],
#  [0,0,0,1,1,1,1,0,0,0],
#  [0,0,1,1,1,1,1,1,0,0],
#  [0,1,1,1,1,1,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0]]
# Output:
#
# [[0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,1,1,1,1,1,1,1,0,0],
#  [0,1,0,0,0,0,0,1,0,0],
#  [0,1,0,0,0,0,0,1,0,0],
#  [0,1,1,1,1,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0]]
# ARRAYS
# Solution
def bounding_box(image_array):
    if not image_array: return []
    most_left = most_up = float('inf')
    most_right = most_down = float('-inf')
    for row in range(len(image_array)):
        for col in range(len(image_array[0])):
            if image_array[row][col] == 1:
                most_left, most_right = min(most_left, col), max(most_right, col)
                most_up, most_down = min(most_up, row), max(most_down, row)
    for row in range(len(image_array)):
        for col in range(len(image_array[0])):
            if (row >= most_up and row <= most_down):
                if (row == most_up or row == most_down) and col >= most_left and col <= most_right:
                    image_array[row][col] = 1
                elif col == most_left or col == most_right:
                    image_array[row][col] = 1
                else: image_array[row][col] = 0
            else: image_array[row][col] = 0
    return image_array