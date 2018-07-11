#############################
# Author:   Donnie Brasco   #
# Date:     Sure            #
#                           #
# xword.py                  #
#                           #
# Crossword solver          #
#############################


def hit(tup):
    global data

    b = tup[0]
    c = tup[1]
    print(tup)

    pot = { 'above' :   (b-1,c),
            'right' :   (b,c+1),
            'below' :   (b+1,c),
            'left'  :   (b,c-1),
            'TR'    :   (b-1,c+1),
            'BR'    :   (b+1,c+1),
            'BL'    :   (b+1,c-1),
            'TL'    :   (b-1,c-1)   }

    pos = []

    flagT = b == 0
    flagB = b == len(data) - 1
    flagR = c == len(data[b]) - 1
    flagL = c == 0
    
    if flagT:
        if flagR:
            pos = [pot.get('left'),pot.get('BL'),pot.get('below')]
        elif flagL:
            pos = [pot.get('right'),pot.get('BR'),pot.get('below')]
        else:
            pos = [pot.get('left'),pot.get('BL'),pot.get('below'),pot.get('BR'),pot.get('right')]
    elif flagB:
        if flagR:
            pos = [pot.get('left'),pot.get('TL'),pot.get('above')]
        elif flagL:
            pos = [pot.get('right'),pot.get('TR'),pot.get('above')]
        else:
            pos = [pot.get('left'),pot.get('TL'),pot.get('above'),pot.get('TR'),pot.get('right')]
    elif flagR:
        pos = [pot.get('above'),pot.get('TL'),pot.get('left'),pot.get('BL'),pot.get('below')]
    elif flagL:
        pos = [pot.get('above'),pot.get('TR'),pot.get('right'),pot.get('BR'),pot.get('below')]
    else:
        for key in pot.keys():
            pos.append(pot.get(key))
        pos.sort()

    return pos

def trackr(lis):
    global data
    global src
    global flag
    global path

    
    # hey make sure that you keep staying in the same direction

    # first position = (a, b)
    # second hit = (c, d)
    # xDir = c - a
    # yDir = d - b
    # next hits -> (lastX + xDir, lastY + yDir)

    
#    for tupl in lis:
#        if flag == len(src) - 1:
#            return 1
#        if data[tupl[0]][tupl[1]] == src[flag]:
#            flag += 1
#            path.append(tupl)
#            trackr(hit(tupl))
#        else:
#            flag = 1
#            path.clear()



#    while flag != len(src) - 1:
#        for tup in lis:
#            if data[tup[0]][tup[1]] == src[flag]:
#                flag += 1
#                path.append(tup)
#                lis = hit(tup)
#                break
#            else:
#                flag = 1
#                path.clear()
    
data = []
bank = []

with open('xword.txt') as x:
    for line in x:
        itr = line[:len(line)-1].split(',')
        data.append(itr)

with open('bank.txt') as b:
    for line in b:
        bank.append(line[:len(line)-1])

for line in data:
    print(line)

print()

for word in bank:
    print(word)

src = bank[0]
print()
print(src,'\t|\t',len(src),'\n')
path = []
pot = []
fr = []
flag = 1
cap = 0

for b in range(len(data)):
    for c in range(len(data[b])):
        if data[b][c] == src[0]:
            fr.append((b,c))

for tup in fr:
    position = 0
    while tup[position] == src[position] and position < len(tup):
        if True:
            potition += 1
        
for tup in path:
    data[tup[0]][tup[1]] = data[tup[0]][tup[1]].upper()
            
for line in data:
    print(line)

#exit()

