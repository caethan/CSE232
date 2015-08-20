import sys
import heapq

DELAY = 10 * 60 #Swich to seconds to match the input data
N = 30000

#Initialize a flat array making all blocks' release time 0
blocks = []
for i in range(N):
    blocks.append(0)

#Find the first free block and allocate it at time t to be freed at time t + DELAY
def allocate_block(t):
    for i in range(N):
        if blocks[i] <= t:
            blocks[i] = t + DELAY
            return i + 1
            
def access_block(t, b):
    if blocks[b-1] <= t:
        #This block is already freed
        return False
    else:
        blocks[b-1] = t + DELAY
        return True
    
#And now parse the input and print the output
for line in sys.stdin:
    #print blocks[:10]
    line = line.split()
    if len(line) == 2:
        assert line[1] == '+'
        t = int(line[0])
        print allocate_block(t)
    elif len(line) == 3:
        assert line[1] == '.'
        t, b = int(line[0]), int(line[2])
        if access_block(t, b):
            print '+'
        else:
            print '-'
    else:
        print line, len(line), ['|%s|' % item for item in line]
        raise ValueError('parsing error')