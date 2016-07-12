#!/usr/bin/python3

import random
import time
import sys
import Being

# print python version- dev purposes
print(sys.version)

# generic dice
def x_dices_n(x,n):
    result = 0
    for i in range(0, x):
        roll_dice_n = random.randint(1,n)
        result = roll_dice_n + result
    return result

#crude race selector ;)
player = Being.Dwarf ()
print("to jest to miejsce")
print(player.base_line_1)

# roll for stats with generic dice
fresh_stats=[]
for x in range(0, 8):
    fresh_stats.append(x_dices_n(2, 10))

# sorts rolled results, removes lowest result, adds 11 as Shalya'a Favor, sorts again
fresh_stats.sort()	
fresh_stats.pop(0)
fresh_stats.append(11)
fresh_stats.sort(reverse=True)

# print list without brackets(stat_listed_String)
stat_listed_String = ' '.join(str(S) for S in fresh_stats)
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
            index = int(input('? '))    #input stat index
            if (used_stats.count(index)!=0):     #check if not assigned already
                raise StatPresentError()        #give one more time if already assigned
            chosen_stats[index]=val        #assign value to index
            used_stats.append(index)     #notes what is assigned
        except KeyboardInterrupt:
            print('BYE!')
            sys.exit(0)
        except:
            print('Provide once more for what do you want to assign value '+str(val))
            continue
        else:
            break
            
for w in range(0, 80):
    print("*", end='')
print('\n')
print(*stat_first_names, sep='\t')
print(*chosen_stats, sep='\t')

#test purposes
#print(*used_stats, sep='\t')
#print(*fresh_stats, sep='\t')

# increment race base with chosen stats
player.body1 = [sum(x) for x in zip(player.base_line_1, chosen_stats)]
print(*stat_first_names, sep='\t')
#print(player.body1, sep='\t')
print(player.base_line_1)

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
for D in chosen_stats:
    f.write(str(D))
    f.write('\t')
f.write('\n')
for A in player.body1:
    f.write(str(A))
    f.write('\t')
f.close()
