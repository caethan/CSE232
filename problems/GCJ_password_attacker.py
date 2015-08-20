import sys

#All arithmetic will be modulo 1e9+7
MOD = 1000000007

#Simple memoization decorator
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

@memoize
def fact(N):
    if N == 1:
        return 1
    else:
        return (N * fact(N-1)) % MOD

def solve(M, N):
    
    @memoize
    def subsolve(rep, count):
        if count > M:
            return 0
        if rep == 0:
            return 1
        total = count * subsolve(rep - 1, count) + subsolve(rep, count + 1)
        return total % MOD
    
    return (subsolve(N - M, 1) * fact(M)) % MOD

infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    M, N = [int(num) for num in infile.readline().split()]
    output = solve(M, N)
    outfile.write("Case #%i: %s\n" % (i+1, output))
    print "Case #%i: %s" % (i+1, output)
infile.close()
outfile.close()