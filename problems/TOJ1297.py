import sys

S = sys.stdin.readline().strip()

#Suffix tree implementation
tree = {}
END = 'END'

def add_word(tree, word, terminator, marker):
    tree[marker] = True
    if not word:
        tree[END] = terminator
        return
    char = word[0]
    if not char in tree:
        tree[char] = {}
    add_word(tree[char], word[1:], terminator, marker)
    
def add_suffixes(tree, S, marker):
    for i in range(len(S)):
        add_word(tree, S[i:], i, marker)
        
#Build a suffix tree on both the forward and reversed strings, marking nodes by which string they're from
add_suffixes(tree, S, 'forward')
add_suffixes(tree, S[::-1], 'reverse')

#N.B. doesn't get the first longest palindrome

#Find the deepest shared node
def find_shared(tree, char='', m1='forward', m2='reverse'):
    if not ((m1 in tree) and (m2 in tree)):
        #Not a shared node
        return ''
    shared = ''
    for key in tree.keys():
        if key == m1 or key == m2 or key == END:
            continue
        deeper = find_shared(tree[key], key)
        if len(deeper) > len(shared):
            shared = deeper
    return char + shared
    
print find_shared(tree)