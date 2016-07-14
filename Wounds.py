#!/usr/bin/python3
import math

# generic dice
def x_dices_n(x,n):
    result = 0
    for i in range(0, x):
        roll_dice_n = random.randint(1,n)
        result = roll_dice_n + result
    return result
wounds_table = [[11, 9, 8, 10]
                  [12, 10, 9, 11]
                  [13, 11, 10, 12]
                  [14, 12, 11, 13]]

roll = x_dice_n(1, 10)
result = roll / 3
print(result)
line = math.ceil(result)
print(line)

