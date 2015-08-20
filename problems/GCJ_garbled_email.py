import sys
import numpy as np

#First, load the dictionary into a trie
tree = {}
END = ''

def add_branch(tree, word):
    for char in word:
        if not char in tree:
            tree[char] = {}
        tree = tree[char]
    tree[END] = True

infile = open('./garbled_email_dictionary.txt')
for line in infile.readlines():
    add_branch(tree, line.strip())
infile.close()


def match_words(prefix, index, required):
    suffix = S[index:]
 
    #Walk down the tree to find the right branch
    branch = tree
    for char in prefix:
        branch = branch[char]
 
    if suffix == '':
        if END in branch:
            return 0
        else:
            return -1
 
    def check(best, new, inc=0):
        if new == -1:
            return best
        if best is None:
            best = new + inc
        else:
            best = min(best, new + inc)
        return best
 
    best = None
 
    char = suffix[0]
    if char in branch: #valid match
        if END in branch[char]: #end of a word
            best = check(best, mincosts[index + 1, max(0, required - 1)])
        best = check(best, match_words(prefix + char, index + 1, max(0, required - 1)))
    if required == 0: #We're allowed to get this character wrong!
        for this in branch:
            if this == END or this == char:
                continue
            if END in branch[this]:
                best = check(best, mincosts[index + 1, 4], 1)
            if best is None or best > 1: #Don't bother checking if best is already good enough
                best = check(best, match_words(prefix + this, index + 1, 4), 1)
 
    if best is None:
        return -1
    else:
        return best
 
#Start input/output   
infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')   
cases = int(infile.readline().strip('\n'))
for i in range(cases):
    S = infile.readline().strip()
    
    #Initialize our DP cost matrix and fill it in in the correct order
    mincosts = np.zeros((len(S) + 1, 5), dtype=int)
    
    for index in range(len(S))[::-1]:
        for required in range(5):
            mincosts[index, required] = match_words('', index, required)

    outfile.write('Case #%i: %s\n' % (i+1, mincosts[0,0]))
    print 'Case #%i: %s' % (i+1, mincosts[0,0])
infile.close()
outfile.close()
