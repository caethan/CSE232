import sys

def read_case(infile):
    N = int(infile.readline().strip())
    adjacency_list = []
    for i in range(N):
        adjacency_list.append([])
        line = infile.readline().split()
        for j in range(int(line[0])):
            adjacency_list[i].append(int(line[j+1]) - 1) #0-index
    return adjacency_list

def dfs(graph, root):
    stack = [root]
    reached = [False for i in range(len(graph))]
    reached[root] = True
    while stack:
        root = stack.pop()
        for child in graph[root]:
            if reached[child]:
                return True
            reached[child] = True
            stack.append(child)
    return False

def is_diamond(graph):
    for i in range(len(graph)):
        if dfs(graph, i):
            return "Yes"
    return "No" 

infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    adjacency_list = read_case(infile)
    output = is_diamond(adjacency_list)
    outfile.write("Case #%i: %s\n" % (i+1, output))
    print "Case #%i: %s" % (i+1, output)
infile.close()
outfile.close()