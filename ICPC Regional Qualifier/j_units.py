import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
        
    keys = sys.stdin.readline().split()
    
    factors = {}
    
    for i in range(N-1):
        line = sys.stdin.readline().split()
        k1, scale, k2 = line[0], int(line[2]), line[3]
        
        #Both are new
        if not k1 in factors and k2 in factors:
            factors[k1] = 1
            factors[k2] = scale
            
        #The first (larger) one is new: