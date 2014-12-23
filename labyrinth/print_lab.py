'''
Created on 13.3.2013

@author: Nicke
'''

from labyrinth import Labyrinth
from player import Player

#111, 49
lab  = Labyrinth([20, 20])

if lab.matrix[lab.x_size/2][lab.y_size/2]:
    x = lab.x_size/2+1
    y = lab.y_size/2
    player = Player([x, y])
    lab.matrix[lab.x_size/2+1][lab.y_size/2] = 8
else:
    x = lab.x_size/2
    y = lab.y_size/2
    player = Player([x, y])
    lab.matrix[lab.x_size/2][lab.y_size/2] = 8
    
i = 0
word = ''
while i<lab.y_size:
    for j in lab.matrix:
        word+=str(j[i])
    print word
    word = ''
    i+=1
'''
i = 0
while i<lab.y_size:
    print ' X' *lab.x_size
    i+=1
'''
'''
while not player.at_exit():    
    print ' '*40
    word = ''
    j = 0
    while j<lab.y_size:
        for k in lab.matrix:
            if k[j]==1:
                word+=' X'
            elif k[j]==2:
                word+=' |'
            elif k[j]==3:
                word+=' |'
            elif k[j]==4:
                word+=' >'
            elif k[j]==5:
                word+=' <'
            elif k[j]==7:
                word+=' E'
            elif k[j]==8:
                word+=' P'
            else:
                word+=' .'
        print word
        word = ''
        j+=1
    dir = int(raw_input("Direction:"))
    player.move(dir, lab.matrix)
print ' '*40'''
'''
lab.to_file('haba')
value = lab.from_file('haba')
if value:
    print 'Success!'
else:
    print 'Not that successful..'

i = 0
word = ''
while i<lab.y_size:
    for j in lab.matrix:
        word+=str(j[i])
    print word
    word = ''
    i+=1
'''
solved = lab.solve([x, y])

print ' '*40
#print mat
i = 0
word = ''
while i<lab.y_size:
    for j in solved:
        word+=str(j[i])
    print word
    word = ''
    i+=1

print ' '*40
word = ''
j = 0
while j<lab.y_size:
    for k in solved:
        if k[j]==1:
            word+=' X'
        elif k[j]==2:
            word+=' |'
        elif k[j]==3:
            word+=' |'
        elif k[j]==4:
            word+=' >'
        elif k[j]==5:
            word+=' <'
        elif k[j]==7:
            word+=' E'
        elif k[j]==8:
            word+=' P'
        elif k[j]==9:
            word+=' S'
        else:
            word+=' .'
    print word
    word = ''
    j+=1





