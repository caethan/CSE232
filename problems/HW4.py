import sys
import numpy as np

#Construct the trie
TERMINATOR = ''

def add_branch(tree, word):
    for char in word:
        if not char in tree:
            tree[char] = {}
        tree = tree[char]
    tree[TERMINATOR] = True

tree = {}
wordlist = ['a', 'aac', 'acb', 'baa', 'bbc', 'bc', 'caba', 'caab']
for word in wordlist:
    add_branch(tree, word)
    
S = "abbbcbbc" 
MAXVAL = len(S)

def match_words(prefix, index):
    suffix = S[index:]
    branch = tree
    for char in prefix:
        branch = branch[char]
    
    if suffix == '':
        if TERMINATOR in branch:
            return 0
        else:
            return MAXVAL
            
    best = MAXVAL
    
    char = suffix[0]
    for nextchar in branch:
        #Skip terminating branches
        if nextchar == TERMINATOR:
            continue
        #Check if this is a mismatch
        mismatch = 1
        if nextchar == char:
            mismatch = 0
        #If we end a word here, check the DP array and increment if this is a mismatch
        if TERMINATOR in branch[nextchar]:
            best = min(best, mismatch + min_swaps[index + 1])
        #And then increment our prefix by this character and recurse to the next position
        best = min(best, mismatch + match_words(prefix + nextchar, index + 1))
    
    return best

#Initialize the DP array
min_swaps = np.zeros(len(S)+1, dtype=int)

for i in range(len(S))[::-1]:
    min_swaps[i] = match_words('', i)

print wordlist
print S
print min_swaps[:-1]