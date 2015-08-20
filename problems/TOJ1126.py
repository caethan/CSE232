import sys

def read_nums():
    while True:
        num = int(sys.stdin.readline())
        if num == -1:
            break
        yield num

#Read in M
M = read_nums().next()

"""
#Very efficient way to do it with a double-ended queue (in O(N) time)
#Initialize a double-ended queue to hold the values
from collections import deque
queue = deque()

for i, num in enumerate(read_nums()):
    #Remove items from the head as they get too old for the window
    if len(queue) and (queue[0][1] <= (i - M)):
        queue.popleft() 
    
    #Remove elements from the tail that can't possibly become the maximum
    while len(queue) and (queue[-1][0] <= num):
        queue.pop()

    #Add the new element to the tail
    queue.append((num, i))
    
    #The head value is now the maximum for the current window
    if i >= M-1:
        print queue[0][0]
"""

#Less efficient way to do it in O(N lg N) with a heap
#N.B. python uses minheaps, so we'll multiply everything by -1 to get a maxheap instead
import heapq
nums = []

for i, num in enumerate(read_nums()):
    #Remove items as they get too old for the window
    while len(nums) and (nums[0][1] <= (i - M)):
        heapq.heappop(nums)
        
    #Add the new element
    heapq.heappush(nums, [-num, i])
    
    #Return the root
    if i >= M-1:
        print -nums[0][0]
        
"""
#Even less efficient way to do it in O(N M) by repeated loops
#Gives time limit exceeded!
nums = [num for num in read_nums()]
for i in range(len(nums) - M + 1):
    print max(nums[i:i+M])
"""
    