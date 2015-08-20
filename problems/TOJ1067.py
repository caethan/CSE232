import sys

N = int(sys.stdin.readline())

tree = {}
def add_path(tree, path):
    if not path:
        return
    if not path[0] in tree:
        tree[path[0]] = {}
    add_path(tree[path[0]], path[1:])

def print_tree(tree, depth=0):
    for key in sorted(tree.keys()):
        print '%s%s' % (' ' * depth, key)
        if tree[key]:
            print_tree(tree[key], depth+1)

for i in range(N):
    path = sys.stdin.readline()
    path = path.strip().split('\\')
    add_path(tree, path)
    
print_tree(tree)