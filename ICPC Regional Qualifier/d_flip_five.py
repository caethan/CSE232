import sys

P = int(sys.stdin.readline())

def flip(ID, jvals):
    new = ID
    for j in jvals:
        new ^= (1 << j)
    return new
    
lookup = {}
    
for bitmask in range(pow(2, 9)):
    #Convert the bitmask of flips to a final grid ID
    grid_ID = 0
    count = 0
    
    if bitmask &  (1 << 0):
        grid_ID = flip(grid_ID, [0, 1, 3])
        count += 1
        
    if bitmask &  (1 << 1):
        grid_ID = flip(grid_ID, [0, 1, 2, 4])
        count += 1
        
    if bitmask &  (1 << 2):
        grid_ID = flip(grid_ID, [1, 2, 5])
        count += 1
        
    if bitmask &  (1 << 3):
        grid_ID = flip(grid_ID, [0, 3, 4, 6])
        count += 1
        
    if bitmask &  (1 << 4):
        grid_ID = flip(grid_ID, [1, 3, 4, 5, 7])
        count += 1
        
    if bitmask &  (1 << 5):
        grid_ID = flip(grid_ID, [2, 4, 5, 8])
        count += 1
        
    if bitmask &  (1 << 6):
        grid_ID = flip(grid_ID, [3, 6, 7])
        count += 1
        
    if bitmask &  (1 << 7):
        grid_ID = flip(grid_ID, [4, 6, 7, 8])
        count += 1
        
    if bitmask &  (1 << 8):
        grid_ID = flip(grid_ID, [5, 7, 8])
        count += 1
    
    if grid_ID in lookup:
        lookup[grid_ID] = min(lookup[grid_ID], count)
    else:
        lookup[grid_ID] = count

for i in range(P):
    grid_id = 0
    shift = 8
    for j in range(3):
        line = sys.stdin.readline().strip()
        for k in range(3):
            if line[k] == '*':
                grid_id |= (1 << shift)
            shift -= 1
    
    print lookup[grid_id]