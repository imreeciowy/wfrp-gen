#!/usr/bin/python3

import random
import time
import sys

# print python version- dev purposes
print(sys.version)

# kostka generyczna
def xkn(x,n):
    wynik = 0
    for i in range(0, x):
        rzutkn = random.randint(1,n)
        wynik = rzutkn + wynik
    return wynik

humanBase=[20] * 8

# losowanie statow za pomoca kostki generycznej
freshStats=[]
for x in range(0, 8):
    freshStats.append(xkn(2, 10))

# sortuje wylosowane wyniki, usuwa dwa najnizsze wyniki, dodaje 11, znow sortuje 
freshStats.sort()	
freshStats.pop(0)
freshStats.append(11)
freshStats.sort(reverse=True)

# print listy bez nawiasow (statListedString)
statListedString = ' '.join(str(S) for S in freshStats)
print(statListedString)

# zapis do pliku - testowy - trzeba bedzie tez przekopiowac na koniec generacji, nie usuwac - TEST PURPOSES
timeString = time.strftime("%Y-%m-%d--%H%M%S")
filename = ('statystyki-' + timeString + '.txt')
f = open(filename, 'w')
for S in freshStats:
    f.write(str(S))
    f.write('\t')
f.write('\n'+str(sum(freshStats)))
f.write('\n')
# przygotowanie suchej listy dla wlasciwych statystyk
chosenStats = [0] * 8

# przygotowanie pustej listy dla numeracji uzytych rzutow - dla unikniecia prob kilkukrotnego przypisania do jednego indeksu
usedStats=[]

# przygotowanie krotki z nazwami
statyFirstNames = ('WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel', 'A', 'W', 'SB', 'TB', 'M', 'Mag', 'IP', 'FP')

# przyporzadkowanie statow
# aktualnie przyporzadkowana wartosc jest castowana na string
for idx, val in enumerate(freshStats):
    print('wartosc '+str(val)+' chcesz przyporzadkowac do?')
    for Ind, Vart in enumerate(statyFirstNames):
        if (usedStats.count(Ind))==1:
            print('*',end='')
        print(Vart,end='\t')
    print('\n')
    for i in range(8):
        print(i,end='\t')
    print('\n')
    while True: 
        try:
            index = int(input('? '))    #wprowadz index stata
            if (usedStats.count(index)!=0):     #sprawdza czy juz nie przyporzadkowano
                raise StatPresentError()        #jesli juz przyporzadkowano podaj jeszcze raz
            chosenStats[index]=val        #przyporzodkowac wartosc do indeksu
            usedStats.append(index)     #notuje co juz przyporzadkowano
        except KeyboardInterrupt:
            print('BYE!')
            sys.exit(0)
        except:
            print('Podaj jeszcze raz do czego chcesz przyporzadkowac wartosc'+str(S))
            continue
        else:
            break

for w in range(0, 80):
    print("*", end='')
print('\n')
print(*statyFirstNames, sep='\t')
print(*chosenStats, sep='\t')
#print(*usedStats, sep='\t')
#print(*freshStats, sep='\t')
for i in range(8):
    f.write(str(statyFirstNames[i]))
    f.write('\t')
f.write('\n')
for D in chosenStats:
    f.write(str(D))
    f.write('\t')
f.write('\n')

f.close()

print(*humanBase)
