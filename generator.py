#!/usr/bin/python3

import random
import sys
import time
import kivy
import Being

kivy.require('1.9.1')

# print python version- dev purposes
print(sys.version)


# generic dice
def x_dices_n(x,n):
    result = 0
    for i in range(0, x):
        roll_dice_n = random.randint(1,n)
        result = roll_dice_n + result
    return result


# race selector
program_name = sys.argv[0]
if len(sys.argv) > 1:
    arg = sys.argv[1]
    while True:
        try:
            if arg == 'e':
                player = Being.Elf()
            elif arg == 'h':
                player = Being.Halfling()
            elif arg == 'd':
                player = Being.Dwarf()
            elif arg == 'u':
                player = Being.Human()
            else:
                player = Being.Human()
        except NameError:
            player = Being.Human()
        else:
            break
else:
    player = Being.Human()

# roll for stats with generic dice
fresh_stats=[]
for x in range(0, 8):
    fresh_stats.append(x_dices_n(2, 10))

# roll for wounds
wound_table_roll = x_dices_n(1, 10)
if wound_table_roll <= 3:
    player.base_line_2[1] = player.wounds_table[0]
elif wound_table_roll <=6:
    player.base_line_2[1] = player.wounds_table[1]
elif wound_table_roll <=9:
    player.base_line_2[1] = player.wounds_table[2]
else:
    player.base_line_2[1] = player.wounds_table[3]

# roll for fate points
fate_points_table_roll = x_dices_n(1, 10)
if fate_points_table_roll <=4:
    player.base_line_2[7] = player.fate_table[0]
elif fate_points_table_roll <=7:
    player.base_line_2[7] = player.fate_table[1]
else:
     player.base_line2[7] = player.fate_table[2]

# sorts rolled results, removes lowest result, adds 11 as Shalya'a Favor, sorts again
fresh_stats.sort()
fresh_stats.pop(0)
fresh_stats.append(11)
fresh_stats.sort(reverse=True)

# print list without brackets(stat_listed_String)
stat_listed_String = ' '.join(str(S) for S in fresh_stats)
print('rolled')
print(stat_listed_String)

# raw list for chosen stats
chosen_stats = [0] * 8

# empty list for roll enumeration - to avoid doubled attribution
used_stats=[]

# tuple with stat names
stat_first_names = ('WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel')
# tuple with second line stat names
stat_second_names = ('A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP')

# stats preparation
# value as a string
for idx, val in enumerate(fresh_stats):
    print('value '+str(val)+' you want to have as ?')
    for Ind, Vart in enumerate(stat_first_names):
        if (used_stats.count(Ind))==1:
            print('*',end='')
        print(Vart,end='\t')
    print('\n')
    for i in range(8):
        print(i,end='\t')
    print('\n')
    while True: 
        try:
            index = int(input('? '))    # input stat index
            if (used_stats.count(index)!=0):     # check if not assigned already
                raise StatPresentError()        # give one more time if already assigned
            chosen_stats[index]=val        # assign value to index
            used_stats.append(index)     # notes what is assigned
        except KeyboardInterrupt:
            print('BYE!')
            sys.exit(0)
        except:
            print('Provide once more for what do you want to assign value '+str(val))
            continue
        else:
            break
            
for w in range(0, 60):
    print("*", end='')
print('\n')
print(*stat_first_names, sep='\t')
print(*chosen_stats, sep='\t')

# increment race base with chosen stats
print('Your character body')
player.body1 = [sum(x) for x in zip(player.base_line_1, chosen_stats)]
player.base_line_2[2] = player.body1[2] // 10
player.base_line_2[3] = player.body1[3] // 10
player.body2 = player.base_line_2 # to have naming consistency, yes it duplicates list but is consistent
print(*stat_first_names, sep='\t')
print(*player.body1, sep='\t')
print(*stat_second_names, sep='\t')
print(*player.body2, sep='\t')

# save to file
time_string = time.strftime("%Y-%m-%d--%H%M%S")
filename = ('statistics-' + time_string + '.txt')
f = open(filename, 'w')
for S in fresh_stats:
    f.write(str(S))
    f.write('\t')
f.write('\n'+str(sum(fresh_stats)))
f.write('\n')
for i in range(8):
    f.write(str(stat_first_names[i]))
    f.write('\t')
f.write('\n')
for A in player.body1:
    f.write(str(A))
    f.write('\t')
f.write('\n')
for i in range(8):
    f.write(str(stat_second_names[i]))
    f.write('\t')
f.write('\n')
for A in player.body2:
    f.write(str(A))
    f.write('\t')
f.write('\n')
f.close()
