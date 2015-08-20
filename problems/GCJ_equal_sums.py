import sys
import random

def solve_prob(nums):
    d = {}
    N = len(nums)
    while True:
        S = (sorted(random.sample(nums, 5)))
        total = sum(S)
        if total in d and d[total] != S:
            return d[total], S
        d[total] = S

infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    nums = [int(num) for num in infile.readline().split()][1:]
    set1, set2 = solve_prob(nums)
    output = "\n%s\n%s" % (' '.join(map(str, set1)), ' '.join(map(str, set2)))
    outfile.write("Case #%i: %s\n" % (i+1, output))
    print "Case #%i: %s" % (i+1, output)
    print sum(set1), sum(set2)
infile.close()
outfile.close()