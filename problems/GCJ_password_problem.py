import sys

def solve_prob(A, B, probs):
    #First option: press enter immediately
    mincost = B + 2
    
    #Cycle through deleting from A to 0 characters
    prob = 1.0
    for i, k in enumerate(range(A+1)[::-1]):
        cost = prob * (B - A + 2 * k + 1) + \
               (1 - prob) * (2 * B - A + 2 * k + 2)
        mincost = min(mincost, cost)
        try:
            prob = prob * probs[i]
        except IndexError:
            pass #we're looping through 1 more than probs has
    return mincost

infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    A, B = [int(num) for num in infile.readline().split()]
    probs = [float(num) for num in infile.readline().split()]
    output = solve_prob(A, B, probs)
    outfile.write("Case #%i: %.6f\n" % (i+1, output))
    print "Case #%i: %.6f" % (i+1, output)
infile.close()
outfile.close()