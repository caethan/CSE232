#F. Mixed Fractions

import sys

while True:
    line = sys.stdin.readline()
    n, d = [int(x) for x in line.split()]
    if n == 0 and d == 0:
        break
    
    i = 0
    while n > d:
        i += 1
        n -= d
    print '%i %i / %i' % (i, n, d)