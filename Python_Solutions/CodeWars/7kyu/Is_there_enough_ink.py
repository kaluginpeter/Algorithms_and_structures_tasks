# Is there enough ink for printing the image?
#
# You will get an image and the level of ink for each primary color in the tank of the printer. The image is a matrix where each cell is the color of a pixel. The color is a string of a RGB hexadecimal notation (e.g white is 'ffffff' and black is '000000'). Each primary color is a integer.
#
# A pixel with the color code 'fefdfc' need 1 unit of Red, 2 units of Green and 3 units of Blue.
#
# A pixel with the color code '00ff01' need 255 units of Red, 0 units of Green and 254 units of Blue.
#
# The image is two dimensional. E.g: image = [["ffffff", "ffffff"], ["ffffff", "ffffff"]]
#
# Your task is to determine if they are enough ink in the tank to print the image.
#
# If the ink is enough, the "enough_ink()" function should return True. False otherwise.
#
# Have fun!
#
# FUNDAMENTALS
def enough_ink(image, r, g, b):
    for chunk in image:
        for char in chunk:
            ned_r, ned_g, ned_b = [255 - int(char[i:i+2], 16) for i in (0, 2, 4)]
            r, g, b = r - ned_r, g - ned_g, b - ned_b
            if any(i < 0 for i in (r, g, b)): return False
    return True