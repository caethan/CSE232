import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
total = 0
for x in range(a, b+1):
    total += pow(x, 2)
print total