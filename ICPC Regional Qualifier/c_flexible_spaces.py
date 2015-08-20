import sys

W, P = [int(x) for x in sys.stdin.readline().split()]

positions = [0]
for x in sys.stdin.readline().split():
    positions.append(int(x))
positions.append(W)

widths = [False for i in range(W)]

for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        this = positions[j] - positions[i]
        #print this - 1, len(widths)
        widths[this - 1] = True
        
valid = [str(i+1) for i, b in enumerate(widths) if b]
print ' '.join(valid)
    