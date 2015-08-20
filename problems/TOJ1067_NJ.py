#!bin/python

from sys import *


def buildTree(tree, path):
    if (len(path) == 0):
        return tree
    else:
        if (path[0] in tree):
            buildTree(tree[path[0]], path[1:])

        else:
            tree[path[0]] = {}
            buildTree(tree[path[0]], path[1:])

    return tree

 
def printTree(tree, lvl):
    if (len(tree) == 0):
        return lvl-1
    else:
        for key in sorted(tree.keys()):
            print lvl*" " + key
            printTree(tree[key], lvl+1)

numDir = ord(stdin.readline()[0]) - 48
print numDir
directory = {}
for i in range(numDir):
    print "iteration " + str(i)
    line =  stdin.readline()[:-1].split('\\')
    #print line
    directory = buildTree(directory, line)

print directory
printTree(directory, 0)