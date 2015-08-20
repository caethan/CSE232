import sys
import numpy as np

class UnionFind(object):
    def __init__(self, items):
        self.sets = np.arange(len(items))
        self.mapping = {}
        for i, item in enumerate(items):
            self.mapping[item] = i
            
    def union(self, item, other):
        item_root, item_len = self.find(item)
        other_root, other_len = self.find(other)
        item = self.mapping[item]
        other = self.mapping[other]
        if item_root == other_root:
            return
        elif item_len < other_len:
            self.sets[item] = other_root
        else:
            self.sets[other] = item_root
        
    def find(self, item):
        item = self.mapping[item]
        count = 0
        links = [item]
        while not self.sets[links[-1]] == links[-1]:
            links.append(self.sets[links[-1]])
            count += 1
        for link in links:
            self.sets[link] = links[-1]
        return links[-1], count
        
    def count(self):
        groups = set()
        for key in self.mapping.keys():
            groups.add(self.find(key)[0])
        return len(groups)

def primes(max=None):
    composites = {}
    #Yield 2 first, then only loop through odd numbers
    yield 2
    q = 3
    while max is None or q <= max:
        if q not in composites:
            yield q        
            composites[q * q] = [q]
        else:
            for p in composites[q]:
                try:
                    composites[p+q].append(p)
                except KeyError:
                    composites[p+q] = [p]
            del composites[q]
        q += 2

def solve_prob(A, B, P):
    width = B - A + 1
    #Initialize a union-find on the integers in the range
    numbers = UnionFind(range(A, B+1))
    #Loop through primes between P and width
    for p in primes(width):
        if p < P:
            continue
        #Find the smallest number divisible by p that is >= A
        minnum = (A // p) * p
        if A % p > 0:
            minnum += p
        num = minnum + p
        while num <= B:
            #print A, p, minnum, num
            numbers.union(minnum, num)
            num += p
    #print numbers.sets
    #print numbers.mapping
    return numbers.count()

infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    A, B, P = [int(num) for num in infile.readline().split()]
    output = solve_prob(A, B, P)
    outfile.write("Case #%i: %i\n" % (i+1, output))
    print "Case #%i: %i" % (i+1, output)
infile.close()
outfile.close()