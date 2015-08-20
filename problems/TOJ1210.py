import sys

N = int(sys.stdin.readline())
MAXCOST = 1 << 16

mincosts = [0]

for i in range(N):
    K_i = int(sys.stdin.readline())
    newcosts = [MAXCOST for k in range(K_i)]
    for k in range(K_i):
        line = [int(i) for i in sys.stdin.readline().split()]
        assert line[-1] == 0
        line = line[:-1]
        for j in range(len(line) / 2):
            src, cost = line[j * 2], line[j * 2 + 1]
            if mincosts[src - 1] + cost < newcosts[k]:
                newcosts[k] = mincosts[src - 1] + cost
    sys.stdin.readline() #The asterisk lines
    mincosts = newcosts
print min(mincosts)