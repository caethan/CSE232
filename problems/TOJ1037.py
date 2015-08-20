import sys
import heapq

DELAY = 10 * 60 #Swich to seconds to match the input data
N = 30000
CLEARED = 'block_cleared'

#Initialize a priority queue for free block IDs with all blocks starting as free
free_blocks = range(1, N + 1)
heapq.heapify(free_blocks)

#Initialize priority queue for allocated blocks along with the time when they will be freed
allocated_blocks = []

#We'll also store a dictionary of all allocated blocks so we can quickly check whether a block
#is available or not
locations = {}

#Now let's set up some functions to handle allocating, accessing, and releasing blocks
def release_blocks(t):
    """Release any allocated blocks that have expired by time t, pushing them back onto the
    free block priority queue."""
    while allocated_blocks and allocated_blocks[0][0] <= t:
        entry = heapq.heappop(allocated_blocks)
        block = entry[1]
        if block is not CLEARED:
            heapq.heappush(free_blocks, entry[1])
            del locations[block]

def allocate_block(t):
    """Find the first free block and allocate it at time t to be freed at time t + DELAY."""
    release_blocks(t)
    
    block = heapq.heappop(free_blocks)
    entry = [t + DELAY, block]
    locations[block] = entry
    heapq.heappush(allocated_blocks, entry)
    return block
  
def access_block(t, b):
    """Access block b at time t, increasing its expiration time by marking the old block as
    CLEARED and inserting a new block with the new expiration time into the priority queue
    
    Returns True if successful and False if unsuccessful (because block b isn't allocated)."""
    release_blocks(t)

    if not b in locations:
        return False
    
    entry = locations.pop(b)
    entry[-1] = CLEARED
    entry = [t + DELAY, b]
    locations[b] = entry
    heapq.heappush(allocated_blocks, entry)
    
    return True

    
#And now parse the input and print the output
for line in sys.stdin:
    line = line.split()
    if len(line) == 2:
        t = int(line[0])
        print allocate_block(t)
    elif len(line) == 3:
        t, b = int(line[0]), int(line[2])
        if access_block(t, b):
            print '+'
        else:
            print '-'