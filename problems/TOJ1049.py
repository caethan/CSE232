import sys
from math import sqrt

#Dynamic prime generator using the Sieve
def primes(max=None):
    composites = {}
    #Yield 2 first, then only loop through odd numbers
    yield 2
    q = 3
    while max is None or q < max:
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
        
def factor(N, f=None):
    if f is None:
        f = {}
    for p in primes(sqrt(N)):
        if p > N:
            break
        while (N % p) == 0:
            try:
                f[p] += 1
            except KeyError:
                f[p] = 1
            N = N // p
    if N > 1:
        try:
            f[N] += 1
        except KeyError:
            f[N] = 1
    return f

#Sum up the prime factors of each number    
f = {}
for i in range(10):
    num = int(sys.stdin.readline())
    f = factor(num, f)

#Calculate the number of positive integer divisors
count = 1
for key in f.keys():
    count = count * ((f[key] + 1) % 10)
    count = count % 10
print count
