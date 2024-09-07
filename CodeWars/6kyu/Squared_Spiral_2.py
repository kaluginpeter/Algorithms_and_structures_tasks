# Squared Spiral #2
# Given the coordinates (x,y) of a number on a square spiral, find out what is it's index in the sequence, like the drawings bellow.
#
# Coordinates
#          ...  ←  1,2  ←  2,2
#                           ↑
#                           ↑
#                           ↑
# -1,1  ←  0,1  ←  1,1     2,1
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#   ↓               ↑       ↑
# -1,0     0,0  →  1,0     2,0
#   ↓                       ↑
#   ↓                       ↑
#   ↓                       ↑
# -1,-1 →  0,-1 →  1,-1 →  2,-1
# Numbers
#          ...  ←  013  ←  012
#                           ↑
#                           ↑
#                           ↑
#  004  ←  003  ←  002     011
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#  005     000  →  001     010
#   ↓                       ↑
#   ↓                       ↑
#   ↓                       ↑
#  006  →  007  →  008  →  009
# The spiral starts at 0 which is located at coordinates (0,0), number 1 is at (1,0), number 2 is at (1,1), number 3 is at (0,1) and so on. The spiral always starts to the right and goes in an anti-clockwise direction.
#
# 100 fixed tests and another 500 random tests are performed with coordinates ranging from (-100,-100) to (100,100).
#
# GEOMETRYPUZZLES
# Python
def squared_spiral(x, y):
    cur_x = cur_y = number = 0
    if cur_x == x and cur_y == y: return number
    right: bool = True
    up = left = down = False
    step: int = 0
    while True:
        if right:
            right, up = False, True
            step += 1
            for move in range(step):
                cur_x += 1
                number += 1
                if cur_x == x and cur_y == y:
                    return number
        elif up:
            up, left = False, True
            for move in range(step):
                cur_y += 1
                number += 1
                if cur_x == x and cur_y == y:
                    return number
        elif left:
            left, down = False, True
            step += 1
            for move in range(step):
                cur_x -= 1
                number += 1
                if cur_x == x and cur_y == y:
                    return number
        else:
            down, right = False, True
            for move in range(step):
                cur_y -= 1
                number += 1
                if cur_x == x and cur_y == y:
                    return number

# C++
int squaredSpiral(int x, int y)
{
  int cur_x, cur_y, number;
  cur_x = cur_y = number = 0;
  if (cur_x == x && cur_y == y) {
    return number;
  }
  bool right, up, left, down;
  right = true;
  up = left = down = false;
  int step = 0;
  while (true) {
   if (right) {
     right = false;
     up = true;
     step += 1;
     for (int move = 0; move < step; move++) {
       cur_x += 1;
       number += 1;
       if (cur_x == x && cur_y == y) {
         return number;
       }
     }
   } else if (up) {
     up = false;
     left = true;
     for (int move = 0; move < step; move++) {
       cur_y += 1;
       number += 1;
       if (cur_x == x && cur_y == y) {
         return number;
       }
     }
   } else if (left) {
     left = false;
     down = true;
     step += 1;
     for (int move = 0; move < step; move++) {
       cur_x -= 1;
       number += 1;
       if (cur_x == x && cur_y == y) {
         return number;
       }
     }
   } else {
     down = false;
     right = true;
     for (int move = 0; move < step; move++) {
       cur_y -= 1;
       number += 1;
       if (cur_x == x && cur_y == y) {
         return number;
       }
     }
   }
  }
}