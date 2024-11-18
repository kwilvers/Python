import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    print(f"light(x,y) = ({light_x},{light_y})", file=sys.stderr, flush=True)
    print(f"Thor(x,y) = ({initial_tx},{initial_ty})", file=sys.stderr, flush=True)
    print(f"remaining_turns = {remaining_turns}", file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    delta_x = abs(light_x - initial_tx)
    delta_y = abs(light_y - initial_ty)

    cosine = math.atan2(light_y - initial_ty, light_x - initial_tx) * 180 / math.pi
    print(f"cosine = {cosine}", file=sys.stderr, flush=True)


    if cosine>=-22.5 and cosine<=22.5:
        print("E")
        initial_tx += 1
        initial_ty += 0
    elif cosine>=22.5 and cosine<=67.5:
        print("SE")
        initial_tx += 1
        initial_ty += 1
    elif cosine>=67.5 and cosine<=112.5:
        print("S")
        initial_tx += 0
        initial_ty += 1
    elif cosine>=112.5 and cosine<=157.5:
        print("SW") 
        initial_tx -= 1
        initial_ty += 1
    elif cosine>=157.5:
        print("W")
        initial_tx -= 1
        initial_ty += 0
    elif cosine<=-22.5 and cosine>=-67.5:
        print("NE")
        initial_tx += 1
        initial_ty -= 1
    elif cosine<=-67.5 and cosine>=-112.5:
        print("N")
        initial_tx += 0
        initial_ty -= 1
    elif cosine<=-112.5 and cosine>=-157.5:
        print("NW") 
        initial_tx -= 1
        initial_ty -= 1
    elif cosine<=-157.5:
        print("W")
        initial_tx -= 1
        initial_ty += 0