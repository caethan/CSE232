import numpy as np
import sys

class memoize(object):
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value

def read_input(infile):
    P, Q = np.array(infile.readline().split(), dtype=int)
    released = np.array(infile.readline().split(), dtype=int)
    return P, released

def solve_case(P, released):
    
    @memoize
    def find_min_cost(mincell, maxcell):
        cost = 0
        valid = (mincell <= released) & (released <= maxcell)
        for num in released[valid]:
            tmp = maxcell - mincell + find_min_cost(mincell, num-1) + find_min_cost(num+1, maxcell)
            if (not cost) or (tmp < cost):
                cost = tmp
        return cost
        
    return find_min_cost(1, P)
    
infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')   
cases = int(infile.readline().strip('\n'))
for i in range(cases):
    case = read_input(infile)
    output = solve_case(*case)
    outfile.write('Case #%i: %s\n' % (i+1, output))
    print 'Case #%i: %s' % (i+1, output)
infile.close()
outfile.close()

    