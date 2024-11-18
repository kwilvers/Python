import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
minx = 0
miny = 0
maxx = w-1
maxy = h-1
x = x0
y = y0
print(f"x0:{x0}  y0:{y0}", file=sys.stderr, flush=True)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(f"{bomb_dir} x:{minx}:{maxx}  y:{miny}:{maxy}", file=sys.stderr, flush=True)
    if bomb_dir == "U":
        maxy = y - 1 
    elif bomb_dir == "UR":
        maxy = y - 1 
        minx = x + 1
    elif bomb_dir == "R":
        minx = x + 1
    elif bomb_dir == "DR":
        minx = x + 1
        miny = y + 1
    elif bomb_dir == "D":
        miny = y + 1
    elif bomb_dir == "DL":
        miny = y + 1
        maxx = x - 1
    elif bomb_dir == "L":
        maxx = x - 1
    elif bomb_dir == "UL":
        maxy = y - 1
        maxx = x - 1 

    print(f"{bomb_dir} x:{minx}:{maxx}  y:{miny}:{maxy}", file=sys.stderr, flush=True)
    x = int(round(minx + (maxx-minx)/2,0))
    y = int(round(miny + (maxy-miny)/2,0))
    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
